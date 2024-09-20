class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print(f"{self.nome} foi destruído")

    def falar(self):
        print(f"{self.nome} está falando...")

    def acordar(self):
        if self.acordado:
            print(f"{self.nome} está acordado")
        else:
            print(f"{self.nome} não está acordado")
        
        self.acordado = not self.acordado
        

c1 = Cachorro("rex", "marrom")
c1.falar()

c1.acordar()
c1.acordar()
