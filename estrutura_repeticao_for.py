texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = " ")
else:        
    print() # adiciona uma quebra de linha
    
# exemplo utilizando a função built-in range
for numero in range (0,51,5):
    print(numero, end =" ") 
    # O end serve apenas para ficar um dígito ao lado do outro, se for retirado, cada número ficará em uma linha