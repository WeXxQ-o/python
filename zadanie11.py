#Nájdi maximum a minimum zo zadaných čísel oddelených medzerou
a = input().split()
maxi =  0
mini = a[0]
for i in a:
    if i.isdigit():
        if int(i) > int (maxi):
            maxi = i
        if int(i) < int (mini):
            mini = i
print("Maximum is:",maxi)   
print("Minimum is:",mini)