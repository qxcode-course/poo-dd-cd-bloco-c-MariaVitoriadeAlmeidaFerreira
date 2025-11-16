class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome

class Budega:
    def __init__(self, num_caixa: int):
        self.caixa: list[Pessoa | None] = [None] * num_caixa
        self.espera: list[Pessoa] = []

    def call(self, index: int):
        if index < 0 or index >= len(self.caixa):
            print("fail: caixa inexcistente")
            return
        if self.caixa is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print ("fail: caixa vazio")
            return
        self.caixa[index] = self.espera[0]
        del self.espera[0]

    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)
    
    def finish(self, index:int):
        if index < 0 or index >= len(self.caixa):
            print("indice ine")
            return
        if self.caixa[index] is None:
            print("fail: caixa ocupado")
        self.caixa[index] = None

    def giveUp(self, nome:str):
        for i, pessoa in enumerate(self.espera):
            


    def __str__(self):
        self.caixa =[Pessoa("Maria"), None, Pessoa("Pedro")]
        caixa = ", ".join (["----" if x is None else str (x) for x in self.caixa])
        espera = ", ".join ([str (x) for x in self.espera])
        return f"caixas:{caixa}\nfila de espera:{espera}"
    
pessoa = Pessoa("Pedro")
print(pessoa)

budega = Budega(5)
budega.enter(Pessoa("Vitoria"))
budega.enter(Pessoa("Ph"))

print(budega)
    