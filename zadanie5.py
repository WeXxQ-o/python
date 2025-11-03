#Desifruj text zašifrovaný Cezarovou šifrou s posunom 3
sifra = input()
desifra = ''
for i in sifra:
    if 'a' <= i <='z':
        desifra += chr((ord(i) - 97 - 3) % 26 + 97)
print(desifra)
