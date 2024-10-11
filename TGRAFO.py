from GRAFO import Vertice
from GRAFO import Aresta
from Grafo import Grafo


class TagsNaoExistentes(Exception):
    pass



class TaggedVertice(Vertice):
    def __init__(self, nome, clip,tag=None):
       
        super().__init__(nome)
        self.clip = clip 
        self.tags = tag  
    
    


class TGrafo(Grafo) :

    def __init__(self,direcionado = False, nome = "TGRAFO"):
        super().__init__(direcionado,nome)
    
    def addTVertice(self, nome,clip = "test",tag = None):
        vertice = TaggedVertice(nome,clip,tag)
        self.vertices.append(vertice)
        self.verticesNum += 1  
        return vertice
    
   
    
    def addTAresta(self, v1:Vertice ,v2 :Vertice , peso=1):
        aresta = TaggedAresta()
        
        if(v1 in self.vertices and v2 in self.vertices):
            aresta.conectar(v1, v2,peso)  
            aresta.peso = peso 
            aresta.direcionado = self.direcionado  
            v1.addAresta(aresta)  
            if not self.direcionado:
                v2.addAresta(aresta)
            self.arestasNum += 1  
            return aresta
        else:
            raise VerticesNaoExistentes("Error message")
        


class TaggedAresta:
    def __init__(self,tags=None):
       
        super().__init__()
        self.tags = tags 

    def addTag(self,tag):
        try:
            self.tags.append(tag)
        except Exception:
            self.tags=tag 


    def conectar(self,v1 : TaggedVertice ,v2 : TaggedVertice,peso = 1):
        tag1 = v1.tags
        tag2 = v2.tags
        self.peso = peso
        bothTags = get_common_items(tag1,tag2)
        
       
       
        if len(bothTags) !=0:
            self.tags = bothTags
            self.vertice1 = v1 
            self.vertice2 = v2 
        else: 
            raise TagsNaoExistentes
    