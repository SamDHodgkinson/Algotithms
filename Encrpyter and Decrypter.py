# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
    

while True:        
    Input = input("Enter a short sentence:")
    if all(char.isalpha() or char.isspace() for char in Input):
        break
    else:
        print("You must only enter letters(and spaces)!")
    
while True:
    i = int(input("Enter a shift value from 1 to 26:"))
    if i <= 0 or i >= 27:
        print("You must enter an integer between 1 and 26!")
    else:
        break

def encrypt(a,b):
    List = list(a.lower())
    List2 = []
    for letter in List:
        if letter.isspace():
            new = chr(32)
        else:   
            number = ord(letter)
            if number + int(b) >= 123:
                number = number - 26
            elif number + int(b) <= 96:
                number = number + 26
            new = chr(number + int(b))
        List2.insert(len(List2) ,new)
    return "".join(List2)

Output = encrypt(Input, i)
print("Encrpyting this sentence gives us:")
print(Output)
print("Decrypting the scrambled sentence gives us:")
print(encrypt(Output,-i))

