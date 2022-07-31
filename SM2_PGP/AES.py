import base64
import binascii
import random 
from gmssl import sm2, func
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

def AES_encrypt(data):
    key=get_random_bytes(16)
    iv=get_random_bytes(16)
    cipher=AES.new(key,AES.MODE_CBC,iv)
    encrypted_data=cipher.encrypt(pad(data,AES.block_size))

    print(encrypted_data)

    
AES_encrypt(b"202000161245")
