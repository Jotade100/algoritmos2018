#Problema 2

possible_heap = [16,14,10,8,7,9,3,2,4,1]

contador = 0

def AumentaContador():
	global contador 
	contador = contador +1


def VerificaSiEsHeap(arreglo, inicio):
	AumentaContador()
	if inicio < len(arreglo):
		#calcular hijo izquierdo y derecho
		left = 2*inicio +1
		right =  2*inicio +2
		if (left < len(arreglo)):
			if(arreglo[left] <= arreglo[inicio]):
				VerificaSiEsHeap(arreglo, left)
			else:
				print("No es Heap ya que el hijo es: ", arreglo[left], " y el padre es ", arreglo[inicio])
		if (right < len(arreglo)):
			if(arreglo[right] <= arreglo[inicio]):
				VerificaSiEsHeap(arreglo, right)
			else:
				print("No es Heap ya que el hijo es: ", arreglo[right], " y el padre es ", arreglo[inicio])
			
			
print("Si el arreglo no es un heap se listarán las razones siguientes: ")
VerificaSiEsHeap(possible_heap, 0)
print("-------------------------------FIN----------------------------------")
print("El programa ingresó al método ", contador, " veces y su razón con el número de elementos es ", contador/len(possible_heap))



		
			