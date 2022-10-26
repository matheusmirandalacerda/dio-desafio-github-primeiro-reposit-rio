def criar_carro(modelo,ano,placa,/,marca,motor,combistivel,):
    print(modelo,ano,placa,marca,motor,combistivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combistivel="Gasolina") # válido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combistivel="Gasolina") 
# inválido devido a barra, tudo antes da barra deverá seguir sem o parametro