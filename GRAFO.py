class Aresta:
    def __init__(self, vertice1=None, vertice2=None, peso=1, direcionado=False):
        self.peso = peso
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.direcionado = direcionado

    def conectar(self, v1, v2, peso=1):
        self.vertice1 = v1
        self.vertice2 = v2
        self.peso = peso  # Corrigido para usar o valor correto do peso

    def print(self):
        if self.direcionado:
            print(f"[ {self.vertice1} ---> {self.vertice2} , Peso: {self.peso} ]", end="")
        else:
            print(f"[ {self.vertice1} ---- {self.vertice2} , Peso: {self.peso} ]", end="")


class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.arestas = []

    def generateBlankArresta(self):
        aresta = Aresta()
        self.arestas.append(aresta)
        return aresta

    def addAresta(self, aresta: Aresta):
        self.arestas.append(aresta)

    def __str__(self):
        return f"{self.nome}"

    def print(self):
        print(f"{self.nome}:[", end="")
        for aresta in self.arestas:
            aresta.print()
        print("]")


class Grafo:
    def __init__(self, direcionado=False, nome="GRAFO"):
        self.nome = str(nome)
        self.arestasNum = 0
        self.verticesNum = 0
        self.vertices = []
        self.direcionado = direcionado

    def addVertice(self, nome):
        vertice = Vertice(nome)
        self.vertices.append(vertice)
        self.verticesNum += 1
        return vertice

    def addAresta(self, v1: Vertice, v2: Vertice, peso=1):
        aresta = Aresta()
        if v1 in self.vertices and v2 in self.vertices:
            aresta.conectar(v1, v2, peso)
            aresta.peso = peso
            aresta.direcionado = self.direcionado
            v1.addAresta(aresta)
            if not self.direcionado:
                v2.addAresta(aresta)
            self.arestasNum += 1
            return aresta
        else:
            raise ValueError("Um ou ambos os vértices não existem no grafo.")

    def print(self):
        print(f"grafo: {self.nome}")
        print(f"numero de vertices: {self.verticesNum}")
        print(f"numero de Arestas: {self.arestasNum}")
        for v in self.vertices:
            v.print()


# Teste do código
grafo = Grafo()
a = grafo.addVertice("a")
b = grafo.addVertice("b")
c = grafo.addVertice("c")
d = grafo.addVertice("d")
e = grafo.addVertice("e")
f = grafo.addVertice("f")

grafo.addAresta(a, b, 6)
grafo.addAresta(a, c, 15)
grafo.addAresta(a, e, 8)
grafo.addAresta(b, c, 20)
grafo.addAresta(b, e, 10)
grafo.addAresta(b, f, 8)
grafo.addAresta(c, d, 9)
grafo.addAresta(e, f, 5)
grafo.addAresta(d, f, 7)


grafo.print()



        