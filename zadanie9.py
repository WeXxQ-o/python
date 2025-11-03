#Spočítaj súčet všetkých čísel v reťazci (napr. "abc12x3" → 15)

a = input("Zadaj reťazec: ")
a += " " 
sucet = 0
aktualne_cislo = ""

for i in a:
    if i.isdigit():
        aktualne_cislo += i
    elif aktualne_cislo:
        sucet += int(aktualne_cislo)
        aktualne_cislo = ""

print("Súčet všetkých čísel v reťazci je:", sucet)