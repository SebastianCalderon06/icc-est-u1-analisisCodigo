import time
import random
from metodos_ordenamiento import MetodosOrdenamiento
class Benchmarking():
    def __init__(self):
        print('Bench Inicializado')
        
        def ejemplo():
            
            self.mOrdenamiento = MetodosOrdenamiento()
            arreglo = self.build_arreglo(10000)
            tarea = lambda: self.mOrdenamiento.sort_Bubble(arreglo)
            tiempoMillis = self.contar_con_current_time_millis(tarea)
            tiempoNano = self.contar_con_nano_time(tarea)
            print (f'tiempo{tiempoMillis}')
            print (f'tiempo{tiempoNano}')
        
        
    def build_arreglo(self, size):
        array = []
        for i in range(size):
            numero = random.randint(0,99999)
            array.append(numero)
        return array 
    
    #import time
    #ejecutar tarea tarea()
    
    # x = time.time()
    def contar_con_current_time_millis(self,tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return (fin - inicio)
    
    # x = time.time_ns()
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio)/1_000_000_000.0
    
    def medir_tiempo(self,tarea,array):
        inicio=time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin - inicio
        