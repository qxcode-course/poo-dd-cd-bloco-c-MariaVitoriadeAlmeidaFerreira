class Cliente:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def getId(self):
        return self.id
    
    def getPhone(self):
        return self.phone

    def setId(self, id):
        self.id  = id

    def setPhone(self, phone):
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.id}:{self.phone}"
    
class Teatro:
    def __init__(self, capacidade: int):
        self.assentos: list[Cliente | None] = [None] * capacidade
        self.capacidade: int = capacidade

    def __str__(self) -> str:
        return f"{self.assentos}"

    def procurar(self, nome_cliente: str) -> int:
        for i, cliente in enumerate(self.assentos):
            if cliente is not None and cliente.getId() == nome_cliente:
                return i
            return -1 # verica depois de tudo



teatro = Teatro(5)
print(teatro.assentos)




#def main():
   # teatro = Teatro()
  #  while True:
   #     line: str = input()
    #    print("$" + line)
     #   args: list[str] = line.split(" ")
      #  if args[0] == "end":
       #     break
        #elif args[0] == "show":
         #   print(teatro)
#main()