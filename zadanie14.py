vstup = input().split()
mini = vstup[0]
maxi = ''
temp = 0
poc = 0
for i in vstup:
    temp += len(i)
    if len(mini) > len(i):
        mini = i
    if len(maxi) < len(i):
        maxi = i
print(f'Najkratsie slovo je {mini} {len(mini)} znakov.')
print(f'Najdlhzie slovo je {maxi} {len(maxi)} znakov.')
print(f'priemerna dlzka slov je {round(temp/len(vstup), 2)} znakov.')
    