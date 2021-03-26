def bubblesort(lista):
    tmp = 0
    count = 1
    while len(lista)-1-tmp > 0 and count != 0:
        count = 0
        for i in range(len(lista)-1-tmp):
            if lista[i+1] < lista[i]:
                lista[i+1], lista[i] = lista[i], lista[i+1]
                count += 1
        tmp += 1
