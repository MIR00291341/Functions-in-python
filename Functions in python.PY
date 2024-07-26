def maxThree(): 
    a = int(input("Enter Frist Number: "))
    b = int(input("Enter Second Number: "))
    c = int(input("Enter Third Number: "))

    if a >= b and a >= c: 
        largeNumber = a
        
    elif b >= a and b >= c:
        largeNumber = b 
       
    else: 
        largeNumber = c 
        
        
    return(largeNumber)



print(maxThree(),"is Largest Number")
