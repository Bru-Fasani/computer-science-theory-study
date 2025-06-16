def criar_grafo(arestas):
    grafo = {}
    for aresta in arestas:
        vertice1, vertice2 = aresta
        if vertice1 not in grafo:
            grafo[vertice1] = []
        if vertice2 not in grafo:
            grafo[vertice2] = []
        grafo[vertice1].append(vertice2)
        grafo[vertice2].append(vertice1)  # Para grafo não direcionado
    return grafo

arestas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]
grafo = criar_grafo(arestas)
print(grafo)
