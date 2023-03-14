import openai
api_key = "/home/anbe/Documentos/anbecodes/ChatGPTPy/api_key.txt"

openai.api_key = api_key

question = "Hola"


completion = openai.Completion.create(engine="text-davinci-003",
                         prompt=question,
                         n=1,
                         max_tokens=2048)

print(completion.choices[0].text)