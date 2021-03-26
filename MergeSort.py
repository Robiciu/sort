def mergesort(lista):
    if len(lista) > 1:
        border = len(lista)//2
        part1 = lista[:border]
        part2 = lista[border:]
        mergesort(part1)
        mergesort(part2)
        i = j = k = 0
        while i < len(part1) and j < len(part2):
            if part1[i] < part2[j]:
                lista[k] = part1[i]
                i += 1
            else:
                lista[k] = part2[j]
                j += 1
            k += 1
        while i < len(part1):
            lista[k] = part1[i]
            i += 1
            k += 1
        while j < len(part2):
            lista[k] = part2[j]
            j += 1
            k += 1


