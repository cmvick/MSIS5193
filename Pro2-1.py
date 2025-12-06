#%pip install langchain-ollama

from langchain_ollama import ChatOllama
import streamlit as st
import fitz

llm = ChatOllama(model = 'llama3.2:1b', temperature = 0) 
# temperature is a common parameter from 0 to 1 that allows llm to be more verbose.
# example llm = ChatOllama(model = 'llama3', temperature = 1) ... I think 

# Streamlit question
st.title("Does this work")
text = st.text_input("Enter your question:")
context = st.file_uploader("Upload attachment:")


prompt = '''
Be polite and and don't provide information you don't know. If you don't know an answer, indicate that.

The <pdf> 
'''

#input_msg = prompt + text

if text:
    if context:
        doc = fitz.open(stream=context.read(), filetype='pdf')
        pdf = "".join(p.get_text() for p in doc)
        input_msg = prompt + pdf + text
        doc.close()
    else:
        input_msg = prompt + text
    st.header('AI Response:')
    ai_msg = llm.invoke(input_msg)

    st.write(ai_msg.content)




