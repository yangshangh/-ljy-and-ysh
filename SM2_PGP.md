#  PGP加密实现
1、随机生成密钥K（此处采用AES密钥生成）  
2、用SM2生成的公钥pk去加密随机生成密钥K  
3、用对称密码AES以及随机生成密钥加密消息M

#  PGP解密实现  
1、用SM2的私钥sk解密出随机生成密钥K  
2、用对称密码AES以及密钥K解密消息M  

代码运行结果如下图所示：

![ysh_PGP encrypt_decrypt](https://user-images.githubusercontent.com/109864695/182010284-4c94ecad-184a-4527-8826-3799e707a05c.png)

参考链接：
>
