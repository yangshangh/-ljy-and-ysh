#  SM3 optimize
本实验由杨尚华独立完成  

在网上了解之后，发现对Python的优化大多数还是需要底层的C语言去做，因此在本项目中，并未从头实现c++语言的SM3。  
而是从网上复制了一个SM3代码去进行优化。  
对程序的软件优化有一下几个思想：  
1、循环展开  
2、多线程  
3、流水线  
4、SIMD语言  
在本次实验中，想去尝试循环展开和多线程并行编程，但是由于SM3需要迭代，因此无法使用多线程并行，只采用了循环展开的方法。 
循环展开在计算机领域中也是一个取折中的思想，如果展开过于多，会导致代码冗长从而使得运行速度过低，展开过于少，不利于提速。  
在本次实验中，对几处的循环进行了展开，在对比时间之后，并没有几倍的提升，只有大约10%左右时间的减少。  

下图为循环展开前程序运行时间:  
![ysh_SM3_not optimized](https://user-images.githubusercontent.com/109864695/182009112-f615fd7b-d0a1-43ce-baa2-4acec5f4835c.png)


下图为循环展开后程序运行时间：

![ysh_SM3_optimize(c++循环展开)](https://user-images.githubusercontent.com/109864695/182009118-f2126a7d-5aba-4437-960a-385a17b9f512.png)

参考链接如下：
>https://blog.csdn.net/nicai_hualuo/article/details/121555000
