本实验由杨尚华独立完成
# PGP加密实现  
1、生成随机密钥K（此处用的是AES生成）  
2、用SM2算法以及SM2的公钥pk加密随机密钥K  
3、用对称密码AES以及随机密钥K加密消息M

#  PGP解密实现
1、用SM2算法以及私钥SK解密出随机密钥K  
2、用AES算法以及随机密钥K解密出消息M  

注：本次程序中所使用的公私钥是固定的，随机密钥是由AES中生成的
程序运行结果如下图所示：

![ysh_PGP encrypt_decrypt](https://user-images.githubusercontent.com/109864695/182010554-4656ae2a-39d9-484d-b65c-f2239b522790.png)

参考链接：
>https://github.com/duanhongyi/gmssl
