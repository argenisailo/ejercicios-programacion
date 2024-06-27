def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    left_arr = mergeSort(left_arr)
    right_arr = mergeSort(right_arr)

    return Merge(left_arr, right_arr)

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
    print(mergeSort(arr))