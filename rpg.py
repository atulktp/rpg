#imports
import os
import random as rnd
#import pyperclip

#os clear screen
os.system("cls")

atulktp = '''
\u001b[1m
          _             _   _      _           
         | |           | | | |    | |          
   __ _  | |_   _   _  | | | | __ | |_   _ __  
  / _` | | __| | | | | | | | |/ / | __| | '_ \ 
 | (_| | | |_  | |_| | | | |   <  | |_  | |_) |
  \__,_|  \__|  \__,_| |_| |_|\_\  \__| | .__/ 
                                        | |    
                                        |_|    
\u001b[0m
\u001b[31mInstagram:- atulktp \u001b[0m
\u001b[31mGithub:- atulktp \u001b[0m


'''

print(atulktp)


#password patterns
lString="abcdefghijklmnopqrstuvwxyz"
uString="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER="0123456789"
Symbol="[]{}()#*$@"

#password combination
Latter=lString+uString
LatterNumbers=lString + uString + NUMBER
all=lString + uString + NUMBER + Symbol

#password length
pswdLength = int(input('''
\u001b[42m Please!, Choose Your Password Length. :-  
\u001b[40m'''))

#choose password pattern
pswdPattern=int(input('''
\u001b[42m Please!, Choose Your Password Pattern \u001b[40m

1 Uppercase + Lowercase Latters
2 Uppercase + Lowercase + Numbers
3 Uppercase + Lowercase + Numbers + Symbols
'''))

#generate password by choice
if pswdPattern==1:
	password = "".join(rnd.sample(Latter,pswdLength))
	print("\u001b[42m The Password Your Generated is:- \u001b[40m",password)
	#pyperclip.copy(password)
	#print("Also Copied in Your Clipboard.")
elif pswdPattern==2:
	password = "".join(rnd.sample(LatterNumbers,pswdLength))
	print("\u001b[42m The Password Your Generated is:- \u001b[40m",password)
	#pyperclip.copy(password)
	#print("Also Copied in Your Clipboard.")
elif pswdPattern==3:
	password = "".join(rnd.sample(all,pswdLength))
	print("\u001b[42m The Password Your Generated is:- \u001b[40m",password)
	#pyperclip.copy(password)
	#print("Also Copied in Your Clipboard.")
else:
	print("\u001b[41m Please!, Provide Correct Input \u001b[40m")
