passwd = ''

while(True):
    
    passwd = input()

    if passwd == 'END': break

    print(''.join(reversed(passwd)))