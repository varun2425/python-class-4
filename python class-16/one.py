'''
dict -group of key: value pair as one entity 
     -where allowed duplicate values
       but not keys
     - index is not applicable
     - dict mutable object
'''

emp={'eid':101,
     'ename':'Varun',
     'esal':45000

}
#print all emp -values
print(emp['eid']) #101
print(emp['ename']) #Varun
print(emp['esal']) #45000
print(emp['eloc']) #key error
