def encryt(key, plain):
    cipher = ''
    for i in range(len(plain)):
        cipher += chr(ord(key[i % len(key)]) ^ ord(plain[i]))
    
    return cipher
def getPlainText():
    plain = ''
    with open('plain.txt') as f:
        while True:
            line = f.readline()
            if line:
                plain += line
                continue
            break
    return plain

def main():
    key = 'LordCasser'
    plain = getPlainText()
    cipher = encryt(key, plain)
    with open('cipher.txt', 'w') as f:
        f.write(cipher.encode('base_64'))

if __name__ == '__main__':
    main()