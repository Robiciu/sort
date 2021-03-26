def heapify(lista, n, i):
	parent = i
	left_child = 2*i + 1
	right_child = 2*i + 2
	if left_child < n and lista[parent] < lista[left_child]:
		parent = left_child
	if right_child < n and lista[parent] < lista[right_child]:
		parent = right_child
	if parent != i:
		lista[i], lista[parent] = lista[parent], lista[i]
		heapify(lista, n, parent)


def heapsort(lista):
	n = len(lista)
	for i in range(n // 2 - 1, -1, -1):
		heapify(lista, n, i)
	for i in range(n-1, 0, -1):
		lista[i], lista[0] = lista[0], lista[i]
		heapify(lista, i, 0)
		
