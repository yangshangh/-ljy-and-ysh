import base64
import binascii
import random 
from gmssl import sm2, func
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

#参考链接：https://github.com/duanhongyi/gmssl
#16进制的公钥和私钥
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt = sm2.CryptSM2(
    public_key=public_key, private_key=private_key)
# 对接java 时验签失败可以使用
#sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=private_key, asn1=True)


def sm2_encrypt(data):
#数据和加密后数据为bytes类型

    enc_data = sm2_crypt.encrypt(data)
    #dec_data =sm2_crypt.decrypt(enc_data)
    #assert dec_data == data
    return enc_data

def sm2_decrypt(enc_data):
    dec_data =sm2_crypt.decrypt(enc_data)
    return dec_data

def sign(data):
#sign and verify
    #data = b"111" # bytes类型
    random_hex_str = func.random_hex(sm2_crypt.para_len)
    sign = sm2_crypt.sign(data, random_hex_str) #  16进制
    assert sm2_crypt.verify(sign, data) #  16进制

#生成SM2公私钥对
def generate_key():
    private_key = int(secrets.token_hex(32), 16)#生成一个十六进制格式的安全随机文本字符串
    public_key = elliptic_mult(private_key, G)
    return private_key, public_key

'''def AES_encrypt(data):
    
    
    K=get_random_bytes(16)
    iv=get_random_bytes(16)
    
    cipher=AES.new(K,AES.MODE_CBC,iv)
    encrypted_data=cipher.encrypt(pad(data,AES.block_size))

    print("encrypted data=",encrypted_data)

    print("random key=",K)


def PKEnc(K):
    jdfkajdjfa=sm2_encrypt(K)
    return jdfkajdjfa'''


    



def AES_encrypt_decrypt(data):
    key=get_random_bytes(16)
    iv=get_random_bytes(16)
    cipher=AES.new(key,AES.MODE_CBC,iv)
    encrypted_data=cipher.encrypt(pad(data,AES.block_size))

    cipher=AES.new(key,AES.MODE_CBC,iv)
    tmp=cipher.decrypt(encrypted_data)
    decrypted_data=unpad(tmp,AES.block_size)
    
    return key,encrypted_data,decrypted_data
    


'''PGP加密部分'''
print("PGP加密部分")
lst=[]
lst=AES_encrypt_decrypt(b"202000161245")
print("-----------------------------------")
print("data=",b"202000161245")
print("-----------------------------------")
print("encrypted_data=",lst[1])

print("-----------------------------------")

print("random key=",lst[0])

print("-----------------------------------")
jdfka=sm2_encrypt(lst[0])

print("jdfkajdjfa=",jdfka)

print("-----------------------------------")


'''PGP解密部分'''
print()
print()
print("PGP解密部分")
print("-----------------------------------")
K=sm2_decrypt(jdfka)#random key

print("random decrypted_key=",K)
print("-----------------------------------")
print("AES_decrypted_data=",lst[2])

print("----------------------------------*")






    






























    
