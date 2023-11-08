# Neste exemplo, a resposta que o ChatGPT manda como resposta vem palavra por palavra
# Isso permite fazer um chatbot que começa a responder mais rápido quando a resposta é longa
# Voce precisa incluir o parametro "stream"
# e fazer um print das partes
# Ao mesmo tempo criei uma resposta completa que vai de uma só vez

import openai # pip install openai
import time

openai.api_key = "sua-api-openai"

def generate_answer(messages):
    try:
        #response = openai.ChatCompletion.create( # api antiga
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": messages}],
            temperature=1.0,
            stream=True,
        )

        resposta_completa = ""
        for parte in response:
            if not parte.choices[0].delta == {}:
                print(str(parte.choices[0].delta.content), end="")
                resposta_completa += str(parte.choices[0].delta.content)

        return resposta_completa
    except Exception as e:
        print("Erro", e)
        return "Erro: " + str(e)

pergunta = "Bom dia! Como se faz café?"

print("Enviando\n")

start = time.time()
answer = generate_answer(pergunta)
end = time.time()

print("\nPergunta:", pergunta)
print("Resposta ChatGPT:", answer)

print("\nTempo de resposta:", end - start)

