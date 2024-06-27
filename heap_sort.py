def heapSort(arr):
    sorted_arr = []
    length = len(arr)

    while length > 0:
        sorted_arr.insert(0, Heapify(arr))
        length -= 1

    return sorted_arr

def Heapify(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > arr[(i-1)//2]:
            aux = arr[(i-1)//2]
            arr[(i-1)//2] = arr[i]
            arr[i] = aux
    
    return arr.pop()

if __name__ == "__main__":
    arr = [4, 7, 8, 3, 2, 9, 5, 10, 6, 1]
    print(heapSort(arr))