alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
        #e.g.
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        #print_output: "The encoded text is mjppt"

        #? Algorithm
        #? For every character in the text, I would like to get it's index number then add it to the shift in and then print the letter represented by the sum of the two values add them together and get the encrypted text.
# My solution
# def encrypt(plain_text, shift_amount):
#     single_char_index =[]
#     for char in text:
#         char_index = alphabet.index(char)
#         shift_index = shift + char_index
#         single_char_index.append(shift_index)
#     #print(single_char_index)

#     encrypted_text = ""
#     for index in single_char_index:
#         encrypted_letter = alphabet[index]
#         #print(encrypted_letter)
#         encrypted_text += encrypted_letter
#     #print(encrypted_text)

#     print(f"The encoded text is {encrypted_text}")

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if (direction == "encode"):
    encrypt(plain_text=text, shift_amount=shift)
elif (direction == "decode"): 
    print("decode")
else:
    print("Please follow the instruction provided.")
