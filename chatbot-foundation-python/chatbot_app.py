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
        "who are you": "This chatbot is developed by Shivani."
    }
    return responses.get(user_input.lower(), "Sorry, I didn't understand that.")
    
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You:")
if user_input:
    reply = chatbot_response(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", reply))

for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")


