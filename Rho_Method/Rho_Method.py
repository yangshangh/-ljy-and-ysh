from gmssl import sm3,func
import random
import time

collision_len = 8   #检测hash结果的后collision_len位是否碰撞,且长度为4的倍数

def str_to_list(str):
    ret=[]
    for i in str:
        ret.append(ord(i))

    return ret

def rho_method(len):
    start = time.time()
    initial_data_0 = func.bytes_to_list(bytes(str(random.randint(0, 2**64)), encoding='utf-8'))
    data_0 = sm3.sm3_hash(initial_data_0)
    initial_data_1 = str_to_list(data_0)
    data_1 = sm3.sm3_hash(initial_data_1)
    while(data_0[int(64 - len / 4):] != data_1[int(64 - len /4):]):
        initial_data_1 = str_to_list(data_1)
        data_1 = sm3.sm3_hash(initial_data_1)
    end = time.time()
    print("发现碰撞")
    print("产生碰撞的原象0为：", func.list_to_bytes(initial_data_0))
    print("产生碰撞的原象1为：", func.list_to_bytes(initial_data_1))
    print("原象0的hash结果为：", data_0)
    print("原象1的hash结果为：", data_1)
    print("原象0和原象1的hash结果后%d位相同，用时%s秒" % (len, end - start))


rho_method(collision_len)