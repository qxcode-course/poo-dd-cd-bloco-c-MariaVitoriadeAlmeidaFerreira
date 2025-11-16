class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome

class Budega:
    def __init__(self, num_caixa: int):
        self.caixa: list[Pessoa | None] = [None] * num_caixa
        self.espera: list[Pessoa] = []
    
    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def __str__(self):
        self.caixa =[Pessoa("Maria"), None, Pessoa("Pedro")]
        caixa = ", ".join (["----" if x is None else str (x) for x in self.caixa])
        espera = ", ".join ([str (x) for x in self.espera])
        return f"caixas:{caixa}\nfila de espera:{espera}"
    
pessoa = Pessoa("Pedro")
print(pessoa)

budega = Budega(5)
budega.caixa[2] = pessoa
budega.espera.append(pessoa)
print(budega) 

    