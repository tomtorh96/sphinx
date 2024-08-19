import streamlit as st
#from langchain.llms import OpenAI
#from langchain.prompts import PromptTemplate
st.sidebar.page_link("pages/1_syllabus_extractor.py", label="question generation")
st.sidebar.page_link("pages/2_Chat_with_search.py", label="option 2")
st.sidebar.page_link("pages/3_Langchain_Quickstart.py", label="option 3")
st.sidebar.page_link("pages/4_Langchain_PromptTemplate.py", label="option 4",disabled=True)
st.sidebar.page_link("pages/5_Chat_with_user_feedback.py", label="option 5")
st.sidebar.page_link("pages/6_Chatbot.py", label="option 6")
st.sidebar.page_link("home.py", label="log out")
# st.title("🦜🔗 Langchain - Blog Outline Generator App")

# openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


# def blog_outline(topic):
#     # Instantiate LLM model
#     llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
#     # Prompt
#     template = "As an experienced data scientist and technical writer, generate an outline for a blog about {topic}."
#     prompt = PromptTemplate(input_variables=["topic"], template=template)
#     prompt_query = prompt.format(topic=topic)
#     # Run LLM model
#     response = llm(prompt_query)
#     # Print results
#     return st.info(response)


# with st.form("myform"):
#     topic_text = st.text_input("Enter prompt:", "")
#     submitted = st.form_submit_button("Submit")
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#     elif submitted:
#         blog_outline(topic_text)
# st.sidebar.page_link("home.py", label="log out")
st.title("comming soon")
st.header("function not realized will be in the futre :wink:")