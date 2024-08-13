# add your code here
def cipher(text,s):
    crypt = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            crypt += chr((ord(char) + s-65) % 26 + 65)

        else:
            crypt += chr((ord(char) + s - 97) % 26 + 97)

    return crypt
text = "welcome to code"
print ("Text  : " + text)
print ("Cipher: " + cipher(text,5))




