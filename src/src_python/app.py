from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__=="__main__":
    print("funciona")
    
    metodos=MetodosOrdenamiento()
    benchmark = Benchmarking()
    
    tam=10000
    arreglo_base = benchmark.build_arreglo(tam)
    
    #diccionario
    #2 elementos
    metodos = {
        "burbuja": metodos.sort_Bubble,
        "seleccion": metodos.sort_seleccion,
    }
    
    resultados=[]
    for nombre, metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tuplaResultado = (tam,nombre,tiempo)
        resultados.append(tuplaResultado)
        
    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print(f"Tamano: {tam}, Matodo: {nombre}, Tiempo: {tiempo:.6f} segundos")