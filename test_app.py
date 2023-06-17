import pytest
import requests

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

def test_streamlit():
    assert check_streamlit == 200

def test_model():
    assert check_model == 200

def test_app():
    assert check_app == 200

