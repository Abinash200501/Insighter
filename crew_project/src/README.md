# Insigther

**Insigther** is an AI-powered query insight tool that classifies user queries, performs web searches, retrieves structured content, and generates concise summaries. It leverages **CrewAI** and **LLMs** to deliver actionable insights and save results in Markdown format.

---

## Project Structure

- **main.py**: Streamlit-based user interface and app entry point  
- **my_crew.py**: Defines custom agents and tasks for CrewAI  
- **config/agents.yml**: Configuration for the agents  
- **config/tasks.yml**: Configuration for the tasks  
- **output/**: Directory where generated Markdown summaries are saved  
- **requirements.txt**: Lists required Python packages  
- **.env**: Contains API keys and environment variables (not included in the repository)  

---

## Setup and Installation

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/insigther.git
cd insigther

Create a virtual environment:

python -m venv venv


Activate the virtual environment:

# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate


Install required packages:

pip install -r requirements.txt


Create a .env file in the project root and add your API keys:

SERPERDEV_API_KEY=your_serperdev_api_key
GEMINI_API_KEY=your_gemini_api_key

Usage

Run the Streamlit App:

streamlit run main.py


Enter your query in the input box. The app will:

- Classify the query
- Search the web
- Retrieve and structure content
- Summarize the information


View results:

- Results are displayed in the app
- Summaries are automatically saved as Markdown files under the output/ folder