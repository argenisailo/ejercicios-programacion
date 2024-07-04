def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = mergeSort(left)
    right = mergeSort(right)

    return Merge(left, right)

def Merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while len(left) > 0:
        result.append(left.pop(0))

    while len(right) > 0:
        result.append(right.pop(0))

    return result

if __name__ == "__main__":
    arr = [4, 7, 8, 3, 2, 9, 5, 10, 6, 1]

    print(f'Unsorted array = {arr}')
    print(f'Sorted array = {mergeSort(arr)}')