# SM2实现
本实验由杨尚华个人独立完成
##SM2加解密部分
下图为SM2加解密实现流程：

![image](https://user-images.githubusercontent.com/109864695/182009767-8a187bac-51b1-424c-adf1-3794661582d7.png)

其中最困难的部分就是椭圆曲线上面的操作。经过查询资料后进行一步步实现即可。公私钥生成可以用gmssl库来直接生成。

SM2加解密运行结果如下图所示：

![ysh_SM2_encrypt_decrypt](https://user-images.githubusercontent.com/109864695/182009909-fc68148d-49f4-4e70-96bd-48cfd61442a9.png)

##  SM2签名验证部分
下图为SM2签名验证的运行结果：

![ysh_SM2_sign_verify](https://user-images.githubusercontent.com/109864695/182009908-e11577fa-91ff-464e-baa9-77294936147b.png)

在开源的gmssl库中，并未有密钥协商的操作，这一点日后需要补充。调库使用SM2在后续的PGP加密中也有所使用。

参考链接：
>https://blog.csdn.net/qq_43339242/article/details/123221091?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165924080716782184694709%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165924080716782184694709&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-3-123221091-null-null.142^v35^new_blog_fixed_pos&utm_term=SM2%E7%94%A8Python%E5%AE%9E%E7%8E%B0&spm=1018.2226.3001.

>https://blog.csdn.net/qq_33439662/article/details/122590298?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165924080716782184694709%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165924080716782184694709&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-122590298-null-null.142^v35^new_blog_fixed_pos&utm_term=SM2%E7%94%A8Python%E5%AE%9E%E7%8E%B0&spm=1018.2226.3001.4187
>
>https://blog.csdn.net/boksic/article/details/7013480?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165924140516782246414316%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165924140516782246414316&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-7013480-null-null.142^v35^new_blog_fixed_pos&utm_term=%E6%A4%AD%E5%9C%86%E6%9B%B2%E7%BA%BF&spm=1018.2226.3001.4187
>
>https://sca.gov.cn/sca/xwdt/2010-12/17/1002386/files/b791a9f908bb4803875ab6aeeb7b4e03.pdf
