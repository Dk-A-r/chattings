import pytest
import requests
import streamlit as st
import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain


SECRET = os.environ['SECRET']


@pytest.fixture()
def check_streamlit():
    x = requests.get('https://streamlit.io/')
    return x.status_code


@pytest.fixture()
def check_model():
    x = requests.get('https://huggingface.co/google/flan-t5-xxl')
    return x.status_code


@pytest.fixture()
def check_app():
    x = requests.get('https://dk-a-r-chattings-main-4jb2u4.streamlit.app/')
    return x.status_code


@pytest.fixture()
def invitation_to_write():
    st.write('This chatbot is based on HuggingFace Hub.\
    Please, enter your huggingface token.')
    return 0


@pytest.fixture()
def token_field():
    x = 0
    st.text_input("Token: ", key=x, type='password',
                  placeholder='Please, enter your huggingface token')
    return 0


@pytest.fixture()
def prompt():
    TEMPLATE = """Question: {question}
    Answer: Let's think step by step."""
    PROMPT = PromptTemplate(template=TEMPLATE, input_variables=["question"])
    llm_chain = LLMChain(prompt=PROMPT,
                         llm=HuggingFaceHub(huggingfacehub_api_token=SECRET,
                                            repo_id="google/flan-t5-xxl",
                                            model_kwargs={"temperature": 0.9,
                                                          "max_length": 512}))
    response = llm_chain.run('Where the London is located?')
    return bool(response)


def test_streamlit(check_streamlit):
    assert check_streamlit == 200


def test_model(check_model):
    assert check_model == 200


def test_app(check_app):
    assert check_app == 200


def test_invitation(invitation_to_write):
    assert invitation_to_write == 0


def test_token_field(token_field):
    assert token_field == 0


def test_prompt(prompt):
    assert prompt

