def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a = a.replace("0b", "")
    b = b.replace("0b", "")
    int_a = integerization(a)
    int_b = integerization(b)
    sum_ab = int_a+int_b
    binary_sum = binaryization(sum_ab)
    return "0b" + binary_sum

def integerization(j):
    result = 0
    power = 0
    for bit in j[::-1]:  
        if bit == '1':
            result += 2 ** power
        power += 1
   
    return result
def binaryization(n):
    if n == 0:
        return "0"   
    resu = ""
    while n > 0:
        remainder = n % 2
        resu = str(remainder) + resu
        n = n // 2
    return resu
    
    
    

