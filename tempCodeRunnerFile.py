n = int(input().strip())
if 1<=n<=150:
    for i in range(1, (n+1)):
            
            #print(i, end = '')
            #print(i, end = '\n')  
            print(i, end = '@nonewlineconcate')    
else: 
    print("Out of the range of 1 to 20")
