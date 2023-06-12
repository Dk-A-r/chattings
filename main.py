import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl")

st.write('This chatbot is based on HuggingFace LLM.\
Please, enter your prompt:')

prompt = st.text_input("Prompt: ", key=x, type='password',
                      placeholder='Please, enter your prompt: ')

input_ids = tokenizer(prompt, return_tensors="pt").input_ids
outputs = model.generate(input_ids)

st.write(outputs[0])
