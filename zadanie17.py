naj_zamestnanec = ""
naj_plat = 0

while True:
  vstup = input()
  if vstup == "0":
    break
  meno, plat = vstup.rsplit(",", 1)
  plat = int(plat)
  if plat > naj_plat:
    naj_plat = plat
    naj_zamestnanec = meno
print(naj_zamestnanec)
  