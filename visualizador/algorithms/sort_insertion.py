"""# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

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
    return {"done": True}"""""


## ajustes desde aqui
items = []
n = 0
i = 1   # elemento que queremos insertar
j = 1   # cursor de desplazamiento hacia la izquierda
current_val=0  # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j, current_val
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = i
    current_val = 0

def step():
    if i >= n:
        return {"a":0, "b":0, "swap": False , "done": True}
    if j==i and j> 0 and current_val ==0:
        current_val = items[i]
    if j>0 and items[j-1] > current_val:
        items[j] = items[j-1]
        punt_a = j-1
        punt_b = j
        j -= 1
        return {"a": punt_a, "b": punt_b, "swap": True , "done": False}
    items[j] = current_val
    i += 1
    j = i
    current_val = 0
    return {"a": j, "b": j, "swap": False , "done": False}