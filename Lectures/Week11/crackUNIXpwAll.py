#Cracking UNIX Passwords
#import cryptography package
import crypt
import subprocess

def testCommonPasswords(cryptPass):
    # grab the Salt characters (Position 0 and 1)
    salt = cryptPass[0:2]

    # Open dictionary file and iterate through each common passwords
    dictFile = open("commonpasswords.txt",'r')

    #for loop that iterates per line
    for word in dictFile.readlines():

        #strip will remove return characters from string
        word = word.strip('\n')

        #Create hash common password with the combination of SALT
        cryptWord = crypt.crypt(word,salt)

        #Compare the hashed common password with the current hashed password
        if (cryptWord == cryptPass):
            print("  [+] Found Password using Dictionary: "+word+"\n")
            return
    print("  [-] Password Not Found in Dictionary.\n")
    return

def testRainbow(cryptPass):
    #Interesing call on line 33. See anything that you remember?
    output = None
    try:
        output = subprocess.check_output(['/bin/grep', cryptPass, 'rainbow.txt'])
    except:
        output = None

    if(output):
        #Decode it since it is byte format
        passwordArray = output.decode().split(",")
        print("  [+] Successful find in rainbow table!")
        print("  [+] Password:", passwordArray[1])
        return "Success"
    else:
        print("  [-] Password not found in rainbow table!")
        return "Failure"

def main():
    #parse user/password file for hashed password
    passFile = open('password.txt')
    
    for line in passFile.readlines():
        
        #Need a branch to search for a key 
        # word that identifies a line with a password
        if ":" in line:

            #Split the line up to identify the user name and password
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(" ") 

            print("[*] Cracking Password For: "+user)

            # Use our function to see if the user's password matches
            # the rainbow table first, if no match
            # then try the dictionary attack using common passwords
            testRainbow(cryptPass)
            testCommonPasswords(cryptPass)


if __name__ == "__main__":
    main()