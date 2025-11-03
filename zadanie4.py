#Nájdi maximum a minimum zo zadaných čísel oddelených 'x'
a = input().split('x')
maxi = 0
mini = int(a[0])
for i in a:
    if int(i) > maxi :
        maxi = int(i)
    if mini > int(i):
        mini = int(i)
print(maxi,mini)


