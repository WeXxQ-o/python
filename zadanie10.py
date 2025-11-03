#Pozri či je zadané slovo palindróm
a = input()
if a == a[::-1]:
    print("PALINDROM")
else:
    print("NENI PALINDROM")