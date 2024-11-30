# random password generator
import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
         'o','p','q','r','s','t',
         'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I',
         'J','K','L','M','N','O','P','Q','R',
         'S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9','10']
symbol=['!','@','$','#','%','*','^']
password=[]
hardpassword=''
print('Welcome to radom no generator')
passwordlength=int(input("Enter the length of your password\n"))
numberlength=int(input("Enter no of number you want in your password\n"))
symbollength=int(input("Enter no of symbol you want in your password\n"))


for i in range(0,numberlength):
    password+=random.choice(numbers)

for i in range(0,symbollength):
    password+=random.choice(symbol)

for i in range(0,passwordlength-(numberlength+symbollength)):
    password+=random.choice(letters)

random.shuffle(password)            
for i in password:
    hardpassword+=i
    
print(f"Your Password: {hardpassword}")    