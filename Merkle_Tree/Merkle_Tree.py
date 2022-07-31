from gmssl import sm3,func

class Node(object):
    def __init__(self, hash, position, isLeaf):
        self.isLeaf = isLeaf
        self.hash = hash
        if isLeaf == True:
            self.left = -1
            self.right = -1
        else:
            self.left = position * 2 + 1
            self.right = position * 2 + 2
        if position != 0:
            self.parent = int((position - 1) / 2)
        else:
            self.parent = -1

class Merkel_Tree(object):
    NodeList = []
    num = 0
    def __init__(self):
        lfnum = int(input("输入原始数据片段数:"))
        self.num = 2 * lfnum - 1
        self.NodeList = [0 for i in range(self.num)]
        for i in range(lfnum):
            data = input("输入第%d个数据：" %i)
            hash = sm3.sm3_hash(func.bytes_to_list(bytes(data, encoding='utf-8')))
            self.NodeList[lfnum + i - 1] = Node(hash, lfnum + i - 1, True)
        for i in range(lfnum - 2, -1, -1):
            data = self.NodeList[2 * i + 1].hash + self.NodeList[2 * i + 2].hash
            hash = sm3.sm3_hash(func.bytes_to_list(bytes(data, encoding='utf-8')))
            self.NodeList[i] = Node(hash, i, False)

MT = Merkel_Tree()
for i in MT.NodeList:
    if i.isLeaf == True:
        print("该节点为叶子节点，只储存了对应数据的hash值，hash为：" + i.hash)
    else:
        print("该节点不是叶子节点，该节点储存的hash值为：" + i.hash + "，可得到其对应原象为：\n" + MT.NodeList[i.left].hash + MT.NodeList[i.right].hash)










