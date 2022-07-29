Sm2-RFC6979实现代码说明及运行结果
=======
1、原理
-------

SM2是非对称加密算法，它是基于椭圆曲线密码的公钥密码算法标准，其密钥长度256bit，SM2采用的是ECC 256位的一种，其安全强度比RSA 2048位高，且运算速度快于RSA。
<br>
![image](https://github.com/ZehaoLiukey/Liuzehao-experiment/blob/main/sm2-rfc6979/4.png)<br>

2、代码说明
----------
Crypto.Signature.DSS：用来实现数字签名,为遵循RFC6979，使用’deterministic-rfc6979’<br>
3、运行截图
------
![image](https://github.com/ZehaoLiukey/Liuzehao-experiment/blob/main/sm2-rfc6979/3.png)<br>


