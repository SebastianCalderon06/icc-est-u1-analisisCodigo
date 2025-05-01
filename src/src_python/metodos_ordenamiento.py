class MetodosOrdenamiento:
    
    def sort_Bubble(self, arreglo):
        arreglo = arreglo.copy()
        n=len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i],arreglo[j] = arreglo[j], arreglo[i]
        return arreglo            
    
    
    def sort_seleccion(self, array):
        aux = 0
        n=len(array) 
        array = array.copy()
        for i in range (n):
            maxIdx=i
            for j in range (i+1, n):
                if (array[maxIdx] > array[j]):
                     maxIdx = j
                     if (maxIdx != i):
                        aux = array[maxIdx]
                        array[maxIdx] = array[i]
                        array[i] = aux
                    
                           
