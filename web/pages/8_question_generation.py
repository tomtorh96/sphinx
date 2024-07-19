import streamlit as st
from openai import OpenAI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import global_var as var
st.title("📝 Question generation")
with st.sidebar:
    #anthropic_api_key = st.text_input("Anthropic API Key", key="file_qa_api_key", type="password")
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

prompt = f"""
Create a multiple-choice question for python programming course. only on this given subject{var.saved_array.get_array}. Format the question and answers as follows:

- Start with "Question X:" (where X is the question number).
- Provide the question text.
- List the answers in a numbered format:
  - "A)"
  - "B)"
  - "C)"
  - "D)"

The text should be clear and understandable. Do not include any additional text outside of the question and answers.

Example subject: "Python Functions"
"""
content = """You're a seasoned educator with a strong background in computer science,
 specializing in creating engaging and informative multi-choice questions for programming concepts.
   Your expertise lies in crafting questions that effectively assess a learner's understanding of programming languages,
     data structures, and software development principles"""

# if openai_api_key:
#     client = OpenAI(api_key=openai_api_key)
#     #client.chat
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": content},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     st.text(response)
st.text("questions go here :)")