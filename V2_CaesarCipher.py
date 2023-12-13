#Code Kentucky Cipher Exercise
def cc_method(user_text: str,shift: int):
    encrypted_text = ""
    #Define alphabet characters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    special_chrs = ' .!?'
    for letter in user_text:
        if special_chrs.find(letter) != -1:
            encrypted_text += letter
        elif letter.isalpha():
            #Handle for errors: spaces, upper and lowercase
            letter_index = alphabet.index(letter.lower().strip())
            if (letter_index + shift) > 25:
                shift_index = shift - (26 - letter_index)
            else:
                #Shift Five
                shift_index = letter_index + shift
            encrypted_text += alphabet[shift_index]
            #            print(f'letter_index:{letter_index} shift_index:{shift_index} shift_value:{shift_value}')
    return encrypted_text

if __name__ == '__main__':
    user_input = input("Please enter a sentence: ")
    encrypted_text = cc_method(user_text=user_input,shift=5)
    print(f'The encrypted sentence is: {encrypted_text}')