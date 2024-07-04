def heapify(arr, size, index):
    left = 2 * index
    right = 2 * index + 1
    largest = index

    if left < size and arr[left] > arr[index]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, size, largest)

def maxHeap(arr):
    size = len(arr)

    for index in range(size//2, 0, -1):
        heapify(arr, size, index)

if __name__ == "__main__":
    arr = [4, 7, 8, 3, 2, 9, 5, 10, 6, 1]
    
    maxHeap(arr)

    print(f'Heap: {arr[1:]}')