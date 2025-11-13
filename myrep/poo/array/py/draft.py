class NA:
    def __init__(self, N: int):
        self.x = N
    #construtor

    def __str__(self):
        return f'NA({self.x})'
    #to string

import random #importando uma biblioteca para criar uma lista aleatorio

lista_aleatorio = [random.randint(1,100) for _ in range(5)]
lista_vazia: list[int] = [] #lista vazia
lista_preenchida: list[int] = [1, 2, 3, 4, 5] 
lista_preencida_objetos: list[NA] = [NA(1), NA(2), NA(3), NA(4), NA(5)]
lista_frase = ["ola", "tudo", "bem?"]

lista_vazia.append(1) #adicionar no final
lista_preencida_objetos.append(NA(6)) #adiciona um novo objeto

lista_preenchida.remove(3) # remove o valor 3
obj_removidoB = lista_preencida_objetos.pop(0) #remove o primeiro NA
obj_removidoA = lista_preencida_objetos.pop(-1) #remove na ultimo posicao

sorteio  = sorted(lista_preenchida)

lista_preenchida.insert(0, 13) #inserindo 13 na 1 posicao
lista_preenchida.insert(5, 22) #inserindo 22 na ultima posicao

returno = " ".join(lista_frase) #tirando os espaços

pN = lista_preenchida[0] # vai para o primeiro obj
uObj = lista_preenchida[-1] # vai para o ultimo obj

b = 5
vetor_vazio = []
for valor in lista_preenchida:
    if valor != b:
        vetor_vazio.append(valor)

tamanho = len(lista_preenchida) #vericando o tamanho com len
print(f"o tamanho da lista é {tamanho}")

n = 10
sequencia = list(range(n + 1))
        
x = 4 in lista_preenchida #verificar se tem o 4 na lista

a = 5
if a in lista_preenchida:
    posicao = lista_preenchida.index(a) #encontrar 5 na lista
    print(f"elemento {a} encontrando em {posicao}")
else:
    print(f"elemento {a} nao foi encontrado")

for i in range(len(lista_preenchida)):
    print(f"indice {i}: valor = {lista_preenchida[i]}")

embaralhar = random.shuffle(lista_preenchida) #shuflle serve para embaralhar as ordens das variaveis


limpar = lista_preenchida.clear() #limpa a lista


print("lista preenchida:", lista_preenchida)
#precisa formar em um str antes
print("Objs:", ", ".join(str(obj) for obj in lista_preencida_objetos)) # join() para formar a lista da array
print("obj removido na primeira posicao:", obj_removidoA)
print("obj removido na ultima posicao:", obj_removidoB)
print("Ordena a lista no lugar:", sorteio)
print(f"o tamanho da lista é {tamanho}")
print("Frase separa:", lista_frase)
print("frase bem feita:", returno)
print("primeiro objeto:", pN)
print("Ultimo Objeto:", uObj)
print("tem esse valor?", x) # true ou false
print("lista vazia:", limpar)
print("todos os valores removidos:", vetor_vazio)
print("sequencia da n:", sequencia)
print("sequencia aleatoria:", lista_aleatorio)
print("lista embaralhada:", embaralhar)