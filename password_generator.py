#
#password generator
#
import random
from io import open
file = open("prueba.txt", "a")
def generator_password():

    string_lower = "abcdefghijklmnopqrstuvwxyz"
    string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    size_pass = random.randint(8,16)
    
    new_pass = ""
    aux = size_pass//3
    
    for i in range (0,aux):
        numbers = random.randint(0,9)
        new_pass += str(numbers)
        upper = random.choice(string_upper)
        new_pass += upper
        lower = random.choice(string_lower)
        new_pass += lower
    if (3*aux) == size_pass:
        return new_pass
    else:
        aux1 = size_pass - (3*aux)
        for j in range (0,aux1):
            numbers = random.randint(0,9)
            new_pass += str(numbers)
        return new_pass

def register1():
    file = open("prueba.txt","a")
    file.write(app +" : "+ password +"\n")
    file.close()
    #return

###
register = {}
user_input = "0"

while user_input!="3":
    print ("1. Generator Password")
    print ("2. Get Password")
    print ("3. Exit")
    user_input = input("Your option: ")
    
    if user_input == "1":
        app = input("Name of your application: ")
        password = generator_password()
        register[app] = password
        print("Your password is: " + password)
        register1()
    elif user_input == "2":
        app = input("Name of your application: ")
        if register.get(app,0) == 0:
            print("No password was generated for that app, choose another option")
        else:
            print("Your password is: " + register.get(app))
        
    else:
        ##valor del while infinito = False
        user_input = "3"
        print("End of program")
print("Exit") 