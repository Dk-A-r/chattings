import streamlit as st
import os
from langchain.llms import OpenAI
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

option = st.selectbox('Choose your LLM: ',
                      ('OpenAI', 'flan(HuggingFaceHub)'))

st.write('This chatbot is based on two large language models.\
Please, enter your token from chosen model.')

x = 0

TOKEN = st.text_input("Token: ", key=x, type='password',
                      placeholder='Please, enter your token')

if option:
    if TOKEN:
        if option=='OpenAI':
            os.environ["OPENAI_API_KEY"] = TOKEN
            model = OpenAI()
        elif option=='flan(HuggingFaceHub)':
            os.environ["HUGGINGFACEHUB_API_TOKEN"] = TOKEN
            model = HuggingFaceHub(repo_id="google/flan-t5-xxl",
                                   model_kwargs={"temperature": 0.9,
                                   "max_length": 512})

        TEMPLATE = """Question: {question}
        Answer: Let's think step by step."""
        PROMPT = PromptTemplate(template=TEMPLATE, input_variables=["question"])

        if TOKEN:
            llm_chain = LLMChain(prompt=PROMPT,
                                 llm=model)

            st.write(
                'Now we will start the conversation.\
                 If you become bored, you can type "quit"\
                  in your prompt to exit. Good luck!')

        x = x + 1

        question = st.text_input("User: ", key=x)

        while question:
            x = x + 1

            if question == 'quit':
                st.write("Goodbye!")
                break
            response = llm_chain.run(question)
            st.write(f"Answer is: {response}")
            st.write("What is your next question?")
            question = st.text_input("User: ", key=x)
