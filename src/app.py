import streamlit as st
from AIResponseProcessor import AIResponseProcessor
import shelve


st.title("Jtech Chatbot")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"



# Load chat history from shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])


# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages


# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])

# Display chat messages
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("Como posso ajudar?"):
    # Adicionar a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Exibir a mensagem do usuário na interface
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    # Processar a resposta da IA
    
    ia_response = AIResponseProcessor().process_input_and_generate_response(prompt)

    # Adicionar a resposta da IA ao histórico
    st.session_state.messages.append({"role": "assistant", "content": ia_response})

    # Exibir a resposta da IA na interface
    with st.chat_message("assistant", avatar=BOT_AVATAR):
        st.markdown(ia_response)

save_chat_history(st.session_state.messages)