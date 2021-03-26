def selectionsort(lista):
    tmp = 0
    while tmp < len(lista):
        min_val = lista[0]
        ind = 0
        for i in range(len(lista)-tmp):
            if lista[i] < min_val:
                min_val = lista[i]
                ind = i
        tmp += 1
        el = lista.pop(ind)
        lista.append(el)
