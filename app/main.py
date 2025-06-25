import streamlit as st
from chatbot import get_response
from translator import translate
from prompts import get_persona_prompt

st.set_page_config(page_title="Diabetic Assistant Chatbot", page_icon="💬", layout="wide")

# Sidebar for settings and info
with st.sidebar:
    st.title("💬 Diabetic Assistant")
    st.markdown("""
    **A Gemini-powered chatbot for diabetes-related queries.**
    
    - Multi-language support
    - Choose a persona (General, Dietician, Doctor)
    - Export your chat
    """)
    language = st.selectbox("Choose your language", ["English", "Hindi", "Telugu", "Tamil"])
    prompt_type = st.selectbox("Choose persona", ["General", "Diabetes Dietician", "Doctor"])
    st.markdown("---")
    st.info("Your conversations are private and not stored.")

st.title("👩‍⚕️ Diabetic Assistant Chatbot")
st.markdown("""
Welcome! Ask any diabetes-related question below. Select your language and persona from the sidebar.
""")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Chat input area
with st.container():
    user_input = st.text_input("Type your question and press Enter:", key="user_input")
    send_col, export_col = st.columns([1, 1])
    send_clicked = send_col.button("Send", use_container_width=True)
    export_clicked = export_col.button("Export Chat", use_container_width=True)

    if send_clicked and user_input:
        translated_input = translate(user_input, language, "en")
        persona_prompt = get_persona_prompt(prompt_type)
        response = get_response(translated_input, persona_prompt, st.session_state['chat_history'])
        translated_response = translate(response, "en", language)
        st.session_state['chat_history'].append((user_input, translated_response))
        st.experimental_rerun()

    if export_clicked:
        chat_text = "\n".join([f"You: {q}\nBot: {a}" for q, a in st.session_state['chat_history']])
        st.download_button("Download Chat", chat_text, file_name="chat_history.txt")

# Chat history display with styled bubbles
st.markdown("## 🗨️ Chat History")
for i, (q, a) in enumerate(st.session_state['chat_history']):
    with st.container():
        st.markdown(f"<div style='background-color:#e1f5fe;padding:10px;border-radius:10px;margin-bottom:5px'><b>You:</b> {q}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color:#fff3e0;padding:10px;border-radius:10px;margin-bottom:15px'><b>Bot:</b> {a}</div>", unsafe_allow_html=True) 