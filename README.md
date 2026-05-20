# 📧 Email Intent & Urgency Detector

An AI-powered application that analyzes emails and predicts:

- Intent
- Urgency
- Tone

using LangChain, Groq LLM, JsonOutputParser, and Streamlit.

---

# 🚀 Features

✅ Intent Detection  
✅ Urgency Prediction  
✅ Tone Analysis  
✅ Structured JSON Output  
✅ Interactive Streamlit UI  
✅ Groq LLM Integration  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| LangChain | LLM workflow |
| Groq | AI inference |
| Streamlit | Web application |
| JsonOutputParser | Structured output |
| dotenv | API key security |

---

# 📂 Project Structure

```text
Email_Intent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
⚙️ Installation
Clone Repository
git clone YOUR_GITHUB_REPO_LINK
Move into Folder
cd Email_Intent
🧪 Create Virtual Environment
Windows
python -m venv email
Activate Environment
email\\Scripts\\activate
📦 Install Libraries
pip install -r requirements.txt
🔑 Setup API Key

Create .env file:

GROQ_API_KEY=your_api_key_here
▶️ Run Streamlit App
streamlit run app.py
📥 Example Input
Please resolve this issue immediately.
Users are unable to login.
📤 Example Output
{
  "intent": "Request",
  "urgency": "High",
  "tone": "Urgent"
}
🧠 How It Works
User enters email
Prompt template analyzes email
Groq LLM predicts:
intent
urgency
tone
JsonOutputParser converts response into JSON
Streamlit displays structured output
🚀 Deployment

Deploy using:

Streamlit Cloud
Hugging Face Spaces
👩‍💻 Author

Lalitha

⭐ Future Improvements
Spam Detection
Email Summarization
Confidence Scores
Multi-language Support
Database Integration
