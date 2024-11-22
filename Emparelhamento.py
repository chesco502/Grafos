from GRAFO import Grafo
class EmparelhamentoPerfeito:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.emparelhamento = []

    def encontrar_emparelhamento_perfeito(self):
        """
        Encontra e retorna um emparelhamento perfeito para o grafo.
        """
        # Verifica se o número de vértices é par
        if self.grafo.verticesNum % 2 != 0:
            print("O grafo não pode ter um emparelhamento perfeito, pois possui um número ímpar de vértices.")
            return []

        # Inicializa um dicionário para rastrear os vértices emparelhados
        emparelhados = {vertice: False for vertice in self.grafo.vertices}

        # Limpa o emparelhamento
        self.emparelhamento = []

        # Itera pelos vértices e tenta formar pares
        for vertice in self.grafo.vertices:
            if not emparelhados[vertice]:
                for aresta in vertice.arestas:
                    v1 = aresta.vertice1
                    v2 = aresta.vertice2
                    if not emparelhados[v2]:  # Se o outro vértice ainda não está emparelhado
                        self.emparelhamento.append((v1, v2))
                        emparelhados[v1] = True
                        emparelhados[v2] = True
                        break  # Sai do loop ao encontrar um par para o vértice

        # Verifica se o emparelhamento cobre todos os vértices
        if len(self.emparelhamento) == self.grafo.verticesNum // 2:
            print("Emparelhamento perfeito encontrado:")
            for v1, v2 in self.emparelhamento:
                print(f"{v1.nome} -- {v2.nome}")
        else:
            print("O grafo não possui um emparelhamento perfeito.")
            self.emparelhamento = []

        return self.emparelhamento



