# ReAct AI Agent 

## **Overview**  
This project implements an **intelligent AI agent** that follows a **structured reasoning process** to answer complex queries. The agent interacts with **Groq’s API**, applies **mathematical computations**, and retrieves **planetary mass data** using predefined functions.  

The agent follows a loop of **Thought → Action → PAUSE → Observation → Answer**, making it capable of **multi-step reasoning and execution**.  

## **Features**  
✅ **Conversational AI** – Uses Groq API (LLaMA3-70B) for natural language processing.  
✅ **Structured Reasoning** – Follows a **Thought → Action → PAUSE → Observation → Answer** framework.  
✅ **Tool Integration** – Supports:
  - **Mathematical calculations** (e.g., `calculate: 5.972e24 * 2`)  
  - **Planetary mass retrieval** (e.g., `get_planet_mass: Earth`)  
✅ **Automated Execution** – Iterates through multi-step logic until a final answer is reached.  

## **How It Works**  
1. **User asks a complex question.**  
2. **AI identifies the required steps** to solve it.  
3. **Executes an action (calculation or API request)** and waits (`PAUSE`).  
4. **Observes the result** and continues reasoning.  
5. **Final answer is produced.**  

### **Example Workflow**  
🔹 **Question:** _"What is the mass of Mercury times 5?"_  
```
[ Thought ] "I need to find the mass of Mercury."
[ Action ] get_planet_mass: Mercury
[ PAUSE ]
↓
Observation: 3.285e23
↓
[ Thought ] "I need to multiply this by 5."
[ Action ] calculate: 3.285e23 * 5
[ PAUSE ]
↓
Observation: 1.6425e24
↓
[ Answer ] "The mass of Mercury times 5 is 1.6425e24 kg."
```

## **Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/ai-agent-groq.git
cd ai-agent-groq
```

### **2️⃣ Install Dependencies**  
Ensure you have Python installed. Then, install required libraries:  
```bash
pip install groq
```

### **3️⃣ Set Up Environment Variables**  
Replace `"your_api_key_here"` with your **Groq API key**.  
```python
import os
os.environ['GROQ_API_KEY'] = "your_api_key_here"
```

## **Usage**  
### **Run the AI Agent**  
```python
from agent import loop

loop(query="What is the mass of Earth plus the mass of Saturn and all of that times 2?")
```

## **Project Structure**  
```
ai-agent-groq/
│── agent.py        # AI agent logic (Thought, Action, Observation, Answer)
│── tools.py        # Functions for calculations and planetary data retrieval
│── main.py         # Runs the agent with example queries
│── README.md       # Project documentation
```

## **Contributing**  
Feel free to **fork** the repository, submit **pull requests**, or suggest **new tools and improvements**! 🚀  

## **License**  
This project is licensed under the **MIT License**.  
