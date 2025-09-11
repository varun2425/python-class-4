unames = ['Varun', 'Annu', 'Vani', 'Karthik', 'Ammu', 'Rohan', 'James', 'Ritivik', 'Renuka']

new_users=list(filter(
    lambda name:name.startswith('r'),
    unames
    ))
print(unames)
print(new_users)