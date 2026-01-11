import streamlit as st

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 Conversational AI Chatbot")
st.caption("Built using Python + Streamlit")

def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "bye": "Goodbye! Have a nice day!",
        "help": "I can answer basic questions.",
        "who are you": "I am a chatbot developed by Shivani."
    }
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")

# 👉 chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# 👉 input box
user_input = st.text_input("You:")

# 👉 when user types something
if user_input:
    reply = chatbot_response(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", reply))

# 👉 DISPLAY CHAT (THIS WAS MISSING)
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
