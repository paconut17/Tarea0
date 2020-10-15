import numpy as np 
from time import time
import matplotlib.pylab as pb
####Parametros para la funcion y lista vacia a llenar
N=15
M=5
timeTarea=[]

def Funcion_Tarea_1(M,N):
	for i in range(1,M):
		for j in range(1,N):
			print(i,j)

def Complejidad_Tarea_1(funcion,lista,M,N):
	for i in range(M):
		for j in range(N):			
			t_inicio=time()*1000
			funcion(i,j)
			t_fin=time()*1000
			t_total=t_fin-t_inicio
		lista.append(t_total)

#Aplicacion de la funcion complejidad a la Funcion de la Tarea 1 y obtencion del aregglo  time Tarea[]
Complejidad_Tarea_1(Funcion_Tarea_1,timeTarea,N,M)
print(timeTarea)  
x=[i for i in range(len(timeTarea))]

pb.title('Complejidad en tiempo') #titulo
pb.xlabel('n')  #nombre del eje x
pb.ylabel('Tiempo de ejecución') #nombre del eje y
pb.plot(x,timeTarea,label='Algoritmo de la Tarea 1')
pb.legend()
pb.show()
