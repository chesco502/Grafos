import tkinter as tk
from Emparelhamento import EmparelhamentoPerfeito
from tkinter import messagebox
from GRAFO import Grafo
from tkinter import simpledialog
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import tkinter.simpledialog as simpledialog
from TGRAFO import TGrafo
from caminho_hamiltoniano import  HamiltonianPathFinder
from Caminho_euleriano import EulerianPathFinder
from Coloraçao import GraphColoring
from Salvar_grafo import salvar_grafo_em_txt
from grafo_visual import visualizar_grafo
from TGRAFO import TGrafo
from leitura_arquivo_txt import  carregar_grafo_modelado
from leitura_pasta_videos import lerClips

class GraphApp:
    def __init__(self, root):
        self.grafo = Grafo()
        self.root = root
        self.root.title("Gerenciador de clipes de seguraca por meio de Grafo")
        
        # Criar botões
        self.create_buttons()

    def create_buttons(self):
        
        buttons = [
            ("Ler dados de Pasta de Clips", self.clips),
            ("Ler dados do arquivo grafo.txt", self.ler_dados),
            ("Gravar dados no arquivo grafo.txt", self.gravar_dados),
            ("Inserir vértice", self.inserir_vertice),
            ("Inserir aresta", self.inserir_aresta),
            ("Remove vértice", self.remove_vertice),
            ("Remove aresta", self.remove_aresta),
            ("Mostrar grafo", self.mostrar_grafo),
            ("Mostrar grafo visual", self.mostrar_grafo_visual),
            ("Procurar caminho euleriano", self.caminho_euleriano),
            ("Procurar caminho hamiltoniano", self.caminho_hamiltoniano),
            ("Coloracao do grafo", self.coloracao_do_grafo),
            ("Emparelhamento", self.emparelhamneto),
            ("Informacoes", self.informacoes),
            ("Encerrar a aplicação", self.encerrar_aplicacao),
        ]

        for text, command in buttons:
            button = tk.Button(self.root, text=text, command=command, width=40, padx=10, pady=5)
            button.pack(pady=5)
    def clips(self):
        self.grafo =  lerClips("clips segurança")
        messagebox.showinfo("sucesso", "Arquivo lido e grafo montado!")
    
    def emparelhamneto(self):
        emparelhador = EmparelhamentoPerfeito(self.grafo)
        emparelhamento = emparelhador.encontrar_emparelhamento_perfeito()
        messagebox.showinfo("sucesso","Resultado presente em prompt de commando")
    





    def mostrar_grafo_visual(self):
        visualizar_grafo(self.grafo)
        
    def caminho_euleriano(self):
        euler = EulerianPathFinder(self.grafo)
        euler.find_eulerian_path()
        messagebox.showinfo("sucesso","Resultado presente em prompt de commando")

   
        

    def caminho_hamiltoniano(self):
        euler = HamiltonianPathFinder(self.grafo)
        euler.find_hamiltonian_path()
        messagebox.showinfo("sucesso","Resultado presente em prompt de commando")

    def coloracao_do_grafo(self):
        cor = GraphColoring(self.grafo)
        cor.color_graph()
        cor.print_coloring()
        messagebox.showinfo("sucesso","Resultado presente em prompt de commando")

    def navegacao(self):
        
        VideoPlayer(self.root, self.grafo,)
        root.mainloop()
    def informacoes(self):
        messagebox.showinfo("informacoes", "Essa aplicacao foi feita Por Francesco Zangrandi Coppola")

    def ler_dados(self):
        self.grafo = carregar_grafo_modelado("GRAFO.txt")
        
        messagebox.showinfo("sucesso", "Arquivo lido e grafo montado!")

    def gravar_dados(self):
        salvar_grafo_em_txt(self.grafo, "GRAFO.txt", tipo_grafo=1)
        messagebox.showinfo("Ação", "Gravar dados no arquivo grafo.txt")

    def inserir_vertice(self):
        try:
            self.grafo.addVertice(str(self.grafo.verticesNum +1))
        except Exception:
            self.grafo.addTVertice(str(self.grafo.verticesNum +1))
        
        messagebox.showinfo("sucesso", f"vertice inserido: {self.grafo.verticesNum }")


    def inserir_aresta(self):
        vertice1 = simpledialog.askinteger("onde a aresta comeca?", "Digite o numero do primeiro vertice:")
        vertice2 = simpledialog.askinteger("onde a aresta termina?", "Digite o numero do segundo vertice:")
        vertice1=self.grafo.getVertice(vertice1)
        vertice2=self.grafo.getVertice(vertice2)
        
        try:
            self.grafo.addAresta(vertice1,vertice2)
        except Exception:
            self.grafo.addTAresta(vertice1,vertice2)
        messagebox.showinfo("sucesso", "aresta inserida")

    def remove_vertice(self):
        vertice = simpledialog.askinteger("Qual vertice quer remover", "Digite o nome do vertice:")
        vertice=self.grafo.getVertice(vertice)
        self.grafo.remover_vertice(vertice)
        messagebox.showinfo("sucesso", "vertice "  +str(vertice)+" removido")

    def remove_aresta(self):
        vertice1 = simpledialog.askinteger("onde a aresta comeca?", "Digite o numero do primeiro vertice:")
        vertice2 = simpledialog.askinteger("onde a aresta termina?", "Digite o numero do segundo vertice:")
        vertice1=self.grafo.getVertice(vertice1)
        vertice2=self.grafo.getVertice(vertice2)
        self.grafo.remove_aresta(vertice1,vertice2)
       
        messagebox.showinfo("sucesso", "aresta removida")

  
        

    def mostrar_grafo(self):
        self.grafo.print()
        messagebox.showinfo("sucesso", "grafo exibido em pronpt de commando")

    
       

    def encerrar_aplicacao(self):
        self.root.quit()


