import streamlit as st
import sys
import os


# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import global_var as var
st.sidebar.page_link("home.py", label="log out")
st.sidebar.page_link("pages/1_File_Q&A.py", label="enter a silbus")
st.markdown("select the topics to create questions from")
# need to see how to add 2 button to select all and unselect all
if "bool" not in st.session_state:
    st.session_state.bool = None
st.session_state._bool = False
def setbool():
    st.session_state.bool = st.session_state._bool
def setChceckBox(bool):
    st.session_state.bool = bool
col = st.columns(3)
if col[0].button("select all"):
    setChceckBox(True)
if col[1].button("unselect all"):
    setChceckBox(False)
col[2].text(st.session_state.bool)
temptext = var.saved_array.get_array()
temp = []
for subject in temptext:
    if st.checkbox(subject,value=st.session_state.bool):
        temp.append(subject) 
if st.button("confirm"):
    var.saved_topics.set_array([])
    for x in temp:
        st.write(x)
        var.saved_topics.add_to_array(x)
    st.switch_page("pages/8_question_generation.py")
