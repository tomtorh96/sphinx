import streamlit as st
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import global_var as var
st.sidebar.page_link("home.py", label="log out")
st.sidebar.page_link("1_File_Q&A.py", label="go to start")
temp = {}
temptext = "hi#bye#lol#tot"
newtemp=[]
arr = temptext.split("#")
for subject in arr:
    temp.update({subject:st.checkbox(subject,value=False)})
if st.button("button"):
    for x in temp.keys():
        if temp.get(x):
            st.write(x)
            newtemp.append(x)
            var.saved_array.add_to_array(x)
if newtemp is not None:
    #st.write(newtemp)
    st.page_link("pages/8_question_generation.py",label="question")
#st.write(var.saved_text.get_string())