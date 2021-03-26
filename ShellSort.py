from BubbleSort import bubblesort as bubble


def shellsort(lista,step):
    x = 0
    t = 0
    while x < len(lista):
        lista_tmp = []
        indexy = []
        for i in range(t, len(lista), step):
            lista_tmp.append(lista[i])
            indexy.append(i)
            x += 1
        bubble(lista_tmp)
        for i in indexy:
            lista[i] = lista_tmp.pop(0)
        t += 1
    bubble(lista)
