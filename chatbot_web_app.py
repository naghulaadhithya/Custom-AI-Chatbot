"""
Project 1: Custom AI Chatbot with Memory - WEB VERSION
Decode Labs - Generative AI Internship
Blue Modern Theme - Beautiful UI
Using Groq API (free, fast, no quota issues)
"""

import streamlit as st
from groq import Groq
from datetime import datetime
import io
from copy import deepcopy
import pyperclip
import fitz
from docx import Document

# STEP 1: Put your Groq API key here
API_KEY = "YOUR_GROQ_API_KEY"

client = Groq(api_key=API_KEY)

# STEP 2: Page setup
st.set_page_config(
    page_title="Custom AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# STEP 3: Initialize session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = []
if "message_count" not in st.session_state:
    st.session_state.message_count = 0
if "last_user_prompt" not in st.session_state:
    st.session_state.last_user_prompt = ""

# STEP 4: Beautiful Blue CSS
st.markdown("""
    <style>
    /* ===== HIDE STREAMLIT DEFAULT ELEMENTS ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {
    background: transparent !important;
    }
    .stDeployButton {display: none;}

    /* ===== GLOBAL ===== */
    .stApp {
        background: linear-gradient(160deg, #020818 0%, #0a1628 50%, #0d1f3c 100%) !important;
        color: #e2e8f0 !important;
    }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a1628 0%, #0d1f3c 100%) !important;
        border-right: 1px solid #1e3a5f !important;
    }
    section[data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    section[data-testid="stSidebar"] .stButton button {
        background: linear-gradient(135deg, #1a3a6b, #1e4d8c) !important;
        color: #e2e8f0 !important;
        border: 1px solid #2d6bc4 !important;
        border-radius: 10px !important;
        padding: 10px 15px !important;
        width: 100% !important;
        font-size: 0.85em !important;
        margin: 3px 0 !important;
        font-weight: 500 !important;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background: linear-gradient(135deg, #1e4d8c, #2563eb) !important;
        border-color: #3b82f6 !important;
    }

    
    /* ===== DOWNLOAD BUTTON ===== */
    .stDownloadButton button {
     background: linear-gradient(135deg, #1a3a6b, #1e4d8c) !important;
     color: #e2e8f0 !important;
     border: 1px solid #2d6bc4 !important;
     border-radius: 10px !important;
     padding: 10px 15px !important;
     width: 100% !important;
     font-size: 0.85em !important;
     font-weight: 500 !important;
    }

    .stDownloadButton button:hover {
    background: linear-gradient(135deg, #1e4d8c, #2563eb) !important;
    border-color: #3b82f6 !important;
}
            

    /* ===== NEW CHAT BUTTON ===== */
    .new-chat-btn > div > button {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 0.9em !important;
        padding: 12px !important;
    }

    /* ===== MAIN AREA ===== */
    .main-header {
        text-align: center;
        padding: 25px 0 5px 0;
    }
    .main-title {
        font-size: 2.2em;
        font-weight: 700;
        background: linear-gradient(90deg, #60a5fa, #3b82f6, #2563eb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .main-subtitle {
        text-align: center;
        color: #64748b;
        font-size: 0.85em;
        margin: 5px 0 15px 0;
    }
    .badge {
        background: linear-gradient(135deg, #166534, #15803d);
        color: white;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: 0.72em;
        font-weight: 600;
        vertical-align: middle;
    }

    /* ===== WELCOME CARD ===== */
    .welcome-card {
        background: linear-gradient(135deg, #0a1f3d, #0f2d5a);
        border: 1px solid #1e3a5f;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin: 10px auto;
        max-width: 650px;
    }
    .welcome-card h2 {
        color: #e2e8f0 !important;
        font-size: 1.6em;
        margin-bottom: 10px;
    }
    .welcome-card p {
        color: #94a3b8 !important;
        font-size: 0.95em;
        line-height: 1.7;
    }
    .feature-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-top: 20px;
    }
    .feature-item {
        background: linear-gradient(135deg, #1a3a6b, #1e4d8c);
        border: 1px solid #2d6bc4;
        border-radius: 12px;
        padding: 14px;
        color: #bfdbfe !important;
        font-size: 0.88em;
        font-weight: 500;
    }

    /* ===== CHAT MESSAGES ===== */
    .stChatMessage {
        background: transparent !important;
        border: none !important;
        padding: 5px 0 !important;
    }
    .stChatMessage p {
        color: #e2e8f0 !important;
        font-size: 0.95em !important;
        line-height: 1.7 !important;
    }
    .stChatMessage div {
        color: #e2e8f0 !important;
    }
    [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, #0f2347, #132d5e) !important;
        border: 1px solid #1e3a5f !important;
        border-radius: 14px !important;
        padding: 14px 18px !important;
    }

    /* ===== CHAT INPUT ===== */
    [data-testid="stFileUploader"]{
       background:#0f2347 !important;
       border:1px solid #2d6bc4 !important;
       border-radius:12px !important;
       padding:8px !important;
    }

    .stFileUploader button{
       background:#2563eb !important;
       color:white !important;
       border:none !important;
    }

    [data-testid="stFileUploader"] label{
        color:white !important;
    }
    
    [data-testid="stFileUploader"] small{
        color:#cbd5e1 !important;
    }
            
    .stChatInputContainer,
    [data-testid="stChatInputContainer"] {
       background: linear-gradient(135deg,#0a1628,#0d1f3c) !important;
       border-top:1px solid #1e3a5f !important;
       padding:6px 12px !important;
    }

    [data-testid="stBottom"] {
        padding:4px 10px !important;
    }
    .stChatInput textarea, [data-testid="stChatInput"] textarea {
        background: linear-gradient(135deg, #0f2347, #132d5e) !important;
        color: #e2e8f0 !important;
        border: 1px solid #2d6bc4 !important;
        border-radius: 14px !important;
        font-size: 0.95em !important;
        padding: 14px 18px !important;
        caret-color: #60a5fa !important;
    }
    .stChatInput textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
    }
    .stChatInput textarea::placeholder {
        color: #64748b !important;
    }
    /* Fix white bottom bar */
    .stBottom,
    [data-testid="stBottom"] {
        background: linear-gradient(135deg,#0a1628,#0d1f3c) !important;
        border-top:1px solid #1e3a5f !important;

        padding-top:4px !important;
        padding-bottom:4px !important;
    }

    /* ===== STAT BOXES ===== */
    .stat-box {
        background: linear-gradient(135deg, #0f2347, #132d5e);
        border: 1px solid #1e3a5f;
        border-radius: 10px;
        padding: 9px 12px;
        font-size: 0.82em;
        color: #bfdbfe !important;
        text-align: center;
        margin: 4px 0;
    }

    /* ===== HISTORY ITEM ===== */
    .history-item {
        background: linear-gradient(135deg, #0f2347, #132d5e);
        border: 1px solid #1e3a5f;
        border-left: 3px solid #3b82f6;
        border-radius: 8px;
        padding: 10px 12px;
        margin: 5px 0;
        font-size: 0.82em;
        color: #94a3b8 !important;
    }
    [data-testid="stBottomBlockContainer"]{
        padding-top:0 !important;
        padding-bottom:0 !important;
    }

    [data-testid="stBottom"]{
        min-height:60px !important;
    }

    /* ===== DIVIDER ===== */
    hr {
        border-color: #1e3a5f !important;
        margin: 10px 0 !important;
    }

    /* ===== CAPTION ===== */
    .stCaption, caption {
        color: #64748b !important;
        font-size: 0.75em !important;
    }

    /* ===== SPINNER ===== */
    .stSpinner > div {
        border-top-color: #3b82f6 !important;
    }

    /* ===== SCROLLBAR ===== */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: #020818; }
    ::-webkit-scrollbar-thumb { background: #1e3a5f; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #3b82f6; }
            
    [data-testid="stSidebarCollapsedControl"] button {
     background: #FFFFFF !important;
    }

    [data-testid="stSidebarCollapsedControl"] svg {
     stroke: #2563eb !important;
    }
            
    </style>
""", unsafe_allow_html=True)

# STEP 5: Sidebar
with st.sidebar:
    st.markdown("### 🤖 Custom AI Chatbot")

    st.markdown("---")

    st.markdown('<div class="new-chat-btn">', unsafe_allow_html=True)
    if st.button("✏️  New Conversation"):
        st.session_state.chat_sessions.append({
          "time": datetime.now().strftime("%d %b, %I:%M %p"),
          "messages": st.session_state.message_count,
          "history": deepcopy(st.session_state.conversation_history)
        })
        st.session_state.conversation_history = []
        st.session_state.message_count = 0
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🧹 Clear All Chats", use_container_width=True):
       st.session_state.confirm_delete = True

    if st.session_state.get("confirm_delete", False):

       st.warning("⚠️ This will permanently delete all chats.")

       col1, col2 = st.columns(2)

       with col1:
        if st.button("✅ Yes"):
            st.session_state.chat_sessions = []
            st.session_state.conversation_history = []
            st.session_state.message_count = 0
            st.session_state.confirm_delete = False
            st.rerun()

       with col2:
        if st.button("❌ No"):
            st.session_state.confirm_delete = False
            st.rerun()

    st.markdown("---")

    if st.session_state.conversation_history:

     chat_text = ""

     for msg in st.session_state.conversation_history:

        role = "👤 User" if msg["role"] == "user" else "🤖 AI"

        chat_text += f"{role}\n"
        chat_text += f"{msg['content']}\n"
        chat_text += "-" * 50 + "\n"

     st.download_button(
        label="📄 Download Chat",
        data=chat_text,
        file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain",
        use_container_width=True
     )

    st.markdown("---")

    st.markdown("---")

    if st.button("🔄 Regenerate Response", use_container_width=True):

     if st.session_state.last_user_prompt != "":

        # Remove the last AI response
        if (
            len(st.session_state.conversation_history) > 0
            and st.session_state.conversation_history[-1]["role"] == "assistant"
        ):
            st.session_state.conversation_history.pop()

        with st.spinner("Regenerating response..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": msg["role"],
                        "content": msg["content"]
                    }
                    for msg in st.session_state.conversation_history
                ]
            )

            ai_reply = response.choices[0].message.content

        st.session_state.conversation_history.append({
            "role": "assistant",
            "content": ai_reply,
            "time": datetime.now().strftime("%I:%M %p")
        })

        st.rerun()

    st.markdown("**📊 Session Stats**")
    st.markdown(f"""
        <div class='stat-box'>💬 Messages: {st.session_state.message_count}</div>
        <div class='stat-box'>🧠 Memory: Active ✅</div>
        <div class='stat-box'>⚡ Llama 3.3 70B</div>
        <div class='stat-box'>🟢 Status: Online</div>
    """, unsafe_allow_html=True)

    
    st.markdown("---")
    st.markdown("**📜 Previous Chats**")

    if len(st.session_state.chat_sessions) == 0:
     st.markdown(
        "<p style='color:#64748b; font-size:0.82em;'>No history yet.<br>Click New Conversation to save!</p>",
        unsafe_allow_html=True
     )

    else:
     recent_sessions = st.session_state.chat_sessions[-5:]

     for i, session in enumerate(reversed(recent_sessions)):

        actual_index = len(st.session_state.chat_sessions) - 1 - i

        st.markdown(f"""
        <div class='history-item'>
            🕐 {session['time']}<br>
            💬 {session['messages']} messages
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("📂 Load", key=f"load_{actual_index}"):
                st.session_state.conversation_history = session["history"].copy()
                st.session_state.message_count = session["messages"]
                st.rerun()

        with col2:
            if st.button("🗑 Delete", key=f"delete_{actual_index}"):
                del st.session_state.chat_sessions[actual_index]
                st.rerun()


    st.markdown("---")
    st.markdown("<p style='color:#64748b; font-size:0.78em;'>💡 Memory is active during this session.</p>", unsafe_allow_html=True)

# STEP 6: Main header
st.markdown("""
    <div class='main-header'>
        <span class='main-title'>🤖 Custom AI Chatbot</span>
        &nbsp;<span class='badge'>● ONLINE</span>
    </div>
    <div class='main-subtitle'>Decode Labs &nbsp;·&nbsp; Generative AI Internship Project 1 &nbsp;·&nbsp; Powered by Groq + Llama 3.3</div>
""", unsafe_allow_html=True)

st.divider()


# STEP 7: Compact Welcome Screen

if len(st.session_state.conversation_history) == 0:

    st.markdown("""
    <div style="
        text-align:center;
        padding:15px 0;
    ">

    <h2 style="
        color:white;
        margin-bottom:8px;
    ">
    Welcome! How can I help you today?
    </h2>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        display:flex;
        justify-content:center;
        gap:25px;
        flex-wrap:wrap;
        color:#60a5fa;
        font-size:17px;
        font-weight:600;
        margin-bottom:20px;
    ">

    <span>🧠 Memory</span>

    <span>⚡ Fast</span>

    <span>📄 File Upload</span>

    <span>💬 History</span>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

# STEP 8: Display messages
for message in st.session_state.conversation_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "time" in message:
            st.caption(f"🕐 {message['time']}")


# ==============================
# STEP 9: File Upload + Chat Input
# ==============================

col1, col2 = st.columns([1, 6])

# ---------- File Upload ----------
uploaded_file = st.file_uploader(
    "📎 Upload a document (PDF, TXT, DOCX)",
    type=["pdf", "txt", "docx"]
)

uploaded_text = ""

if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        for page in pdf:
            uploaded_text += page.get_text()

    elif uploaded_file.type == "text/plain":
        uploaded_text = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(uploaded_file)

        for para in doc.paragraphs:
            uploaded_text += para.text + "\n"

    st.success("✅ File uploaded successfully!")

# ---------- Chat Input ----------
user_input = st.chat_input(
    "Message Custom AI Chatbot...",
    key="chat_input"
)

# ---------- Send Message ----------
if user_input and user_input.strip() != "":

    st.session_state.last_user_prompt = user_input

    current_time = datetime.now().strftime("%I:%M %p")

    # Show user message
    with st.chat_message("user"):
        st.write(user_input)
        st.caption(f"🕐 {current_time}")

    # Save user message
    st.session_state.conversation_history.append({
        "role": "user",
        "content": user_input,
        "time": current_time
    })

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            messages = []

            # Add uploaded document as system prompt
            if uploaded_text != "":
                messages.append({
                    "role": "system",
                    "content": f"""
You are an AI assistant.

Answer the user's questions using ONLY the uploaded document whenever possible.

Uploaded Document:

{uploaded_text}
"""
                })

            # Add conversation history
            messages.extend([
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.conversation_history
            ])

            # Call Groq
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )

            ai_reply = response.choices[0].message.content

        st.write(ai_reply)
        st.caption(f"🕐 {datetime.now().strftime('%I:%M %p')}")

    # Save AI response
    st.session_state.conversation_history.append({
        "role": "assistant",
        "content": ai_reply,
        "time": datetime.now().strftime("%I:%M %p")
    })

    st.session_state.message_count += 1