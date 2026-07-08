# 🤖 Custom AI Chatbot with Memory

A modern AI-powered chatbot built using **Python**, **Streamlit**, **Groq API**, and **Meta's Llama 3.3 70B** model. This chatbot provides intelligent, context-aware conversations with session-based memory and document upload support.

This project was developed as **Project 1** during my **Generative AI Internship at Decode Labs**.

---

## 🚀 Features

- 🧠 Session-based conversation memory
- 💬 Context-aware AI conversations
- 📄 Upload and analyze PDF, TXT, and DOCX files
- 🔄 Regenerate AI responses
- 📜 Chat history management
- 🧹 Clear chat functionality
- 📥 Download chat as TXT
- ⚡ Fast AI responses using Groq API
- 🎨 Modern dark-themed responsive UI
- 📊 Session statistics dashboard

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq SDK
- Groq API
- Meta Llama 3.3 70B
- HTML
- CSS
- PyMuPDF
- python-docx

---

## 📂 Project Structure

```
Custom-AI-Chatbot/
│
├── chatbot_web_app.py
├── requirements.txt
├── README.md
└── assets/
    └── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/custom-ai-chatbot.git

cd custom-ai-chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add your Groq API Key

Replace the API key in:

```python
API_KEY = "YOUR_GROQ_API_KEY"
```

or store it securely using Streamlit Secrets.

### Run the application

```bash
streamlit run chatbot_web_app.py
```

---

## 📸 Screenshots

> Add screenshots of your application here.
- Home Screen
<img width="1600" height="723" alt="image" src="https://github.com/user-attachments/assets/669edd07-7f30-49f8-9614-3e88bcfb2e84" />



- Chat Interface
  <img width="1600" height="897" alt="image" src="https://github.com/user-attachments/assets/362b382f-4969-4617-82eb-fcd9ecd185fb" />


  
- File Upload
<img width="1600" height="726" alt="image" src="https://github.com/user-attachments/assets/3f17c580-251c-4cbf-8edf-6858625ead80" />



- Chat History
<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/0dd9850e-465b-4e1e-8a21-3176ca3b226f" />


---

## 📖 How It Works

1. Enter your question in the chat input.
2. Optionally upload a PDF, TXT, or DOCX document.
3. The chatbot extracts the document text.
4. The uploaded content is sent as context to the AI model.
5. The chatbot generates intelligent responses while maintaining conversation history during the session.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Generative AI Application Development
- Large Language Model (LLM) Integration
- API Integration using Official SDKs
- Session State Management
- Prompt Engineering
- Streamlit Web Development
- File Processing
- UI/UX Design

---

## Acknowledgements

This project was developed as **Project 1** during my **Generative AI Internship at Decode Labs**.

Special thanks to Decode Labs for providing practical exposure to Generative AI application development through hands-on projects.

---

