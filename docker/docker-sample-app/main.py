# 08.02.22
# Mahak Faheem
# Vigenere Cipher
def main():

    plaintext = input("Enter text to be encrypted : ")
    plaintext = plaintext.upper()
    keyword = input("Enter key : ")
    ptLength = len(plaintext)
    
    # generate key
    def generateKey(length, key):
        key = list(key)
        if length == len(key):
            return(key)
        else:
            for i in range(length -len(key)):
                key.append(key[i % len(key)])
            return("" . join(key))
            
    # encryption
    def cipherText(string, key):
        ctext = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i])) % 26
            x += ord('A')
            ctext.append(chr(x))
        return("" . join(ctext))

    # cryptanalysis
    def decrypt(cipher_text, key):
        dtext = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            dtext.append(chr(x))
        return("" . join(dtext))


    key = generateKey(ptLength, keyword)
    print("Key is :", key)
    cipher_text = cipherText(plaintext,key)
    print("Cipher text is :", cipher_text)
    print("Decrypted text is :", decrypt(cipher_text, key))    


    

if __name__ == '__main__':
    main()