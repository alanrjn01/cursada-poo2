from matplotlib import pyplot as plt
import networkx as nx

class Grafo:
    aristas=[]
    vertices=[]
    grafoNx = nx.Graph()
    primerEscena=1
    escenaFinal=0

    def __init__(self):
        pass

    def crear_grafo(self):
        archivo = open("entrada.in")
        contador=0
        for linea in archivo:
            if contador==0:
                l = linea.split(" ")
                contador+=1
                continue
            else:
                l= linea.split(" ")
                self.vertices.append([l[0],int(l[1]),int(l[2])])
                

    def unir_escenas(self):
        flag=0
        segmentoAnterior=[]
        for segmento in self.vertices:
            if flag==0:
                segmentoAnterior = segmento
                flag+=1
                continue
            else:
                for segmentoSiguiente in self.vertices:
                    self.grafoNx.add_node(segmentoAnterior[0])
                    self.grafoNx.add_node(segmentoSiguiente[0])
                    print("Cosas: ")
                    print(segmentoSiguiente)
                    print(segmentoAnterior)
                    if segmentoSiguiente[0] == segmentoAnterior[0]:
                        continue
                    elif segmentoAnterior[2] == segmentoSiguiente[1]:
                        diferencia = 1
                        #self.grafoNx.add_weighted_edges_from(segmentoAnterior[0],segmentoSiguienteLista[0],diferencia)
                        continue
                    elif segmentoAnterior[2] < segmentoSiguiente[1]:
                        diferencia = segmentoAnterior[2] - segmentoSiguiente[1]
                        #self.grafoNx.add_weighted_edges_from(segmentoAnterior[0],segmentoSiguiente[0],diferencia)
                        segmentoAnterior = segmentoSiguiente
                        continue

                
                    
                    
    
    def unir_escenas_grafo(self):
        nx.draw(self.grafoNx, with_labels=True)
        plt.show()
        pass
                
        
    def crear_archivo(self,texto,recorrido):
        archivo = open("salida.out","w")
        archivo.write(texto + str(recorrido))
        archivo.close()

ex = Grafo()
ex.crear_grafo()
ex.unir_escenas()