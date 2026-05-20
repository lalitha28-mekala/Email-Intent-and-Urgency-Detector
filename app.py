import os
from dotenv import load_dotenv

load_dotenv()

api_key =os.getenv('GROQ_API_KEY')

# ******Pip Install libraries****
# pip install python-dotenv
# pip install -U langchain-groq
# pip install streamlit


# llm
from langchain_groq import ChatGroq

llm= ChatGroq(
    model="openai/gpt-oss-120b")

# Output Parser

from langchain_core.output_parsers import JsonOutputParser
parser = JsonOutputParser()

# Prompt template

from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(
    ''' Analyze the given mail carefully

    Identify
    1. Intent
    2. Urgency
    3.Tone

    Possible intent values:
    - Request
    - Complaint
    - Information
    - Inquiry

    Possible urgency values:
    - High
    - Medium
    - Low

    Possible tone values:
    - Polite
    - Neutral
    - Urgent
    - Angry

    Return ONLY valid JSON format.

    Example:
    {{
      "intent": "Request",
      "urgency": "High",
      "tone": "Urgent"
    }}

    Email:
    {email}
'''
    )
chain = prompt_template | llm | parser

# Check

email = """Dear Lalitha Mekala,
Your OTP to reset your password is 933646
Do not share you OTP.
This OTP will expire in 10 minutes.

Regards
Innomatics Research Labs"""


response = chain.invoke({"email":email})
#print(response)


# ****** Streamlit***********

import streamlit as st

st.set_page_config(page_title = "Email Detector",
                   page_icon= "📧",
                   layout= 'centered')

st.title("📧 Email Intent & Urgency Detector")

email = st.text_area("Enter Email")

if st.button("Analyze Email"):
    if email.strip()=="":
        st.warning("Please enter email text!")
    else:
        result = chain.invoke({'email':email})
        st.subheader("Prediction")
        st.json(result)

