def find(num):
    # code logic here
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

num = int(input('Enter the number: '))  
numtype = find(num)                     
print('Given number is',numtype).      
