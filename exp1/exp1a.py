# Caesar Cipher

class CaesarCipher:
    def encrypt(self, message, key):
        result = ""
        key = key % 26   # NEW: supports negative keys

        for char in message:
            if char.isalpha():
                shift = key % 26
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        
        return result
    
    def decrypt(self, message, key):
        result = ""
        key = key % 26   # NEW: supports negative keys

        for char in message:
            if char.isalpha():
                shift = key % 26
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += char
        
        return result

    def bruteforce(self, message):  # NEW FEATURE 2
        for k in range(26):
            print(f"Key {k}: {self.decrypt(message, k)}")

if __name__ == "__main__":
    caesar_cipher = CaesarCipher()
    message = str(input("Enter a message: "))
    key = int(input("Enter a key: "))

    cipher_text = caesar_cipher.encrypt(message, key)
    print("Encrypted Message: ", cipher_text)

    plain_text = caesar_cipher.decrypt(cipher_text, key)
    print("Decrypted Message: ", plain_text)

    print("\nBruteforce Results:")
    caesar_cipher.bruteforce(cipher_text)
