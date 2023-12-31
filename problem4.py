digit1 = 100
digit2 = 100

def palindrome(num): 
    
    # Converting the number into string
    string = str(num)

    # Run loop from 0 to len/2 
    for i in range(0, len(string)//2): 
        if string[i] != string[len(string)-i-1]: 
            return False
            
    # If the above loop doesn't  
    #return then it is palindrome 
    return True

max = 0

while digit1 < 1000 and digit2 < 1000:
    
    # get the product
    product = digit1 * digit2

    # check if the product is a palindrome
    if palindrome(product) and product > max:
        max = product

    if digit1 == 999:
        digit2 += 1
        digit1 = 100
    else:
        digit1 += 1

print(max)