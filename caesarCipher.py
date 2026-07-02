def encrypt(message,shiftNumber):
    letters='abcdefghijklmnopkrstuvwxyzabcdefghijklmnopkrstuvwx'
    letterslist=[]
    for letter in letters:
        letterslist.append(letter)


    messagelist=[]
    for letter in message.lower():
        messagelist.append(letter)
    
    encryptedList=[]
    for letter in messagelist:
        x=letterslist.index(letter)
        x=x+shiftNumber
        encryptedList.append(letterslist[x])
    encryption="".join(encryptedList)
    print(f"Here is your encoded result: {encryption}")

def decrypt(message,shiftNumber):
    letters='zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedc'
    letterslist=[]
    for letter in letters:
        letterslist.append(letter)


    messagelist=[]
    for letter in message.lower():
        messagelist.append(letter)
    
    decryptedList=[]
    for letter in messagelist:
        x=letterslist.index(letter)
        x=x+shiftNumber
        decryptedList.append(letterslist[x])
    decryption="".join(decryptedList)
    print(f"Here is your decoded result: {decryption}")

