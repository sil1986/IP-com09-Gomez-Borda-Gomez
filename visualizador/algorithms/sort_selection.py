"""# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

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
    return {"done": True}"""

##aqui empece a alterar el sort_selection.py
items = []  
n = 0
i = 0       # El índice del inicio de la parte no ordenada
j = 0       # El índice que recorre la parte no ordenada para buscar el mínimo
min_idx = 0

def init(vals: list[int]) -> None:
    """
    Inicializa el algoritmo de Ordenamiento por Selección.
    """
    global items, n, i, j, min_idx
    
    # 1. Guardar copia e inicializar n (Contrato)
    items = list(vals)
    n = len(items)
    
    # 2. Inicializar punteros/estado interno
    i = 0
    min_idx = i
    j = i + 1

def step() -> dict:
    """
    Ejecuta un único micro-paso del Selection Sort.
    """
    global items, n, i, j, min_idx
    
    # 1. CONDICIÓN DE PARADA: Si i ha llegado al final (todo ordenado)
    if i >= n - 1:
        # Devuelve done=True para indicar al visualizador que terminó
        return {"a": 0, "b": 0, "swap": False, "done": True}

    # -----------------------------------------------
    # FASE 1: Búsqueda del Mínimo
    # -----------------------------------------------
    if j < n:
        # Punteros a devolver: Comparamos j con min_idx
        puntero_a = j
        puntero_b = min_idx

        # Comparación: Actualizamos min_idx si encontramos un valor más pequeño
        if items[j] < items[min_idx]:
            min_idx = j # Nuevo mínimo encontrado
            
        j += 1 # Avanzamos el puntero de búsqueda (j)
        
        # Devolvemos la comparación (no hay swap en esta fase)
        return {"a": puntero_a, "b": puntero_b, "swap": False, "done": False}

    # -----------------------------------------------
    # FASE 2: Intercambio (Swap) y Reinicio
    # -----------------------------------------------
    else:
        # El ciclo interno (j) terminó. Se encontró el mínimo (min_idx).
        puntero_a = i
        puntero_b = min_idx
        
        # Realizar el intercambio solo si el mínimo no es el elemento actual (i)
        if i != min_idx:
            # Realiza el SWAP en la lista (Regla del Contrato)
            items[i], items[min_idx] = items[min_idx], items[i]
            swap_hecho = True
        else:
            swap_hecho = False
            
        # Preparar para la siguiente pasada (mover la frontera de la parte ordenada)
        i += 1
        min_idx = i
        j = i + 1 # Reiniciar el puntero de búsqueda para la nueva pasada
        
        # Devolvemos el resultado del intercambio
        return {"a": puntero_a, "b": puntero_b, "swap": swap_hecho, "done": False}