def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and arr[largest]<arr[l]:
        largest = l
    if r<n and arr[largest]<arr[r]:
        largest = r
    if largest!=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
