import pytest
import streamlit as st

@pytest.fixture()
def input_invitation():
    st.write('This chatbot is based on HuggingFace Hub.\
    Please, enter your huggingface token.')
    return 0

@pytest.fixture()
def input_field():
    HUG_TOKEN = st.text_input("Token: ", type='password',
                          placeholder='Please, enter your huggingface token')
    return 0


def test_input_invitation():
    assert  input_invitation == 0

def test_input_field():
    assert test_input_field == 0