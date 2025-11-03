slovo = input()
podretazec = input()
temp = 0
temp1 = 0
for i in range(len(slovo)):

    if podretazec[0] == slovo[i]:
        if podretazec[1] == slovo[i + 1]:
            temp += 1

    if podretazec[-1] == slovo[-(i + 1)]:
        if podretazec[-2] == slovo[-(i + 2)]:
            temp1 += 1

print(temp)
print(temp1)
