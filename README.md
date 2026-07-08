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
- Chat Interface
- File Upload
- Chat History

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

