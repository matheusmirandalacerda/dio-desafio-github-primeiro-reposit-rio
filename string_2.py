nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28} # utilizção de .format(**dados))

print("Nome: %s Idade: %d" % (nome,idade))
print() # apenas para quebra de linha
print("Nome: {} Idade: {}".format (nome,idade))
print() # apenas para quebra de linha
print("Nome: {1} Idade: {0}".format (idade,nome))
print() # apenas para quebra de linha
print("Nome: {1} Idade: {0} Nome: {1}  {1}".format (idade,nome))
print() # apenas para quebra de linha
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print() # apenas para quebra de linha
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print() # apenas para quebra de linha
print("Nome: {nome} Idade: {idade}".format(**dados))
print() # apenas para quebra de linha
print(f"Nome: {nome} Idade: {idade}")
print() # apenas para quebra de linha
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print() # apenas para quebra de linha
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print() # apenas para quebra de linha
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:7.2f}")
print() # apenas para quebra de linha



