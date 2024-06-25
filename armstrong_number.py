# Libraries approach
def isArmstrongV1(number):
    number_list = list(str(number))
    result = 0

    for i in range(len(number_list)):
        result += pow(int(number_list[i]), len(number_list))

    if result != number:
        return False
    
    return True

# Raw approach
def isArmstrongV2(number):
    number_string = str(number)
    number_list = []
    result = 0

    # Slicing
    for i in number_string[::-1]:
        number_list.append(int(i))

    for i in range(len(number_list)):
        result += pow(int(number_list[i]), len(number_list))
    
    if result != number:
        return False
    
    return True

if __name__ == "__main__":
    number = 153

    print(isArmstrongV1(number))
    print(isArmstrongV2(number))