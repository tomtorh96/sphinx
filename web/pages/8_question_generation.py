import streamlit as st
from openai import OpenAI
from groq import Groq
import sys
import os
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import global_var as var
st.title("📝 Question generation")
st.sidebar.page_link("home.py", label="log out")
st.sidebar.page_link("pages/1_File_Q&A.py", label="enter a silbus")
with st.sidebar:
    #anthropic_api_key = st.text_input("Anthropic API Key", key="file_qa_api_key", type="password")
    groq_api_key = st.text_input("Groq API Key", key="chatbot_api_key", type="password",value="a")
groqKey ="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"
prompt = f"""
Create a multiple-choice question for python programming course. only on this given subject{var.saved_topics.get_array}. Format the question and answers as follows:

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
import re

def extract_questions_and_answers(text):
    # Define the regular expression patterns for questions and answers
    question_pattern = r'^\d+\.\s*(.*?)\n'
    answer_pattern = r'^[A-D]\)\s*(.*?)(?:\n|$)'

    # Split the text into individual questions using a regular expression
    question_blocks = re.split(r'(?=\d+\.\s)', text, flags=re.MULTILINE)

    # Initialize lists to store the questions and answers
    questions = []
    answers = []

    for block in question_blocks:
        if block.strip():  # Skip any empty blocks
            # Extract the question
            question_match = re.search(question_pattern, block, re.MULTILINE)
            question = question_match.group(1) if question_match else None
            
            # Extract the answers
            answer_matches = re.findall(answer_pattern, block, re.MULTILINE)
            
            # Append the extracted question and answers to the lists
            if question:
                questions.append(question)
                answers.append(answer_matches)

    return questions, answers


if groq_api_key:
  client = Groq(
    api_key=groqKey,)
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
    temperature=0.05,
    max_tokens=3200,
    top_p=1,
    )
  text =chat_completion.choices[0].message.content
  #questions, answers = extract_questions_and_answers(text)
  questions = ["What is the capital of France?","Which planet is known as the Red Planet?"]
  answers = [["Berlin","Madrid","Paris","Rome"],["Earth","Mars","Jupiter","Saturn"]]
  q_a =""
  num_tabs = int(len(questions)/10)
  tab_names = [f"page {i+1}" for i in range(num_tabs + 1)]

  # Create tabs
  tabs = st.tabs(tab_names)

  # Add content to tabs
  for tab in tabs:
    with tab:
      for i in range(int(len(questions)%10)):
        q_a += f"Question {i + 1}: {questions[i]}\n\n"
        #print(f"Question {i + 1}: {questions[i]}")
        for j, answer in enumerate(answers[i]):
            #print(f"{chr(65 + j)}) {answer}")
            q_a +=f"{chr(65 + j)}) {answer}\n\n"
        with st.container(height= 225):
          st.markdown(q_a)
        q_a =""    