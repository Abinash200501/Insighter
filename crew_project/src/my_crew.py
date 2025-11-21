from crewai import Agent, Task, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.project import agent, task
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

AGENTS_YAML = Path("config/agents.yml")
TASKS_YAML = Path("config/tasks.yml")

def load_yaml(file_path: Path):
    if not file_path.exists():
        raise FileNotFoundError(f"YAML not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class Custom_Agents:
    def __init__(self):
        self.llm = LLM(model="gemini/gemini-2.0-flash")
        self.agents_config = load_yaml(AGENTS_YAML)

        self.agent_map = {
            "query_classifier": self.classifier,
            "searcher": self.web_searcher,
            "retriever": self.retriever,
            "summarizer": self.summarizer,
        }

    @agent
    def classifier(self) -> Agent:
        config = self.agents_config.get("query_classifier")
        return Agent(
            config=config,
            llm=self.llm,
            verbose=True
        )

    @agent
    def web_searcher(self) -> Agent:
        config = self.agents_config.get("searcher")
        return Agent(
            config=config,
            tools=[SerperDevTool()],
            llm=self.llm,
            verbose=True
        )

    @agent
    def retriever(self) -> Agent:
        config = self.agents_config.get("retriever")
        return Agent(
            config=config,
            tools=[ScrapeWebsiteTool()],
            llm=self.llm,
            verbose=True
        )

    @agent
    def summarizer(self) -> Agent:
        config = self.agents_config.get("summarizer")
        return Agent(
            config=config,
            llm=self.llm,
            verbose=True
        )

class Custom_Tasks:
    def __init__(self, agents: Custom_Agents):
        self.tasks_config = load_yaml(TASKS_YAML)
        self.agents = agents 

    @task
    def classifer_task(self) -> Task:
        config = self.tasks_config["query_classifier_task"]
        agent_name = config["agent"]

        return Task(
            description=config["description"],
            expected_output=config["expected_output"],
            agent=self.agents.agent_map[agent_name](), 
            outputs=config.get("outputs", {})
        )
    
    @task
    def web_searcher_task(self) -> Task:
        config = self.tasks_config["web_searcher_task"]
        agent_name = config["agent"]

        return Task(
            description=config["description"],
            expected_output=config["expected_output"],
            agent=self.agents.agent_map[agent_name](),
            inputs={"topic": "{topic}"}, 
            outputs=config.get("outputs", {}),
            context=[self.classifer_task()]
        )

    @task
    def retriever_task(self) -> Task:
        config = self.tasks_config["retriever_task"]
        agent_name = config["agent"]

        return Task(
            description=config["description"],
            expected_output=config["expected_output"],
            agent=self.agents.agent_map[agent_name](),
            inputs={"topic": "{topic}"}, 
            outputs=config.get("outputs", {}),
            context=[self.web_searcher_task(), self.classifer_task()]  
        )

    @task
    def summarizer_task(self) -> Task:
        config = self.tasks_config["summarizer_task"]
        agent_name = config["agent"]

        return Task(
            description=config["description"],
            expected_output=config["expected_output"],
            agent=self.agents.agent_map[agent_name](),
            inputs={"topic": "{topic}"}, 
            outputs=config.get("outputs", {}),
            context=[self.retriever_task(), self.classifer_task()]
        )

    @task
    def save_as_md(self) -> Task:
        config = self.tasks_config["save_as_md"]

        return Task(
            description=config["description"],
            expected_output=config["expected_output"],
            context=[self.summarizer_task()]
        )
