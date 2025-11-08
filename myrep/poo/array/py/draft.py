class NA:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'NA({self.x})'

lista_vazia: list[int] = [] #lista vazia
lista_preenchida: list[int] = [1, 2, 3, 4, 5]
lista_preencida_objetos: list[NA] = [NA(1), NA(2), NA(3), NA(4), NA(5)]

lista_vazia.append(1) #adicionar no final
lista_preenchida.append(NA(6)) #remover do final 
lista_preencida_objetos.append(NA(3))
lista_preenchida.remove(3) # remove o valor 3
obj_removido = lista_preencida_objetos.pop(0) #remove o primeiro NA

#precisa formar em um str antes
print("lista preenchida:", ", ". join(str(obj) for obj in lista_preencida_objetos)) # join() para formar a lista da array
print("obj removido:", obj_removido)