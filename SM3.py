import math
import time
import re

#初始变量
IV = [0x7380166F, 0x4914B2B9, 0x172442D7, 0xDA8A0600, 0xA96F30BC, 0x163138AA, 0xE38DEE4D, 0xB0FB0E4E]
T = [0x79cc4519, 0x7a879d8a]

#循环移位
def ROL(X,i):
    i=i%32
    return ((X<<i)&0xFFFFFFFF)|((X&0xFFFFFFFF)>>(32-i))

#置换函数
def Replace_P0(X):
    X_9=ROL(X,9)
    X_17=ROL(X,17)
    X=X^X_9^X_17
    return X

def Replace_P1(X):
    X_15=ROL(X,15)
    X_23=ROL(X,23)
    X=X^X_15^X_23
    return X

#布尔函数
def FF(X,Y,Z,j):
    if j>=0 and j<=15:
        return X^Y^Z
    else:
        return ((X&Y)|(X&Z)|(Y&Z))

def GG(X,Y,Z,j):
    if j>=0 and j<=15:
        return X^Y^Z
    else:
        return ((X&Y)|(~X&Z))

#常量Tj
def T_(j):
    if j>=0 and j<=15:
        return T[0]
    else:
        return T[1]

#消息填充
def Fill(message):
    m = bin(int(message,16))[2:]
    if len(m) != len(message)*4:
        m = '0'*(len(message)*4-len(m)) + m
    l = len(m)
    l_bin = '0'*(64-len(bin(l)[2:])) + bin(l)[2:]
    m = m + '1'
    m = m + '0'*(448-len(m)%512) + l_bin
    m = hex(int(m,2))[2:]
    print("填充后的消息为:",m)
    return m


#分组
def fenzu(m):
    m=Fill(m)#消息填充
    len_m=len(m)/128#分组的个数
    m_list=[]
    for i in range(int(len_m)):#进行分组
        a = m[0 + 128 * i:+128 * (i + 1)]
        m_list.append(a)
    return m_list

#消息扩展
def expand(M,n):
    W = []
    W_ = []
    for j in range(16):
        W.append(int(M[n][0+8*j:8+8*j],16))
    for j in range(16,68):
        W.append(Replace_P1(W[j-16]^W[j-9]^ROL(W[j-3],15))^ROL(W[j-13],7)^W[j-6])
    for j in range(64):
        W_.append(W[j]^W[j+4])
    Wstr = ''
    W_str = ''
    for x in W:
        Wstr += (hex(x)[2:] + ' ')
    for x in W_:
        W_str+= (hex(x)[2:] + ' ')
    print("第{}个消息分组 扩展后消息：".format(n+1))
    print("W:",Wstr)
    print("W':",W_str)
    return W,W_

#压缩函数
def CF(V,M,i):
    A,B,C,D,E,F,G,H = V[i]
    W,W_ = expand(M,i)
    for j in range(64):
        SS1= ROL((ROL(A,12)+E+ROL(T_(j),j%32))%(2**32),7)
        SS2=SS1^ROL(A,12)
        TT1=(FF(A,B,C,j)+D+SS2+W_[j])%(2**32)
        TT2=(GG(E,F,G,j)+H+SS1+W[j])%(2**32)
        D=C
        C=ROL(B, 9)
        B=A
        A=TT1
        H=G
        G=ROL(F, 19)
        F=E
        E=Replace_P0(TT2)
        print("j={}:".format(j))
        print(hex(A), hex(B),hex(C),hex(D),hex(E),hex(F),hex(G),hex(H))
    a,b,c,d,e,f,g,h=V[i]
    V_= [a^A, b^B, c^C, d^D, e^E, f^F, g^G, h^H]
    return V_

#迭代函数
def Iterate(M):
    n=len(M)
    V=[]
    V.append(IV)
    for i in range(n):
        V.append(CF(V,M,i))
    return V[n]



if __name__ == '__main__':
    message = '61626364616263646162636461626364616263646162636461626364616263646162636461626364616263646162636461626364616263646162636461626364'
    start=time.time()
    #message=input('请输入需要加密的值:')
    m = Fill(message)
    M = fenzu(m)
    Vn=Iterate(M)
    result = ''
    for x in Vn:
        result += (hex(x)[2:]+' ')
    print("杂凑值:",result)
    end=time.time()
    print("运行时间为:",(end-start),"s")






