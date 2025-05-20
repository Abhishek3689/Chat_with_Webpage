import os
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
# from langchain_core.prompt import PromptTemplate

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[AIMessage(content='Hi I m bot . How may I help You')]

def get_response(user_input):
    return "I dont Know"

st.title("This is Homepage")
# st.text_input("Enter your question")
user_input=st.chat_input("Enter You Message Here")
if user_input:
    response=get_response(user_input)
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.chat_history.append(AIMessage(content=response))

## Conversation

for message in st.session_state.chat_history:
    if isinstance(message,AIMessage):
        with st.chat_message('AI'):
            st.write(message.content)
    if isinstance(message,HumanMessage):
        with st.chat_message('Human'):
            st.write(message.content)
    
with st.sidebar:
    st.write(st.session_state.chat_history)
with st.sidebar:
    url_input=st.text_input("Enter The Url")
    if url_input:
        st.write("Url is Inputed")
    else:
        st.write("Empty URL")

with st.sidebar:
    st.header("Upload your file")
    st.file_uploader('Upload')
    option_selected=st.selectbox(
        'Choose from below',
        ['PDF','EXCEL']
    )
    if option_selected=='PDF':
        st.write("Selected is PDF")
    else:
        st.write("Selected is EXCEL")

    st.subheader("Select from check box")
    check1=st.checkbox("Choose options 1")
    check2=st.checkbox("Choose options 2")
    if check1:
        st.write("checkbix first is seleted")
    else:
        st.write("checkbix second is seleted")