items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
pivote = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"
def init(vals):
    global items, n, i, j, pivote, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    pivote = items[n/2]   # Pivote el de la derecha
    fase = "buscar"




def step():


    global items, n, i, j, pivote, fase
   
    # Caso base: si ya ordenamos todo
    if n<=1:
        return  {"done": True}
    elif fase == "buscar":
         pivote = items[n/2]  # Elegir el pivote
         # Buscar el siguiente elemento menor que el pivote
         while j < n:
            if items[j] < pivote:
                menores = []
                mayores = []
                for k in range(n):
                    if items[k] < pivote:
                        menores.append(items[k])
                    elif items[k] > pivote:
                        mayores.append(items[k])    
               


                fase = "swap"
                return {"a": j, "b": n-1, "swap": True, "done": False}
            j += 1
            # Si no hay más elementos menores, pasar a swap
            # pero sin hacer swap
            # return {"a": j-1, "b": n-1, "swap": False, "done": False}
         fase = "swap"  
         return step()
    elif fase == "swap":
        # Preparar para la siguiente pasada
        n -= 1
        i = 0
        j = i + 1
    while i < n:
        if items[i] < pivote:
                menores = []
                mayores = []
                for k in range(n):
                    if items[k] < pivote:
                        menores.append(items[k])
                    elif items[k] > pivote:
                        mayores.append(items[k])    
               


                fase = "swap"
                return {"a": i, "b": n-1, "swap": True, "done": False}
                items = menores + [pivote] +  mayores


    return {"done": True}
