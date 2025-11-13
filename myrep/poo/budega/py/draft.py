class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome

class Budega:
    def __init__(self, num_caixa: int):
        self.caixa: list[Pessoa | None] = [] * num_caixa
        self.espera: list[Pessoa] = []

    def __str__(self):
        caixa = ", ". join ([str (x) for x in self.caixa])
        espera
        return f"{self.caixa}\n{self.espera}"
    
pessoa = Pessoa("Pedro")
print(pessoa)

budega = Budega(5)
budega.caixa[2] = pessoa
budega.espera.append(pessoa)
print(budega) 

    