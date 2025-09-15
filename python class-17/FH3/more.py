fp1=open("abc.txt",'r')
fp2=open("data.txt",'w')

 
print(fp1.readable())  #True
print(fp1.writable())  #Flase
print(fp1.name)        #abc.txt
print(fp1.mode)        #r
print(fp1.closed)      #Flase




print("\n")
 
print(fp2.readable())  #Flase
print(fp2.writable())  #True
print(fp2.name)        #data.txt
print(fp2.mode)        #w
print(fp2.closed)      #Flase