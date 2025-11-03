a = input().split()
temp = ''
poc = 0
for i in range(len(a)):
    if len(a[i]) % 2 == 1:
        temp += a[i] + '='
        poc += 1
print(temp[0:len(temp) -1] + '.')
print(poc)
