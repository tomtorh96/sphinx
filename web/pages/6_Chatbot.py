from openai import OpenAI
import streamlit as st
st.sidebar.page_link("pages/1_syllabus_extractor.py", label="enter a silbus")
st.sidebar.page_link("pages/2_Chat_with_search.py", label="option 2",disabled=True)
st.sidebar.page_link("pages/3_Langchain_Quickstart.py", label="option 3")
st.sidebar.page_link("pages/4_Langchain_PromptTemplate.py", label="option 4")
st.sidebar.page_link("pages/5_Chat_with_user_feedback.py", label="option 5")
st.sidebar.page_link("pages/6_Chatbot.py", label="option 6")
st.sidebar.page_link("home.py", label="log out")
# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# st.title("💬 Chatbot")
# st.caption("🚀 A Streamlit chatbot powered by OpenAI")
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input():
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()

#     client = OpenAI(api_key=openai_api_key)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)
# st.sidebar.page_link("home.py", label="log out")
st.title("comming soon")
st.header("function not realized will be in the futre :wink:")