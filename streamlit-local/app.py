# https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/
import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index import SimpleDirectoryReader

from llama_index.llms import Ollama

llm = Ollama(model="zephyr")
system_prompt = \
    "You are an expert on Linus Torvalds and your job is to answer questions about him." \
    "Assume that all questions are related to Linus Torvalds or Linux." \
    "Keep your answers brief and based on facts – do not hallucinate facts."

st.header("Everything you want to know about Linux or Linus")

if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Linus or Linux"}
    ]


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the document data – might take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./docs", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=Ollama(model="zephyr"), embed_model="local", system_prompt=system_prompt)
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

chat_engine = index.as_chat_engine(
    chat_mode="react", verbose=True
)

if prompt := st.chat_input("Ask me a question about Linus or Linux"): 
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Querying..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
