# 🤖 Custom AI Chatbot with Memory

A modern AI-powered chatbot built using **Python**, **Streamlit**, **Groq API**, and **Meta Llama 3.3 70B**. The chatbot provides intelligent, context-aware conversations with user authentication, persistent chat history, document upload support, and a modern responsive UI.

This project was developed as **Project 1** during my **Generative AI Internship at Decode Labs**.

---

# 🚀 Features

- 🔐 User Login & Registration System
- 👤 Secure Password Authentication (bcrypt)
- 🧠 Conversation Memory
- 💬 Context-Aware AI Conversations
- ⚡ Powered by Groq API (Llama 3.3 70B)
- 📄 Upload and Analyze PDF, TXT & DOCX Files
- 📂 Persistent Chat History (Stored as JSON)
- 📜 Previous Chat Sessions
- 🔄 Regenerate AI Responses
- 📋 Copy AI Responses
- 📥 Download Chat as TXT
- 🧹 Clear All Chats
- 📊 Session Statistics Dashboard
- 🎨 Modern Dark-Themed Responsive UI
- ⚙️ Sidebar Chat Management

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Groq SDK
- Groq API
- Meta Llama 3.3 70B
- HTML
- CSS
- PyMuPDF
- python-docx
- bcrypt
- JSON
- Pillow (PIL)

---

# 📂 Project Structure

```text
Custom-AI-Chatbot/
│
├── chatbot_web_app.py
├── requirements.txt
├── README.md
├── users.json
├── chat_history/
├── asselogin_robot.png
└── .streamlit/
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/custom-ai-chatbot.git

cd custom-ai-chatbot
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Add Your Groq API Key

Replace the API key inside:

```python
API_KEY = "YOUR_GROQ_API_KEY"
```

or store it securely using **Streamlit Secrets**.

## Run the Application

```bash
streamlit run chatbot_web_app.py
```

---

# 📸 Screenshots

### 🏠 Login Screen

<img width="1919" height="867" alt="image" src="https://github.com/user-attachments/assets/50451132-6e46-4e1b-a744-7226b0e8e057" />


---

### 💬 Chat Interface

<img width="1919" height="873" alt="image" src="https://github.com/user-attachments/assets/dbc5a471-7c09-4c58-a203-bcf1f35bd415" />


---

### 📄 File Upload

<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/8ed79e9b-ba81-4b82-b9a6-084274ecbb0b" />


---

### 📜 Chat History

<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/ed59beef-3c3c-4cdf-a1d5-7c25526fdbe7" />


---

# 📖 How It Works

1. Create an account or log in.
2. Start a new conversation.
3. Ask any question.
4. Optionally upload a PDF, TXT, or DOCX file.
5. The chatbot extracts text from the uploaded document.
6. The extracted content is added as context for the AI model.
7. Groq API generates an intelligent response.
8. Conversations are stored automatically for each user.
9. Users can download or manage their chat history.

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Generative AI Application Development
- Large Language Model (LLM) Integration
- Prompt Engineering
- API Integration using Official SDKs
- Authentication System Development
- Password Hashing with bcrypt
- Session State Management
- Persistent Chat History Management
- File Processing
- Streamlit Web Development
- UI/UX Design
- Responsive Interface Development

---

# 🔒 Security Features

- Passwords are encrypted using **bcrypt**
- User-specific chat history
- Secure login and registration
- Session-based authentication

---

# 📁 Chat History Storage

Each user's conversations are stored locally in JSON format.

Example:

```text
chat_history/
    username/
        conversation_1.json
        conversation_2.json
```

---

# 🔮 Future Improvements

- 🌙 Dark / Light Theme Toggle
- 🎙️ Voice Input
- 🔊 Text-to-Speech Responses
- 🌐 Multi-language Support
- ☁️ Cloud Database Integration
- 📱 Mobile Responsive Improvements
- 📤 Export Chat as PDF
- 🔍 Chat Search
- 🤖 Multiple AI Model Selection

---

# 🤝 Acknowledgements

This project was developed as **Project 1** during my **Generative AI Internship at Decode Labs**.

Special thanks to **Decode Labs** for providing practical exposure to Generative AI application development through hands-on projects.

---

# 📜 License

This project is intended for educational and portfolio purposes.
