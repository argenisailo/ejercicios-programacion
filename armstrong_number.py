def isArmstrong(num):
    number = list(str(num))

    aux = 0

    for i in range(len(number)):
        aux += pow(int(number[i]), len(number))

    if aux != num:
        return False
    
    return True

if __name__ == "__main__":
    number = 120

    print(isArmstrong(number))
