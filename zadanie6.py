#Zisti či zadané 3 čísla môžu byť stranami pravouhlého trojuholníka. Ak áno, vypíš aj jeho obsah
cislo = input().split(',')
a = int(cislo[0])
b = int(cislo[1])
c = int(cislo[2])

if a + b > c and a + c > b and b + c > a:
    if a > b and a > c:
        prepopna = a
        odvesna1 = b
        odvesna2 = c

    elif b > a and b > c:
        prepopna = b
        odvesna1 = a
        odvesna2 = c
        
    else:
        prepopna = c
        odvesna1 = a
        odvesna2 = b

    if prepopna**2 == odvesna1**2 + odvesna2**2:
        obsah = (odvesna1 * odvesna2) / 2
        print('ano', int(obsah))
    else:
        print('nie')
else:
    print('nie')