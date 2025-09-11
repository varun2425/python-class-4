unames = ['Varun', 'Annu', 'Vani', 'Karthik', 'Ammu', 'Rohan', 'James', 'Ritivik', 'Renuka']

def checkname(name):
    return name.startswith('r')

new_users=list(filter(checkname,unames))
print(unames)
print(new_users)



