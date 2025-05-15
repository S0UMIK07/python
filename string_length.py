
num=input("Enter The String\n")
temp=0
for x in num:
    if(x!=' '):
        temp+=1
print("The Number of Char present in string is "+str(temp))