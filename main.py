'''

this is Vinh Vu's main.py

'''

def encode(password):
    return ''.join(str((int(char) + 3) % 10) for char in password)

def decode(encoded_password):
    return ''.join(str((int(char) - 3) % 10) for char in encoded_password)

def main():
    menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n"
    encoded_password = None

    def encode_password():
        nonlocal encoded_password
        password_to_encode = input("Enter password to encode: ")
        encoded_password = encode(password_to_encode)
        print("Your password has been encoded and stored!\n")

    def decode_password():
        if encoded_password:
            original_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}\n")
        else:
            print("No encoded password stored.\n")

    options = {
        '1': encode_password,
        '2': decode_password,
        '3': exit
    }

    while True:
        print(menu)
        option = input("Enter an option: ")
        action = options.get(option)
        if action:
            if option == '3':
                break
            action()
        else:
            print("Invalid option, please try again.\n")

if __name__ == '__main__':
    main()
