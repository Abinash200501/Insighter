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

   - git clone https://github.com/Abinash200501/Insighter.git
   - cd insigther

2. Create a virtual environment and activate it:

   - python -m venv venv
   - source venv/bin/activate - for Linux
   - venv\Scripts\activate  - for Windows


3. Install required packages:

    - pip install -r requirements.txt


4. Create a .env file in the project root and add your API keys:

    - SERPERDEV_API_KEY=your_serperdev_api_key
    - GEMINI_API_KEY=your_gemini_api_key

## **Usage**

1. Run the Streamlit App:

    streamlit run main.py


2. Enter your query in the input box. The app will:

- Classify the query
- Search the web
- Retrieve and structure content
- Summarize the information


View results:

- Results are displayed in the app
- Summaries are automatically saved as Markdown files under the output/ folder