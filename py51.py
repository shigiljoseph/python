n=input("Enter the list:").split()
s=input("Enter the element to search:")
c=0
for i in n:
    if(i==s):
        c+=1
print('Occurance of ',s,'=',c)
