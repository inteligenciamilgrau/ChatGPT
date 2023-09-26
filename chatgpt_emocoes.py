import openai

openai.api_key = "API_KEY_DA_OPENAI"
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

texto1 = """Comprei este computador recentemente e estou muito satisfeito com suas funcionalidades.
    Ele oferece muito mais do que eu imaginava e atendeu às minhas necessidades de trabalho e entretenimento.
    A performance é incrível, e a qualidade de construção é excelente. Isso era esperado de um Turbo Power PC.
    No entanto, o preço foi um grande obstáculo para mim. 
    Eu estava esperando gastar menos, mas decidi investir um pouco mais para obter um produto de qualidade. 
    Mesmo assim, a etiqueta de preço foi bem acima do que eu inicialmente planejava.
    Além disso, a entrega foi bem demorada. 
    Eu esperava recebê-lo em poucos dias, mas demorou semanas até que finalmente chegasse. 
    Isso foi um pouco frustrante, pois eu estava ansioso para começar a usar o computador.
    No geral, estou feliz com a compra, mas o preço elevado e a \
    demora na entrega são pontos negativos a serem considerados."""

texto2 = """Minha experiência com este computador foi extremamente desagradável.
    Primeiro, a entrega atrasou consideravelmente.
    Eu estava esperando receber o produto em poucos dias, mas levou semanas até que finalmente chegasse.
    Quando o computador finalmente chegou, fiquei chocado com a péssima qualidade do produto.
    A construção parecia barata e frágil, e a performance estava muito abaixo das minhas expectativas.
    Ele travava frequentemente e não conseguia lidar com tarefas simples. Nada esperado de um Turbo Power PC.
    Além disso, o preço estava errado. Fui cobrado muito mais do que o valor que estava inicialmente listado.
    Fiquei extremamente bravo com essa discrepância, pois isso afetou negativamente o meu orçamento.
    No geral, minha experiência com este computador foi terrível.
    Atraso na entrega, qualidade péssima e preço errado tornaram esta compra uma grande decepção."""

texto = texto2

prompt = f"""
Identifique uma lista de emoções que o autor da
seguinte análise está expressando. Inclua não mais do que
cinco itens na lista. Formate sua resposta como uma lista de
palavras em minúsculas separadas por vírgulas.

Texto da análise: '''{texto}'''
"""

prompt2 = f"""
Identifique os seguintes itens no texto da análise:

- Sentimento (positivo ou negativo)
- O avaliador está expressando raiva? (verdadeiro ou falso)

A análise está delimitada por três acentos graves. \
Formate sua resposta como um objeto JSON com \
as chaves "Sentimento", "Raiva", "Item" e "Marca".\
Se a informação não estiver presente, utilize "desconhecido" como valor.\

Faça sua resposta o mais concisa possível.
Formate o valor da Raiva como um booleano.

Texto da análise: '''{texto}'''
"""
response = get_completion(prompt)
print("Sentimentos:", response)

response = get_completion(prompt2)
print("Análise:", response)
