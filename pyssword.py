#!/usr/bin/python
import random
#import string
import os
# Define Avalible chars in password
alpha_printable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']
passwd = [] # declares password as list
delimiter = '' # Changes the character between characters in password

def genpasswd():
    for i in range(int(passwd_len)):
        passwd.append(random.choice(alpha_printable))
        i = i + 1
    return 0

def save_passwd():
    fname = input("File name & path (/home/bill/pw) => ")
    if os.path.exists(fname) == True:
        print("File already exist.")
        print("Not saving!")
    else:
        f = open(fname, "x")
        f.close()
        f = open(fname, "a")       
        f.write("%s" % str(delimiter.join(passwd)))
        i = False

print("Pyssword, enter length of password")
passwd_len = input("=> ")
if passwd_len.isdigit() == True:
    genpasswd()
    print(delimiter.join(passwd))
    saveq = input("Would you like to save password? (y/N) => ")
    if saveq == "y":
        save_passwd()
    else:
        exit()
else:
    print("Please enter number.")