#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit
#from openai import OpenAI

#from dotenv import load_dotenv
#load_dotenv()

from langchain_openai import ChatOpenAI
import streamlit as st

# It's good practice to initialize the model outside the main app flow
chat_model = ChatOpenAI()

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")

# You can display the subject only if it has been entered
if subject:
    st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    if subject:
        with st.spinner("시 작성중 ..."):
            result = chat_model.invoke(subject + "에 대한 시를 써줘")
            st.write(result.content)
    else:
        # Handle case where the button is clicked without a subject
        st.warning("시의 주제를 먼저 입력해주세요.")

