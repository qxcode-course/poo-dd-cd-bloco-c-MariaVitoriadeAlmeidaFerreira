class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome

class Budega:
    def __init__(self, num_caixa: int):
        self.num_caixa = num_caixa
        self.caixa: list[Pessoa | None] = [None] * num_caixa
        self.espera: list[Pessoa] = []

    def call(self, index: int):
        if index < 0 or index >= len(self.caixa):
            print("fail: caixa inexcistente")
            return
        if self.caixa[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print ("fail: sem clientes")
            return
        self.caixa[index] = self.espera.pop(0)

    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)
    
    def finish(self, index:int):
        if index < 0 or index >= len(self.caixa):
            print("fail: caixa inexistente")
            return
        if self.caixa[index] is None:
            print("fail: caixa vazio")
        self.caixa[index] = None

    def giveUp(self, nome:str):
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                aux = self.espera[i]
                del self.espera[i]
                return aux

    def __str__(self):
        caixa = ", ".join (["-----" if x is None else str (x) for x in self.caixa])
        espera = ", ".join ([str (x) for x in self.espera])
        return f"Caixas: [{caixa}]\nEspera: [{espera}]"
    
def main():
    budega = Budega(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            num_caixa = int(args[1])
            budega = Budega(num_caixa)
        elif args[0] == "show":
            print(budega)
        elif args[0] == "arrive":
            budega.enter(Pessoa(args[1]))
        elif args[0] == "call":
            index = int(args[1])
            budega.call(index)
        elif args[0] == "finish":
            index = int(args[1])
            budega.finish(index)
        elif args[0] =="Giveup":
            budega.giveUp(Pessoa(args[1]))
        
main()