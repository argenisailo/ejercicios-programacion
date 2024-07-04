# Libraries approach
def isPalindromeV1(number):
    number_string = str(number)
    number_list = list(reversed(number_string))
    result = ''
    
    for element in number_list:
        result += element
    
    if result != number_string:
        return False
    
    return True

# Raw approach
def isPalindromeV2(number):
    number_string = str(number)
    reversed_number = ''

    for i in range(len(number_string), 0, -1):
        reversed_number += number_string[i-1]

    if reversed_number != number_string:
        return False
    
    return True

if __name__ == "__main__":
    number = 2002

    print(isPalindromeV1(number))
    print(isPalindromeV2(number))