class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrummm...")
    
    # def __str__(self) -> str:
    #     return f"{self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])} "
        

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
# b1.buzinar()
# b1.correr()
# b1.parar()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2020, 800)
# Bicicleta.buzinar(b2)
print(b1)
print(b2)