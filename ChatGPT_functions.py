import openai
import json

f = open('chat_key.json')
chave = json.load(f)
openai.api_key = chave['api_key']

modelo = "gpt-3.5-turbo-0613"
#modelo = "gpt-4-0613"

def mandar_um_recado(nome, recado):
    print("Rodando a funcao")
    enviar_recado = {
        "nome": nome,
        "recado": recado,
    }
    print("Verifiquei o tempo e esta sol")
    return json.dumps(enviar_recado)

# Passo 1, manda o texto pro modelo e prepara a funcao caso ela seja chamada
def run_conversation(mensagem):
    print("Recebido:", mensagem)
    #response = openai.ChatCompletion.create( # api antiga
    response = openai.chat.completions.create( # api nova
        model=modelo,
        messages=[{"role": "user", "content": mensagem}],
        functions=[
            {
                "name": "mandar_um_recado",
                "description": "Avisar uma pessoa sobre alguma informação",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "nome": {
                            "type": "string",
                            "description": "nome da pessoa",
                        },
                        "recado": {"type": "string", "description": "informação que a pessoa precisa saber"}
                    },
                    "required": ["nome", "recado"],
                },
            }
        ],
        function_call="auto",
    )

    #first_response = response["choices"][0]["message"] # api antiga
    first_response = response.choices[0].message.content # api nova
    
    print("Primeira resposta:", first_response['content'])

    # Passo 2, verifica se o modelo quer chamar uma funcao
    if first_response.get("function_call"):
        function_name = first_response["function_call"]["name"]
        function_args = json.loads(first_response["function_call"]["arguments"])

        print("")
        print("Detectou uma função", function_name, function_args)
        print("")

        # Passo 3, chama a funcao
        # Detalhe: a resposta em JSON do modelo pode não ser um JSON valido
        if function_name == "mandar_um_recado":
            function_response = mandar_um_recado(
                nome=function_args.get("nome"),
                recado=function_args.get("recado"),
            )

            # Passo 4 - opcional , manda pro modelo a resposta da chamada de funcao
            #second_response = openai.ChatCompletion.create( # api antiga
            second_response = openai.chat.completions.create( # api nova
                model=modelo,
                messages=[
                    {"role": "user", "content": mensagem},
                    first_response,
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    },
                ],
            )
            #print("Segunda Resposta:", second_response["choices"][0]["message"]['content']) # api antiga
            print("Segunda Resposta:", second_response.choices[0].message.content) # api nova
        else:
            print("Nao achei a funcao pedida")

mensagem = "Diz pra Maria que ela ganhou na loteria e ela precisa verificar como está o tempo em Floripa!"
print("Enviando mensagem sem chamada de funcao")
run_conversation("Bom dia")
print("")
print("Enviando mensagem com chamada de funcao")
run_conversation(mensagem)
