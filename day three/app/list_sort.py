thislist = [4, 9.5, "a", 2, 6, 7, 5]

evens = []
odds = []
chars = []
thisdict = dict()
def list_sort():
    for x in thislist:
        if( isinstance(x,int) and x%2 == 0):
            evens.append(x)
        elif ( isinstance(x,int) and x%2 == 1):
            odds.append(x)
        elif isinstance(x,str):
            chars.append(x)

    thisdict["evens"]=sorted(evens)
    thisdict["odds"]=sorted(odds)
    thisdict["chars"]=sorted(chars)
    print(thisdict)
print(sorting_function())    

