vstup = input().split()
temp=''
for i in vstup:
    if i.isdigit():
        temp+= ''
    else:
        for znak in i:
            if not znak.isdigit():
                temp += znak
print(temp)