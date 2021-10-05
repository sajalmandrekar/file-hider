import os

def askpermission():
    username = input("Enter Username:")
    passkey = input("Enter key:")
    if username == 'opensimsim' and passkey == '5057':
        return True
    else:
        return False

def decrypt():

    decrypt = {"lxv":"mp4","zjb":"mkv","wqs":"mov","asf":"mp3","hdb":"jpg","nrk":"png","vfd":"jpeg","fmd":"gif"}

    for name in os.listdir():
        if name[-1] == '%':
            fullname_list = name.split('.')
            extention = fullname_list[-1][:-1]

            if extention in decrypt.keys():
                dec_ext = decrypt[extention]
                fullname_list[-1] = dec_ext
                dec_name = '.'.join(fullname_list)
                os.rename(name,dec_name)
                print(name,"successfully renamed to",dec_name)
                print(" ".ljust(30,'*'))
            else:
                print(name,": extention not in the dictionary")
                print(" ".ljust(30,'*'))

        else:
            print(name,"not encrypted")
            print(" ".ljust(30,'*'))


if askpermission():
  decrypt()
else:
  print("permission denied!")