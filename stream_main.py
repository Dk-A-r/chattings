import streamlit as st
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

st.write('This chatbot is based on HuggingFace Hub')
hug_token = st.text_input('Token', 'Please, enter your huggingface token')

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=HuggingFaceHub(huggingfacehub_api_token=hug_token, repo_id="google/flan-t5-xl", model_kwargs={"temperature":0, "max_length":64}))

st.write('Now we will start the conversation. If you become bored, you can type \"quit\" in your prompt to exit. Good luck!')

while True:
    question = st.text_input("User: ", 'Enter your prompt')
    if question == 'quit':
        st.write("Goodbye!")
        break
    response =llm_chain.run(question)
    st.write(f"Answer is: {response}. \n What is your next question?")
