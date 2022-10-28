class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
      #  return super().voar() # implementação da classe pai
      print("Pardal pode voar")

    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(Passaro):
    Passaro.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
# plano_voo(Pardal()) # mesmo resultado de chamar p1
# plano_voo(Avestruz()) # mesmo resultado de chamar p2
plano_voo(Aviao())
