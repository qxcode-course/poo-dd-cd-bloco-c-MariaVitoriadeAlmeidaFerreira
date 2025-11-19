class Cliente:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getId(self):
        return self.__id
    
    def getPhone(self):
        return self.__phone

    def setId(self, id):
        self.__id  = id

    def setPhone(self, phone):
        self.__phone = phone

    def __str__(self) -> str:
        return f"{self.__id}:{self.__phone}"
    
class Teatro:
    def __init__(self, capacidade: int):
        self.__assentos: list[Cliente | None] = [None] * capacidade
        self.capacidade: int = capacidade

    def __str__(self) -> str:
        assentos_capa = [str(cliente) if cliente else "-" for cliente in self.__assentos]
        return "[" + " ".join(assentos_capa) + "]"

    def procurar(self, nome_cliente: str) -> int:
        for i, cliente in enumerate(self.__assentos):
            if cliente is not None and cliente.getId() == nome_cliente:
                return i
        return -1 # verica depois de tudo
    
    def verificarIndex(self, index: int) -> bool:
        return 0  <= index  < len(self.__assentos)
    
    def resevar(self, id: str, phone: int, index: int) -> bool:
        if not self.verificarIndex(index):
            print("fail: cadeira nao existe")
            return False
        if self.procurar(id) != -1:
            print("fail: cadeira ja esta ocupada")
            return False
        if self.__assentos[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False

        self.__assentos[index] = Cliente(id, phone)
        return True

            
            
    
#teatro = Teatro(5)
#print(teatro.vericarIndex(0))
#print(teatro.vericarIndex(4))
#print(teatro.vericarIndex(5))
#print(teatro.vericarIndex(-1))

def main():
    teatro = Teatro(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            teatro = Teatro(int(args[1]))
        elif args[0] == "show":
            print(teatro)
        elif args[0] == "reservas":
            teatro.resevar(args[1], int(args[2]), int(args[3]))
main()