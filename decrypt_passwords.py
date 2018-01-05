""" decrypt unix passwords using the crypt() library & a Dictionary method"""
import crypt

def testPass(cryptedPass):
    salt = cryptedPass[:2]
    with open('dictionary.txt', 'r') as f:
        for word in f.readlines():
            word = word.strip('\n') 
            cryptedWord = crypt.crypt(word, salt)
            if cryptedWord == cryptedPass :
                print "[+] Password Found : ", word, "\n"
                return 
    print "[-] Password Not Found\n"

def main():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():  
            line = line.strip('\n')
            if ':' in line : # in case the line is written this way -> user:password
                s = line.split(':')
                user = s[0]
                cryptedPass = s[1]
                print "[*] Cracking Password For : ", user
                testPass(cryptedPass)
            else :
                print "[*] Cracking Password ", line
                testPass(cryptedPass)


if __name__ == "__main__":
    main()
    