numbers=[10,20,30,40]

def addplusone(num):
    return num+1

map_obj=map(addplusone,numbers)
new_number=list(map_obj)
print(new_number)