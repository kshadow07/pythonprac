# TO encode and decode given password using Caesar Cipher



leave=False

def encode_decode(type:str,password,encrption_length:int):
    global leave
    encrypted_password=""
    if type=="e":
        for i in password:
            encrypted_password+=chr(ord(i)+encrption_length)
        print(f"Your encrypted password is:{encrypted_password}")
        play=input("Do you want to use the tool again yes or no: ").lower()
        if play=="yes":
            leave=False
            
        elif play=="no":
            leave=True
            print("Thanks for playing")
    elif type=="d":
         for i in password:
            encrypted_password+=chr(ord(i)-encrption_length)
         print(f"Your encrypted password is:{encrypted_password}")    
         play=input("Do you want to use the tool again yes or no: ").lower()
         if play=="yes":
            leave=False
         elif play=="no":
            leave=True 
            print("Thanks for playing")  
    else:
        print("You have chosen the wrong keyword Try again")
        play=input("Do you want to use the tool again yes or no: ").lower()
        if play=="yes":
            leave=False
        elif play=="no":
            leave=True 
            print("Thanks for playing")             
    
    
while not leave:
    choice=input("Welcome to encryption app i you want to encode type e or d for decode type:\n")
    password=input("Enter your password:\n")
    encrption_length=int(input("Write the no of places you want to skip:\n"))
    encode_decode(type=choice,password=password,encrption_length=encrption_length)
    
       
               



        
