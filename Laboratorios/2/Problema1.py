#Problema 1 del laboratorio
import math

website_page_ranks = [3,39,61,91,57,22,75,89,9,90,63,78,28,73,20]
contador = 0

def AumentaContador():
	global contador 
	contador = contador +1

def MergeSort(arreglo):
	AumentaContador()
	if len(arreglo)>1:
		mitad = math.floor(len(arreglo)/2)
		L = arreglo[:mitad]
		R = arreglo[mitad:]
		MergeSort(L)
		MergeSort(R)
		i=0
		j=0
		k=0
		while i < len(L) and j < len(R):
			if L[i] > R[j]:
				arreglo[k]=L[i]
				i=i+1
			else:
				arreglo[k]=R[j]
				j=j+1
			k=k+1
		while i < len(L):
			arreglo[k]=L[i]
			i=i+1
			k=k+1
		while j < len(R):
			arreglo[k]=R[j]
			j=j+1
			k=k+1
		

		   

print(website_page_ranks)
MergeSort(website_page_ranks)
print("El arreglo ordenado queda así: ", website_page_ranks, "Y entra al método MergeSort ", contador, "veces. ")
print("Por lo tanto la relación entre el número de ítems es", contador/len(website_page_ranks))


