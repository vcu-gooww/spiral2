def spiralize(size, n=1):
    
    sum = []
    for n in range(1, size, 2):
        
    a = n**2 #a is top right diagonal
    
    b = a - (n-1) #b is top left diagnoal
    
    c = b - (n-1) #c is bottom left diagonal
    
    d = c - (n-1) #d is bottom right diagonal
    
        Diagonal_Sum = a + b + c +d
        
    sum = Diagonal_Sum + sum
    
    return_value = sum(sum) 
    
    return return_value
# 1st Try.
