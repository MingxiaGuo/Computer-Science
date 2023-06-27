#  Computer Network

Book
* 《TCP/IP详解》（[TCP/IP illustrated](https://book.douban.com/subject/1741925/)）—— 斯蒂文森（W. Richard Stevens） 🚩强烈推荐🚩
* 《计算机网络：[自顶向下](https://www.baidu.com/s?wd=自顶向下&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)的学习方法》
* 《计算机网络》
* 《UNIX网络编程》

Open Course
* [Stanford Unniversity: CS144 Introduction to Computer Network](https://www.youtube.com/watch?v=-nciJGUPyAM&index=1&list=PLvFG2xYBrYAQCyz4Wx3NPoYJOFjvU7g2Z)
* [bilibili 韩立刚](https://www.bilibili.com/video/av23124815/?p=3)

计算机网络涉及学科：数学、概率论、随机过程、矩阵论、物理学、光学、计算机科学。





张南南

老师您好，我想请教您一个问题，我用一些组件比如java中的HttpClient，发送一个post请求，然后就得到了一个响应，HTTP协议是怎么自动转化成了TCP层，操作系统做了哪些事情，还有就是有很多HTTP请求，他是怎么把HTTP请求和HTTP的响应对应起来的，这两个问题希望您能不吝赐教，谢谢啦~

2018-08-31 08:31

作者回复

底层实现还是socket，就到了tcp层，http的默认行为是一去一回，上一个回了，下一个才能去，所以才有http 2.0
