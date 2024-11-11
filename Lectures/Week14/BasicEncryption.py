#Encryption (Very Basic Example)
#Must install module "progress". Run pip3 install progress from console
# from <something> import <this>
# something is called a package, this is a module
#Example: pip3 install progress
import string
import time
from progress.bar import Bar

def dramaticPause(message):   
    with Bar(message + "....", fill='*', suffix='%(percent).1f%% - %(eta)ds') as bar:
        for i in range(100):
            time.sleep(.03)
            bar.next()
 
def convertLetter(letter,number):   
    letterList = list(string.ascii_lowercase + string.ascii_uppercase + " ")
    currentIndex = letterList.index(letter)

    newIndex = currentIndex + number

    if newIndex > 52:
        newIndex = (currentIndex - 52)
    elif newIndex < 0:
        newIndex = (52 - currentIndex)

    newLetter = letterList[newIndex]

    return newLetter

def encrypt(message,clicks):
    #Small pause for dramatic effect
    dramaticPause("Encrypting")

    encryptedMessage = ""
    for letter in message:
        try:
            encryptedMessage += convertLetter(letter,clicks)
        except:
            encryptedMessage += letter
    print("Encrypted: ",encryptedMessage)
    return encryptedMessage

def decrpyt(message,clicks):
    #Small pause for dramatic effect
    dramaticPause("Decrypting")

    decrpytedMessage = ""
    for letter in message:
        decrpytedMessage += convertLetter(letter,-clicks)

    print("Decrypted: ",decrpytedMessage)
    return decrpytedMessage


def main():
    #message = input("What is the secret message? ")
    #clicks = input("Number of clicks? ")
    #encryptedMessage = encrypt(message,int(clicks))
    #decrpyt(encryptedMessage, int(clicks))
    print("")


if __name__ == "__main__":
    main()
