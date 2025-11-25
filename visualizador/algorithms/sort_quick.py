items = []
stack = []       # pila de subrangos pendientes
i = j = 0
pivote = None
fase = "buscar"

def init(vals):
    global items, stack, i, j, pivote, fase
    items = list(vals)
    stack = [(0, len(items)-1)]   # rango inicial completo
    i = j = 0
    pivote = None
    fase = "buscar"

def step():
    global items, stack, i, j, pivote, fase

    # Caso base: si no quedan subrangos
    if not stack:
        return {"done": True}

    # Tomar el subrango actual
    left, right = stack[-1]

    if left >= right:
        stack.pop()
        return {"done": False}

    # Fase buscar: elegir pivote y preparar índices
    if fase == "buscar":
        pivote = items[right]   # pivote = último elemento
        i = left - 1
        j = left
        fase = "particionar"

    # Fase particionar: recorrer y hacer swaps
    if fase == "particionar":
        if j < right:
            if items[j] <= pivote:
                i += 1
                items[i], items[j] = items[j], items[i]
                j += 1
                return {"a": i, "b": j-1, "swap": True, "done": False}
            else:
                j += 1
                return {"a": j-1, "b": j-1, "swap": False, "done": False}
        else:
            # colocar pivote en su lugar
            items[i+1], items[right] = items[right], items[i+1]
            pos = i+1
            stack.pop()
            # agregar subrangos izquierdo y derecho
            stack.append((left, pos-1))
            stack.append((pos+1, right))
            fase = "buscar"
            return {"a": pos, "b": right, "swap": True, "done": False}