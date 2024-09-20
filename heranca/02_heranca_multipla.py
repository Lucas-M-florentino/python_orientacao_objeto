class Animal:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

    def amamentar(self):
        print("Amamentando")
    def emitir_som(self):
        print("Som de mamífero")

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

    def voar(self):
        print("Voando")
    def emitir_som(self):
        print("Som de ave")

class Morcego(Ave, Mamifero):
    def __init__(self, **kw):
        print(Morcego.__mro__)
        
        super().__init__(**kw)
    
class Foo: 
     def hello(self): 
        print(self.__class__.__name__.lower()) 

class Bar(Foo): 
    def hello(self): 
        return super().hello() 
    
bar = Bar() 
bar.hello()


# morcego = Morcego(nome="Morcego", cor_pelo="preto", cor_bico="verde")
# morcego.voar()
# morcego.amamentar()
# morcego.emitir_som()