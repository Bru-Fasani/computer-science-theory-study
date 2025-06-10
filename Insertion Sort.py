def insertion_sort(lista):
    """
    Ordena uma lista usando o algoritmo de ordenação por inserção.

    Args:
        lista: A lista a ser ordenada.

    Returns:
        A lista ordenada.
    """
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# Exemplo de uso:
lista = [5, 2, 4, 6, 1, 3]
lista_ordenada = insertion_sort(lista)
print("Lista ordenada:", lista_ordenada)  # Saída: Lista ordenada: [1, 2, 3, 4, 5, 6]
