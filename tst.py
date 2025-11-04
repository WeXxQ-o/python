#Zistite počet deliteľov zadaného čísla a usporiadajte ich od najväčšieho po najmenšie oddelené čiarkami a medzerou do podoby.
cislo = int(input())
delitele = []
for i in range(1, cislo + 1):
    if cislo % i == 0:
        delitele.append(i)
delitele.sort(reverse=True)
print(", ".join(map(str, delitele)))