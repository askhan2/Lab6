def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

def main():
    while True:
        print("1. Encode Password")
        print("2. Decode Password")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter an 8-digit password: ")
            if len(password) != 8 or not password.isdigit():
                print("Invalid input. Please enter an 8-digit password containing only integers.")
                continue
            encoded_password = encode(password)
            print(f"Encoded Password: {encoded_password}")
        elif choice == "2":
            encoded_password = input("Enter the encoded password: ")
            if len(encoded_password) != 8 or not encoded_password.isdigit():
                print("Invalid input. Please enter an 8-digit encoded password containing only integers.")
                continue
            decoded_password = decode(encoded_password)
            print(f"Decoded Password: {decoded_password}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()

