fp1=open('data.txt','r')
data=fp1.read()


fp2=open('abc.txt','w')
fp2.write(data)
print('New file created')