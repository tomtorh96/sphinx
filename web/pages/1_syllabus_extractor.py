import streamlit as st
from openai import OpenAI
from groq import Groq
import PyPDF2
import sys
import os
import re
import time
# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from global_var import saved_array
#TODO remove the groqkey and remove the value in the text input
groqKey ="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"

with st.sidebar:
    #anthropic_api_key = st.text_input("Anthropic API Key", key="file_qa_api_key", type="password")
    #openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    groq_api_key = st.text_input("Groq API Key", key="chatbot_api_key", type="password",value="a")
    

st.title("📝 Topics extractor")
uploaded_file = st.file_uploader("Upload an syllabus", type=("pdf"))
# question = st.text_input(
#    "Ask something about the article",
#    placeholder="Can you give me a short summary?",
#    disabled=not uploaded_file,
#)
myprompt = """
You are an advanced data processing AI assigned to extract programming-related topics from a PDF document outlining a course curriculum.

Objective: Generate a concise bullet-point list that specifically highlights the programming topics covered in the course.
The list should include only the core programming concepts with any subtopics condensed under the main subject title.

Instructions:
- Exclude irrelevant titles, such as general introductions, assessments not related to programming,
self-learning subjects,reading textbooks or bibliography,websites, or any vague or non-specific topics.
- If a subject has sub-subjects add a new line to the list with the format of "subject - sub-subject".
- dont name a programming langange
- Do not include any preliminary or concluding remarks.
- Ensure that the list is clear, focused and devoid of any non-programming content or titles that are not a subject.
- Present the programming topics in a clean, itemized format.
- Dont add the example to the output
example:
input:
Java - loop (for, while, do while)
output:
-loops - for
-loops - while
-loops - do while
"""

# def switch_page():
#     st.switch_page("pages/7_Show_checkbox.py")
topics =[]
saved_array.set_array([])
if uploaded_file  and not groq_api_key:
    st.info("Please add your Groq API key to continue.")

def extract_text_from_pdf(pdf):
    pdf_text = ""
    reader = PyPDF2.PdfReader(pdf)
    for page in reader.pages:
        pdf_text += page.extract_text()
    return pdf_text

if uploaded_file and groq_api_key:
    text = extract_text_from_pdf(uploaded_file)
    #st.text(text)
    client = Groq(
    api_key=groqKey,)
    #client = Groq(api_key=groq_api_key)

    #client.chat
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": myprompt
            },
            {
                "role": "user",
                "content": text,
            }
        ],
    model="llama3-8b-8192",
    temperature=0.02,
    max_tokens=3200,
    top_p=1,
    )
    text =chat_completion.choices[0].message.content.strip().split('\n')
    topics =[line.strip("• ").strip() for line in text[1:] if line.startswith('•')]
    saved_array.set_array(topics)
    if len(saved_array.get_array()) >0:
        with st.spinner("please wait"):
            time.sleep(2)
        st.markdown(f"process complete :smile::thumbsup:")
        if st.button("picking the topics",type="primary"):
            st.switch_page("pages/7_Show_checkbox.py")    
st.sidebar.page_link("pages/1_File_Q&A.py", label="enter a silbus",disabled=True)
st.sidebar.page_link("pages/2_Chat_with_search.py", label="option 2")
st.sidebar.page_link("pages/3_Langchain_Quickstart.py", label="option 3")
st.sidebar.page_link("pages/4_Langchain_PromptTemplate.py", label="option 4")
st.sidebar.page_link("pages/5_Chat_with_user_feedback.py", label="option 5")
st.sidebar.page_link("pages/6_Chatbot.py", label="option 6")
st.sidebar.page_link("home.py", label="log out")
