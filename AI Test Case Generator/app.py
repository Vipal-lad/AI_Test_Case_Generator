import openai
import streamlit as st
\

OPEN_API_KEY = 'your-api-key'

def generate_test_cases(requirement):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant capable of generating software test cases."},
            {"role": "user", "content": requirement}
        ]
    )
    return response.choices[0].message['content']


st.title('AI-powered Test Case Generator')
st.write('Enter your software requirement to generate test cases.')

requirement = st.text_area("Requirement", height=150)

if st.button('Generate Test Cases'):
    if requirement:
        with st.spinner('Generating...'):
            try:
                test_cases = generate_test_cases(requirement)
                st.success('Generated Test Cases')
                st.write(test_cases)
            except Exception as e:
                st.error('An error occurred while generating test cases.')
                st.error(e)
    else:
        st.error('Please enter a requirement to generate test cases.')

