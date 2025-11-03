#Zo zadaného textu vypíš všetky slová začínajúce veľkým písmenom
a = input("Zadaj text: ")
slova = a.split()
for slovo in slova:
    if slovo[0].isupper():
        print(slovo, end=' ')  