import os

'''
all media extentions except .py and .txt will be encrypted.
encrypted files will have % sign t the end to signify that the
file has been encrypted.
'''
######################################################################
def askpermission():
  print("type in 'Yes' if you want to proceed with encryption")
  permission = input(":")
  if permission.upper() == 'YES':
    return True
  else:
    return False

#######################################################################
def encrypt():
  
  encrypt = {"mp4":"lxv","mkv":"zjb","mov":"wqs","mp3":"asf","jpg":"hdb","png":"nrk","jpeg":"vfd","gif":"fmd"}

  for name in os.listdir():
    if name[-1] == '%':
      print(name+' has already been encrypted!')
      print("".ljust(30,'*'))
      continue
  
    fullname_list = name.split('.')
    extention = fullname_list[-1]

    if extention in encrypt.keys():
      enc_ext = encrypt[extention]
      fullname_list[-1] = enc_ext+'%'
      enc_name = '.'.join(fullname_list)
      os.rename(name,enc_name)
      print(name,"successfully renamed to",enc_name)
      print("".ljust(30,'*'))
    else:
      print(name,": extention not in the dictionary")
      print(" ".ljust(30,'*'))

#######################################################################
if askpermission():
  print("Ma man! Encrypting in process!")
  encrypt()
else:
  print("Permission denied! F*ck Off!")
