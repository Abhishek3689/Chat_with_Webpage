import os,time
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader,PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import streamlit as st
from langchain_core.messages import AIMessage,HumanMessage
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()
start=time.time()

## Load the LLM Model
llm=ChatGroq(
    model='llama3-70b-8192',
    temperature=0,
    max_tokens=None,
    max_retries=2,
    timeout=10
)


## Load the Embedding Model
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2')



if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]

if 'vector_store' not in st.session_state:
     st.session_state.vector_store=None

if 'chunks' not in st.session_state:
    st.session_state.chunks = None

## Load the memory
memory=ConversationBufferMemory(memory_key='chat_history', return_messages=True)


st.set_page_config(page_title='Chat with URL',page_icon='💬')
st.title("Welcome to WebChat")
user_input=st.chat_input("Enter the Question to ask :")
if user_input:
    
    if st.session_state.vector_store:
         ## Retriever
        retriever=st.session_state.vector_store.as_retriever(search_kwargs={"k":2})
        
        ## Conversation Chain
        conversation=ConversationalRetrievalChain.from_llm(
            memory=memory,
            llm=llm,
            retriever=retriever
            )
        
        ret_result=conversation.invoke(user_input)
        
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.chat_history.append(AIMessage(content=ret_result['answer']))

for message in st.session_state.chat_history:
    if isinstance(message,AIMessage):
        st.chat_message('AI')
        st.write(message.content)
    if isinstance(message,HumanMessage):
        st.chat_message('Human')
        st.write(message.content)


with st.sidebar:
    st.header("Step 1: Enter URL")
    url_link=st.text_input("Enter the URL to read :")
    if url_link:
        try:
            loader=WebBaseLoader(url_link)
            docs=loader.load()

            ## create chunks
            splitter=RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            st.session_state.chunks=splitter.split_documents(docs)

            ## Create Vector Store
            vector_store=FAISS.from_documents(
                documents=st.session_state.chunks,
                embedding=embeddings
            )
            st.session_state.vector_store=vector_store
           
            st.markdown("**Preview of Chunks**")
            st.write(st.session_state.chunks)
            
        except Exception as e:
            st.error(f"Error Loading URL:{e}")
    else:
        st.warning("Please Enter a valid URL .")
end=time.time()
st.write(f"Time Taken to complete the procss :{end-start}")