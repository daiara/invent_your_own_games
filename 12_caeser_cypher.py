### CAESAR CYPHER

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONOPQRSTUVWXYZ'
max_key_size = len(symbols)

def get_mode():
    while True:
        mode = input("Do you wish to encrypt or decrypt or brute force a message? ").lower()
        if mode in ['encrypt','e','decrypt','d','brute','b']:
            return mode
        else:
            print("You can also type 'e','d' or 'b' instead of 'encrypt', 'decrypt' or 'brute'\nTry again:")

def get_message():
    print("Enter your message:")
    return input()

def get_key():
    key = 0
    while True:
        key = int(input("Enter a key number (1-%s): " %(max_key_size)))
        if (key >=1 and key <= max_key_size):
            return key

def get_translated_message(mode, message, key):
    if mode[0] == 'd':
        key = -key

    translated = ''
    for letter in message:
        letter_index = symbols.find(letter)
        
        if letter_index == -1:
            translated += letter
        else:
            letter_index += key
            
            if letter_index >= len(symbols):
                letter_index -= len(symbols)
                
            elif letter_index < 0:
                letter_index += len(symbols)
                

            translated += symbols[letter_index]
    return translated

mode = get_mode()
message = get_message()
if mode[0] != 'b':
    key = get_key()
print("Your translated message is:")
if mode[0] != 'b':
    print(get_translated_message(mode,message,key))
else:
    for key in range(1, max_key_size +1):
        print(key, get_translated_message('d',message,key))