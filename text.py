import os

mensagens = []

nome = input("Nome: ")

while True:
    #limpar chat
    os.system('cls')
    os.system('clear')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    
    print("___________")

    #obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break
    elif texto == "sair":
        break

    #adc mensagens na lista mensagens = []
    mensagens.append({
        "nome": nome,
        "texto": texto
    })