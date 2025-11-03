#Vytvor obdĺžnik z 'x' a 'y' podľa zadaných rozmerov
a = int(input())
b = int(input())
print ('y' * b)
for i in range (a - 2):
    print('y' + 'x' * (b-2) + 'y')
print ('y' * b)
    