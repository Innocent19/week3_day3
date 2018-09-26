a = int(input("Enter integer a : "))
b = int(input("Enter integer b : "))
def power(a,b):
    
    if b==0:
        return 1
    

    if b<0:
       
        return 1/a*power(a,b+1)
    
    return a*power(a,b-1)
    

print(power(a,b))