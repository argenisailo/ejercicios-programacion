def isPalindrome(number):
    number_string = str(number)
    number_list = list(reversed(number_string))

    result = ''
    for element in number_list:
        result += element
    
    if result != number_string:
        return False
    
    return True

if __name__ == "__main__":
    number = 2002

    print(isPalindrome(number))