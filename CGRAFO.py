from TGRAFO import TGrafo
from TGRAFO import TaggedVertice

class CVertice(TaggedVertice):
        def __init__(self, nome,clip = None,tag=None,color=None):
            self.color = color
            super().__init__(nome,clip,tag,color=None)
        def changeColor(self, color):
             self.color = color
        
        





class CGrafo(TGrafo):
    def __init__(self,direcionado = False, nome = "CGRAFO"):
        super().__init__(direcionado,nome)
        
    
    def addVertice(self, nome,clip = None ,tag = None,color = None):
        vertice = CVertice(nome,clip,tag,color)
        self.vertices.append(vertice)
        self.verticesNum += 1  
        
                 
        return vertice
    
    def changeColor(self,V,color):
        V.color = color
         
    


grafo = CGrafo()
a = grafo.addVertice("a","teste")
b = grafo.addVertice("b","teste")
c = grafo.addVertice("c","teste")
d = grafo.addVertice("d","teste")
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
