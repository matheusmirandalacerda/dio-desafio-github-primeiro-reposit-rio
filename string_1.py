nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())
print()
texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")
print()
menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(20, "#"))
print()
print("p-y-t-h-o-n")

for letra in menu:
    print(letra, end = "-")
print() # apenas para quebrar a linha

print("-".join(menu))

