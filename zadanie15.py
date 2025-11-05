a = int(input())

for i in range(a):
    riadok = 'o' * (a - i) + '*' * (i + 1)
    print(riadok[1:])