# thislist = [1,2,7,8,[5,6,10],[11,12]]
def sum_items(thislist):
    total = 0
    for index in range(len(thislist)):   
        if isinstance(thislist[index], list):
            total = total +  sum_items(thislist[index])
        else:    
            total += thislist[index]    
    return total
print(sum_items([1,2,7,8]))
print(sum_items([1,2,7,8,[5,6,10], 2, [6,8]]))

