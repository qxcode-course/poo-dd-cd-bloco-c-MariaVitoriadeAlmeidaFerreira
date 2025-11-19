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

    def __str__(self):
        return f"{self.id}:{self.phone}"
    
class Teatro:
    def __init__(self, capacidadde: int):
        self.assentos = list[Cliente] = []
        self.pesquisar = [name] * int
    

