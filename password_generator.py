#
#password generator
#
import random

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
    print("The new password is: " + new_pass)
else:
    aux1 = size_pass - (3*aux)
    for j in range (0,aux1):
        numbers = random.randint(0,9)
        new_pass += str(numbers)
    print("The new password is: " + new_pass)