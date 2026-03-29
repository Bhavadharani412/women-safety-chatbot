import streamlit as st
import ollama

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Women Safety Chatbot",
    page_icon="🛡",
    layout="wide"
)

# -------------------- HEADER --------------------
st.title("🛡 Women Safety Awareness Chatbot")
st.markdown("Ask about **safety, emergencies, travel, or online harassment.**")

# -------------------- SIDEBAR --------------------
st.sidebar.title("🚨 Emergency Help")

st.sidebar.markdown("### India Helpline Numbers")
st.sidebar.info("""
📞 Emergency: 112  
📞 Women Helpline: 1091  
📞 Women Helpline (All India): 181  
📞 Police: 100  
""")

st.sidebar.success("Stay aware. Stay safe. 💜")

# -------------------- SESSION STATE --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- DISPLAY CHAT HISTORY --------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------- SYSTEM PROMPT --------------------
SYSTEM_PROMPT = """
You are a women safety assistant.

Your responsibilities:
- Provide safety tips
- Share emergency contacts (India priority)
- Help in unsafe situations
- Give travel safety advice
- Guide on online harassment

Rules:
- Be clear and supportive
- If situation is dangerous, prioritize emergency help
- Keep answers short and practical
"""

# -------------------- HELPER FUNCTION --------------------
def get_ai_response(user_input):
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages

        response = ollama.chat(
            model="phi3",
            messages=messages
        )

        return response["message"]["content"]

    except Exception as e:
        return "⚠️ Error connecting to AI. Make sure Ollama is running."

# -------------------- SMART SAFETY DETECTION --------------------
def check_emergency(text):
    danger_keywords = ["help", "danger", "follow", "stalk", "attack", "unsafe"]

    for word in danger_keywords:
        if word in text.lower():
            return True
    return False

# -------------------- CHAT INPUT --------------------
user_input = st.chat_input("Ask about women safety...")

if user_input:

    # Save & display user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Emergency alert
    if check_emergency(user_input):
        st.warning("🚨 If you are in immediate danger, call 112 right now!")

    # Get AI response
    bot_reply = get_ai_response(user_input)

    # Save & display bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# -------------------- CLEAR CHAT BUTTON --------------------
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()