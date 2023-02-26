alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, dir):
    if dir == "encode":
        cipher_text = ""
        for i in text:
            cipher_text += alphabet[(ord(i) - ord('a') + shift) % 26]
        print(f"The encoded text is {cipher_text}")
    elif dir == "decode":
        plain_text = ""
        for i in text:
            new_pos = ord(i) - ord('a') - shift
            while new_pos < 0:
                new_pos += 26
            plain_text += alphabet[new_pos]
        print(f"The decoded text is {plain_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text = text, shift = shift, dir = direction)
