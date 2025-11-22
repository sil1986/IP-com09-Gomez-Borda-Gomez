# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    # TODO:
    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    return {"done": True}


## ajustes desde aqui

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    
    items = list(vals)
    n = len(items)
    
    # Común: arrancar en el segundo elemento
    i = 1 
    j = None

def step():
    global items, n, i, j

    # 1. Si i >= n: devolver {"done": True}
    if i >= n:
        return {"done": True}

    # 2. Si j es None: empezar desplazamiento para el items[i]
    if j is None:
        # Iniciamos el desplazamiento desde la posición i
        j = i
        return {"a": j - 1, "b": j, "swap": False, "done": False}

    # 3. Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j)
    if j > 0 and items[j - 1] > items[j]:
        
        # Hacemos el swap y mantenemos el puntero j en el nuevo índice del elemento.
        items[j - 1], items[j] = items[j], items[j - 1] 
        
        puntero_a = j - 1
        puntero_b = j
        
        # Retroceder j para la siguiente comparación
        j -= 1
        
        # Devolvemos el resultado del swap
        return {"a": puntero_a, "b": puntero_b, "swap": True, "done": False}

    # 4. Si ya no hay que desplazar: avanzar i y setear j=None
    #    Esto se ejecuta cuando: (j==0) O (items[j-1] <= items[j])
    i += 1  # Avanzar la frontera para el siguiente elemento a insertar
    j = None # Reiniciar j para indicar que debe empezar la siguiente pasada
    
    # Devolver el final de la pasada, comparando el elemento insertado (i-1) con el nuevo (i)
    return {"a": i - 1, "b": i, "swap": False, "done": False}