# chattings
Настоящее приложение интегрирует Free Inference API одной из LLM с сайта huggingface.co (а именно, flan-t5-xxl) в приложение на Streamlit. Результатом получается достаточно простой аналог чат-бота в рамках Streamlit.

Приложение понимает запросы на английском языке и возвращает ответы на нем же. Для начала работы с приложением необходимо ввести token с HuggingfaceHub (с правом write).

Для связки LLM с Free Inference API используется модуль langchain (для построения цепочки "запрос-ответ").

Команда: Карпов Данил

Ссылка на приложение:
https://dk-a-r-chattings-main-4jb2u4.streamlit.app/
