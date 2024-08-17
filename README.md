# 🎈 Sphinx

## Overview of the Sphinx

This app showcases a use of LLM to create questions for teacters.

## Get an Groq API key

You can get your own Groq API key by following the following instructions:

1. Go to https://console.groq.com/keys.
2. login to your accunt
2. Click on the `Create API key` button.
3. Next, enter an identifier name (optional) and click on the `submit` button.

## How can setup this in visual studio code (in windows)
1.  Download the latest python version and find where was it installed
2.  Uninstall python that was installed in the Microsoft store(if there is)
3.  Search and Open `edit the system environment variables`
4.  Click on environment variables
5.  In the variable PATH select it and click edit
6.  Add the path where your python is located and add also the scripes folder in the python folder
7.  Click ok on all the windoes to exit the system environment variables
8.  Reopen visual studio code hit `Shift + '>'` and search "python: select interpreter"
9.  Select the newest version of python that you have installed, it will also recomaned you to select it.
10. Now you can install all the libraries that were used and run streamlit 
11. Run these commands to install all the libraries and then to run the program
```sh
pip install -r requirements.txt
cd .\web\
streamlit run home.py
```
