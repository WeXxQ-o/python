vstup = input()
temp=''
for i in vstup:
    if i not in '/+-"=*':
        temp+= i
print(temp)