#comments here are used after every block of code to explain what the code (above it) does.
from Crypto.Random import get_random_bytes
from Crypto.Protocol. KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
salt = b'R\xf5\xbc\xd3\xb4"9\x1eu\'ENR\xa14\xda\xb5,\xba\x85\xd2\xfd(\xc9$I\xe9\xcb\xff\x89R%'
password = "password123"

key = PBKDF2(password,salt, dkLen = 32)

message = b"This is the message."
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

print(ciphered_data)
#now we have encrypted our data

with open("encrypted.bin","wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
#exporting the encrypted data

with open("encrypted.bin","rb") as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv = iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)

#decrypting the data

with open("key.bin", "wb") as f:
    f.write(key, )

