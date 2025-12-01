
# AgenticAI - ADK Project

This repository demonstrates two agents built using Google's Agent Development Kit (ADK):

1. Tool Agent – uses external tools such as fetching the current time.  
2. Greeting Agent – greets the user and asks for their name.  

---

## 🗂 Project Structure


```markdown
AgenticAI/
│
├── 1-basic-agent/        # Greeting agent
│   └── init.py       # Imports agent.py
|   └── agent.py      # Agent defination  
├── 2-tool-agent/         # Tool agent
│   └── init.py       # Imports agent.py
|   └── agent.py       # Agent defination
├── requirements.txt      # Python dependencies
└── .gitignore            # Ignored files (.venv, pycache, .env,etc)

````

---

## ⚙️ Agent Overview

### Tool Agent
- Located in `2-tool-agent/`.  
- Uses tools like `get_current_time`.  
- Tools can be enabled or disabled by commenting/uncommenting in the configuration(for now, improvements to be made).

### Greeting Agent
- Located in `1-basic-agent/`.  
- Greets the user by asking their name.  
- Does not use additional tools.


---

## 🔧 Setup Instructions (Local + ADK Web)

Follow these steps after downloading the repository:
````
### 1. Navigate to your project folder
```powershell
cd <local directory>
````

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Set up environment variables

In each agent folder (`1-basic-agent` and `2-tool-agent`), create a `.env` file:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

> You can obtain your API key from the [Google Generative AI console](https://developers.generativeai.google/products).

### 5. Make sure `__init__.py` exists in each agent folder

 `1-basic-agent/__init__.py`
 `2-tool-agent/__init__.py`

This ensures the agent module can be imported correctly.

---

## 🌐 Running Agents via ADK Web

1. Navigate to the agent folder:

```powershell
cd greeting_agent
# or
cd tool_agent
```

2. Launch ADK Web:

```powershell
adk web
```

3. Interact with the agent live in the browser.

4. To close the connection, press:

```
CTRL + C
```

---

## ⚡ Ending the Virtual Environment

When done, deactivate the environment:

```powershell
deactivate
```

---

## ✅ Notes

 `.venv`, `__pycache__`, `.env`, and other temporary files are ignored using `.gitignore`.
 * Always keep your API key secret.
 * Agent automatically reads .env file for the API key
 * You can switch between agents or tools by editing the agent configuration files.
 * ADK Web is the recommended way to run agents live without local setup.

```
