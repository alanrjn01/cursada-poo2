import networkx as nx
import os

import matplotlib.pyplot as plt

class Grafo:

    aristas=[]
    vertices=[]
    graph = nx.Graph()
    posPrincipe=0
    posPrincesa=0
    posDragones=[]

    def __init__(self):
        pass

    def crear_grafo(self):
        self.graph.add_nodes_from(self.vertices)
        self.graph.add_weighted_edges_from(self.aristas)


    def buscar_princesa_dijkstra(self):
        print("princesa", self.posPrincesa)
        print("principe", self.posPrincipe)
        print("vertices", self.vertices)
        print("aristas", self.aristas)
        if(nx.has_path(self.graph,self.posPrincipe,self.posPrincesa)):
            self.graph.remove_nodes_from(self.posDragones)
            if(nx.has_path(self.graph,self.posPrincipe,self.posPrincesa)):
                self.crear_archivo("",dijkstra)
            else:
                self.crear_archivo("INTERCEPTADO","")
        else:
           self.crear_archivo("NO HAY CAMINO","")
        dijkstra=nx.dijkstra_path(self.graph,self.posPrincipe,self.posPrincesa)
        nx.draw(self.graph, pos=nx.circular_layout(self.graph), node_color='r', edge_color='r', with_labels=True)
        plt.show()

    def leer_archivo(self):
        archivo = open("entrada.in")
        contador=0
        cantidadDragones=0
        for linea in archivo:
            if contador==0:
                l = linea.split(" ")
                for i in range(0,int(l[0])):
                    self.vertices.append((i+1).__str__())
                cantidadDragones+=int(l[2])
                contador+=1
                continue
            if contador==1:
                l= linea.split(" ")
                aux1= int(l[0])-1
                aux2= int(l[1])-1
                self.posPrincesa=self.vertices[aux1]
                self.posPrincipe=self.vertices[aux2]
                contador+=1
                continue
            if contador==2:
                l= linea.split(" ")
                for i in range(0,cantidadDragones):
                    aux = int(i)-1
                    self.posDragones.append(self.vertices[aux])
                contador+=1
                continue
            else:
                l= linea.split(" ")
                self.aristas.append((l[0],l[1],int(l[2])))
                pass
        
    def crear_archivo(self,texto,recorrido):
        archivo = open("salida.out","w")
        archivo.write(texto + str(recorrido))
        archivo.close()


grafo1 = Grafo()
grafo1.leer_archivo()
grafo1.crear_grafo()
grafo1.buscar_princesa_dijkstra()