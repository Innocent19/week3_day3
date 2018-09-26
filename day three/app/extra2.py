thislist= [2,4,1,7,4,8,9,11]
x = sorted(thislist)
new_list = []
y = x[-1]
print(y)
z = x[0]
print(z)
for i in range(z,y+1):
    if i not in thislist:
        new_list.append(i)
print(new_list)        