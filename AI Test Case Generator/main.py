from openai import OpenAI
import streamlit as st

import os
from dotenv import load_dotenv

OPENAI_API_KEY = 'openai_key'
client = OpenAI(api_key = OPENAI_API_KEY)

load_dotenv()
open_api_key = os.getenv('OPEN_API_KEY')


def generate_test_cases(requirement):
    response = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=[
            {"role": "system", "content": "You are a helpful assistant capable of generating software test cases. Please provide test cases in a numbered list format."},
            {"role": "user", "content": f"Generate test cases for the following requirement:\n\n{requirement}"}
        ]
    )
    return response.choices[0].message['content']

##st.title("Streamlit Example")
##st.header("Introduction to Streamlit")
##st.write("Streamlit is easy to use.")
##st.markdown("### Features of Streamlit:\n- Interactive widgets\n- Fast development")

st.title('AI-powered Test Case Generator')
st.write('Enter your software requirement to generate test cases.')

requirement = st.text_area("Requirement", height=150)
num_test_cases = st.slider("Number of test cases to generate", 1, 10, 5)

if st.button('Generate Test Cases'):
    if requirement:
        with st.spinner('Generating...'):
            try:
                test_cases = generate_test_cases(requirement)
                st.success('Generated Test Cases')
                st.markdown(test_cases)
                
                # Add option to download test cases
                st.download_button(
                    label="Download Test Cases",
                    data=test_cases,
                    file_name="generated_test_cases.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error('An error occurred while generating test cases.')
                st.error(e)
    else:
        st.error('Please enter a requirement to generate test cases.')

