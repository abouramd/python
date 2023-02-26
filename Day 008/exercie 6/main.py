alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, dir):
    if dir != "encode" and dir != "decode":
        return
    end_text = ""
    for i in text:
        if i.islower() is True:
            new_pos = ord(i) - ord('a')
            if dir == "encode":
                new_pos = (new_pos + shift) % 26
            elif dir == "decode":
                new_pos = new_pos - shift
                while new_pos < 0:
                    new_pos += 26
            end_text += alphabet[new_pos]
        else:
            end_text += i
    print(f"The {dir}d text is {end_text}")
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

restart = True
while restart is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    caesar(text=text, shift=shift, dir=direction)
    print("do you want to restart the cipher program?")
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    restart = False
    if answer == "yes":
        restart = True
        