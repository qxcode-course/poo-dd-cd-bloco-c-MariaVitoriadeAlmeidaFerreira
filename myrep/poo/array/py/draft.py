import random

class NA: 
    def __init__(self, N: int):
        self.x = N

    def __str__(self):
        return f"NA({self.x})"
    

#######    listas iniciais ##############
lista_aleatoria = [random.randint(1, 100) for _ in range(5)]
lista_preenchida: list[int] = [1, 2, 3, 4, 5]
lista_vazia: list[int] = []
lista_obj: list[NA] = [NA(1), NA(2), NA(3), NA(4), NA(5)]
lista_frase = ["ola", "tudo", "bem?"]

print("-----------")
print("lista preenchida:", lista_preenchida)
print("lista vazia:", lista_vazia)
print(", ".join(str (x) for x in lista_obj))
print("lista frase:", lista_frase)
print("lista aleatoria",lista_aleatoria)

print("-----------\n")


######### adicoes e remocao ###############

lista_vazia.append(1)
lista_obj.append(NA(6))

lista_preenchida.remove(3)

obj_rev_primeira = lista_obj.pop(0)
obj_rev_ultimo = lista_obj.pop(-1)

print("adição e remoção\n")
print("lista vazia:", lista_vazia)
print("lista preenchida:",lista_preenchida)
print("Primeiro objeto removido:", obj_rev_primeira)
print("Ultimo objeto removido:", obj_rev_ultimo)

print("-----------\n")


###########ordenação##############

sorteio = sorted(lista_preenchida)

print("Ordenação\n")
print("lista ordenada:", sorteio)
print("-----------\n")


##########inserções##############

lista_preenchida.insert(0, 13)
lista_preenchida.insert(len(lista_preenchida), 22)
print("Inserções\n")
print("Inserções:",lista_preenchida)
print("-----------\n")


##########join############

retorno = " ".join(lista_frase)
print("Join\n")
print("frase unida:", retorno)
print("-----------\n")

####### primeiro e ultimo###########

primeiro = lista_preenchida[0]
ultimo = lista_preenchida[-1]

print("Primeiro e ultimo\n")
print("primeiro elemento:", primeiro)
print("ultimo elemento:", ultimo)
print("-----------\n")
