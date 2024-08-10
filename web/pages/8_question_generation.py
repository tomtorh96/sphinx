import streamlit as st
from openai import OpenAI
from groq import Groq
import sys
import os
import re
import datetime as dt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import global_var as var
st.title("📝 Question generation")
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", key="chatbot_api_key", type="password",value="a")
st.sidebar.page_link("home.py", label="log out")
st.sidebar.page_link("pages/1_File_Q&A.py", label="back to entering a silbus")


groqKey ="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"
prompt = f"""
Create 25 multiple-choice questions for python programming course. only on these given subjects{var.saved_topics.get_array()}. Format the question and answers as follows:

- Start with "X." (where X is the question number) followed by the Provide the question text.
- List the answers in a numbered format:
  - "A)"
  - "B)"
  - "C)"
  - "D)"
- After that the correct answer which formated like:
 "*Y"(where Y is the correct answers letter)
The text should be clear and understandable. Do not include any additional text outside of the question and answers.

Example:
1. what is 1+1
A) 1
B) 2
C) 3
D) 4
*B

remove the first line of the return.
"""
content = """You're a seasoned educator with a strong background in computer science,
 specializing in creating engaging and informative multi-choice questions for programming concepts.
   Your expertise lies in crafting questions that effectively assess a learner's understanding of programming languages,
     data structures, and software development principles"""
import re
if "bool" not in st.session_state:
    st.session_state.bool = None
st.session_state._bool = False
def setbool():
    st.session_state.bool = st.session_state._bool
def setChceckBox(bool):
    st.session_state.bool = bool

def save_to_folder(arrayQ,arrayA,arrayC):
  if arrayQ is None or arrayA is None or len(arrayQ) != len(arrayA):
      return
  myDate = dt.datetime.now()
  name = f"Quiz-{dt.date.today()}_{myDate.hour}-{myDate.minute}-{myDate.second}"
  quizName = f"{name}.txt"
  answersName = f"{name}-solution.txt"
  file_path = os.path.join("C:\\Users","ASUS", "Desktop","Seminar","Output",quizName)#change to the path you want to got to
  #print(file_path)
  # with open(file_path, 'w') as file:
  #     for i, question in enumerate(arrayQ):
  #       file.write(f"Question {i + 1}: {question}\n")
  #       for j, answer in enumerate(arrayA[i]):
  #           file.write(f"{chr(65 + j)}) {answer}\n")
  #       file.write("\n")
  with open(file_path,'w') as file:
    for i, question in enumerate(arrayQ):
      file.write(f"question {i+1}) {question}\n")
      for j, answer in enumerate(arrayA[i]):
        file.write(f"{chr(65+j)}) {answer}\n")
      file.write("\n")
  

  file_path = os.path.join("C:\\Users","ASUS", "Desktop","Seminar","Output",answersName)
  with open(file_path,'w') as file:
     file.write("the solution for the quiz:\n")
     for k,answer in enumerate(arrayC):
        file.write(f"{k+1}) {answer}\n")
def extract_questions_and_answers(text):
    # Define the regular expression patterns for questions and answers
    question_pattern = r'^\d+\.\s*(.*?)\n'
    answer_pattern = r'^[A-D]\)\s*(.*?)(?:\n|$)'
    correct_answer_pattern = r'\*(\b[A-D]\b)'
    # Split the text into individual questions using a regular expression
    question_blocks = re.split(r'(?=\d+\.\s)', text, flags=re.MULTILINE)

    # Initialize lists to store the questions and answers
    questions = []
    answers = []
    correct_answers = []
    for block in question_blocks:
        if block.strip():  # Skip any empty blocks
            # Extract the question
            question_match = re.search(question_pattern, block, re.MULTILINE)
            question = question_match.group(1) if question_match else None
            # Extract the answers
            answer_matches = re.findall(answer_pattern, block, re.MULTILINE)
            correct_answer_match = re.search(correct_answer_pattern, block, re.MULTILINE)
            correct_answer = correct_answer_match.group(1) if correct_answer_match else None
            # Append the extracted question and answers to the lists
            if question:
                questions.append(question)
                answers.append(answer_matches)
                correct_answers.append(correct_answer)
    return questions, answers,correct_answers
if groq_api_key:
  client = Groq(api_key=groqKey,)
  chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": content
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
    model="llama3-8b-8192",
    temperature=0.02,
    max_tokens=3200,
    top_p=1,)
  text = chat_completion.choices[0].message.content.strip()

  questions, answers,correct_answers = extract_questions_and_answers(text)
  #q_a =""
  #TODO  remove print(questions)
  col = st.columns(2)
  if col[0].button("select all"):
    setChceckBox(True)
  if col[1].button("unselect all"):
    setChceckBox(False)
  
  tabsize = 10
  num_tabs = int(len(questions)/tabsize)
  tab_names = [f"page {i+1}" for i in range(num_tabs + 1)]
  arrayQ = []
  arrayA = []
  arrayC = []
  # Create tabs
  tabs = st.tabs(tab_names)
  # Add content to tabs
  for t, tab in enumerate(tabs):
    with tab:
      for i in range(t*tabsize, min(len(questions),(t+1)*tabsize)):
        #q_a += f"Question {i + 1}: {questions[i]}\n\n"
        with st.container(height= 280):
          if st.checkbox("label",key = i ,label_visibility="collapsed",value=st.session_state.bool):
             arrayQ.append(questions[i])
             arrayA.append(answers[i])
             arrayC.append(correct_answers[i])
          st.markdown(f"Question {i + 1}: {questions[i]}")
          for j, answer in enumerate(answers[i]):
              #q_a +=f"{chr(65 + j)}) {answer}\n\n"
              st.markdown(f"{chr(65 + j)}) {answer}")
          #st.markdown(q_a)
        #q_a =""
if len(arrayQ) >0:
  disable = False
else:
  disable = True
with st.sidebar:
  if st.button(":printer:",disabled=disable):
      save_to_folder(arrayQ,arrayA,arrayC)
      st.success("file saved")