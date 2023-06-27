# Operating System


一般的汇编语言的书都会简单介绍x86的机制，以及简单的汇编语言。例如，《汇编语言：基于x86处理器》这本书里，你可以重点看第2章x86处理器架构和第3章汇编语言基础，掌握这些基本就可以了。



* Book

  * 《Operating System Concepts》 ——Abraham Silberschatz/Peter B. Galvin/Greg Gagne
  * 《Modern Operating Systems》—— Andrew S. Tanenbaum
  * 《The MINUX book -- Operating Systems Design and Implementation》—— Andrew S. Tanenbaum
* opencourse

  * [MIT 6.828 Operating System Engineering](https://pdos.csail.mit.edu/6.828/2014/schedule.html)
  * [清华大学操作系统课程](https://github.com/chyyuu/os_course_info)

    * [wiki](http://os.cs.tsinghua.edu.cn/oscourse/OS2015)
    * [学堂在线](https://www.xuetangx.com/courses/TsinghuaX/30240243X/2015_T1/about)
    * [在线交流](https://piazza.com/tsinghua.edu.cn/spring2015/30240243x/home)
    * [bilibili video](https://www.bilibili.com/video/av6538245/)
  * 南京大学计算机操作系统

    * [coursera](https://www.coursera.org/learn/jisuanji-caozuo-xitong#reviews)
* website

  * [鸟哥的Linux私房菜](http://linux.vbird.org)
  * [Linux中国](https://linux.cn)
  * [实验楼](https://www.shiyanlou.com):有Linux在线开发环境
  * [Linux下载站](http://www.linuxdown.net)
  * [Linux公社](https://www.linuxidc.com)


整个Linux的学习过程中，要爬的坡有六个，分别是熟练使用Linux命令行、使用Linux进行程序设计、了解Linux内核机制、阅读Linux内核代码、实验定制Linux组件，以及最后落到生产实践上：

- 熟练使用Linux命令行: 如果你想全面学习Linux命令，推荐你阅读《**鸟哥的Linux私房菜**》。如果想再深入一点，推荐你阅读《**Linux系统管理技术手册**》。这本砖头厚的书，可以说是Linux运维手边必备。
- 使用Linux进行程序设计:**通过系统调用或者glibc，学会自己进行程序设计.** 如果要进一步学习Linux程序设计，推荐你阅读**《UNIX环境高级编程》**，这本书有代码，有介绍，有原理，非常实用。
- 了解Linux内核机制,**反复研习重点突破:** 有助于你更好地使用命令行和进行程序设计，能让你的运维和开发水平上升一个层次，但是我不建议你直接看代码，先了解一下Linux内核机制，知道基本的原理和流程就可以了.《**深入理解LINUX内核**》。这本书言简意赅地讲述了主要的内核机制。看完这本书，你会对Linux内核有总体的了解。不过这本书的内核版本有点老，不过对于了解原理来讲，没有任何问题。
- 阅读Linux内核代码: **一开始阅读代码不要纠结一城一池的得失，不要每一行都一定要搞清楚它是干嘛的，而要聚焦于核心逻辑和使用场景.** 这个时候，你就可以有针对性地去做课题，把所学和你现在做的东西结合起来重点突破。例如你是研究虚拟化的，就重点看KVM的部分；如果你是研究网络的，就重点看内核协议栈的部分。推荐一本书，《**LINUX内核源代码情景分析**》。这本书最大的优点是结合场景进行分析，看得见、摸得着，非常直观，唯一的缺点还是内核版本比较老。
- 实验定制Linux组件，
- 落到生产实践上: **面向真实场景的开发，实践没有终点**
- ![bcf70b988e59522de732bc1b01b45a5b](https://static001.geekbang.org/resource/image/bc/5b/bcf70b988e59522de732bc1b01b45a5b.jpeg)