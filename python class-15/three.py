unames = ['Varun', 'Annu', 'Vani', 'Karthik', 'Ammu', 'Rohan', 'James', 'Ritivik', 'Renuka']

new_users=[]
for uname in unames:
    if uname.startswith('r'):
        new_users.append(uname)

print(unames)
print(new_users)