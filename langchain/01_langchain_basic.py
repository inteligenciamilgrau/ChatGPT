import json
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
import os

f = open('chat_key.json')
chave = json.load(f)
os.environ["OPENAI_API_KEY"] = chave['api_key']

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

prompt = PromptTemplate(
    input_variables=['country'],
    template="Where is the capital of {country}?")

text = prompt.format(country='Brazil')
answer = chat([HumanMessage(content=text)])

print(answer.content, type(answer))
