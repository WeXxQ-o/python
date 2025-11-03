#Nájdi najdlhšie a najkratšie slovo zo zadaných slov oddelených medzerou, vypíš ich dĺžky a priemernú dĺžku slov
a = input().split()
maxi = ''
mini = a[0]
temp = 0
for i in a:
    temp += len(i)
    if len(maxi) < len(i):
        maxi = i
    if len(mini) > len(i):
        mini = i
print(f'Najdlhzie slovo je {maxi} {len(maxi)} znakov.')
print(f'Najkratsie slovo je {mini} {len(mini)} znakov.')
print(f'priemerna dlzka slov je {round(temp/len(a), 2)} znakov.')