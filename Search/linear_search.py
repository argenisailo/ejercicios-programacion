def linearSearch(arr, element):
    for index in range(len(arr)):
        if element == arr[index]:
            return f'Element was located at index {index}'
    
    return "Element was not located"

if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    element = 12

    print(linearSearch(arr, element))