class VideoPlayer:
    def __init__(self, window, grafo):
        self.window = window
        self.window.title("Video Player")
        self.grafo = grafo

        # Inicializa o vértice e os vídeos associados
        self.current_vertex = None
        self.video_sources = []

        # Configurar o primeiro vértice e carregar os vídeos associados
        self.set_initial_vertex()

        # Carregar o primeiro vídeo (se houver)
        self.vid = cv2.VideoCapture(self.video_sources[0]) if self.video_sources else None

        # Criar rótulo para exibir o vídeo
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        # Criar botões para navegação
        self.buttons_frame = tk.Frame(window)
        self.buttons_frame.pack()

        # Atualizar os botões
        self.update_buttons()

        # Atualizar a exibição do vídeo
        self.update()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def set_initial_vertex(self):
        """Define o vértice inicial e popula os vídeos associados."""
        if self.grafo.vertices:
            self.current_vertex = self.grafo.vertices[0]
            self.populate_video_sources(self.current_vertex)

    def populate_video_sources(self, vertex):
        """Popula a lista de vídeos com base nas arestas do vértice atual."""
        self.video_sources = [aresta.vertice2.clip for aresta in vertex.arestas]
        if not self.video_sources:
            self.video_sources = [vertex.clip]  # Adiciona o próprio clipe se não houver conexões

    def switch_video(self, index):
        """Troca para outro vídeo na lista de fontes."""
        if self.vid is not None:
            self.vid.release()  # Libera o vídeo atual

        if self.video_sources:
            self.vid = cv2.VideoCapture(self.video_sources[index])
        else:
            self.vid = None

    def switch_vertex(self):
        """Troca para o próximo vértice no grafo."""
        if self.current_vertex:
            current_index = self.grafo.vertices.index(self.current_vertex)
            next_index = (current_index + 1) % len(self.grafo.vertices)
            self.current_vertex = self.grafo.vertices[next_index]
            self.populate_video_sources(self.current_vertex)
            self.update_buttons()

    def update(self):
        """Atualiza a exibição do vídeo frame a frame."""
        if self.vid is not None:
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)

    def update_buttons(self):
        """Atualiza os botões de navegação."""
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        # Botões para vídeos associados ao vértice atual
        for index, video in enumerate(self.video_sources):
            button = tk.Button(self.buttons_frame, text=f"Vídeo {index + 1}", command=lambda i=index: self.switch_video(i))
            button.pack(side=tk.LEFT)

        # Botão para alternar vértices
        next_vertex_button = tk.Button(self.buttons_frame, text="Próximo Vértice", command=self.switch_vertex)
        next_vertex_button.pack(side=tk.LEFT)

    def on_closing(self):
        """Libera recursos e fecha a janela."""
        if self.vid is not None:
            self.vid.release()
        self.window.destroy()


# Função auxiliar para encontrar tags comuns
def elementos_iguais(lista1, lista2):
    return list(set(lista1) & set(lista2))

root = tk.Tk()
app = GraphApp(root)
root.mainloop()