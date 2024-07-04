def binarySearch(arr, left, right, element):
    if right >= left:
        middle = left + (right - left) // 2

        if arr[middle] == element:
            return f'Element was located at index {middle}'
        elif arr[middle] > element:
            return binarySearch(arr, left, middle-1, element)
        else:
            return binarySearch(arr, middle+1, right, element)
    else:
        return "Element was not located"

if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    left = 0
    right = len(arr)

    element = 12

    print(binarySearch(arr, left, right, element))