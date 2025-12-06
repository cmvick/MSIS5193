#pips to install for anaconda powershell
#pip install langchain_groq
#pip install fritz

from langchain_groq import ChatGroq
import streamlit as st
import fitz


GROQ_API_KEY = "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"  # <- API key here
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0
)


# Streamlit question
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
