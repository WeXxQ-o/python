#Vypíš iba tie čísla zo vstupu, ktoré sú deliteľné 3
a = input('Zadaj string: ').split()
for i in a:
    if i.isdigit() and int(i) % 3 == 0:
        print(i)