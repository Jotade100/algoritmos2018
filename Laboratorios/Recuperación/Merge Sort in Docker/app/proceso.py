from multiprocessing import Process, Manager
from multiprocessing import Queue
import string
from random import *
import time;
import math;


# El código de Merge-Sort no es mío. Fuente: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
# Ordena cadenas de caracteres perfectamente. :)
# Luego insertaré el hecho en clase. La idea es insertarlo una vez funcione. ^^
# Fue usado como base.
def mergeSortFijo(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSortFijo(lefthalf)
        mergeSortFijo(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


# Algoritmo modificado para uso paralelo :)			
def mergeSortVariable(alist, a):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = Manager().list(alist[:mid])
        righthalf = Manager().list(alist[mid:])

        #mergeSortFijo(lefthalf)
        p = Process(target = mergeSortVariable, args=(lefthalf, 1))
		#mergeSortFijo(righthalf)
        q = Process(target = mergeSortVariable, args=(righthalf, 1))
        p.start()
        q.start()
        p.join()
        q.join()
		

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


			
# La función se ejecuta por cada nodo activo
def funcionMergeSortFijo(arreglo, output):
	mergeSortFijo(arreglo)
	output.put(arreglo)


def funcionMergeSortVariable(arreglo):
	p = Process(target=mergeSortVariable, args=(arreglo,1))
	p.start()
	p.join()
	
# El programa principal según documentación...
if __name__ == '__main__':
	with Manager() as manager:
		#variables de uso general
		nodos = 8
		nombredelPrograma = "app/texto.txt"
		nombredelPrograma2 = "app/resultado.txt"
		output = Queue()
		text_file = open(nombredelPrograma, "r")
		text_file2 = open(nombredelPrograma2, "a")
		lines = text_file.readlines()
		# # # # # # # # # # # # # # si separa por nodos fijos # # # # # # # # # # # # # #
		# No se usa por ser ineficiente
		#texto = [None]*nodos
		
		# separando el archivo de texto en nodos
		#for x in range(0, nodos):
		#	print(x)
		#	texto[x] = lines[(len(lines)*x)//nodos:(len(lines)*(x+1))//nodos]
		#
		#
		#p = [Process(target=funcionMergeSortFijo, args=(x, output)) for x in texto]
		#for item in p:
		#	item.start()
		#	item.join()
		#results = [output.get() for item in p]
		#print(results)
		#print(len(results))
		# # # # # # # # # # # # # # ------------------------- # # # # # # # # # # # # # #
		
		
		# # # # # # # # # # # # # # si crea nodos al ir separando cada merge # # # # # # # # # # # # # #
		
		inicio = time.time()
		lines = manager.list(lines)
		#p = Process(target=mergeSortVariable, args=(lines,1))
		#p.start()
		#p.join()
		mergeSortVariable(lines, 1)
		#mergeSortFijo(lines)
		print("Tardó :", time.time() - inicio)
		for i in lines:
			text_file2.write(i)
		
		#print(len(lines))
		# # # # # # # # # # # # # # ---------------------------- # # # # # # # # # # # # # #