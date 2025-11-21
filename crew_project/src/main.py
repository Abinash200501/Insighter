from my_crew import Custom_Agents, Custom_Tasks
from crewai import Crew, Process
import streamlit as st
from pathlib import Path
from datetime import datetime
import mlflow

mlflow.set_experiment("CrewAI_Experiment")
mlflow.set_tracking_uri("http://localhost:5000")

mlflow.crewai.autolog()

class MyCrew:
    def __init__(self, topic):
        self.topic = topic
        self.agents = Custom_Agents()
        self.tasks = Custom_Tasks(self.agents)

    def save_to_md(self, inputs):
        topic = inputs.get("topic", "NoTopic")
        summary = inputs.get("summary", "")

        output_dir = Path("output")

        output_dir.mkdir(exist_ok=True, parents=True)

        file_path = output_dir / f"{topic}.md"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {topic}\n\n{summary}")

    def run(self):
        self.crew = Crew(
                    agents=[self.agents.classifier(),self.agents.web_searcher(), self.agents.retriever(), self.agents.summarizer()],
                    tasks=[self.tasks.classifer_task(),self.tasks.web_searcher_task(), self.tasks.retriever_task(), self.tasks.summarizer_task()],
                    verbose=True,
                    process=Process.sequential
                )

        result = self.crew.kickoff(inputs={"topic":self.topic})
        st.text(result)

        return result
    
def main():
    st.title("Insigther")

    topic = st.text_input("Enter your query")

    if topic:
        crew = MyCrew(topic=topic)
        result = crew.run()

        print("Result : ", result)
        crew.save_to_md({"topic": topic, "summary": result})

        st.success(f"Results saved for '{topic}'")
        st.markdown(result)


if __name__ == "__main__":
    main()