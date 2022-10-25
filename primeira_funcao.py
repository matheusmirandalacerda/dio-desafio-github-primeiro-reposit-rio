def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome): # Caso não seja reservado um argumento em nome no momento de rodar a função, ocorrerá erro na execução
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")



exibir_mensagem()
exibir_mensagem_2(nome = "Guilherme") # Obrigatoriamente terá que informar o argumento de nome, caso contrário, ocorré erro 
exibir_mensagem_2("Guilherme") # Obrigatoriamente terá que informar o argumento de nome, caso contrário, ocorré erro
exibir_mensagem_3()
exibir_mensagem_3(nome = "Chappie")
exibir_mensagem_3("Chappie")
