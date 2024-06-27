# Dictionary approach
def printStringV1(string, char, count):
    char_dictionary = {}

    for i in range(len(string)-1):
        if string[i] in char_dictionary:
            char_dictionary[string[i]] += 1
        else:
            char_dictionary[string[i]] = 1

    if char_dictionary[char] == count or char_dictionary[char] == 0:
        print(string)
    else:
        print('Empty string')

# Different approach
def printStringV2(string, char, count):
    counter, i = 0, 0

    if count == 0:
        print(string)

    for i in range(len(string)):
        if string[i] == char:
            counter += 1

        if counter == count:
            break

    if i < len(string) - 1:
        print(string)
    else:
        print('Empty string')

if __name__ == "__main__":
    string = 'aaa'
    char = 'a'
    count = 3

    printStringV1(string, char, count)
    printStringV2(string, char, count)