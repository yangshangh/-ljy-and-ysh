 #  SM3 birthday attack
 本实验由杨尚华独立完成
 ##  SM3实现
本次实现对于国密算法SM3的实现基于网上算法的学习以及课堂中SM3的学习。  
SM3的步骤大体可分为四步：  
1、消息填充  
2、消息扩展  
3、迭代压缩  
4、输出结果  
过程中也学习到了如何使用gmssl算法去调用SM3，这在实现库中的SM2项目也有所涉及。    
代码运行结果如下图所示：  

![ysh_sm3](https://user-images.githubusercontent.com/109864695/182008069-54b35057-97db-4114-a13d-6115ddbdf274.png)

##  SM3 birthday attack
生日问题也叫做生日悖论，它是这样这样描述的：  
假如随机选择n个人，那么这个n个人中有两个人的生日相同的概率是多少。如果要想概率是100%，那么只需要选择367个人就够了。因为只有366个生日日期（包括2月29日）。  
如果想要概率达到99.9% ，那么只需要70个人就够了。50%的概率只需要23个人。
下图为生日攻击概率分布图
![birthday attack](https://user-images.githubusercontent.com/109864695/182008648-0d755d75-1382-49d8-9d8f-1b990de1320d.png)

依据此问题，我们需要对SM3寻找碰撞。
大致思想为：生成随机字符串与哈希所得字符串对比是否碰撞成功。
本次实验中，貌似是由于生成随机字符串的问题，导致匹配过慢从而无法寻找大bit的碰撞。
代码运行结果如下图所示：
![ysh_SM3_birthday attack](https://user-images.githubusercontent.com/109864695/182008632-eaaae3f7-ba00-4e3e-a207-d587a5663047.png)

参考链接如下：
>https://blog.csdn.net/cscs2123456/article/details/117787537  
>https://blog.csdn.net/weixin_45688634/article/details/123292997
