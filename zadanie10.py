# Check if the input string is a palindrome
a = input()
if a == a[::-1]:
    print("PALINDROM")
else:
    print("NENI PALINDROM")