def heapSort(arr):
    sorted_arr = []
    length = len(arr)

    while length > 0:
        sorted_arr.insert(0, heapify(arr))
        length -= 1
    
    return sorted_arr

def heapify(arr):
    for index in range(len(arr)-1, -1, -1):
        if arr[index] > arr[(index-1)//2]:
            aux = arr[(index-1)//2]
            arr[(index-1)//2] = arr[index]
            arr[index] = aux

    return arr.pop()

if __name__ == "__main__":
    arr = [4, 7, 8, 3, 2, 9, 5, 10, 6, 1]

    print(f'Unsorted array = {arr}')
    print(f'Sorted array = {heapSort(arr)}')