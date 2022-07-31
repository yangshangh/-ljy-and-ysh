import secrets
import base64
import binascii
import random
from hashlib import sha256
from gmssl import sm2, func
from gmssl import sm3, func
#基础参数
A = 0
B = 7
Q = 115792089237316195423570985008687907853269984665640564039457584007908834671663
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
G_X = 55066263022277343669578718895168534326250603453777594175500187360389116729240
G_Y = 32670510020758816978083085130507043184471273380659243275938904335757337482424
G = (G_X, G_Y)


def gcd(a,b): #求最大公因子
    while a!=0:
        a,b=b%a,a
    return b

def xgcd(a,m): #扩展欧几里得算法求模逆
    if gcd(a,m)!=1:
        return None
    u1,u2,u3=1,0,a
    v1,v2,v3=0,1,m
    while v3!=0:
        q=u3//v3
        v1,v2,v3,u1,u2,u3=(u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m



'''二次剩余的代码参照链接：
https://blog.csdn.net/qq_51999772/article/details/122642868'''
def Legendre(n,p): # 这里用勒让德符号来表示判断二次（非）剩余的过程
    return pow(n,(p - 1) // 2,p)

def Tonelli_Shanks(n,p):
    assert Legendre(n,p) == 1
    if p % 4 == 3:
        return pow(n,(p + 1) // 4,p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        q = q // 2
        s += 1
    for z in range(2,p):
        if Legendre(z,p) == p - 1:
            c = pow(z,q,p)
            break
    r = pow(n,(q + 1) // 2,p)
    t = pow(n,q,p)
    m = s
    if t % p == 1:
        return r
    else:
        i = 0
        while t % p != 1: # 外层循环的判断条件
            temp = pow(t,2**(i+1),p) # 这里写作i+1是为了确保之后内层循环用到i值是与这里的i+1的值是相等的
            i += 1
            if temp % p == 1: # 内层循环的判断条件
                b = pow(c,2**(m - i - 1),p)
                r = r * b % p
                c = b * b % p
                t = t * c % p
                m = i
                i = 0 # 注意每次内层循环结束后i值要更新为0
        return r

#EC加法运算
def elliptic_add(p, q):
    if p == 0 and q == 0:
        return 0
    elif p == 0:
        return q
    elif q == 0:
        return p
    else:
        if p[0] > q[0]:#交换p、q
            temp = p
            p = q
            q = temp
        r = []
        rel= (q[1] - p[1])*xgcd(q[0] - p[0], Q) % Q

        r.append((rel*rel - p[0] - q[0]) % Q)
        r.append((rel*(p[0] - r[0]) - p[1]) % Q)

        return (r[0], r[1])

#2P
def elliptic_double(p):
    r = []

    rel = (3*p[0]**2 + A)*xgcd(2*p[1], Q) % Q

    r.append((rel*rel - 2*p[0])%Q)
    r.append((rel*(p[0] - r[0]) - p[1])%Q)

    return (r[0], r[1])

#EC乘法运算
def elliptic_mult(s, p):
    n = p
    r = 0 #无穷远点

    s_binary = bin(s)[2:]
    s_length = len(s_binary)

    for i in reversed(range(s_length)):
        if s_binary[i] == '1':
            r = elliptic_add(r, n)
        n = elliptic_double(n)

    return r

def get_length_bin(x):
    if isinstance(x, int):
        num = 0
        tmp = x >> 64
        while tmp:
            num += 64
            tmp >>= 64
        tmp = x >> num >> 8
        while tmp:
            num += 8
            tmp >>= 8
        x >>= num
        while x:
            num += 1
            x >>= 1
        return num
    elif isinstance(x, str):
        return len(x.encode()) << 3
    elif isinstance(x, bytes):
        return len(x) << 3
    return 0

def pre_compute(ID, a, b, G_X, G_Y, x_A, y_A):#ID，椭圆曲线参数a、b,G点x、y,公钥x、y
    a = str(a)
    b = str(b)
    G_X = str(G_X)
    G_Y = str(G_Y)
    x_A = str(x_A)
    y_A = str(y_A)
    ENTL = str(get_length_bin(ID))

    t = ENTL + ID + a + b + G_X + G_Y + x_A + y_A
    t_b = bytes(t, encoding='utf-8')#转为字节串
    digest = sm3.sm3_hash(func.bytes_to_list(t_b))
    return int(digest, 16)

#生成公私钥对
def generate_key():
    private_key = int(secrets.token_hex(32), 16)#生成一个十六进制格式的安全随机文本字符串
    public_key = elliptic_mult(private_key, G)
    return private_key, public_key

#签名
def sign(private_key,message,Z_A):
    M=Z_A+message
    M_b=bytes(M,encoding='utf-8')
    e=sm3.sm3_hash(func.bytes_to_list(M_b))
    e=int(e,16)#转化为十进制
    k=secrets.randbelow(Q)
    random_point=elliptic_mult(k,G)
    r = (e + random_point[0]) % N
    s = (xgcd(1 + private_key, N) * (k - r * private_key)) % N
    return (r, s)

#验证函数
def verify(pk,ID,message,sig):
    r=sig[0]
    s=sig[1]
    Z=pre_compute(ID,A,B,G_X,G_Y,pk[0],pk[1])
    M=str(Z)+message
    M_b = bytes(M, encoding='utf-8')
    e = sm3.sm3_hash(func.bytes_to_list(M_b))
    e = int(e, 16)
    t = (r + s) % N

    point = elliptic_mult(s, G)
    point_1 = elliptic_mult(t, pk)
    point = elliptic_add(point, point_1)

    x1 = point[0]
    x2 = point[1]
    R = (e + x1) % N

    return R == r

'''private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=private_key)
def sm2_encrypt_decrypt(data):
#数据和加密后数据为bytes类型
    #进行加解密操作
    enc_data = sm2_crypt.encrypt(data)
    dec_data =sm2_crypt.decrypt(enc_data)
    assert dec_data==data
    return enc_data,dec_data'''



if __name__=='__main__':
    message="202000161245"
    
    sk,pk=generate_key()
    print("message=",message)
    print('----------------------------------------')
    print("public key:",pk)
    
    ID='1234567812345678'#sm2使用固定值
    
    Z_A = pre_compute(ID, A, B, G_X, G_Y, pk[0], pk[1])
    signature = sign(sk, message, str(Z_A))
    print('----------------------------------------')
    print("signature: ", signature)
    
    #此处signature中的r、s是数字方便verify
    if verify(pk, ID, message, signature) == 1:
        print('----------------------------------------')
        print('验证签名:True')

















    

