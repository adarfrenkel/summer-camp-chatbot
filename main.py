import os

import ApplicationPrompt
import QuestionPrompt
import RouterPrompt
import streamlit as st
import openai

openai_api_key = os.environ["OPENAI_API_KEY"]

if __name__ == '__main__':
    input_data = ""
    response = ""
    doneApplication = False
    st.title("☀️🏕️  GenAi Chatbot Assistant  🛶🏖")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("OpenAI API key is missing.")
            st.stop()

        openai.api_key = openai_api_key
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        intent, question = RouterPrompt.complete(prompt)
        if intent == "ASK":
            response = QuestionPrompt.complete(prompt)
        elif intent == "ENROLL":
            enrollPrompt = "Please provide the following information: your full name, phone number, email, and your kid age."
            st.session_state.messages.append({"role": "assistant", "content": enrollPrompt})
            st.chat_message("assistant").write(enrollPrompt)
            response = ApplicationPrompt.complete(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

    print("context refresh")