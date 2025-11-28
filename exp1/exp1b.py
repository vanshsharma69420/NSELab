# Vigenere Cipher

class VigenereCipher:
    def encrypt(self, message, key):
        cipher_text = []
        key = key.upper()
        key_length = len(key)
        j = 0   # NEW: Proper key index control

        for i, char in enumerate(message):
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                key_char = key[j % key_length]   # UPDATED
                key_shift = ord(key_char) - 65
                encrypted_char = chr((ord(char.upper()) - 65 + key_shift) % 26 + offset)
                j += 1   # NEW: increment only on alphabetic chars
        
                if char.islower():
                    encrypted_char = encrypted_char.lower()
                cipher_text.append(encrypted_char)
            else:
                cipher_text.append(char)
        
        return ''.join(cipher_text)
    
    def decrypt(self, message, key):
        plain_text = []
        key = key.upper()
        key_length = len(key)
        j = 0   # NEW: Proper key index control

        for i, char in enumerate(message):
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                key_char = key[j % key_length]   # UPDATED
                key_shift = ord(key_char) - 65
                decrypted_char = chr((ord(char.upper()) - 65 - key_shift + 26) % 26 + offset)
                j += 1   # NEW
        
                if char.islower():
                    decrypted_char = decrypted_char.lower()
                plain_text.append(decrypted_char)
            else:
                plain_text.append(char)
        
        return ''.join(plain_text)

    def bruteforce_length1(self, message):   # NEW FEATURE 2
        for k in range(26):
            key = chr(65 + k)
            print(f"Key {key}: {self.decrypt(message, key)}")

if __name__ == "__main__":
    vigenere_cipher = VigenereCipher()
    message = str(input("Enter a message: "))
    key = str(input("Enter a key: "))

    cipher_text = vigenere_cipher.encrypt(message, key)
    print("Encrypted Text: " + cipher_text)

    decrypted_text = vigenere_cipher.decrypt(cipher_text, key)
    print("Decrypted Text: " + decrypted_text)

    print("\nBruteforce (Key Length 1):")
    vigenere_cipher.bruteforce_length1(cipher_text)
