import json
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType, load_tools
import os

f = open('chat_key.json')
chave = json.load(f)

os.environ["OPENAI_API_KEY"] = chave['api_key']
os.environ["SERPAPI_API_KEY"] = chave['serpi_key']

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, verbose=True)

tools = load_tools(["serpapi", "llm-math"], llm=chat)
agent = initialize_agent(tools, chat, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

with get_openai_callback() as cb:
    response = agent.run("Quem é o ator principal que interpretou o Capitão Nascimento no filme Tropa de Elite? qual sua idade atual elevada a 0.35 potencia")
    print("response", response)
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")

basico = False
if basico:
    prompt = PromptTemplate(
        input_variables=['country'],
        template="Where is the capital of {country}?")

    chain = LLMChain(llm=chat, prompt=prompt)

    answer = chain.run("Brazil")

    print(answer, type(answer))

