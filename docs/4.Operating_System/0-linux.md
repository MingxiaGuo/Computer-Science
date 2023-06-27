# Linux



除此之外，极客时间出品的《数据结构与算法之美》《深入浅出计算机组成原理》也是非常优秀的学习资料。

**“先读薄，再读厚，再读薄”这样的三遍学习法**。

---

## Overview

操作系统：将硬件资源分配（CPU，内存，硬盘，网络）给不同用户程序使用，并在适当的时间将资源拿回来，再分配给其他用户进程。

操作系统在计算机中承担着“大管家”的角色。它合理分配计算机硬件和软件资源给不同的用户程序使用，并且在适当的时间将这些资源拿回来，再分配给其他的用户进程。并处理多种基本事务，比如管理与配置内存、决定系统资源供需的优先次序、控制输入与输出设备、操作网络与管理文件系统等，还提供一个让用户与系统交互的操作界面。硬件资源包括：CPU，内存，硬盘，网络。操作系统就是协调各种资源，帮助我们成事的



假设，我们现在就是在做一家外包公司，我们的目标是把这家公司做上市。其中，操作系统就是这家外包公司的老板。我们把这家公司的发展阶段分为这样几个时期：

- **初创期**：这个老板基于开放的营商环境（x86体系结构），创办一家外包公司（系统的启动）。因为一开始没有其他员工，老板需要亲自接项目（实模式）。
- **发展期**：公司慢慢做大，项目越接越多（保护模式、多进程），为了管理各个外包项目，建立了项目管理体系（进程管理）、会议室管理体系（内存管理）、文档资料管理系统（文件系统）、售前售后体系（输入输出设备管理）。
- **壮大期**：公司越来越牛，开始促进内部项目的合作（进程间通信）和外部公司合作（网络通信）。
- **集团化**：公司的业务越来越多，会成立多家子公司（虚拟化），或者鼓励内部创业（容器化），这个时候公司就变成了集团。大管家的调度能力不再局限于一家公司，而是集团公司（Linux集群），从而成功上市（从单机操作系统到数据中心操作系统）。

