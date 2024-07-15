str = input()
changeStr = ""

for i in range(len(str)):
    if (str[i].isupper()):
        changeStr += str[i].lower()
    else:
        changeStr += str[i].upper()
print(changeStr)