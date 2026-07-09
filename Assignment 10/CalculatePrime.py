def ChkPrime(No):
    if No <= 1 :
        return False
    
    for i in range(2, No):
        if No % 2 == 0 :
            return False

    return True
