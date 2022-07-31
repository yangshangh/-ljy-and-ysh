
import time
import random
import string
from gmssl import sm3, func

# 部分bit的hash的碰撞
# 二进制位数
bin_length = 8
# 十六进制位数
hex_length = bin_length // 4

#随机生成2的bin_length次方个字符串

def get_random_str(size):
    chars=string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def birthday_attack():
    str_list = get_random_str(pow(2,bin_length))
    # 散列表存取散列值
    hash_list = []
    for i in range(len(str_list)):
        hash_value = sm3.sm3_hash(func.bytes_to_list(bytes(str_list[i], encoding='utf-8')))[0:hex_length]
        #判断是否找到碰撞
        if hash_value in hash_list:
            if str_list[hash_list.index(hash_value)]!=str_list[i]:
                
                print("m1=:", str_list[hash_list.index(hash_value)])
                print("------------------------------------------------")
                print("The hash value of message:",
                      sm3.sm3_hash(func.bytes_to_list(bytes(str_list[hash_list.index(hash_value)], encoding='utf-8'))))
                print("------------------------------------------------")
                print("m2:", str_list[i])
                print("------------------------------------------------")
                print("The hash value of message 2:",
                      sm3.sm3_hash(func.bytes_to_list(bytes(str_list[i], encoding='utf-8'))))
                return True
        hash_list.append(hash_value)

if __name__ == '__main__':
    print("--------------------------------------------")
    print("There are ({}bits) hash value collisions:".format(bin_length))
    print("--------------------------------------------")
    start = time.time()
    #进行循环，一次生成的2^bit_length个字符串可能找不到碰撞
    while 1:
        if birthday_attack():
            break
    end = time.time()
    print("running time:",(end-start),"s")
  
