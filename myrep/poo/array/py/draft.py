class NA:
    def __init__(self, N: int):
        self.x = N
    #construtor

    def __str__(self):
        return f'NA({self.x})'
    #to string

lista_vazia: list[int] = [] #lista vazia
lista_preenchida: list[int] = [1, 2, 3, 4, 5] 
lista_preencida_objetos: list[NA] = [NA(1), NA(2), NA(3), NA(4), NA(5)]
lista_frase = ["ola", "tudo", "bem?"]

lista_vazia.append(1) #adicionar no final
lista_preencida_objetos.append(NA(6)) #adiciona um novo objeto

lista_preenchida.remove(3) # remove o valor 3
obj_removido = lista_preencida_objetos.pop(0) #remove o primeiro NA

lista_preenchida.insert(2, 13) #inserindo 13 na 4 posicao

returno = " ".join(lista_frase) #tirando os espaços

pN = lista_preenchida[0] # vai para o primeiro obj
uObj = lista_preenchida[-1] # vai para o ultimo obj

x = 4 in lista_preenchida #verificar se tem o 4 na lista


print("lista preenchida:", lista_preenchida)
#precisa formar em um str antes
print("Objs:", ", ".join(str(obj) for obj in lista_preencida_objetos)) # join() para formar a lista da array
print("obj removido:", obj_removido)
print("Frase separa:", lista_frase)
print("frase bem feita:", returno)
print("primeiro objeto:", pN)
print("Ultimo Objeto:", uObj)
print("tem esse valor?", x) # true ou false
print