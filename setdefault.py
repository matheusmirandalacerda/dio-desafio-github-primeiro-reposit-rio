contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# contato.setdefault ("nome", "Giovanna")
# print(contato) # não irá alterar a chave nome, pois já há uma definicição para ela

contato.setdefault("idade", 28)
print(contato) # irá acrescentar uma chave, uma vez que não exite essa chave