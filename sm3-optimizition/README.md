sm3优化代码说明及运行结果
=======
1、	原理
-----
循环展开顾名思义就是将循环体展开，全部展开或者展开一部分都可以有效提高性能。循环展开无论是在 CPU 还是 GPU 上，都可以有效的提高应用程序运行速度。本实验主要优化sm3的消息扩展函数，将循环展开。<br><br>

-------
2、	代码说明
------
将string extension(string str)消息扩展函数里面的两个循环进行扩展<br><br>
3、代码截图
------
![image](https://github.com/ZehaoLiukey/Liuzehao-experiment/blob/main/sm3-optimizition/1.png) <br>

![image](https://github.com/ZehaoLiukey/Liuzehao-experiment/blob/main/sm3-optimizition/2.png) <br>
4、结果总结
------
经过循环展开优化之后，运行速度快了0.35s，效果明显

