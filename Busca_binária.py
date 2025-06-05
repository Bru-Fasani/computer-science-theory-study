def busca_binaria(lista, alvo):
    low = 0
    high = len(lista) -1

while low <= high:
meio = (low + high) //2

  if lista[meio] == alvo:
   return meio

 elif lista[meio] < alvo:
    low = meio + 1

else:
   high = meio - 1
   return -1

