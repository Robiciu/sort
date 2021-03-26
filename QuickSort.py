def partition(lista, start, end):
    pivot = lista[start]
    less_ind = start
    more_ind = end
    while True:
        while lista[less_ind] < pivot:
            less_ind += 1
        while lista[more_ind] > pivot:
            more_ind -= 1
        if less_ind >= more_ind:
            break
        lista[less_ind], lista[more_ind] = lista[more_ind], lista[less_ind]
    return more_ind


def quicksort(lista, start, end):
    if start >= end:
        return
    tmp = partition(lista, start, end)
    quicksort(lista, start, tmp-1)
    quicksort(lista, tmp+1, end)