![](https://static001.geekbang.org/resource/image/7d/a5/7d7b2f705d4877bb331b4ea3ff3450a5.jpg)

![80a4502300dfa51c8520001c013cee5d](https://static001.geekbang.org/resource/image/80/5d/80a4502300dfa51c8520001c013cee5d.jpeg)

除此之外，极客时间出品的《数据结构与算法之美》《深入浅出计算机组成原理》也是非常优秀的学习资料。所有基础知识，本是一家。如果有精力，推荐你认真学习这两个专栏，对我们这门课会非常有帮助。



**操作系统：**

如果你想全面学习Linux命令，推荐你阅读《**鸟哥的Linux私房菜**》。如果想再深入一点，推荐你阅读《**Linux系统管理技术手册**》。这本砖头厚的书，可以说是Linux运维手边必备。

《自己动手写操作系统》

《UNIX 环境高级编程》

《一个操作系统的实现》

《系统虚拟化原理与实现》

《深入理解Linux虚拟内存管理》

《深入理解Linux内核》

《深入Linux内核架构》

《穿越计算机的迷雾》

《程序员的自我修养：链接、装载与库》

《操作系统真象还原》

《操作系统设计与实现》

《x86汇编语言：从实模式到保护模式》

《linux内核设计的艺术图解》

《Linux设备驱动开发详解》

《Linux内核完全注释》

《Linux内核设计与实现》

《Linux多线程服务端编程》

《Linux 内核分析及编程》

《IBM PC汇编语言程序设计》

《深入理解计算机系统》

《性能之巅：洞悉系统、企业与云计算》

《Linux内核协议栈源代码解析》

《UNIX网络编程》

《Linux/UNIX系统编程手册》

《深入Linux设备驱动程序内核机制》

《深入理解Linux驱动程序设计》

《Linux Device Drivers》

《TCP/IP详解卷》

《The TCP/IP Guide》

《深入理解LINUX网络技术内幕》

《Linux内核源代码情景分析》

《UNIX/Linux系统管理技术手册》

关于操作系统，有一本国外的教材叫做OSTEP(Operating System Three Easy Picies) 虽然貌似没有中文版的，但里面的内容讲的相当通俗易懂，强烈推荐给大家作为理论层面的补充

给大家推荐一本非常棒的入门图书Unix/Linux编程实践教程(Understanding UNIX/LINUX Programming)，绝版了. 我的博客https://www.cnblogs.com/rocedu/p/6016880.html就是对这本书的核心方法的总结，供大家参考







## 操作系统架构

![21a9afd64b05cf1ffc87b74515d1d4f5](https://static001.geekbang.org/resource/image/21/f5/21a9afd64b05cf1ffc87b74515d1d4f5.jpeg)

linux源代码：https://github.com/torvalds/linux

* 系统调用：kernel/
* 进程管理：kernel/, arch/`<arch>`/kernel
* 内存管理：mm/, arch/`<arch>`/mm ; mm更多的是CPU体系结构的内存管理，与具体物理内存管理相关的代码在 arch/`<arch>`/mm
* 文件管理：fs/: （file system）
* 设备管理：drivers/char, drivers/block ； drivers存放各种硬件的驱动程序，drivers/block 下存放块设备的驱动程序
* 网络管理：net/

References:
\* https://www.kernel.org/
\* https://courses.linuxchix.org/kernel-hacking-2002/08-overview-kernel-source.html

操作系统本质上是构建的一层抽象层，用来屏蔽复杂的底层硬件，向上层用户提供一种“假象”。。 CPU(单核情况)，实际上是只有一个的，在一个特定时刻也只可能有一个程序跑在一个CPU上(因为寄存器只有一组)，但是我们在上层观察到的却是系统上好像同时运行着那么多的程序，这实际上是操作系统用进程这个概念对CPU做的抽象。
内存也是相似的概念，真实的内存和我们程序员看到的内存截然不同，操作系统通过内存映射等一系列技术让上层的程序员以为自己在操作一片连续的内存空间，实际上这只是操作系统对内存的抽象，是操作系统给程序员的幻象。
文件系统也是如此，我们看到的所谓的abcd盘符，真实的情况可能是一块机械硬盘，要找数据必须来回的寻道，找到数据的位置，操作系统通过一系列的操作，把如此复杂的过程层层抽象，抽象出了上层看起来简单的文件系统。





学习笔记+作业+提问，知识点真多啊，老师这文章货太干了。
一、 创建进程
\#### 创建进程的总结：
1、Linux中父进程调用fork创建子进程。
2、父进程调用fork时，子进程拷贝所有父进程的数据接口和代码过来。
3、当前进程是子进程，fork返回0；当前进程是父进程，fork返回子进程进程号
4、如果返回0，说明当前进程是子进程，子进程请求execve系统调用，执行另一个程序。
5、如果返回子进程号，说明当前进程是父进程，按照原父进程原计划执行。
6、父进程要对子进程负责，调用waitpid将子进程进程号作为参数，父进程就能知道子进程运行完了没有，成功与否。
7、操作系统启动的时候先创建了一个所有用户进程的“祖宗进程”，课时1，第3题A选项：0号进程是所有用户态进程的祖先
\##### 创建进程的系统调用：fork
\##### 执行另一个程序的系统调用：execve
\##### 将子进程的进程号作为参数传给它，父进程就能知道子进程运行完了没有，成功与否：waitpid

二、 内存管理
\##### 内存管理总结
1、每个进程都有独立的进程内存空间，互相之间不干扰。（隔离性）
2、进程内存空间，存放程序代码的部分，称为代码段（Code Segment）。
3、存放进程运行中产生数据的部分，称为数据段（Data Segment）。
4、进程写入数据的时候，现用现分物理内存给进程使用。
5、分配内存数量比较小时，使用brk调用，会和原来的堆数据连在一起。
6、需要分配的内存数据量比较大的时候，使用mmap，重新划分一块内存区域。
\##### 分配较小内存数量，和原来堆内数据连在一起：brk
\##### 分配较大内存数量，重新划分一块内存区域：mmap

三、 文件管理
\##### 文件的操作六个最重要系统调用：
\##### 打开文件：open
\##### 关闭文件：close
\##### 创建文件：creat
\##### 打开文件后跳到文件某个位置：lseek
\##### 读文件：read
\##### 写文件：write
\##### Linux一切皆文件
\##### 一切皆文件的优势即使统一了操作的入口，提供了极大的便利。

四、 信号处理（异常处理）
进程执行过程中一旦有变动，就可以通过信号处理服务及时处理。

五、 进程间通信
\#### 有两种方式实现进程间通信
\#### 消息队列方式
\##### 创建一个新的队列：msgget
\##### 发送消息到消息队列：msgsnd
\##### 取出队列中的消息：msgrcv

六、 共享内存方式
\##### 创建共享内存块：shmget
\##### 将共享内存映射到自己的内存空间：shmat

\#### 利用信号量实现隔离性
\##### 占用信号量：sem_wait
\##### 释放信号量：sem_post
伪代码：
假设信号量为1
signal = 1
sem_wait伪代码
while True {
if sem_wait == 1；
signal -=1;
break;
}
code.code;
sem_post伪代码
signal +=1;

七、 网络通信
\##### 网络插口：socket
\##### 网络通信遵循TCP/IP网络协议栈
\#####

八、 glibc
\##### glibc是Linux下开源标准C库
\##### glibc把系统调用进一步封

\##### sys_open对应glibc的open函数
\##### 一个单独的glibcAPI可能调用多个系统调用
\##### printf函数调用sys_open、sys_mmap、sys_write、sys_close等等系统调用

\### 课后作业
strace ls -la
查看有如下系统调用
execve
brk
mmap
access
open
fstat
mmap
close
read
stat
write
lseek
lstat
getxattr
socket
connect
mprotect

\##### 疑问：局部变量，在当前函数执行的时候起作用，就是说当前函数执行中产生的局部变量是存放在内存中的。为什么不是暂存在CPU缓存或者寄存器，进入另一个函数时，丢掉局部变量，而不写入内存，提升效率。 [1

用strace跟踪”whoami"命令，执行的系统调用有：
（1）execve执行/usr/bin/whoami程序
（2）brk、mmap 内存映射，mprotect内存权限更改
（3）access、openat、fstat、read、lseek、close 文件权限、属性查看、打开、跳到文件某个位置，关闭等操作
（4）geteuid 获取用户id
（5）socket、connect网络通信
（6）write 文件写入
（7）arch_pctcl、exit_group 设计架构的进程或线程状态和退出进程中的所有线程
[1赞]



* 看过刘超老师的趣谈网络，收获蛮多
  对于操作系统，我看了下老师的课程目录，下面的一些内容可能没有，希望刘超老师可以讲到以下内容
  1.信号在内核中的实现，如何在进程间传递
  2.epoll 在linux中的实现
  3.进程组的概念，前台进程，后台进程
  4.系统调用中，同步，异步，阻塞，非阻塞的严格定义
  5.linux系统中可重入的api和非可重入的api的区别，以及使用说明
  6.多线程程序中，对于linux系统api调用需要使用可重入的接口吗，不是的话哪些需要呢
  7.linux 多线程的实现
  8.linux中经典的一些并发处理 [47赞]

* 作为服务器开发，对刘超老师的话深有同感。因为对Linux缺乏一个系统的学习，遇到很多问题都都只能傻眼，问别人、百度谷歌一下吧，又发现其实是最简单的原理问题。买过《深入理解操作系统》，一大厚本没看得下去。。买过《Linux内核分析》一类的书，满满的内核C语言实现，确实又太“硬核”了一些。。通过学《Linux性能优化专栏》，对CPU上下文切换、平均负载、各种I/O有了进一步的理解，不过，还迫切需要知道进程调度、进程相关的知识，以及最最头疼的网络知识，socket通信和网络包的具体实现，急需拯救！ [8赞]
* 网络基础、数据结构与算法、操作系统这些基础，真的很重要。。所有的抽象都是基于这些进行封装的，所以学懂他们理解概念与理论很重要。所有的技术与编程语言都是基于此，后面学习其他新技术都是事半功倍。一定要跟上 [6赞]
* 
* 我很期待，最近在研究Goroutine及其调度。遇到瓶颈，回头补基础找遍经典OS教材也只有进程、线程理论层面的介绍，缺少协程介绍。即使是线程，也没有描述用户级线程到底是如何映射到内核级线程，如何委托内核级线程执行等等一系列问题，希望和老师及同学们讨教｡◕‿◕｡ [4赞]
* 
* 我是一名java开发者，昨天遇到一个问题，一个线程跑着跑着就没了。我目前感触是，我在Linux上只会看spring等应用的日志，我觉得线程没了肯定是报错了，但是我的日志就是没有找到报错。后来和运维询问，大概是说内存不足导致的。我的问题是，像内存不足的报错，我能在操作系统的什么地方看到系统级别的日志吗？ [3赞]
* Geek_540e1b 2019-03-26 19:41:47

  从事嵌入式领域，主要是RTOS，但是对linux也非常感兴趣，以后如果可以从事linux相关开发工作会非常开心，技术的都是相通的，希望学习了这个课程，会让自己的知识构架更加清晰，把以前会的重新整理，接下来学的也可以安排的井井有条！！！ [3赞]

第二个原则就是 **图解** 。Linux操作系统中的概念非常多，数据结构也很多，流程也复杂，一般人在学习的过程中很容易迷路。所谓“一图胜千言”，我希望能够通过图的方式，将这些复杂的概念、数据结构、流程表现出来，争取用一张图串起一篇文章的知识点。最终，整个专栏下来，你如果能把这些图都掌握了，你的知识就会形成体系和连接。在此基础上再进行深入学习，就会如鱼得水、易如反掌。

![](https://static001.geekbang.org/resource/image/bf/02/bf0bcbea6a24bc5084bc0d4ffca7c502.jpeg)

## Linux Distribution

ubuntu ---- Canonical

* Canonical Launchpad: a software collaboration platform that provides: https://launchpad.net/
* PPA: Personal Package Archives: https://launchpad.net/ubuntu/+ppas

Redhat

* How to create a Linux RPM package: https://www.redhat.com/sysadmin/create-rpm-package



## 源码

https://github.com/torvalds/linux



# [Linux下设置和查看环境变量](https://www.cnblogs.com/qiuhong10/p/7815943.html)

#### Linux的变量种类

按变量的生存周期来划分，Linux变量可分为两类：   
1 永久的：需要修改配置文件，变量永久生效。   
2 临时的：使用export命令声明即可，变量在关闭shell时失效。

#### 设置变量的三种方法

1 在/etc/profile文件中添加变量【对所有用户生效\(永久的\)】   
用VI在文件/etc/profile文件中增加变量，该变量将会对Linux下所有用户有效，并且是“永久的”。   
例如：编辑/etc/profile文件，添加CLASSPATH变量   
\# vi /etc/profile   
export CLASSPATH=./JAVA\_HOME/lib;$JAVA\_HOME/jre/lib

注：修改文件后要想马上生效还要运行\# source /etc/profile不然只能在下次重进此用户时生效。

2 在用户目录下的.bash\_profile文件中增加变量【对单一用户生效\(永久的\)】   
用VI在用户目录下的.bash\_profile文件中增加变量，改变量仅会对当前用户有效，并且是“永久的”。   
例如：编辑guok用户目录\(/home/guok\)下的.bash\_profile   
vi/home/guok/.bash.profile添加如下内容：exportCLASSPATH=./JAVAHOME/lib;vi/home/guok/.bash.profile添加如下内容：exportCLASSPATH=./JAVAHOME/lib;JAVA\_HOME/jre/lib   
注：修改文件后要想马上生效还要运行$ source /home/guok/.bash\_profile不然只能在下次重进此用户时生效。

3 直接运行export命令定义变量【**只对当前shell\(BASH\)有效\(临时的\)**】   
在shell的命令行下直接使用\[export 变量名=变量值\] 定义变量，

该变量只在当前的shell\(BASH\)或其子shell\(BASH\)下是有效的，

shell关闭了，变量也就失效了，再打开新shell时就没有这个变量，需要使用的话还需要重新定义。

#### 环境变量的查看

1 使用echo命令查看单个环境变量。例如：   
echo $PATH   
2 使用env查看所有环境变量。例如：   
env   
3 使用set查看所有本地定义的环境变量。

#### 使用unset删除指定的环境变量

set可以设置某个环境变量的值。清除环境变量的值用unset命令。如果未指定值，则该变量值将被设为NULL。示例如下：   
export TEST="Test..." \#增加一个环境变量TESTexport TEST="Test..." \#增加一个环境变量TESTenv\|grep TEST \#此命令有输入，证明环境变量TEST已经存在了   
TEST=Test...   
unset  TEST \#删除环境变量TEST   
$ env\|grep TEST \#此命令没有输出，证明环境变量TEST已经删除

#### 常用的环境变量

PATH 决定了shell将到哪些目录中寻找命令或程序   
HOME 当前用户主目录   
HISTSIZE　历史记录数   
LOGNAME 当前用户的登录名   
HOSTNAME　指主机的名称   
SHELL 当前用户Shell类型   
LANGUGE 　语言相关的环境变量，多语言可以修改此环境变量   
MAIL　当前用户的邮件存放目录   
PS1　基本提示符，对于root用户是\#，对于普通用户是$

  





## References：

* 鸟哥的Linux私房菜（http://vbird.dic.ksu.edu.tw/）
* Linux中国（https://linux.cn/）：Linux的资讯网站
* 实验楼（https://www.shiyanlou.com/）：IT学习网站，网站配有Linux在线开发环境
* Linux下载站（http://www.linuxdown.net/）：下载到各种Linux各种发行版，可以去官网下载
* Linux公社（http://www.linuxidc.com/）：Linux资讯网站

linux 鸟哥的私房菜

[Supervisor](http://www.supervisord.org)

[linux kernel](https://www.kernel.org/)
[linux standard base](https://wiki.linuxfoundation.org/lsb/start)
[Filesystem Hierarchy Standard](http://www.pathname.com/fhs/)
[red hat](https://www.redhat.com/en)


# Linux介绍

linux命令大全: [http://man.linuxde.net/](http://man.linuxde.net/)

## linux操作系统

linux指的是linux内核

linux操作系统指的是GNU/linux系统（基于linux的GNU系统）

- linux操作系统的使用基础

  - linux安装、配置
  - 常用命令
  - vi
  - x Window
- linux操作系统的系统与网络管理

  - 如何管理硬件和用户
  - 常用网络服务的配置和维护
- linux下进行程序设计

  - 程序的编辑、编译、调试、运行

## linux系统（发行版）

- GNU软件28%+linux内核3%+其他部件
- Linux是个类UNXI操作系统。（UNIX操作系统诞生于1969年的Bell实验室）
- 同时它是一个自由软件，是免费的，开放源代码，
- 编制它的目的是建立不受任何商品化软件版权制约，全世界都能自由使用的UNIX兼容产品。

## Linux历史

- Linux Torvalds.1990年赫尔辛基大学
- 1991年10月，Linux0.02
- 1994年3月，Linux1.0
- 1996年6月，Linux2.0
- 2001年1月，Linux2.4内核
- 2003年7月，Linux2.6内核测试版

## Linux开源标准

- POSIX

  POSIX（Portable Operating SystemIntertace可移植操作系统接口）是基于UNIX的，这一标准意在期望获得源代码级的软件可移植。
- GNU

  GNU计划，由PichardStallman在1983年9月27日发起，目标是创建一套完全自由的操作系统。
- GPL

  为保证GNU软件可以自由地“使用、复制、修改和发布”，所有GNU软件都包含一份在禁止其他人添加任何限制的情况下，授权所有权利给任何人的协议条款，这个条款被称为GNU通用公共许可在（GNU　GeneralPublic License,GPL）

## Linux系统特点

- 开放性
- 多用户
- 多任务
- 良好用户界面
- 设备独立性
- 提供丰富的网络功能
- 可靠的安全系统（没有蓝屏，不需要安装补丁,etc）
- 良好的可移植性

## Linux系统的组成

- 内核：是系统心脏，实现操作系统的基本功能(是运行程序和管理    像磁盘和打印机等硬件设备的核心程序)

  内核的功用有：进程管理、文件系统、网络功能、内存管理、驱动程序、安全功能等
- Shell:是系统的用户界面，提供用户与系统内核交互的一种接口
- 文件系统：是存放在硬盘上统一组织管理的组织集
- 应用程序：标准的linux系统都有一套应用程序集，包括：文本编辑，上网浏览，编程语言，XWindow 办公软件、Intenert工具、数据库等。

![images](/Volumes/╬╚┤µ/gmx/images_linux/linux compose.jpg)

linux 内核学习路线

![](/Volumes/╬╚┤µ/gmx/images_linux/linux_kernel.png)

## Linux版本

- 内核(Kernel)版本 
  - x.y.z-n 例Linux 2.6.18 （偶数是稳定版，奇数不稳定）
    - X 主版本号
    - Y 次版本号
    - Z 末版本号（表示内核的当前修订状态）
    - N 开发者的修补级别
- 发行(Distribution)版
  - 发行版由个人、松散组织的团队、商业机构以及志愿者组织编写
  - 发行版通常包括其它系统软件和应用软件
  - 发行版通常为许多不同的目的而制作
  - linux常见发行版

    - Red Hat Linux
    - CentOS （企业级，来源于redHat）
    - SUSE Linux
    - Debian 
    - Ubuntu (主要针对客户端操作系统，个人使用)

如何选择linux发行版

- 稳定性
- 硬件兼容性
- 高效率
- 可持续性


 	
# Linux系统安装

[Linux系统镜像下载地址](http://mirrors.163.com/)

## 创建linux分区

1. 创建Linux分区

   - 引导分区（boot分区）

     在弹出的“添加分区”对话框上，在剩余空间创建引导分区，挂载点为/boot，容量可以是100MB，文件系统类型是ext3

- 交换分区（swap分区）

  交换分区是一个特殊的分区，类似于Windows XP里的页面文件，它没有挂载点的概念。此处只需选择文件类型为swap，交换分区的容量通常是内存容量的2倍。
- 根分区（ / 分区）

  在弹出的“添加分区”对话框上，选择挂载点为“/”，选择文件系统类型为ext3，可以将剩余的容量全部分配给根分区，容量大小不低于2GB。

2. 创建其它的Linux分区：

   - /usr 分区:5~20G

     存储Fedora系统的各种软件。

- /var 分区:3~5G

  存储各应用相关的数据。
- /home 分区:

  存储用户的个人文件（比如音乐、视频文件等 ）。

# Linux字符界面

进入字符工作方式的方法

- 在图形环境下直接开启终端窗口
- 在系统启动后直接进入字符界面
- 使用远程登陆方式（SSH、ternet)进入字符工作环境

本地登录和远程登陆

- 本地登录和注销
- 远程登陆linux操作系统（第三方软件：putty,xshell）

  - 学会使用putty

    - putty下载地址
    - Session设置

      192.168.229.134
    - Window设置
    - 保存当前会话配置
    - 指定相关会话进行登陆

系统运行级别与关机

- 系统运行级别

  | 运行级 | 说明                                                                                           |
  | ------ | ---------------------------------------------------------------------------------------------- |
  | 0      | 所有进程将被终止，机器将有序的停止，关机时系统处于这个级别                                     |
  | 1      | 单用户模式，用于系统维护，只有少数进程运行，同时所有服务也不启动                               |
  | 2      | 多用户模式，和运行级别3一样，只有网络服务没有启动                                              |
  | 3      | 多用户模式，允许多用户登陆系统，是系统默认的启动级别                                           |
  | 4      | 留给用户自定义的运行级别.       例如在笔记本电脑的电池用尽时，可以切换到这个模式来做一些设置。 |
  | 5      | 多用户模式，并且在系统启动后运行x-window,图形化登陆                                            |
  | 6      | 所有进程被终止，系统重新启动                                                                   |

  运行级配置文件放在/etc/inittab中（ubuntu没有该文件），有一行“id:5:initdefault”

  root身份在终端上执行telinit n，进入运行级n
- 关机与重启命令

[http://man.linuxde.net/sub/%E7%B3%BB%E7%BB%9F%E5%85%B3%E6%9C%BA%E5%92%8C%E9%87%8D%E5%90%AF](http://man.linuxde.net/sub/%E7%B3%BB%E7%BB%9F%E5%85%B3%E6%9C%BA%E5%92%8C%E9%87%8D%E5%90%AF)

- 退出
  - 文本界面启动，用户退出系统
    - 按 `<Ctrl-D>`键或logout命令
  - 图形界面，用户退出系统，Fedora Core：
    - 鼠标点击“桌面→注销”
  - 关机命令：
    - 命令行方式：shutdown，halt，init 0，poweroff等，需要root权限
  - 图形桌面：鼠标点击“系统→关机”

# 进程管理与作业控制

来自[[http://www.178linux.com/48528](http://www.178linux.com/48528)](%5Bhttp://www.178linux.com/48528%5D(http://www.178linux.com/48528))

## 进程管理



### 2.进程分类：

- 交互进程：有一个Shell启动的进程，可在前台运行，也可在后台运行。
- 批处理进程：不与特定的终端相关联，提交到等待队列中顺序执行的进程。
- 守护进程：在Linux启动时初始化，需要时运行于后台的进程。在系统引导过程中启动的进程，跟终端无关的进程

### 3.进程状态
   在内存中运行的进程也有着各种各样的状态

- 运行态R：running
- 就绪态：ready
- 睡眠态

  - 可中断S：interruptable
  - 不可中断D：uninterruptable
- 停止态T：stopped,暂停于内存中，但不会被调度，除非手动启动
- 僵死态Z：zombie，结束进程，父进程结束前，子进程不关闭

### 4.进程启动方式：

1.手工启动：由用户输入命令直接启动一个进程，分为：

前台启动--直接输入命令,程序执行完就消失了，

后台启动--对于非常耗时进程，可以让进程在后台运行。从后台启动进程其实就是在命令结尾加上一个“&”号 。

2.调度启动：事先设置，根据用户要求让系统自动启动

1）at命令 :在指定时刻执行命令序列

在shell提示符下输入”at 时间”，回车后可以在之后的at>提示符下输入任务指令，每一行输入一个命令，所有命令都输入完毕后按Ctrl+d存盘退出 。

将各个命令写入shell脚本中，然后使用下面格式设置在指定时间执行shell脚本中的命令：at 时间 –f 脚本文件

at命令的写法非常灵活

例1：指定在今天下午6:30执行某命令。假设现在时间是2011年3月25日下午15:30，其命令格式如下：

at 6:30pm

at 18:30

at 18:30 today

at now + 3 hours

at now + 180 minutes

at 18:30 25.3.11

at 18:30 3/25/11

at 18:30 Mar 25

常用at指令

at：      安排延时任务

atq：    查询当前的等待任务

atrm：  删除等待任务

batch：以一个低优先级延时执行任务，

                在资源比较空闲的时候执行命令 

2）cron命令在系统启动时由一个shell脚本自动启动，进入后台。

cron启动后搜索/var/spool/cron目录，寻找以/etc/passwd文件中的用户名命名的crontab文件，被找到的这种文件将载入内存。

如果没有crontab文件，就转入“休眠”状态，释放系统资源。

cron每分钟“醒”过来一次，查看当前是否有需要运行的命令。

3）如果发现某个用户设置了crontab文件，它将以该用户的身份去运行文件中指定的命令。命令执行结束后，任何输出都将作为邮件发送给crontab的所有者，或者/etc/crontab文件中MAILTO环境变量中指定的用户。

crontab文件

  用户把要执行的命令序列放到crontab文件中以获得执行。每个用户都可以有自己的crontab文件。

crontab命令 :用于安装、删除或者列出用于驱动cron后台进程的crontab文件:         crontab [-u `<user>`] `<file>`

crontab文件格式

   `<minute>` `<hour>` `<day-of-month>` `<month-of-year>` `<day-of-week>` `<commands>`

例如：59 23 * * * tar czvf lhy.tar.gz/home/lhy

 

### 5.进程调度

调度策略：调度策略就是这样一组规则：决定什么时候以怎样的方式选择一个新进程运行。所以定义一个进程的优先级来满足这样一种策略。这个策略以0-139的优先级来表示。

实时优先级：1-99

无需调整，数字越大，优先级越高

静态优先级：100-139

可调整，数字越小，优先级越高 

优先级以Nice值调整

Nice：-20—-19 ，存在于task_struct结构体中  

公式如下：        

pri(new)=nice+pri(old)   

调度算法：早起的Linux中，调度算法是根据进程的优先级选择“最佳”进程来执行，它的缺点是时间开销与“可运行进程数量”有关。某种调度算法一定满足一种函数关系，业界称为Big O        

Big O：时间复杂度，用时和规模的关系。有： O(1), O(logn), O(n)线性, O(n^2)抛物线,O(2^n)

 


## 作业控制

作业控制，指控制当前正在运行的进程的行为，也称为进程控制。是Shell的一个特性，使用户能在多个独立进程间进行切换。

常用命令

| 命令或快捷键 | 功能说明                                 |
| ------------ | ---------------------------------------- |
| cmd&         | 该命令在后台运行                         |
| Ctrl+d       | 终止一个正在前台运行的进程(含有正常含义) |
| Ctrl+c       | 终止一个正在前台运行的进程(含有强行含义) |
| Ctrl+z       | 挂起一个正在前台运行的进程               |
| jobs         | 显示后台作业和被挂起的进程               |
|              | 重新启动一个挂起的作业，并在后台运行     |
| fg           | 把一个在后台运行的作业放到前台运行       |

常用的作业标识符

| 标识符 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| %N     | 第N号作业                                                    |
| %S     | 以字符串S开头的被命令行调用的作业                            |
| %?S    | 包含字符串S的被命令行调用的作业                              |
| %+     | 默认作业(前台最后结束的作业，或后台最后启动的作业)，等同于%% |

 

来自[[http://blog.csdn.net/sunleiailiumin/article/details/23788263](http://blog.csdn.net/sunleiailiumin/article/details/23788263)](%5Bhttp://blog.csdn.net/sunleiailiumin/article/details/23788263%5D(http://blog.csdn.net/sunleiailiumin/article/details/23788263))

 

来自[[http://www.178linux.com/48528](http://www.178linux.com/48528)](%5Bhttp://www.178linux.com/48528%5D(http://www.178linux.com/48528))

# 文件系统与目录结构

Linux能支持多种文件系统，如：EXT2、EXT3、FAT、VFAT、NFS、SMB、ISO9660等

## 目录结构及目录路径:

 ![linux file system](/Volumes/╬╚┤µ/gmx/images_linux/linux file system.png)

- /bin ：bin 是二进制（binary）英文缩写。
- /boot ：存放的都是系统启动时要用到的程序。使用grub或lilo引导linux时，会用到这里的一些信息.
- /dev：包含了所有linux系统中使用的外部设备。
- /etc ：存放了系统管理时要用到的各种配置文件和子目录。我们要用到的网络配置文件，文件系统，x系统配置文件，设备配置信息，设置用户信息等都在这个目录下。   Inittab
- /lib ：存放系统动态连接共享库的。几乎所有的应用程序都会用到这个目录下的共享库。
- /sbin ：存放系统管理员的系统管理程序。
- /home ：如果建立一个用户，用户名是“jl”,那么在/home目录下就有一个对应的/home/jl路径，用来存放用户的主目录。
- /mnt ：在一般情况下也是空的。可以临时将别的文件系统挂在这个目录下。
- /proc ：可以在这个目录下获取系统信息。这些信息是在内存中，由系统自己产生的。
- /root ：如果用户是以超级用户的身份登录的，这个就是超级用户的主目录。
- /tmp ：用来存放不同程序执行时产生的临时文件。
- /usr ：这是linux系统中占用硬盘空间最大的目录。
- /opt
- /run
- /snap
- /srv
- /sys
- /var

  ![地址：https://www.shiyanlou.com/courses/1](/Volumes/╬╚┤µ/gmx/images_linux/file_system.png)

Linux需要特别注意的目录

![internetcn.net](images_linux/file_system_2.jpg)

## 文件类型

linux系统下的文件类型包括如下：

| （-） | 普通文件 |
| ----- | -------- |
| （d） | 目录     |
| （l） | 符号链接 |
| （c） | 字符设备 |
| （b） | 块设备   |
| （s） | 套接字   |
| （p） | 命名管道 |

## 文件与目录操作

| 命令  | 功能                                     |                                         |
| ----- | ---------------------------------------- | --------------------------------------- |
| ls    | 显示指定目录和文件的信息                 | ls -a                                   |
| pwd   | 显示当前目录名称                         | pwd                                     |
| cd    | 进入指定目录                             | cd /home  cd /  (退到根目录，绝对路径) |
| mkdir | 创建指定名称的目录                       | mkdir name                              |
| rmdir | 删除指定名称的目录（只用于删除空文件夹） | rmdir name                              |

## 文件操作命令

| 命令  | 功能                                   |                          |
| ----- | -------------------------------------- | ------------------------ |
| file  | 显示指定文件的类型                     | file /etc/passwd         |
| touch | 建立指定名称的文件或更新文件时间       | touch filename           |
| cp    | 复制文件或目录                         | cp filename copyfilename |
| rm    | 删除文件或目录                         | rm filename              |
| mv    | 移动文件或目录，文件或目录重命令       | mv filename /home        |
| cat   | 显示文本文件内容                       | cat filename             |
| more  | 分页显示文本文件内容                   | more passwd              |
| less  | 分页显示文本文件内容，并可方便反复浏览 | less  /etc/passwd       |
| head  | 显示文件首部内容                       | head -5 /etc/passwd      |
| tail  | 显示文件尾部内容                       | tail -5 /etc/passwd      |

## linux文件权限及设置命令

文件权限

    每个文件或目录都有9个基本权限位控制其读、写、执行

| 字符 | 权限     | 对文件的含义       | 对目录的含义               |
| ---- | -------- | ------------------ | -------------------------- |
| r    | 读权限   | 可以读文件的内容   | 可以列出目录中的文件列表   |
| w    | 写权限   | 可以修改、删除文件 | 可以在该目录中创建删除文件 |
| x    | 执行权限 | 可以执行该文件     | 可以使用cd进入该目录       |

    权限说明

    1.目录上只有执行权限，表示可以进入此目录以及深层次目录

    2.目录上只有执行权限，要访问该目录下的有读权限文件，必须知道文件才可以访问

    3.目录上只有执行权限，不能列出目录列表也不能删除该目录

    4.目录上执行权限和读权限的组合，表示可以进入目录并列出目录列表

    5.目录上执行权限和写权限的组合，表示可以在目录中创建和重命名文件

 		![file command-1](/Volumes/╬╚┤µ/gmx/images_linux/file permission-1.png)

 

    ![file command-1](/Volumes/╬╚┤µ/gmx/images_linux/file permission-2.png)

 		d：目录                  -：普通文件

    drwxr：对当前用户可读可写可执行

    r-x：对用户组…

    r-x：对其它用户….

    分配三种基本权限

    文件属主的权限：用于限制文件或目录的创建者

    文件所属组的权限：用于限制文件或目录所属组的成员

    其它用户的权限：用于限制既不是属主又不是所属组的能访问该文件或目录的其他人员

 

    在linux中通过给三类用户分配三种基本权限，就产生了文件或目录的9个基本权位。

 

    查看文件和目录的权限

    ls -l

    ![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_ls.png)

修改某目录或文件的权限

    chmod

    ![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_chmod_1.png)

 	![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_chmod_2.png)

 	![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_chmod_3.png)

 	![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_chmod_4.png)

 	![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_chmod_5.png)

 	![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_chmod_6.png)

    ![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_chmod_7.png)

改变目录或文件的属主或组

    chown

 	![file permission](/Volumes/╬╚┤µ/gmx/images_linux/file permission_chown.png)

特殊权限位

    三个特殊权限位是在可执行程序运行时影响操作权限的。

| 特殊权限   | 说明                                                                                                                                                                                           |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SUID       | 当设置了SUID位的可执行文件被执行时，该文件将以所有者的身份运行，也　就是说无论谁来执行这个文件，它都有文件所有者的特权                                                                         |
| SGID       | 当一个设置了SGID位的可执行文件运行时，该文件将具有所属组的特权，任意存取整个组虽能使用的系统资源；若一个目录设置了SGID，则所有被复制到这个目录下的文件，其所属的组都会被重设为和这个目录一样。 |
| sticky-bit | 对一个文件设置了sticky-bit之后，尽管其它用户有写权限，也必须由属主执行删除、移动等操作；对一个目录设置了sticky-bit权限之后，那么存放在该目录下的文件或目录只能由其属主执行删除、移动等操作     |

    若用户无特殊需要，尽量不要去打开这些权限，避免安全方面出现漏洞

# 重定向和管道

标准输入输出

    linux大部分命令都具有标准的输入/输出设备端口，下图列出标准设备信息

| 名称   | 文件描述符 | 含义     | 设备   | 说明                                 |
| ------ | ---------- | -------- | ------ | ------------------------------------ |
| STDIN  | 0          | 标准输入 | 键盘   | 命令在执行所要的输入数据通过它来获得 |
| STDOUT | 1          | 标准输出 | 显示器 | 命令在执行后的输出结果从该端口输出   |
| STDERR | 2          | 标准错误 | 显示器 | 命令执行时的错误信息通过该端口送出   |

系统重定向

    重定向就是不使用系统的标准输入端口，标准输出端口和标准错误输出端口，而进行重新的指定，所以重定向分为输入，输出和错误重定向，通常情况下重定向到一个文件。

| 重定向符号 | 说明                                                                                                                                                                                                                                                                                                                          |                                              |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| <          | 实现输入重定向，输入重定向不经常使用，因为大多数命令都以参数的形式在命令行上指定输入文件的文件名，尽管如此，当使用一个不接受文件名为输入参数的命令，而需要的输入又是一个已存在的文件例，就可以使用输入重定向解决问题。                                                                                                        | cat `<test1>`test2  将test1的内容写入test2 |
| >或>>      | 实现输出重定向。输出重定向比输入重定向更常用。输出重定向使用户能把一个命令的输出重定向到一个文件里，而不是显示在屏幕上。很多情况下都可以使用这种功能。例如，如果某个命令的输出很多，在屏幕上不能完全显示，即可把它重定向到一个文件里，稍后再用文件编辑器来打开这个文件  使用>重定向，之前的内容就被覆盖了，>>在原有内容上追加 | ls >houdun  cat houdun                       |
| 2>或>>     | 实现错误重定向                                                                                                                                                                                                                                                                                                                | ls &>err                                     |
| &>         | 同时实现输出重定向和错误重定向                                                                                                                                                                                                                                                                                                |                                              |

 

管道

    许多linux命令具有过滤特性，即一条命令通过标准输入端口接受一个文件中的数据，命令执行后产生的结果数据又通过标准输出端口送给后一条命令，作为该命令的输入数据。后一条命令也通过标准输入端口而接受输入数据。

    管道命令“|”将这些命令前后连接在一起，形成一条管道线。格式如下：

    命令格式

    cmd1|cmd2

    cmd是命令名

    |管道连接符

    管道实例

| cat /etc/passwd\| more      | 分屏显示文本文件/etc/passwd的内容           |
| --------------------------- | ------------------------------------------- |
| cat /etc/passwd\| grep root | 查找是否存在root的用户账号                  |
| cat /etc/passwd\| wc        | 统计文本文件/etc/passwd的行数，字数和字符数 |
| dmesg\| grep eth0           | 查看引导信息中关于第1块网卡的信息           |
| rpm -qa\| grep httpd        | 查看系统是否安装了apache软件包              |

# linux系统查找

| which   | 查看可执行文件的位置                                                                |
| ------- | ----------------------------------------------------------------------------------- |
| whereis | 查看文件的位置                                                                      |
| locate  | 配合数据库查看文件位置                                                              |
| find    | 实际搜寻硬盘查询文件名称 (find也可以根据文件大小-size 时间-atime 正则表达式-regex) |

1、which 

语法：  [root [@redhat](http://my.oschina.net/honglv) ~]# which 可执行文件名称  

    which   [-a]    cmdname1 cmdname2......

作用：

locate a command，从环境变量PATH中，定位/返回与指定名字相匹配的可执行文件所在的路径

原理：

执行which命令时，which会在当前环境变量PATH中依次寻找能够匹配所找命令名字的可执行文件名，不加-a   选项，返回第一个匹配的可执行文件的路径，否则依次返回满足条件的所有可执行文件的路径名。

适用场合：

一般用于查找命令/可执行文件所在的路径。有时候可能在多个路径下存在相同的命令，该命令可用于查找当前所执行的命令到底是哪一个位置处 的命令。 

例如：  

[root [@redhat](http://my.oschina.net/honglv) ~]# which passwd  

/usr/bin/passwd  

                   

![](/Volumes/╬╚┤µ/gmx/images_linux/system search_which.jpg)

 

来自[[http://blog.csdn.net/u010625000/article/details/44455023](http://blog.csdn.net/u010625000/article/details/44455023)](%5Bhttp://blog.csdn.net/u010625000/article/details/44455023%5D(http://blog.csdn.net/u010625000/article/details/44455023))

 

2、whereis 

语法：  [root [@redhat](http://my.oschina.net/honglv) ~]# whereis [-bmsu] 文件或者目录名称  

    whereis    [-bmsu]    filename1  filename2.......

参数说明：  

-b ： 只找二进制文件  

-m： 只找在说明文件manual路径下的文件  

-s ： 只找source源文件  

-u ： 没有说明文档的文件  

作用：

locate the binary, source, andmanual page files for a command.即：定位/返回与指定名字匹配的二进制文件、源文件和帮助手册文件所在的路径。

原理：

whereis命令首先会去掉filename中的前缀空格和以.开头的任何字符，然后再在[数据库](http://lib.csdn.net/base/mysql)（var/lib/slocate/slocate.db）中查找与上述处理后的filename相匹配的二进制文件、源文件和帮助手册文件,使用之前可以使用updatedb命令手动更新数据库。

适用场合：

二进制文件、源文件和帮助手册文件路径的查找。

例如：  

将和passwd文件相关的文件都查找出来  

[root [@redhat](http://my.oschina.net/honglv) ~]# whereis passwd  

passwd:/usr/bin/passwd /etc/passwd /usr/share/man/man1/passwd.1.gz/usr/share/man/man5/passwd.5.gz  

只将二进制文件查找出来 

[root [@redhat](http://my.oschina.net/honglv) ~]# whereis -b passwd  

passwd:/usr/bin/passwd /etc/passwd  

![](/Volumes/╬╚┤µ/gmx/images_linux/system_search_whereis.jpg)

 

和find相比，whereis查找的速度非常快，这是因为linux系统会将系统内的所有文件都记录在一个 数据库文件 ( 参考资料1以及大多数文章中都是这样描述的，whereis会在一个数据库文件中查找，在参考资料2中找到这个数据库文件目录/var/lib/slocate/slocate.db，我在服务器中并没有找到这个目录，原因应该是我没有装locate命令，那么whereis到底是怎么查找的呢？ 找了很久没有，从参考资料3中有一种个人比较相信的答案，从 /{bin,sbin,etc} /usr{lib,bin,old,new,local,games,include,etc,src,man,sbin,X386,TeX,g++-include} 

/usr/local/{X386,TeX,X11,include,lib,man,etc,bin,games,emacs} 中查找，也没有去看whereis的源码，如果有确定的可以交流一下 )中，当使用whereis和下面即将介绍的locate时，会从数据库中查找数据，而不是像find命令那样，通过遍历硬盘来查找，效率自然会很高。  

但是 该数据库文件并不是实时更新，默认情况下时一星期更新一次，因此，我们在用whereis和locate 查找文件时，有时会找到已经被删除的数据，或者刚刚建立文件，却无法查找到，原因就是因为数据库文件没有被更新。  

来自[[http://blog.csdn.net/u010625000/article/details/44455023](http://blog.csdn.net/u010625000/article/details/44455023)](%5Bhttp://blog.csdn.net/u010625000/article/details/44455023%5D(http://blog.csdn.net/u010625000/article/details/44455023))

 

 

3、locate  

语法：  `[root@redhat ~]#locate 文件或者目录名称  `

    locate    [option]    filename1 filename2 ......

作用：

find files by name from one or moredatabases prepared by updatedb. 同whereis指令一样，也是从数据库建立的索引中查找，不同的是该命令查找所有部分匹配的文件，使用之前可以使用updatedb命令手动更新数据库

原理：默认情况下(当filename中不包含通配符*)，locate会给出所有与*filename*相匹配的文件的路径。

适用场合：没有文件类型性质的模糊查找（你只记得某个文件的部分名称）。

例如：  

`[root@redhat ~]#locate passwd  `

/home/weblogic/bea/user_projects/domains/zhanggongzhe112/myserver/stage/_appsdir_DB_war/DB.war/jsp/as/user/passwd.jsp  

/home/weblogic/bea/user_projects/domains/zhanggongzhe112/myserver/stage/_appsdir_admin_war/admin.war/jsp/platform/passwd.jsp  

/lib/security/pam_unix_passwd.so  

/lib/security/pam_passwdqc.so  

/usr/include/rpcsvc/yppasswd.x  

/usr/include/rpcsvc/yppasswd.h  

/usr/lib/perl5/5.8.5/i386-linux-thread-multi/rpcsvc/yppasswd.ph  

/usr/lib/kde3/kded_kpasswdserver.la  

/usr/lib/kde3/kded_kpasswdserver.so  

/usr/lib/ruby/1.8/webrick/httpauth/htpasswd.rb  

/usr/bin/vncpasswd  

/usr/bin/userpasswd  

/usr/bin/yppasswd  

…………  

         

![](/Volumes/╬╚┤µ/gmx/images_linux/system_search_locate.jpg)

 

来自[[http://blog.csdn.net/u010625000/article/details/44455023](http://blog.csdn.net/u010625000/article/details/44455023)](%5Bhttp://blog.csdn.net/u010625000/article/details/44455023%5D(http://blog.csdn.net/u010625000/article/details/44455023))

 

 

4、 find  

语法：  [root@redhat ~]# find 路径 参数  

     find    [option]    [path1  path2 ......]    [filename]

参数说明：

时间查找参数：

        -atime  n: 将n*24小时内access过的文件列出来

                 -ctime   n: 将n*24小时内状态发生改变的文件列出来

                 -mtime  n: 将n*24小时内被修改过的文件列出来

                 -newer file: 把比file还要新的文件列出来

           名称查找参数：

 -gid   n:  寻找群组ID为n的文件

         -group name: 寻找群组名称为name的文件

         -uid   n:  寻找拥有者ID为n的文件

         -user name:  寻找拥有者名称为name的文件

         -namefile:    寻找文件名为file的文件（可以使用通配符）

作用：search for files in a directoryhierarchy. 从当前目录递归的搜索文件。

原理：

遍历当前工作目录及其子目录，find命令是在硬盘上遍历查找，非常耗硬盘资源，查找效率相比whereis和locate较低。

适用场合：

能用which、whereis和locate的时候尽量不要用find.  当我们用whereis和locate无法查找到我们需要的文件时，可以使用find，但是find是在硬盘上遍历查找，因此非常消耗硬盘的资源，而且效率也非常低，因此建议大家优先使用whereis和locate。  

例如：  

```
[root@redhat ~]#find / -name zgz  

/home/zgz  

/home/zgz/zgz  

/home/weblogic/bea/user_projects/domains/zgz  

/home/oracle/product/10g/cfgtoollogs/dbca/zgz  

/home/oracle/product/10g/cfgtoollogs/emca/zgz  

/home/oracle/oradata/zgz  
```


```
 
[root@redhat ~]#find / -name '*zgz*'  

/home/zgz  

/home/zgz/zgz1  

/home/zgz/zgzdirzgz  

/home/zgz/zgz  

/home/zgz/zgzdir  

/home/weblogic/bea/user_projects/domains/zgz  

/home/weblogic/bea/user_projects/domains/zgz/zgz.log00006  

/home/weblogic/bea/user_projects/domains/zgz/zgz.log00002  

/home/weblogic/bea/user_projects/domains/zgz/zgz.log00004  

/home/weblogic/bea/user_projects/domains/zgz/zgz.log  

/home/weblogic/bea/user_projects/domains/zgz/zgz.log00008  

/home/weblogic/bea/user_projects/domains/zgz/zgz.log00005  
```



 

![](/Volumes/╬╚┤µ/gmx/images_linux/system_search_find.jpg)

 

来自[[http://blog.csdn.net/u010625000/article/details/44455023](http://blog.csdn.net/u010625000/article/details/44455023)](%5Bhttp://blog.csdn.net/u010625000/article/details/44455023%5D(http://blog.csdn.net/u010625000/article/details/44455023))

 

 4个命令的比较如下表所示：

          

![](/Volumes/╬╚┤µ/gmx/images_linux/system_search.jpg)

 

来自[[http://blog.csdn.net/u010625000/article/details/44455023](http://blog.csdn.net/u010625000/article/details/44455023)](%5Bhttp://blog.csdn.net/u010625000/article/details/44455023%5D(http://blog.csdn.net/u010625000/article/details/44455023))

 

来自[[http://www.cnblogs.com/duanxz/p/5027784.html](http://www.cnblogs.com/duanxz/p/5027784.html)](%5Bhttp://www.cnblogs.com/duanxz/p/5027784.html%5D(http://www.cnblogs.com/duanxz/p/5027784.html))


 

来自[[http://www.jb51.net/LINUXjishu/43356.html](http://www.jb51.net/LINUXjishu/43356.html)](%5Bhttp://www.jb51.net/LINUXjishu/43356.html%5D(http://www.jb51.net/LINUXjishu/43356.html))



#   日志查看

- 日志文件（log files）是包含关于系统消息的文件，包括内核、服务、在系统上运行的应用程序等。
- 不同的日志文件记载不同的信息。
- 多数的日志文件位于/var/log目录下。
- 某些程序（如Apache）在/var/log中有单独的日志文件目录。
- 日志可以滚动。

 ![log_1](/Volumes/╬╚┤µ/gmx/images_linux/log_1.png)

- 可以通过日志滚动配置文件/etc/logrotate/.conf控制日志的自动滚动。
- 多数日志文件都使用纯文本格式，可以使用任何文本编辑器如vi来查看它们。
- 大多数日志文件都需要拥有特权才允许查看。
- 图形化的日志查看器
- 

 ![log_2](/Volumes/╬╚┤µ/gmx/images_linux/log_2.png)

# Shell脚本编程

Shell 是Linux系统的用户界面，提供了用户与内核进行交互操作的一种接口。

shell也被称为Linux命令解释器。它接收用户输入的命令并把它送入内核去执行。

shell除了是命令解释器之外还是一种编程语言。通常将shell编写的程序称为shell脚本或shell程序

 ![shell.png](/Volumes/╬╚┤µ/gmx/images_linux/shell.png)

为什么学习shell script

自动化管理

监控管理

日志数据处理

自动数据备份

shell脚本中的成分

注释——用于对脚本进行解释和说明，在注释行的前面要加上符号#，这样在执行脚本的时候shell就不会对该行进行解释

命令——在shell脚本中可以出现任何在交互方式下可以使用的命令

变量——shell支持字符串变量和整形变量

结构控制语句——用以编写复杂脚本的流程控制语句

# Linux安装软件方法

LLinux 安装软件方法

- yum安装—— Redhat cenos susi
- rRPM安装—— Redhat cenos susi
- apt-get安装——dibian ubuntu
- 程序源代码包的编译安装方式 

应用程序与命令的关系

- 基本命令是linux系统中不可缺少的组成部分
- 命令保存在/bin和/sbin目录中
- 应用程序保存在/usr/bin和/usr/sbin目录中
- 命令的作用是完成对linux系统本身的管理工作，应用程序则完成对linux系统管理相对独立的任务
- 命令只能以命令行的形式运行，命令格式中包括命令字、命令选项和命令参数
- 应用程序可以是以命令行的形式运行，也可以是字符界面或图形界面的窗口程序，形式多样

 

应用程序中不同类型的文件保存在linux系统的不同目录中

| 文件类型                         | 保存目录       |
| -------------------------------- | -------------- |
| 普通执行程序文件                 | /usr/bin       |
| 服务器执行程序文件和管理程序文件 | /usr/sbin      |
| 应用程序配置文件                 | /etc           |
| 应用程序文档文件                 | /usr/share/doc |
| 应用程序手册页文件               | /usr/share/man |

程序源代码包的编译安装方式

源代码安装的一般步骤

确认当前系统中具备软件编译的环境

$ rpm -qa | grep gcc            (如果没安装gcc要安装)

获得应用程序的源代码软件包文件

wget [https://www.程序的网址](https://www.程序的网址)

wget [https://nginx.org/download/nginx-1.3.5.tar.gz](https://nginx.org/download/nginx-1.3.5.tar.gz)

解压源代码软件包文件

$ tar zxf nginx-1.3.5.tar.gz

进行编译前的配置工作

进入源代码目录 $ cd nginx-1.3.5

查看configure命令支持的配置选项(程序源代码目录中configure命令用于完成程序编译前的配置工作)

./configure --help

指定安装路径进行配置

./configure --prefix=/opt/nginx

./configure  (按默认方式安装)

进行程序源代码的编译

$ make

将编译完成的应用程序安装到系统中

$ make install

验证已编译安装完成的程序

$ cd /opt/nginx ; ls

ps：

[Linux如何编译安装源码包软件](http://www.cnblogs.com/pudao/p/5129513.html)

来自[[http://www.cnblogs.com/pudao/p/5129513.html](http://www.cnblogs.com/pudao/p/5129513.html)](%5Bhttp://www.cnblogs.com/pudao/p/5129513.html%5D(http://www.cnblogs.com/pudao/p/5129513.html))

ubuntu安装软件

- 在线安装

  ```
  sudo apt-get install xxx
  ```
- 离线安装

  - 知道你想安装软件的名字，然后根据相应平台下载相应版本的 deb 包，可以在 [http://packages.ubuntu.com/](http://packages.ubuntu.com/) 或者 [http://archive.ubuntu.com/ubuntu/pool/main/](http://archive.ubuntu.com/ubuntu/pool/main/) 中找到你所需要的 deb 包，并下载。 
  - **第二步**，如果你很清楚你即将安装的 deb 包所需的依赖，可以顺便把依赖的 deb 包下载下来。不用担心，上述网站会把每个 deb 包所需的依赖列出来，但是也不必把所有依赖 down 下来，因为 ubuntu系统本来就安装好了大部分基础的库和工具。 
  - 最后，**第三步**，使用 `sudo dpkg -i` 命令安装相应的软件包。如果安装过程中提示“未安装软件包 xxx”之类的错误，可以重复上述操作，直至安装成功。
  - 如果有由于有未安装的依赖导致无法成功安装 使用 sudo apt-get install -f

# Linux系统的网络应用

（各版本的linux操作系统都有服务器版和客户端版）

| 服务类型   | Linux                    | Windows      |
| ---------- | ------------------------ | ------------ |
| Web服务    | Apache                   | IIS,Apache   |
| Mail服务   | Sendmail,Postfix         | Exchange     |
| DNS服务    | BIND                     | Windows  DNS |
| FTP服务    | Vsftpd                   | IIS,ServU    |
| 目录服务   | OpenLDAP                 | 活动目录     |
| 文件服务   | Samba,NFS                | 文件共享服务 |
| 数据库服务 | MySQL，PostgreSQL,Oracle | SQL Server   |

## 用户和组的管理

linux账户分为用户账户和组账户

用户账户分为普通用户和超级用户。

普通用户在系统中的任务是普通工作，

管理员在系统上的任务是对普通用户和整个系统进行管理，管理员对系统具有绝对控制权，能对系统进行一切操作

组是用户的集合。组分为私有组和公共组。

当创建一个新用户时，若没有指定所属的组，linux建立一个和该用户同名的私有组，这个私有组只包括用户自己。标准组可以容纳多个用户

 

linux 账户系统文件

cd /etc/passwd

| 字段       | 说明                                           |
| ---------- | ---------------------------------------------- |
| 用户名     | 用户登录系统时使用的用户名，它在系统中是唯一的 |
| 口令       | 此字段存放的是加密口令                         |
| 用户标识号 | 是一个整数，每个用户的UID都是唯一的            |
| 组标识号   | 是一个整数，系统内部用它来标识用户所属组       |
| 注释性描述 | 存放用户全名信息                               |
| 自家目录   | 用户登陆系统后所进入的目录                     |
| 命令解释器 | 指示该用户使用的shell                          |

/etc/group

| 字段   | 说明                                              |
| ------ | ------------------------------------------------- |
| 组名   | 该组的名称                                        |
| 组口令 | 用户组的口令                                      |
| GID    | 组的识别号，和UID类似，每个组都有自己独有的标识号 |
| 组成员 | 属于这个组的成员                                  |

 

用户的增删改命令

| useradd username                                           | 创建一个新用户                                                  |
| ---------------------------------------------------------- | --------------------------------------------------------------- |
| useradd -G share tom  useradd -c "this is a testuser" lisi | 创建新用户tom,并加入到标准组share中  创建lisi并给lisi用户加备注 |
| usermod -l tom1 tom                                        | 修改tom的用户名为tom1                                           |
| usermod -L tom1  usermod -U tom1                           | 锁定及解除账号tom1                                              |
| userdel tom1                                               | 删除用户                                                        |
| userdel -r test1                                           | 删除用户及它的主目录和邮件                                      |

 

组的增、删、改命令

| groupadd share           | 创建一个新组share     |
| ------------------------ | --------------------- |
| groupmod -n houdun share | 将share组更改为houdun |
| groupdel houdun          | 删除hudun组（）       |

## 密码管理及用户切换

## Linux服务器删除乱码文件和文件夹的方法

由于php大势所趋，所以接触Linux服务器的机会越来越多。不同于Windows服务器，Linux服务器只支持数字、英文等字符，对中文字符没办法识别。所以导致我们打包上传文件解压之后出现中文乱码文件和文件夹。网上有很多解决的办法，但是今天亲测用find命令能快速删除乱码的文件和文件夹，所以跟大家分享一下。

首页进入乱码文件所在文件夹

使用ls -i命令找到文件或文件夹的节点编号

前面的就是节点号了，接下来使用find命令查询并且删除

-inum指根据节点号查询；-delete顾名思义就是删除操作了。这样就成功删除乱码文件了，值得注意的是，此方法只适用于删除文件或空的文件夹。

对于文件夹，尤其是非空的文件夹，上面的方法就不适用了，要用到另外的参数来实现，首先相同的是查看乱码文件夹的节点号

接下来使用find命令删除

虽然提示我们找不到此文件或文件夹，但其实已经表明删除了。-exec作用是查找后执行命令，其中{}代表前面查询到的结果，空格+\;是结束符，其它就不说了。-exec后可以跟任何常用命令，因此这方法不但适用于文件夹，文件也可以。

怎么批量删除呢？其实很简单，用for就好了

文件

文件夹

$n是变量名，与for后面定义的一致，其它没啥好说的，适用其它操作。

后记

不仅仅是删除，其它基本操作如改名、移动、复制等都适用的。

本文永久更新链接地址：[http://www.linuxidc.com/Linux/2015-01/111469.htm](http://www.linuxidc.com/Linux/2015-01/111469.htm)

 

来自[[http://www.linuxidc.com/Linux/2015-01/111469.htm](http://www.linuxidc.com/Linux/2015-01/111469.htm)](%5Bhttp://www.linuxidc.com/Linux/2015-01/111469.htm%5D(http://www.linuxidc.com/Linux/2015-01/111469.htm))

num :

http://www.baidu.com/link?url=m0HGIwzoUxxkDuk1TzjJqS8FG_uooIqyGPCAGKmomknm0-qsCge4rzmCURLaJWLIcEBUr4nEa5NHppgeYlkeXq&wd=&eqid=9abca4d20003bfdb00000003599539c7

qemu+gdb

http://www.baidu.com/link?url=TR_o7REaRJf0HoZ_RIzNJNxv6j7jjh0ca87Vf3EChv___1AlP2WKATa52BUfuD3MwWBxM8cQY5ZemCbed0xp-a&wd=&eqid=88ad5b2e0002cb740000000259953c10

## im-switch命令

**名称                                **
im-switch - 在X Window下设置输入法

http://blog.sciencenet.cn/blog-520608-726761.html

Linux Security Coaching

[Linux Security Coaching](https://link.jianshu.com?t=https://raw.githubusercontent.com/phith0n/Mind-Map/master/Linux%20Security%20Coaching.png)

![](/Volumes/╬╚┤µ/gmx/images_linux/Linux_Security_Coaching.png)
