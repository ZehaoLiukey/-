Sm3-rho method碰撞代码说明及运行结果
=====
1、	原理
----
Rho算法：设置一个函数，不断进行嵌套计算，多次运算后结果会形成一个环，从而形成碰撞<br>
![image](https://github.com/ZehaoLiukey/Liuzehao-experiment/blob/main/sm3-rho/QQ%E5%9B%BE%E7%89%8720220727141832.png)
<br><br>
2、	代码说明
----
def rho(n)为rho算法函数，a为存放多次嵌套计算结果的数组，为加速运行只存储需要碰撞的位数，rho算法函数采用2x+1，in函数判断新生成的结果是否与数组中元素碰撞，若碰撞的话则用index（）函数找出与之碰撞元素的位置，通过初始值加密碰撞元素位置的次数即可得到哈希值。<br><br>
3、	运行截图
---
![image](https://github.com/ZehaoLiukey/Liuzehao-experiment/blob/main/sm3-rho/1.png)
![image](https://github.com/ZehaoLiukey/Liuzehao-experiment/blob/main/sm3-rho/2.png)
<br><br>
4、	结果分析
---
随着需求碰撞位数的增加（大于20bit时），运行时间以及rho所形成的环大小成指数级增加，速度以及碰撞位数相比生日攻击有明显提升，可短时间碰撞28位。
