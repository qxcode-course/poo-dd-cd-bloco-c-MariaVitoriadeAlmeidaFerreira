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

    #def __removeFromList(self, name: str, list: list[Kid]) -> Kid | None:
        
    def arrive(self, kid: Kid) -> None:
        self.__esperar.append(kid)
            #a criança chegou
    def enter (self) -> None:
        if self.__esperar:
            Kid = self.__esperar.pop(0)
            self.__bricando.append(Kid)

    def leave(self):
        if self.__bricando:
            Kid = self.__esperar.pop(0)
            self.__bricando.append(Kid)

    def __str__(self) -> str:
        return [{self.__nome}] => [{self.__bricando}]
    
    def remove_kid(self) -> Kid | None:
        if self.__bricando ():
            aux = self.__bricando
            self.__bricando = None
            return aux
        else:
            print ("fail: {self.__nome} nao esta no pula pula")

    def show(self):
        








    

