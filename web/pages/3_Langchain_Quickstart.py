import streamlit as st
from langchain.llms import OpenAI
st.sidebar.page_link("pages/1_File_Q&A.py", label="enter a silbus")
st.sidebar.page_link("pages/2_Chat_with_search.py", label="option 2")
st.sidebar.page_link("pages/3_Langchain_Quickstart.py", label="option 3",disabled=True)
st.sidebar.page_link("pages/4_Langchain_PromptTemplate.py", label="option 4")
st.sidebar.page_link("pages/5_Chat_with_user_feedback.py", label="option 5")
st.sidebar.page_link("pages/6_Chatbot.py", label="option 6")
st.sidebar.page_link("home.py", label="log out")
# st.title("🦜🔗 Langchain Quickstart App")

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


# def generate_response(input_text):
#     llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#     st.info(llm(input_text))


# with st.form("my_form"):
#     text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
#     submitted = st.form_submit_button("Submit")
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#     elif submitted:
#         generate_response(text)
# st.sidebar.page_link("home.py", label="log out")
st.title("comming soon")
st.header("function not realized will be in the futre :wink:")