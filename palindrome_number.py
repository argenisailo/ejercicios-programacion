def isPalindrome(number):
    number_string = str(number)
    number_list = list(reversed(number_string))

    result = ''
    for number_i in number_list:
        result += number_i
    
    if result != number_string:
        return False
    
    return True

if __name__ == "__main__":
    number = 2002

    print(isPalindrome(number))