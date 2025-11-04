#Pre zadané slovo uvedené v prvom riadku vypíšte znaky, ktoré sa nachádzajú na troch pozíciách zadaných v ďalších riadkoch. Ak je nejaká pozícia väčšia ako počet znakov v slove, vypíšte text "mimo rozsah".
slovo = input()
poz1 = int(input())
poz2 = int(input())
poz3 = int(input())
if poz1 < len(slovo):
    print(slovo[poz1])
else:
    print("mimo rozsah")
if poz2 < len(slovo):
    print(slovo[poz2])
else:
    print("mimo rozsah")
if poz3 < len(slovo):
    print(slovo[poz3])
else:
    print("mimo rozsah")