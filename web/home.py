import streamlit as st
from menu import menu

def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("home.py", label="home page")
    st.sidebar.page_link("pages/1_File_Q&A.py", label="enter a silbus")
    st.sidebar.page_link("pages/2_Chat_with_search.py", label="option 2")
    st.sidebar.page_link("pages/3_Langchain_Quickstart.py", label="option 3")
    st.sidebar.page_link("pages/4_Langchain_PromptTemplate.py", label="option 4")
    st.sidebar.page_link("pages/5_Chat_with_user_feedback.py", label="option 5")
    st.sidebar.page_link("pages/6_Chatbot.py", label="option 6")
    st.sidebar.button("logout",key = 2,on_click=logout())

def logout():
    st.session_state.role = None


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("home.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("home.py")
 
# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None
if "user" not in st.session_state:
    st.session_state.user = None
# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role
st.session_state._user = st.session_state.user
def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role
def set_user():
    # Callback function to save the role selection to Session State
    st.session_state.user = st.session_state._user
# if "role" not in st.session_state:
#     st.session_state.role = None

username = st.session_state.user
password = ""
if st.session_state.role != "user":
    st.write("please enter your username and password")
    username =st.text_input("user name","")
    password =st.text_input("user password","",type="password")
    button = st.button("login",type="primary")
else:
    st.title(f":flag-il: welcome {username}")

if  password == "user" and button:
    st.session_state.role = "user"
    st.session_state.user = username
    st.rerun()
menu() # Render the dynamic menu!
