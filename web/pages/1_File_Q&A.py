import streamlit as st
import anthropic
from openai import OpenAI
from groq import Groq
import PyPDF2
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from global_var import saved_text


with st.sidebar:
    #anthropic_api_key = st.text_input("Anthropic API Key", key="file_qa_api_key", type="password")
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    #groq_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    

st.title("📝 File Q&A with Anthropic")
uploaded_file = st.file_uploader("Upload an article", type=("txt", "pdf"))
# question = st.text_input(
#    "Ask something about the article",
#    placeholder="Can you give me a short summary?",
#    disabled=not uploaded_file,
#) 
myprompt =("You're an advanced data processing AI,"+
            "allocated with the task of extracting only programming-related topics from a PDF document outlining a course curriculum."+
            "Your goal is to generate a bullet list specifically highlighting the topics that will be learned in the programming course."+
            "Ensure to remove any irrelevant titles, such as general introductions, assessments unrelated to programming, or vague topics, leaving behind a concise and focused list of programming concepts and subjects covered in the course."+
            "Please extract the topics related to programming from the given PDF document and present them in a clear, itemized format without including unrelated or generic titles without a Preliminary response.")


if uploaded_file  and not openai_api_key:
    st.info("Please add your openAI API key to continue.")

def extract_text_from_pdf(pdf):
    pdf_text = ""
    reader = PyPDF2.PdfReader(pdf)
    for page in reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

if uploaded_file and openai_api_key:
    text = extract_text_from_pdf(uploaded_file)
    st.text(text)
    client = OpenAI(api_key=openai_api_key)
    #client = Groq(api_key=groq_api_key)

    #client.chat
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {text}"},
            {"role": "user", "content": myprompt}
        ]
    )
    st.text(response)
    saved_text.update_string(response)

st.page_link("pages/7_Show_checkbox.py",label="checkbox")
    # response.choices[0].message['content']
    # response = bot.file
    # st.session_state.messages.append({"role": "user", "content": prompt})
    # st.chat_message("user").write(prompt)
    # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    # msg = response.choices[0].message.content
    # st.session_state.messages.append({"role": "assistant", "content": msg})
    # st.chat_message("assistant").write(msg)
st.sidebar.page_link("pages/1_File_Q&A.py", label="enter a silbus",disabled=True)
st.sidebar.page_link("pages/2_Chat_with_search.py", label="option 2")
st.sidebar.page_link("pages/3_Langchain_Quickstart.py", label="option 3")
st.sidebar.page_link("pages/4_Langchain_PromptTemplate.py", label="option 4")
st.sidebar.page_link("pages/5_Chat_with_user_feedback.py", label="option 5")
st.sidebar.page_link("pages/6_Chatbot.py", label="option 6")
st.sidebar.page_link("home.py", label="log out")
