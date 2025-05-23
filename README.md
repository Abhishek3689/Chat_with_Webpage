# 💬 WebChat – Chat with Any URL

A simple Streamlit app that lets you chat with content from any URL by loading the webpage, indexing it, and answering questions using retrieval-augmented generation (RAG).

---

## 🚀Features

- Enter any public URL (e.g., news article, blog post)
- App loads and processes the content
- Ask questions about the page in a chat interface
- Uses LangChain, FAISS, and HuggingFace embeddings for semantic search
- Clean and responsive UI built with Streamlit

---

  ### Libraries:
- streamlit
- langchain
- langchain-community
- langchain-core
- langchain-groq
- transformers
- sentence-transformers
- faiss (or another vector database)
- beautifulsoup4 (for web scraping)
- requests

## Setup

1. **Clone the Repository**
```
git clone https://github.com/Abhishek3689/Chat_with_Webpage.git
```

2. **Install Dependencies**
```
pip install -r requirements.txt
```
3. **Configure Environment:**
- Add API keys in .env file for the LLM if required (e.g., OpenAI API Key)
- Add Groq Api keys if using Groq inference.

4. **Run The Application**
```
streamlit run web_chat.py
```
