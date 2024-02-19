def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            start = ord('A') if char.isupper() else ord('a')
            modifier = 1 if encrypt else -1
            result += chr((ord(char) - start + modifier * shift) % 26 + start)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

def main():
    while True:
        print("Caesar Cipher Program:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift_value = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift_value, encrypt=True)
            print("Encrypted Message:", encrypted_message)

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift_value = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift_value, encrypt=False)
            print("Decrypted Message:", decrypted_message)

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
