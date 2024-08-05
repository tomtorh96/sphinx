from openai import OpenAI
import streamlit as st
from streamlit_feedback import streamlit_feedback
import trubrics
st.sidebar.page_link("pages/1_File_Q&A.py", label="enter a silbus")
st.sidebar.page_link("pages/2_Chat_with_search.py", label="option 2")
st.sidebar.page_link("pages/3_Langchain_Quickstart.py", label="option 3")
st.sidebar.page_link("pages/4_Langchain_PromptTemplate.py", label="option 4")
st.sidebar.page_link("pages/5_Chat_with_user_feedback.py", label="option 5",disabled=True)
st.sidebar.page_link("pages/6_Chatbot.py", label="option 6")
st.sidebar.page_link("home.py", label="log out")
# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="feedback_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/5_Chat_with_user_feedback.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# st.title("📝 Chat with feedback (Trubrics)")

# """
# In this example, we're using [streamlit-feedback](https://github.com/trubrics/streamlit-feedback) and Trubrics to collect and store feedback
# from the user about the LLM responses.
# """

# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "assistant", "content": "How can I help you? Leave feedback to help me improve!"}
#     ]
# if "response" not in st.session_state:
#     st.session_state["response"] = None

# messages = st.session_state.messages
# for msg in messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input(placeholder="Tell me a joke about sharks"):
#     messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)

#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()
#     client = OpenAI(api_key=openai_api_key)
#     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
#     st.session_state["response"] = response.choices[0].message.content
#     with st.chat_message("assistant"):
#         messages.append({"role": "assistant", "content": st.session_state["response"]})
#         st.write(st.session_state["response"])

# if st.session_state["response"]:
#     feedback = streamlit_feedback(
#         feedback_type="thumbs",
#         optional_text_label="[Optional] Please provide an explanation",
#         key=f"feedback_{len(messages)}",
#     )
#     # This app is logging feedback to Trubrics backend, but you can send it anywhere.
#     # The return value of streamlit_feedback() is just a dict.
#     # Configure your own account at https://trubrics.streamlit.app/
#     if feedback and "TRUBRICS_EMAIL" in st.secrets:
#         config = trubrics.init(
#             email=st.secrets.TRUBRICS_EMAIL,
#             password=st.secrets.TRUBRICS_PASSWORD,
#         )
#         collection = trubrics.collect(
#             component_name="default",
#             model="gpt",
#             response=feedback,
#             metadata={"chat": messages},
#         )
#         trubrics.save(config, collection)
#         st.toast("Feedback recorded!", icon="📝")
# st.sidebar.page_link("home.py", label="log out")
st.title("comming soon")
st.header("function not realized will be in the futre :wink:")