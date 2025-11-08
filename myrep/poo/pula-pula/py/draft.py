class Kid:
    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age

    def getName(self) -> str:
        return self.__name
    
    def getAge(self) -> int:
        return self.__age

    def setAge(self, age: int) -> int:
        self.__age = age
    
    def setName(self, name: str) -> str:
        self.__name = name
    
    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"

class pulaP:
    def __init__(self):
        self.__bricando: list[Kid] = []
        self.__esperar: list[Kid] = []

    def __removeFromList(self, name: str, lista: list[Kid]) -> Kid | None:
       for i, Kid in enumerate(lista):
           if Kid.getName() == name:
               return lista.pop(i) #remove a crianca da primeira posicao
           return None
        
    def arrive(self, kid: Kid) -> None:
        self.__esperar.insert(0, kid) # a criança chegou

    def enter (self) -> None:
        if self.__esperar:
            crianca = self.__esperar.pop()
            self.__bricando.append(crianca) #ficou na ultima posicao

    def leave(self) -> None:
        if self.__bricando:
            crianca = self.__bricando.pop()
            self.__esperar.insert(crianca) 

    def __str__(self) -> str:
            espera_str = ', '.join(str(x) for x in self.__esperar)
            bricando_str = ', '.join(str(x) for x in self.__bricando)
            return f"[{espera_str}] => [{bricando_str}]"
    
    def remove_kid(self) -> Kid | None:
    

def main():
    pula = pulaP()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pula)
        elif args[0] == "arrive":
            pula.arrive(Kid(args[1], int(args[2])))
        elif args[0] == "enter":
            pula.enter()

        
        


main()
        
        








    

