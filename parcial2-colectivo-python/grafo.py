from fcntl import DN_DELETE
from matplotlib import pyplot as plt
import networkx as nx

class Grafo:
    aristas = []
    vertices = []
    recorrido = nx.Graph()
    colectivo = 0
    colegio = 0
    numeroCalles = 0
    dijkstra = []
    distancia = 0
    callesCambio = []

    def __init__(self):
        pass


    def crear_grafo(self):
        self.recorrido.add_nodes_from(self.vertices)
        self.recorrido.add_weighted_edges_from(self.aristas)
        self.dijkstra = nx.dijkstra_path(self.recorrido,self.colectivo,self.colegio)
        self.distancia = nx.dijkstra_path_length(self.recorrido,self.colectivo,self.colegio)


    def cambiar_manos(self):
        #.almacenamos la cantidad de elementos del recorrido de dijkstra en la variable contador
        #.inicializamos una variable numeroCalle en 1 para tener una referencia sobre las aristas
        # que estamos iterando para buscar coincidencia con las obtenidas en el recorrido dijkstra
        #-Para cambiar la mano de las calles vamos a comparar el recorrido de las calles obtenidos
        # al realizar dijkstra con el recorrido de las calles del grafo pero invertidas,
        # simulando así el cambio de mano, si coinciden, se agrega el número de la calle
        # a un array que almacena las calles que se deben cambiar de mano
        contador = len(self.dijkstra)
        numeroCalleCambiar=1
        for i in self.aristas:
            recorridoEsquinasCalle = [i[1],i[0]]
            for j in range(1,contador):
                recorridoEsquinasDijkstra = [self.dijkstra[j-1],self.dijkstra[j]]
                if recorridoEsquinasDijkstra == recorridoEsquinasCalle:
                    self.callesCambio.append(numeroCalleCambiar)
            numeroCalleCambiar+=1
            

    def cargar_datos(self):
        archivo = open("entrada.in")
        contador=0
        for linea in archivo:
            if contador==0:
                l = linea.split(" ")
                for i in range(0,int(l[0])):
                    self.vertices.append(str(i+1))
                aux1= int(l[1])-1
                aux2= int(l[2])-1
                self.colectivo = self.vertices[aux1]
                self.colegio = self.vertices[aux2]
                contador+=1
                continue
            if contador ==1:
                l = linea.split(" ")
                self.numeroCalles= l[0]
                contador+=1
                continue
            else:
                l = linea.split(" ")
                self.aristas.append((l[0],l[1],int(l[2])))
                pass

    def crear_archivo_salida(self):
        archivo = open("salida.out","w")
        archivo.write(str(self.distancia)+"\n")
        for calle in self.callesCambio:
            archivo.write(str(calle)+ " ")
        archivo.close()

grafito = Grafo()
grafito.cargar_datos()
grafito.crear_grafo()
grafito.cambiar_manos()
grafito.crear_archivo_salida()