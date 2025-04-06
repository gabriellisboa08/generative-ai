import streamlit as st
from src.data_processing.AIResponseProcessor import AIResponseProcessor
import shelve

class Chatbot:
    USER_AVATAR = "👤"
    BOT_AVATAR = "🤖"

    def __init__(self):
        st.title("Jtech Chatbot")
        self.initialize_chat_history()
        self.setup_sidebar()
        self.display_chat_messages()
        self.main_chat_interface()
        self.save_chat_history()

    def load_chat_history(self):
        with shelve.open("chat_history") as db:
            return db.get("messages", [])

    def save_chat_history(self):
        with shelve.open("chat_history") as db:
            db["messages"] = st.session_state.messages

    def initialize_chat_history(self):
        if "messages" not in st.session_state:
            st.session_state.messages = self.load_chat_history()

    def setup_sidebar(self):
        with st.sidebar:
            if st.button("Delete Chat History"):
                st.session_state.messages = []
                self.save_chat_history()

    def display_chat_messages(self):
        for message in st.session_state.messages:
            avatar = self.USER_AVATAR if message["role"] == "user" else self.BOT_AVATAR
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])

    def main_chat_interface(self):
        if prompt := st.chat_input("Como posso ajudar?"):
            # Adicionar a mensagem do usuário ao histórico
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Exibir a mensagem do usuário na interface
            with st.chat_message("user", avatar=self.USER_AVATAR):
                st.markdown(prompt)

            # Processar a resposta da IA
            ia_response = AIResponseProcessor().process_input_and_generate_response(prompt)

            # Adicionar a resposta da IA ao histórico
            st.session_state.messages.append({"role": "assistant", "content": ia_response})

            # Exibir a resposta da IA na interface
            with st.chat_message("assistant", avatar=self.BOT_AVATAR):
                st.markdown(ia_response)

if __name__ == "__main__":
    Chatbot()