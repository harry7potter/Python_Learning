def find(num):
    # code logic here
    numtype = "odd"
    if num%2 == 0:
        numtype="even"
    return numtype

num = int(input('Enter the number: '))      
numtype = find(num)                        
print('Given number is',numtype)        
      
