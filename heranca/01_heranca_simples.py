class Veiculo:
    def __init__(self, cor, rodas):
        self.cor = cor
        self.rodas = rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def desligar_motor(self):
        print("Desligando o motor")
        
class Motocicleta(Veiculo):
    def __init__(self, cor, rodas):
        super().__init__(cor, rodas)

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    def empurrar(self):
        print("Empurrando a moto")

    def buzinar(self):
        print("Buzinando a moto")

    def acelerar(self):
        print("Acelerando a moto")

    def frear(self):
        print("Freando a moto")

    def parar(self):
        print("Parando a moto")

class Carro(Veiculo):
    def __init__(self, cor, rodas):
        super().__init__(cor, rodas)

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    def buzinar(self):
        print("Buzinando o carro")

    def acelerar(self):
        print("Acelerando o carro")

    def frear(self):
        print("Freando o carro")

    def parar(self):
        print("Parando o carro")

    def ligar_motor(self):
        print("Ligando o motor do carro")

    def desligar_motor(self):
        print("Desligando o motor do carro")

class Caminhao(Veiculo):
    def __init__(self, cor, rodas, tara):
        super().__init__(cor, rodas)
        self.tara = tara
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    def desligar_motor(self):
        print("Desligando o motor do caminhão")

    def ligar_motor(self):
        print("Ligando o motor do caminhão")

    def empurrar(self):
        print("Empurrando o caminhão")

    def descarregar(self):
        print("Descarregando o caminhão")

    def __del__(self):
        print("Caminhão destruído")

    def acelerar(self):
        print("Acelerando o caminhão")

    def frear(self):
        print("Freando o caminhão")

    def buzinar(self):
        print("Buzinando o caminhão")

    def correr(self):
        print("Vrummm...")

    def parar(self):
        print("Parando o caminhão")
    
        
moto = Motocicleta("preta", 2)
moto.ligar_motor()
moto.empurrar()
moto.buzinar()
moto.acelerar()
moto.frear()
moto.parar()
carro = Carro("branco", 4)
carro.desligar_motor()
carro.ligar_motor()
carro.buzinar()
carro.acelerar()
carro.frear()
carro.parar()
caminhao = Caminhao("vermelho", 8, 1000)
caminhao.ligar_motor()
caminhao.empurrar()
caminhao.descarregar()
caminhao.acelerar()
caminhao.frear()
caminhao.buzinar()
caminhao.correr()
caminhao.parar()