# Recursive approach
def binarySearchV1(arr, low, high, key):
    if high >= low:
        middle = low + (high - low) // 2

        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            return binarySearchV1(arr, low, (middle - 1), key)
        else:
            return binarySearchV1(arr, (middle + 1), high, key)
    else:
        return -1
    
# Iterative approach
def binarySearchV2(arr, low, high, key):
    while low <= high:
        middle = low + (high - low) // 2
        
        if arr[middle] == key:
            return middle
        elif arr[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    return -1

if __name__ == '__main__':
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    low = 0
    high = len(arr)
    key = 2

    result1 = binarySearchV1(arr, low, high, key)
    result2 = binarySearchV2(arr, low, high, key)
    print("Recursive: ", result1)
    print("Iterative: ", result2)