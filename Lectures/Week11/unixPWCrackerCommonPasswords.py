#Cracking UNIX Passwords
#import cryptography package
import crypt
import subprocess

def testCommonPasswords(cryptPass):
    # grab the Salt characters (Position 0 and 1)
    salt = cryptPass[0:2]

    # Open commonpasswords.txt file and iterate through each common passwords
    dictFile = open("commonpasswords.txt")

    #for loop that iterates per line
    for word in dictFile.readlines():
        
        #strip will remove return characters from string
        word = word.strip('/n')
        
        #Create hash common password with the combination of SALT
        cryptWord = crypt.crypt(word,salt)
        print(cryptWord)
        #Compare the hashed common password with the current hashed password
        if (cryptPass == cryptWord):
            print("   [+] Found Password using Dictionary: "+word+"\n")
            return word
    print("   [-] Password Not found in Dictionary.\n")
    return


def main():
    #parse user/password file for hashed password
    passFile = open("password.txt")

    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip()

            print("[*] Cracking Password for: "+user)

            testCommonPasswords(cryptPass)

if __name__ == "__main__":
    main()