# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"
def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"
def step():
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    return {"done": True}

##aqui empece a alterar el sort_selection.py
items = []
n = 0
i = 0         # Cabeza de la parte no ordenada
j = 0         # Cursor que recorre y busca el mínimo
min_idx = 0   # Índice del mínimo de la pasada actual
fase = "buscar" # Fases: "buscar" o "swap"

def init(vals):
    
    global items, n, i, j, min_idx, fase
    
    items = list(vals)
    n = len(items)
    
    i = 0
    j = 1
    min_idx = 0
    fase = "buscar"

def step():

    global items, n, i, j, min_idx, fase
    
    
    if i >= n - 1:
        return {"done": True} 

    if fase == "buscar":
        
        
        if j < n:
            puntero_a = j
            puntero_b = min_idx
            
            if items[j] < items[min_idx]:
                min_idx = j
            
            j += 1
            
            return {"a": puntero_a, "b": puntero_b, "swap": False, "done": False}
        
        else: 
            fase = "swap"
            return step()
    
    elif fase == "swap":
        
        
        puntero_a = i
        puntero_b = min_idx
        swap_hecho = False
        
        if i != min_idx:
            items[i], items[min_idx] = items[min_idx], items[i]
            swap_hecho = True
            
        # Preparar para la siguiente pasada
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        
        return {"a": puntero_a, "b": puntero_b, "swap": swap_hecho, "done": False}