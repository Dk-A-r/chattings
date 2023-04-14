from langchain import PromptTemplate, HuggingFaceHub, LLMChain

hug_token=input("This chatbot is based on HuggingFace Hub.\n\
Please, enter your huggingface token: ")

template = """Question: {question}


Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=HuggingFaceHub(huggingfacehub_api_token=hug_token, repo_id="google/flan-t5-xl", model_kwargs={"temperature":0, "max_length":64}))

print("Now we will start the conversation. If you become bored, you can type \"quit\" in your prompt to exit. Good luck!")

while True:
    question = input("User: ")
    if question == 'quit':
        print("Goodbye!")
        break
    response =llm_chain.run(question)
    print(f"Answer is: {response}. \n What is your next question?")
