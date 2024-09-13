from langchain_community.llms.ollama import Ollama
import streamlit as st
import time
ollama = Ollama(base_url='http://localhost:11434',model='phi3:mini')

prompt= st.chat_input("Ask anything")
if prompt:
   with st.chat_message("user"):
      st.write(prompt)
   with st.spinner("............"):
      result = ollama.invoke(prompt)
      time.sleep(0.2)
      st.write(result)

