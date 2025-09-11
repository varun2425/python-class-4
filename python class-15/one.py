unames = ['Varun', 'Annu', 'Vani', 'Karthik', 'Ammu', 'Rohan', 'James', 'Ritivik', 'Renuka']
enames = []  # You need to initialize the 'enames' list first

for uname in unames:
    enames.append(uname.upper()) # You should apply .upper() to 'uname', not 'unames'

print(unames)
print(enames)