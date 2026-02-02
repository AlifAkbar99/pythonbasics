import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")


plain_text = input("enter a message to encrypt: ")
chiper_text = ""

#encrypt
for letters in plain_text:
    index = chars.index(letters)
    chiper_text += key[index]
    
print(f"your original message: {plain_text}")
print(f"your encryption {chiper_text}")

# decryption
plain_text = ""

for letter in chiper_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f'your decryption is {plain_text}')