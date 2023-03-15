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

# Linux学习路径

![Linux知识脑图](/Volumes/╬╚┤µ/gmx/images_linux/linux_study.png)

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

## LINUX命令

linux命令大全: [http://man.linuxde.net/](http://man.linuxde.net/)

命令基本格式

```shell
cmd [options][arguements]
```

- cmd: 命令名
- options: 选项
- argumenrs :参数

通配符

| *  | 匹配任何字符和任何数目的字符 | ls*.conf               ls /home/*.txt  ls h*.config |
| -- | ---------------------------- | ----------------------------------------------------------------- |
| ？ | 匹配单一数目的任何数目的字符 | ls test?.aa                                                       |
| [] | 匹配中括号之内的任意一个字符 | ls [abc]*                                                         |

获得命令帮助

| 通过命令参数直接查看帮助 | ls --help |
| ------------------------ | --------- |
| 使用main命令获得帮助     | main ls   |
| 使用info命令获得帮助     | info ls   |

基本命令操作

| 注销用户 | Logout   |
| -------- | -------- |
| 关机     | Shutdown |
| 重启     | reboot   |

命令补全：

    table键

    命令补全

    目录名称补全（目录名称都有/标识：sysconfig/） cd e -> cd etc/sys

    文件补全 cat h -> cat h1.txt

    实例

    cd h

    若按两次`<tab><tab>`按后，系统发出蜂鸣声无法补齐，通常是已经输入的部分有错误。

命令历史

    上下方向键

    用history命令来显示历史命令

    用！！执行最近执行过的命令 （执行上一次输入的命令）

    用！执行已经执行过的命令 （）

 	![images](/Volumes/╬╚┤µ/gmx/images_linux/command history-1.png)

![image](/Volumes/╬╚┤µ/gmx/images_linux/command history-2.png)


![](/Volumes/╬╚┤µ/gmx/images_linux/linux_command_2.png)

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

在linux系统中，内核的功用有：进程管理、文件系统、网络功能、内存管理、驱动程序、安全功能等，在这众多的模块中，进程管理是相对重要的一环，即使不像文件系统和网络功能那么复杂。在进程管理中，内核对进程的创建、切换、撤销和调度都有很详细的定义。  

来自[[http://www.178linux.com/48528](http://www.178linux.com/48528)](%5Bhttp://www.178linux.com/48528%5D(http://www.178linux.com/48528))

## 进程管理

### 1.进程

进程(Process)是一个程序在其自身的虚拟地址空间中的一次执行活动。多个程序并发执行，可以提高系统的资源利用率和吞吐量。

```
进程和程序：

程序只是一个静态的数据和指令集合，而进程是一个程序的动态执行过程，具有生命周期，是动态的产生和消亡的。

进程是资源申请、调度和独立运行的单位，因此它使用系统中的运行资源，而程序不占用系统的运行资源。

程序与进程无一一对应关系。一个程序可以由多个进程所共用，即一个程序在运行过程中可以产生多个进程；一个进程在生命周期内可以顺序执行若干个程序。
```

[Linux](http://lib.csdn.net/base/linux)中的进程，每个进程有一个识别号，PID(Process ID)。系统启动后的第一个进程是init，PID是1。init是唯一一个由系统内核直接运行的进程。新的进程可以用系统调用fork产生，从一个旧进程中分出一个新进程来，旧进程是新进程的父进程，新进程是产生他的旧进程的子进程，除了init之外，每一个进程都有父进程。

系统启动后，init进程会创建login进程等待用户登录，当用户登录系统后，login进程就会为用户启动shell进程，此后用户运行的进程都是由shell衍生出来的。

除了PID外，每个进程还有另外4个识别号：

- 实际用户识别号(real user ID)，
- 实际组识别号，
- 有效用户识别号(effect user ID),
- 有效组识别号。

实际用户识别号和实际组识别号用于识别正在运行此进程的用户和组，也即运行此进程的用户的识别号和组的识别号。有效用户识别号和有效组识别号确定一个进程对其访问的文件的权限和优先权。

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

 

### 6.进程管理命令

#### 6.1进程查看命令 ps

```shell
ps [选项]
```

主要选项的含义如下：

```shell
-e：显示所有进程；

-h：不显示标题；

-l ：采用详细的格式来显示进程；

-a：显示所有终端上的进程，包括其他用户的进程；

-r ：只显示当前终端上正在运行的进程；

-x：显示所有进程，不以终端来区分；

-u：以用户为主的格式来显示进程； 

-f 显示完整格式程序信息

-F 显示完整格式的进程信息

-H以进程层级格式显示进程相关信息

-aux  包括了cpu,内存等使用率  （常用）

-ef （常用）

-eFH （常用）
```

#### 6.2删除进程命令kill

```shell
kill [-s <信号>| -p] <进程号> ...
kill -l [信号]
```

选项的含义如下：

```shell
-s：指定需要送出的信号。既可以是信号名也可以是信号名对应的数字。

-p：指定kill命令只显示命名进程的pid， 并不真正送出任何信号。

-l： 显示信号名称列表，该列表也可以在/usr/include/linux/signal.h文件中找到。
```

常用信号：

1) SIGHUP: 无须关闭进程而让其重读配置文件；
2) SIGINT: 中止正在运行的进程；相当于Ctrl+c；
3) SIGKILL: 杀死正在运行的进程；
4) SIGTERM：终止正在运行的进程；
5) SIGCONT：
6) SIGSTOP：

指定信号的方法：

(1) 信号的数字标识；1, 2, 9

(2) 信号完整名称；SIGHUP

(3) 信号的简写名称；HUP

 

来自[[http://www.178linux.com/48528](http://www.178linux.com/48528)](%5Bhttp://www.178linux.com/48528%5D(http://www.178linux.com/48528))

 

#### 6.3删除进程killall

#### 6.4 总结Linux中用于终结进程的kill和pikill及killall命令用法

[http://www.jb51.net/LINUXjishu/420508.html](http://www.jb51.net/LINUXjishu/420508.html)

 

 

#### 系统监控命令top ：

  能显示实时的进程列表，而且还能实时监视系统资源，包括内存、交换分区和CPU的使用率等。

top命令的一般格式是：

```
top [d <间隔秒数>] [n <执行次数>]
```

   ![command_top](/Volumes/╬╚┤µ/gmx/images_linux/command_top.png)

#### 4、进程管理命令之pstree

   pstree – display a tree of processes

   显示进程数

#### 6、进程管理命令之pkill

   pkill [options] pattern    

        -u uid: effective user

        -U uid: real user

        -t terminal: 与指定终端相关的进程

        -l: 显示进程名

        -a: 显示完整格式的进程名

        -P pid: 显示其父进程为此处指定的进程的进程列表

#### 7、进程管理命令之pidof

   根据进程名获取其PID

#### 8、进程管理命令之top

Tasks

| total    | 进程总数     |
| -------- | ------------ |
| running  | 运行进程数   |
| sleeping | 休眠态进程数 |
| stopped  | 停止态进程数 |
| zobie    | 僵死态进程数 |

%Cpu(s)

| us(user space)         | 用户空间占用CPU百分比                            |
| ---------------------- | ------------------------------------------------ |
| sy(system)             | 内核空间占用CPU百分比   注：高负载时：us:sy=7:3 |
| ni(nice)               | 修改nice值占用的CPU百分比                        |
| id(idle)               | 空闲的CPU百分比                                  |
| wa(wait)               | 等待IO完成占用的CPU百分比                        |
| hi(hardware interrupt) | 硬中断占用CPU百分比                              |
| si(software interrupt) | 软中断占用CPU百分比                              |
| st(stole)              | 被偷走的CPU，比如VMware                          |

| buffer(缓冲) | 元数据 |
| ------------ | ------ |
| cache(缓存)  | 数据   |

| PID          | 进程号     |
| ------------ | ---------- |
| USER         | 进程发起者 |
| PR(priority) | 优先级     |
| NI(Nice)     | nice值     |
| VIRT         | 虚拟内存集 |
| RES          | 常驻内存集 |
| SHR          | 共享内存集 |
| S(status)    | 状态       |
| %CPU         | CPU占用比  |
| %MEM         | 内存占用比 |
| TIME+        | 运行时长   |
| COMMAND      | 启动进程   |

对显示排序的方法：

| P | 占据的CPU百分比 |
| - | --------------- |
| M | 占据内存百分比  |
| T | 累积占据CPU时长 |

首部信息显示：

| l     | uptime信息       |
| ----- | ---------------- |
| t     | tasks及cpu信息   |
| #数字 | cpu分别显示      |
| m     | memory信息       |
| s     | 修改刷新时间间隔 |
| Esc   | 退出             |
| k     | 终止指定进程     |
| W     | 保存文件         |
| q     | 退出命令         |

#### 9、进程管理命令之htop   

比top更加高级的进程管理软件

f1帮助

f2切换CPU、mem、swap显示方式

f10退出

    常用选项：

       -d #: 指定延迟时间；

       -u UserName:仅显示指定用户的进程；

       -s COLOMN:以指定字段进行排序；

   命令：

       s: 跟踪选定进程的系统调用；

       l: 显示选定进程打开的文件列表；

       a：将选定的进程绑定至某指定CPU核心；

       t: 显示进程树

   注意：Fedora-EPEL源

 

#### 10、进程管理命令之vmstat 

vmstat-s: 内存的汇总信息

| procs | 项目                                             |
| ----- | ------------------------------------------------ |
| r     | 等待运行的进程的个数，和核心数有关               |
| b     | 处于不可中断睡眠态的进程个数(被阻塞的队列的长度) |

| swap | 项目                             |
| ---- | -------------------------------- |
| si   | 从磁盘交换进内存的数据速率(kb/s) |
| so   | 从内存交换至磁盘的数据速率(kb/s) |

| io | 项目                                           |
| -- | ---------------------------------------------- |
| bi | 从块设备读入数据到内存的速率(kb/s)    读     |
| bo | 从内存写入磁盘的速率(kb/s)            写 |

| memory | 项目                 |
| ------ | -------------------- |
| swad   | 交换内存的使用总量   |
| free   | 空闲物理内存总量     |
| buffer | 用于buffer的内存总量 |
| cache  | 用于cache的内存总量  |

| system             | 项目         |
| ------------------ | ------------ |
| in: interrupts     | 中断速率     |
| cs: context switch | 进程切换速率 |

| cpu | 项目                       |
| --- | -------------------------- |
| us  | 用户空间占用的比例         |
| sy  | 内核空间占用的比例         |
| id  | 空闲空间占用的比例         |
| wa  | 等待IO完成所消耗的时间比例 |
| st  | 被虚拟化技术偷走的时间比例 |

 

来自[[http://www.178linux.com/48528](http://www.178linux.com/48528)](%5Bhttp://www.178linux.com/48528%5D(http://www.178linux.com/48528))

 

 

#### 11、进程管理命令之glances

glances [-bdehmnrsvyz1][-B bind] [-c server][-C conffile] [-p port][-P password] [–password][-t refresh] [-f file][-ooutput]

内建命令：

  a  Sort processesautomatically     l  Show/hide logs

  c  Sort processes by CPU%          b  Bytes or bits for network I/O

  m  Sort processes by MEM%          w  Delete warning logs

  p  Sort processes by name          x  Delete warning and critical logs

  i  Sort processes by I/O rate      1  Global CPU or per-CPU stats

  d  Show/hide disk I/O stats        h  Show/hide this help screen

  f  Show/hide file system stats     t  View network I/O as combination

  n  Show/hide network stats         u  View cumulative network I/O

  s  Show/hide sensors stats         q  Quit (Esc and Ctrl-C also work)

  y  Show/hide hddtemp stats

常用选项：

-b: 以Byte为单位显示网卡数据速率；

-d: 关闭磁盘I/O模块；

-f /path/to/somefile: 设定输入文件位置；

-o {HTML|CSV}：输出格式；

-m: 禁用mount模块

-n: 禁用网络模块

-t #: 延迟时间间隔

-1：每个CPU的相关数据单独显示；

C/S模式下运行glances命令：

服务模式：

glances -s -B IPADDR

IPADDR: 指明监听于本机哪个地址

客户端模式：

glances -c IPADDR

IPADDR：要连入的服务器端地址

 

来自[[http://www.178linux.com/48528](http://www.178linux.com/48528)](%5Bhttp://www.178linux.com/48528%5D(http://www.178linux.com/48528))

 

 

#### 12、进程管理命令之dstat

      dstat [-afv][options..] [delay [count]]

-c: 显示cpu相关信息；

-C #,#,…,total

-d: 显示disk相关信息；

-D total,sda,sdb,…

-g：显示page相关统计数据；

-m: 显示memory相关统计数据；

-n: 显示network相关统计数据；

-p: 显示process相关统计数据；

-r: 显示io请求相关的统计数据；

-s: 显示swapped相关的统计数据；

–top-cpu：显示最占用CPU的进程；

–top-io: 显示最占用io的进程；

–top-mem: 显示最占用内存的进程；

–top-lantency: 显示延迟最大的进程；

 

 

来自[[http://www.178linux.com/48528](http://www.178linux.com/48528)](%5Bhttp://www.178linux.com/48528%5D(http://www.178linux.com/48528))

 

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

语法：  [root@redhat ~]#locate 文件或者目录名称  

    locate    [option]    filename1 filename2 ......

作用：

find files by name from one or moredatabases prepared by updatedb. 同whereis指令一样，也是从数据库建立的索引中查找，不同的是该命令查找所有部分匹配的文件，使用之前可以使用updatedb命令手动更新数据库

原理：默认情况下(当filename中不包含通配符*)，locate会给出所有与*filename*相匹配的文件的路径。

适用场合：没有文件类型性质的模糊查找（你只记得某个文件的部分名称）。

例如：  

[root@redhat ~]#locate passwd  

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

[root@redhat ~]#find / -name zgz  

/home/zgz  

/home/zgz/zgz  

/home/weblogic/bea/user_projects/domains/zgz  

/home/oracle/product/10g/cfgtoollogs/dbca/zgz  

/home/oracle/product/10g/cfgtoollogs/emca/zgz  

/home/oracle/oradata/zgz  

 

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

 

![](/Volumes/╬╚┤µ/gmx/images_linux/system_search_find.jpg)

 

来自[[http://blog.csdn.net/u010625000/article/details/44455023](http://blog.csdn.net/u010625000/article/details/44455023)](%5Bhttp://blog.csdn.net/u010625000/article/details/44455023%5D(http://blog.csdn.net/u010625000/article/details/44455023))

 

 4个命令的比较如下表所示：

          

![](/Volumes/╬╚┤µ/gmx/images_linux/system_search.jpg)

 

来自[[http://blog.csdn.net/u010625000/article/details/44455023](http://blog.csdn.net/u010625000/article/details/44455023)](%5Bhttp://blog.csdn.net/u010625000/article/details/44455023%5D(http://blog.csdn.net/u010625000/article/details/44455023))

 

来自[[http://www.cnblogs.com/duanxz/p/5027784.html](http://www.cnblogs.com/duanxz/p/5027784.html)](%5Bhttp://www.cnblogs.com/duanxz/p/5027784.html%5D(http://www.cnblogs.com/duanxz/p/5027784.html))

# 打包、解压缩、压缩

## tar

Linux下最常用的打包程序就是tar了，使用tar程序打出来的包我们常称为tar包，tar包文件的命令通常都是以.tar结尾的。生成tar包后，就可以用其它的程序来进行压缩了，所以首先就来讲讲tar命令的基本用法： 

tar命令的选项有很多(用man tar可以查看到)，但常用的就那么几个选项，下面来举例说明一下： 

```shell
# 将所有.jpg的文件打成一个名为all.tar的包。-c是表示产生新的包 ，-f指定包的文件名
tar -cf all.tar *.jpg 

# 将所有.gif的文件增加到all.tar的包里面去。-r是表示增加文件的意思
tar -rf all.tar *.gif 

# 更新原来tar包all.tar中logo.gif文件，-u是表示更新文件的意思
tar -uf all.tar logo.gif 

# 列出all.tar包中所有文件，-t是列出文件的意思
tar -tf all.tar 

# 解出all.tar包中所有文件，-x是解开的意思 
tar -xf all.tar 
```

以上就是tar的最基本的用法。为了方便用户在打包解包的同时可以压缩或解压文件，tar提供了一种特殊的功能。这就是tar可以在打包或解包的同时调用其它的压缩程序，比如调用gzip、bzip2等。 

- tar调用gzip 

  gzip是GNU组织开发的一个压缩程序，.gz结尾的文件就是gzip压缩的结果。与gzip相对的解压程序是gunzip。tar中使用-z这个参数来调用gzip。下面来举例说明一下： 

  ```shell
  # 这条命令是将所有.jpg的文件打成一个tar包，并且将其用gzip压缩，生成一个gzip压缩过的包，包名为all.tar.gz 
  tar -czf all.tar.gz *.jpg 

  # 将上面产生的包解开
  tar -xzfall.tar.gz 
  ```
- tar调用bzip2 

  bzip2是一个压缩能力更强的压缩程序，.bz2结尾的文件就是bzip2压缩的结果。与bzip2相对的解压程序是bunzip2。tar中使用-j这个参数来调用gzip。下面来举例说明一下： 

  ```shell
  # 将所有.jpg的文件打成一个tar包，并且将其用bzip2压缩，生成一个bzip2压缩过的包，包名为all.tar.bz2 
  tar -cjfall.tar.bz2 *.jpg 

  # 将上面产生的包解开。 
  tar -xjfall.tar.bz2 
  ```
- tar调用compress 

  compress也是一个压缩程序，但是好象使用compress的人不如gzip和bzip2的人多。.Z结尾的文件就是bzip2压缩的结果。与 compress相对的解压程序是uncompress。tar中使用-Z这个参数来调用compress。下面来举例说明一下： 

  ```shell
  # 将所有.jpg的文件打成一个tar包，并且将其用compress压缩，生成一个uncompress压缩过的包，包名为all.tar.Z 
  tar -cZf all.tar.Z*.jpg 

  # 将上面产生的包解开 
  tar -xZfall.tar.Z 
  ```

有了上面的知识，你应该可以解开多种压缩文件了，下面对于tar系列的压缩文件作一个小结： 

- 对于.tar结尾的文件

  tar -xfall.tar
- 对于.gz结尾的文件

  gzip -d all.gz 

  gunzip all.gz 
- 对于.tgz或.tar.gz结尾的文件 

  tar -xzfall.tar.gz 

  tar -xzfall.tgz 
- 对于.bz2结尾的文件 

  bzip2 -dall.bz2 

  bunzip2all.bz2 
- 对于tar.bz2结尾的文件 

  tar -xjfall.tar.bz2 
- 对于.Z结尾的文件 

  uncompressall.Z 
- 对于.tar.Z结尾的文件 

  tar -xZfall.tar.z 

**另外对于Window下的常见压缩文件.zip和.rar，Linux也有相应的方法来解压它们： **

## .zip 

linux下提供了zip和unzip程序，zip是压缩程序，unzip是解压程序。它们的参数选项很多，这里只做简单介绍，依旧举例说明一下其用法： 

```shell
# 将所有.jpg的文件压缩成一个zip包 
zip all.zip *.jpg 

# 将all.zip中的所有文件解压出来 
unzip all.zip 
```

## .rar 

要在linux下处理.rar文件，需要安装RAR for Linux，可以从网上下载，但要记住，RAR for Linux 不是免费的；可从[http://www.rarsoft.com/download.htm](http://www.rarsoft.com/download.htm)下载RARfor Linux 3.2. 0，然后安装： 

```shell
 tar -xzpvfrarlinux-3.2.0.tar.gz 
 cd rar 
 make 
```

这样就安装好了，安装后就有了rar和unrar这两个程序，rar是压缩程序，unrar 是解压程序。它们的参数选项很多，这里只做简单介绍，依旧举例说明一下其用法： 

```shell
# 将所有.jpg的文件压缩成一个rar包，名为all.rar，该程序会将.rar扩展名将自动附加到包名后。 
rar a all *.jpg 

# 将all.rar中的所有文件解压出来 
unrar eall.rar 
```

 

---

到此为至，我们已经介绍过linux下的tar、gzip、gunzip、bzip2、bunzip2、compress 、 uncompress、 zip、unzip、rar、unrar等程式，你应该已经能够使用它们对.tar 、.gz、.tar.gz、.tgz、.bz2、.tar.bz2、. Z、.tar.Z、.zip、.rar这10种压缩文件进行解压了，以后应该不需要为下载了一个软件而不知道如何在Linux下解开而烦恼了。而且以上方法对于Unix也基本有效。 

本文介绍了linux下的压缩程式tar、gzip、gunzip、bzip2、bunzip2、compress 、uncompress、 zip、 unzip、rar、unrar等程式，以及如何使用它们对.tar、.gz 、.tar.gz、.tgz、.bz2、.tar.bz2、.Z、. tar.Z、.zip、.rar这10种压缩文件进行 

操作。 

 

## 以下补充tar 

```shell
-c: 建立压缩档案 

-x：解压 

-t：查看内容 

-r：向压缩归档文件末尾追加文件 

-u：更新原压缩包中的文件 
 
```

这五个是独立的命令，压缩解压都要用到其中一个，可以和别的命令连用但只能用其中一个。下面的参数是根据需要在压缩或解压档案时可选的。 

```shell
-z：有gzip属性的 

-j：有bz2属性的 

-Z：有compress属性的 

-v：显示所有过程 

-O：将文件解开到标准输出 
```

下面的参数-f是必须的

```shell
-f: 使用档案名字，切记，这个参数是最后一个参数，后面只能接档案名。 s
```

 

```shell
# tar-cf all.tar *.jpg
这条命令是将所有.jpg的文件打成一个名为all.tar的包。-c是表示产生新的包，-f指定包的文件名。 

# tar -rf all.tar*.gif 
这条命令是将所有.gif的文件增加到all.tar的包里面去。-r是表示增加文件的意思。 

# tar -uf all.tarlogo.gif 
这条命令是更新原来tar包all.tar中logo.gif文件，-u是表示更新文件的意思。 

# tar -tfall.tar 
这条命令是列出all.tar包中所有文件，-t是列出文件的意思 

# tar -xfall.tar 
这条命令是解出all.tar包中所有文件，-x是解开的意思 
```

## 压缩 

```shell
tar–cvf jpg.tar *.jpg 
//将目录里所有jpg文件打包成tar.jpg 

tar–czf jpg.tar.gz *.jpg 
//将目录里所有jpg文件打包成jpg.tar后，并且将其用gzip压缩，生成一个gzip压缩过的包，命名为jpg.tar.gz 

tar–cjf jpg.tar.bz2 *.jpg 
//将目录里所有jpg文件打包成jpg.tar后，并且将其用bzip2压缩，生成一个bzip2压缩过的包，命名为jpg.tar.bz2 

tar–cZf jpg.tar.Z *.jpg 
//将目录里所有jpg文件打包成jpg.tar后，并且将其用compress压缩，生成一个umcompress压缩过的包，命名为jpg.tar.Z 

rar ajpg.rar *.jpg 
//rar格式的压缩，需要先下载rar for linux 

zipjpg.zip *.jpg 
//zip格式的压缩，需要先下载zip for linux 
 
```

## 解压 

```shell
tar–xvf file.tar 
//解压 tar包 

tar-xzvf file.tar.gz 
//解压tar.gz 

tar-xjvf file.tar.bz2 
//解压 tar.bz2 

tar–xZvf file.tar.Z 
//解压tar.Z 

unrare file.rar 
//解压rar 

unzipfile.zip 
//解压zip 
 
```

## 总结 

- *.tar用 tar –xvf 解压 
- *.gz用 gzip -d或者gunzip 解压 
- *.tar.gz和*.tgz用 tar –xzf 解压 
- *.bz2用 bzip2 -d或者用bunzip2 解压 
- *.tar.bz2用tar–xjf 解压 
- *.Z用 uncompress 解压 
- *.tar.Z用tar –xZf 解压 
- *.rar用 unrar e解压 
- *.zip用 unzip 解压

 

来自[[http://www.jb51.net/LINUXjishu/43356.html](http://www.jb51.net/LINUXjishu/43356.html)](%5Bhttp://www.jb51.net/LINUXjishu/43356.html%5D(http://www.jb51.net/LINUXjishu/43356.html))

# 文本编辑器vi

附： [http://wiki.dzsc.com/info/7313.html](http://wiki.dzsc.com/info/7313.html)

---

文本编辑器

| 文本编辑器 | 说明                                                                         |
| :--------: | ---------------------------------------------------------------------------- |
|     vi     | linux学习者需要掌握的第一个文本编辑器  大多数linux系统中缺省使用的文本编辑器 |
|   Emacs   | 用于编辑程序源代码文件的文本编辑器                                           |
|    nano    | 在字符界面提供了菜单操作，易用性较好                                         |
|   gedit   | GNOME图形环境中的文本编辑器                                                  |
|    vim    | vi的增强版                                                                   |

vi是Linux/Unix世界里最常用的全屏编辑器，所有的Linux系统都提供该编辑器，而Linux也提供了vi的加强版——vim，同vi是完全兼容，存放路径为/usr/bin/vim

Vi编辑器是一个命令行编辑器，类似于Windows下的记事本。

它有三种基本的操作模式：

1. 指令模式：是vi的默认模式，该状态等待用户输入命令
2. 文本输入模式（编辑模式）：该状态可以编辑文本
3. 末行模式：该状态光标处于文本最末行，以“：”打头 

各个模式之间的切换规则：

1. 输入vi 文件名.后缀名,首先进入指令模式。
2. 在指令模式下输入a/i/o进入文本输入模式。
3. 文本编辑模式下按Esc键进入末行模式。

各个模式下可以进行的操作：

1. 指令模式下可以输入：移动光标功能键0/h/j/k/l$+A/PageDown/PageUp；进入文本编辑模式功能键a/i/o
2. 文本编辑模式下可以输入：任何内容
3. 末行模式下可以输入：q/:q!/:wq

 ![](/Volumes/╬╚┤µ/gmx/images_linux/linux_input_model.jpg) 

命令行模式 （command mode/一般模式）

任何时候，不管用户处于何种模式，只要按一下“ESC”键，即可使Vi进入命令行模式；我们在shell环境（提示符为$）下输入启动Vi命令，进入编辑器时，也是处于该模式下。 

在该模式下，用户可以输入各种合法的Vi命令，用于管理自己的文档。此时从键盘上输入的任何字符都被当做编辑命令来解释，若输入的字符是合法的Vi命令，则Vi在接受用户命令之后完成相应的动作。但需注意的是，所输入的命令并不在屏幕上显示出来。若输入的字符不是Vi的合法命令，Vi会响铃报警。

 

文本输入模式 （input mode/编辑模式）

在命令模式下输入插入命令i（insert）、附加命令a （append）、打开命令o（open）、修改命令c（change）、取代命令r或替换命令s都可以进入文本输入模式。在该模式下，用户输入的任何字符都被Vi当做文件内容保存起来，并将其显示在屏幕上。在文本输入过程中，若想回到命令模式下，按"ESC"键即可。 

 

末行模式 （last line mode/指令列命令模式）

末行模式也称ex转义模式。 

Vi和Ex编辑器的功能是相同的，二者主要区别是用户界面。在Vi中，命令通常是单个键，例如i、a、o等；而在Ex中，命令是以按回车键结束的正文行。Vi有一个专门的“转义”命令，可访问很多面向行的Ex命令。在命令模式下，用户按“:”键即可进入末行模式下，此时Vi会在显示窗口的最后一行（通常也是屏幕的最后一行）显示一个“:”作为末行模式的提示符，等待用户输入命令。多数文件管理命令都是在此模式下执行的（如把编辑缓冲区的内容写到文件中等）。末行命令执行完后，Vi自动回到命令模式。

## 1 vi编辑器的基本使用

vi编辑器是Linux系统下的标准编辑器。虽然命令繁多复杂，并且绝大多数功能的输入都依靠键盘来完成，但如果我们熟悉掌握之后就会发现vi编辑器的功能、效率等都是其他图形界面编辑器无法比拟的，下面让我们来揭开它的神秘面纱。

### 1.1 vi的启动

在终端输入命令vi，后面接着输入想要创建或编辑的文件名，即可进入vi编辑器。

命令的结果如图1-1所示：

 ![vi_start](/Volumes/╬╚┤µ/gmx/images_linux/vi_start.png)

图1-1 vi编辑器新建文件

如果vi命令后面所输入的文件不存在，则系统会自动创建一个以该字符串命名的文本文件。如上图，光标停留在左上方，由于新建文件中没有任何内容，所以每一行的开头都为波浪线。窗口的底部为状态栏，显示当前编辑文件的相关信息。

打开文件后，光标停留在屏幕左上方。状态栏显示了当前编辑文件的文件名、行数以及字符数等信息，如图1-2所示。

vi命令打开文件时还可以带参数，这些参数用于修正vi的打开方式，主要包括如下：

如果只需阅读文件内容而不想对其进行修改时，可以使用这个参数，以防对文件的误操作，如下：

运行命令如图1-3所示。

 ![vi_start_2](/Volumes/╬╚┤µ/gmx/images_linux/vi_start_2.png)

 图1-2vi编辑器打开文件 

 ![vi_start_3](/Volumes/╬╚┤µ/gmx/images_linux/vi_start_3.png)

 图1-3 以只读方式打开文件

该参数可以在保存文件时对其进行加密，以后每次打开都需要输入密钥，否则将出现乱码。

如果在打开vi时，没有给出文件名，也没有给出任何参数，即：

命令结果如图1-4所示：

 ![vi_start_4](/Volumes/╬╚┤µ/gmx/images_linux/vi_start_4.png)

 图1-4 直接打开vi编辑器

此时，vi编辑器中所有行都为空，窗口中央给出的是vi编辑器的使用帮助，当用户在vi中输入文本或执行命令时，该帮助信息会自动消失。另外，如果以这种方式打开vi编辑器，在保存文件时，需要指定文件名。

### 1.2 vi的工作模式

vi有3种工作模式：普通模式、编辑模式和命令模式，这3种模式之间可以相互切换，如图1-5所示。

 ![vi_model](/Volumes/╬╚┤µ/gmx/images_linux/vi_model.png)

 图1-5 vi编辑器的工作模式

1.普通模式

    由Shell进入vi编辑器时，首先进入普通模式。在普通模式下，从键盘输入任何字符都被当作命令来解释。普通模式下没有任何提示符，当输入命令时立即执行，不需要回车，而且输入的字符不会在屏幕上显示出来。

    普通模式下可以输入命令进行光标的移动，字符、单词、行的复制、粘帖以及删除等操作。

2.编辑模式

    编辑模式主要用于文本的输入。在该模式下，用户输入的任何字符都被作为文件的内容保存起来，并在屏幕上显示出来。在普通模式下， 输入a（附加命令）、c（修改命令）、i（插入命令）、o（另起新行）、r（取代命令）以及s（替换命令）都将进入编辑模式，此时vi窗口的最后一行会显示“插入”。输入i命令时屏幕上并无变化，但是通过执行i命令，编辑器由普通模式切换为编辑模式，如图1-6所示。

 ![vi_edit](/Volumes/╬╚┤µ/gmx/images_linux/vi_edit.png)

图1-6 编辑器由普通模式切换为编辑模式

接着输入x=，屏幕显示如图1-7所示。

要返回到普通模式，只需按键Esc即可。

 ![vi_edit_2](/Volumes/╬╚┤µ/gmx/images_linux/vi_edit_2.png)

 图1-7 在编辑模式下输入字符

3.命令模式

    命令模式下，用户可以对文件进行一些附加处理。尽管普通模式下的命令可以完成很多功能，但要执行一些如字符串查找、替换、显示行号等操作还是必须要进入命令模式的。

    在普通模式下输入冒号即可进入命令模式，此时vi窗口的状态行会显示出冒号，等待用户输入命令。用户输入完成后，按回车执行，之后vi编辑器又返回到普通模式下。

### 1.3 文件的保存和退出

当编辑完毕，需要退出vi编辑器时，可以在命令模式下(esc键由输入模式变成命令模式)使用命令退出vi，返回到Shell。

1.保存退出

保存退出是指将缓冲区中的内容写入文件，可以使用的命令为:wq和x，如图1-8所示。

 ![vi_save_quit](/Volumes/╬╚┤µ/gmx/images_linux/vi_save_quit.png)

 图1-8 vi编辑器的保存退出

2.强行退出

    强行退出是指无条件退出，不把缓冲区中的内容写入文件，所使用的命令为:q!。其中感叹号“!”表示不管文件是否被修改，放弃所修改的内容强行退出。

3.直接退出

直接退出和强行退出的区别是如果文件内容有修改则给出提示，如图1-9所示，否则直接退出。直接退出使用的命令为:q。

 ![vi_quit](/Volumes/╬╚┤µ/gmx/images_linux/vi_quit.png)

图1-9 vi编辑器的直接退出

    应该要注意一点，vi编辑器编辑文件时，用户的操作都是基于缓冲区中的副本进行的。如果退出时没有保存到磁盘，则缓冲区中的内容就会被丢失。所以，在退出vi编辑器时应该考虑是否需要保存所编辑的内容，然后再选择执行合适的退出命令。保存命令为w，如果打开vi时没有给出文件名，这时还需要给相互文件名。

### 1.4 光标移动

vi编辑器中的很多命令都是基于光标当前位置的，因此，如何移动光标定位到所需要的位置是一项十分重要的工作，下面进行详细介绍（如无特别说明，下面所讲的命令都是在普通模式下执行）。

\1. 向前移动字符

将光标向前移动一个字符可以使用命令为：l、Space键或方向键→。如果在命令前加一个数字n，就是将光标向前移动n个字符，例如：

\#include<stdio.h>

假设当前光标在include中的字符c上，则使用5l后，光标将移动到e处。但是要注意：光标的移动不能超过当前行的末尾，当然如果给出的数字超过当前光标到行末尾的字符个数，那么也只能移到行尾。

\2. 向后移动字符

将光标向后移动一个字符可以使用命令为：h、空格键或方向键←。同上面类似，如果在命令前加一个数字n，就将光标向后移动n个字符，而且光标不能超出行首。

\3. 移到下一行

将光标移到下一行可以用的命令：+、Enter键、j、Ctrl+n或方向键↓。这些命令之间是有差别的，+和Enter键是将光标移到下一行的行首，其余命令仅是移到下一行，所在的列不变。如果下一行比当前光标所在位置还短，则下标到行尾。

\4. 移到上一行

将光标上移一行可以使用的命令：-、k、Ctrl+p或方向键↑。同上面的命令类似，-命令将光标移到上一行行首，而另外3个保持在同一列。

\5. 移至行首

将光标移到当前行的行首使用的命令为0和^。这两个命令在使用时的差别在于命令0是将光标移到当前行的第一个字符，不管它是否为空白符，而命令^将光标移到当前行的第一个非空白符。

\6. 移至行尾

将光标移到当前行的行尾使用的命令为$。光标移至行尾后，停留在最后一个字符上，如果在该命令前加数字n，则光标将下移到n-1行的行尾。

\7. 按词前移

将光标按词前移使用的命令为w和W。这两个命令都是将光标向前移至下一个单词的开头，它们的区别在：命令w搜索词被定义为以标点符号或空白符（如制表符、换行符或空格符）分隔的字母或数字串；而命令W搜索的词被定义为非空白符字符串。例如有字符串：

echo l> /proc/sys/net/ipv4/conf/default/rp_filter

连续输入命令w，光标从行首移动的位置为：e、l、>、/、p、s、…、/、r、r。

而命令W，光标从行首移动的位置为：e、l、>、/、r。

\8. 按词后移

将光标后移的命令是b和B，这两个命令都是将光标后移至上一个单词的开头，同样，他们对词的定义是有区别的。

\9. 移至词尾

将光标移至当前字符所在词尾的命令是e和E。它们对词的定义与上面的类似。

\10. 移至指定行

将光标移至指定行的开头可以用命令如下：

- ：行号
- 行号G

注意：第一个命令是在命令模式下执行的，而非普通模式。如果没给出行号要显示行号可以用如下命令显示行号：

：set number

：ser nu：

如图1-11所示。

 ![vi_cursor](/Volumes/╬╚┤µ/gmx/images_linux/vi_cursor.jpg)

图1-11 在vi编辑器中显示行号

将行号去掉可以使用命令：

：set nonumber

：set nonu

1.4（2）编辑模式下（光标位置与屏幕滚动）

方向键：进行上下左右方向光标移动

Home：快速定位光标到行首

End：快速定位光标到行尾

PageUp：进行文本的向上翻页

PageDown：进行文本向下翻页

Backspace：删除光标左侧字符

Del：删除光标位置字符

### 1.5 屏幕滚动

在文件的编辑查看过程中经常涉及屏幕的滚动问题。

在vi编辑器中，尽管可以使用键盘上的Page Up键和Page Dawn键来完成这些操作，甚至使用方向键↑和↓，但是效率比较低，下面来看看相关屏幕滚动的命令。

\1. 向后滚动一屏

使用的命令为：Ctrl+f （滚屏后保留上一屏的最后两行）

\2. 向后滚动半屏

使用的命令为：Ctrl+d

\3. 向前滚动一屏

使用的命令为：Ctrl+b

\4. 向前滚动半屏

使用的命令为：Ctrl+u

\5. 屏幕定位

使用命令zz将当前行置为屏幕正中央，使用命令zt会将当前行置为屏幕顶端，命令zb则会将当前行置于屏幕底端。

将屏幕直接定位于文件第一屏或最后一屏也是经常遇到的问题，命令gg和G可以完成这样的功能，使用完这些命令后，光标会定位到第一屏的第一行或最后一屏的最后一行上。

### 1.6 文本输入、删除与修改

文本的输入、删除与修改是文件编辑的基本操作，其中大部分命令会将vi编辑器由普通模式切换为编辑模式，下面来介绍这些命令。

\1. 插入命令

文本的插入命令为i和I。其中i是将其后输出的字符插入到当前光标位置之前。命令I是将其后输入的字符插入到当前光标所在行的行首。

\2. 附加命令

附加文本的命令为a和A，其中命令a是将其后输入的字符插入到当前光标位置之后，而命令A则是将其后输入的字符追加到当前光标所在行的行尾。

\3. 另起新行

另起新行的命令为o和O，其中命令o是在当前行的下面另起一行，命令O是在当前行的上面另起一行。新行创建完后，光标停留在新行行首，等待输入文字。

\4. 删除字符

删除字符的命令为x和X。其中命令x删除光标所在处的字符，而命令X删除光标前面的那个字符。如果之前给出一个数字n，则删除由光标所在字符开始向右的n个字符。

\5. 删除文本对象

命令dd删除光标所在的行，命令D删除从光标所在位置开始到行尾的所有字符。

字母d可以与光标移动命令组合，例如：

- d^：从光标位置删至行首，不包括光标位。
- d$：从光标位置删至行尾，包括光标位，与D作用相同。
- dG：删除当前行至文件尾的内容。
- Dgg：删除当前行至文件头的内容。
- dw：删除当前字符到单词尾

J  删除光标所在行行尾的换行符，相当于合并当前行和下一行的内容

\6. 修改命令

修改文本的命令为c、C和cc，它们的作用是用新输入的文本取代原来的文本，这等价于将原来的文本删除后，利用命令i插入新的文本。

例如有一字符串：Hello World!

假设光标当前处在e处，输入命令cw后，屏幕显示如下：

H World!

此时光标处在H后的空格处，接着输入文本i后按Esc键，屏幕显示如下：

Hi World!

从上面可以看出，cw只是修改光标当前位置到词尾的字符，如果要修改整个单词，可以使用命令caw。

C命令用来修改从光标位置到行尾的文本。如果在前面加一个数字n，那么会把从当前光标位置至当前行下面的n-1行的内容都删除。

命令cc的功能和C相同，只是修改的范围不同，它修改光标所在的整行内容。

cw  删除当前光标到所在单词尾部的字符，并进入插入状态

c$  删除当前光标到行尾的字符，并进入插入状态

c^  命令删除当前光标之前（不包括光标上的字符，到行首的字符，并进入插入状态）

 

\7. 取代命令

取代文本的命令为r和R。其中命令r是用其后输入的单个字符取代光标所在的字符，如果在r前加一个数字n，则用其后输入的单个字符取代光标所在处开始向后的n个字符。

R命令用其后输入的文本取代光标所在处开始的若干个字符，每输入一个字符就取代原有的一个字符，多出的部分附加在后面。

8.撤销操作

u：取消最近一次的操作，并恢复操作结果，可以多次使用u命令恢复已进行的多步操作

U：取消对当前进行的所有操作

ctrl+r：对使用u命令撤销的操作进行恢复

### 1.7 复制与粘帖

vi编辑器中的缓冲区分为无名缓冲区和命名缓冲区。无名缓冲区以数字编号，一共有9个。前面讲过可以使用删除命令x和dd来删除文本，其实被删除的内容还保存在缓冲区中，最近一次删除的内容被保存在缓冲区1中，次近的在缓冲区2中，以此类推，我们可以使用命令把他们提取回来。

\1. 粘帖

粘帖缓冲区内容的命令是p和P，这两个命令的区别是：命令p将文本放在当前行之下或当前光标之后，而命令P将文本放在当前行之上或光标之前。

例：使用vi编辑器打开如下文件，然后进行删除和粘帖操作。

| 1  2  3  4  5  6 | case 5：  case 4：  case 3：  case 2：  case 1：  case 0： |
| ---------------- | ---------------------------------------------------------------- |
|                  |                                                                  |

假设光标当前出在第2行，连续执行dd命令4次，屏幕如下：

| 1  2 | case 5：  case 0： |
| ---- | -------------------- |
|      |                      |

输入命令p，则在屏幕显示如下：

| 1  2  3 | case 5：  case 0：  case 1： |
| ------- | ------------------------------- |
|         |                                 |

输入命令”3p，则屏幕显示如下：

| 1  2  3  4 | case 5：  case 0：  case 1：  case 3： |
| ---------- | ------------------------------------------ |
|            |                                            |

注意：”3用来引用缓冲区3，单个双引号后紧跟缓冲区的编号。

\2. 复制

命名缓冲区是以字母a~z命名的，利用命名缓冲区可以很好地保存若干文本段，便于以后存取、移动或者重排。访问这些缓冲区时，和前面一样，使用单个双引号。

复制文本的命令有如下两种格式：

yy

y<光标移动命令>

其中yy表示复制整行内容，而后者则通过光标移动命令来限定被复制的文本，如果没有指定缓冲区的名字，文本就被插入到无名缓冲区中。如果用大写字母表示缓冲区，则文本就附加到该缓冲区中，缓冲区中原有的内容不会被覆盖。

yw  复制当前光标到单词尾字符的内容到vi缓冲区

y$  复制当前光标到行尾的内容到vi缓冲区

y^复制当前光标到行首的内容到vi缓冲区

 

\3. 不使用缓冲区的复制与移动

使用的命令为co，它的基本格式如下：

:<开始行>,<结束行> co <目标行>

这个命令在命令模式下执行，其中开始行和结束行标识了文本复制的范围，而目标行则是文本粘帖的位置。

### 1.8 查找与替换

\1. 查找

/str向前查找字符串str，并将光标定位在str的第一个字母上，方便继续操作，按下“/”键后光标跳到vi窗口的最后一行，然后等待输入要查找的字符串，输入完成后按Enter键开始搜索，这时编辑器会高亮显示搜索结果。接下来可以使用命令n来实现光标在搜索结果中移动。

命令?与/的工作方式相同，只有搜索方向相反。

使用上面介绍的命令，例如/the来查找时，可能需要搜索匹配单词soothe和there，这时需要使用如下的形式：

/\<the\>

同理，要匹配一行的开头与结尾需要使用^和$字符，例如：

big$

这个命令只能匹配到一行末尾的单词big。

:set ignorecase

如果不关心目标字符串中的大小写，可以用上面的命令来设置。

:set nowrapscan

上面的命令是在输入目标字符串的过程中vi就开始搜索工作，即就是未完成输入事就能找到目标。

 

/word  从上而下在文件查找字符串“word”

?word  从下而上在文件查找字符串“word”

n定位下一个匹配的被查找字符串

N  定位上一个匹配的被查找字符串

\2. 替换命令

使用的命令为s和S，其中命令s用随后输入的文本替换光标所在处的字符。命令S将新输入的文本替换当前整行。

:s/old/new      将当前行中查找到的第一个字符old串替换尾new

:s/old/new/g      将当前行中查找到的所有字符old串替换尾new

:#,#s/old/new/g 在行号”#，#“范围内替换所有的字符串old为new

:%s/old/new/g  在整个文件范围内替换所有的字符串old为new

:s/old/new/c 在替换命令末尾加入c命令，将对每个替换动作提示用户进行确认

\3. 全局替换

全局替换命令有几种常用的格式：

g/s1/s//s2/

将包含字符串s1的所有行中用字符串s2替换s1的首次出现，即就是将所有行中第一次出现的s1替换为s2。

例如程序如下：

| 1  2  3  4  5  6  7 | int main()  {      int x;      for(x=1;x<=10;x++)          printf(“%d\n”,x);      return 0;  } |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
|                     |                                                                                                                         |

输入命令g/x/s//abc/后，上面的程序变为：

| 1  2  3  4  5  6  7 | int main()  {      int abc;      for(abc=1;x<=10;x++)          printf(“%d\n”,abc);      return 0;  } |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
|                     |                                                                                                                               |

可以看到每行中存在x的第一次出现处都被换为abc。

如果要将文件中的所有字符串s1都替换为字符串s2，则使用如下命令：

g/s1/s//s2/g

例如程序如下：

| 1  2  3  4  5  6  7 | int main()  {      int x;      for(x=1;x<=10;x++)          printf(“%d\n”,x);      return 0;  } |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
|                     |                                                                                                                         |

输入命令g/x/s//abc/g后，上面的程序变为：

| 1  2  3  4  5  6  7 | int main()  {      int abc;      for(abc =1; abc <=10;  abc ++)          printf(“%d\n”,  abc);      return 0;  } |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|                     |                                                                                                                                           |

可以看到所有的x都被替换为abc了。

| 1 | g/s1/s//s2/gc |
| - | ------------- |
|   |               |

该命令基本与上面的功能相同，只是在替换之前给出提示要求确认，如果回答y则进行替换，否则不作替换。

### 1.9 在输入vi命令时使用多个文件名作为参数

vifile1 file2 file3…

vi多文件操作命令 

:args  显示多文件信息

:next  向后切换文件

:prew  向前切换文件

:first  定位首文件

:last  定位尾文件

ctrl+^ 快速切换到编辑器中切换前的文件

## 2. vi编辑器之程序编辑

本小节主要介绍vi编辑器在程序设计中可以提高效率的几项操作，包括光标的跳转、关键字补全以及源代码缩进等。

### 2.1程序中光标的跳转

1.括号之间的跳转

命令%可以实现括号之间的跳转，转到与当前光标下的括号相匹配的一个括号上，如果光标在“(”上，就会跳到与它匹配的“)”上，如果当前在“)”上，就向前自动跳到匹配的“(”上。看下面的例子：

| 1  2  3  4  5  6  7 | int main ()  {      int x;      for(x=1;x<=10;x++)          printf("%d\n",x);      return 0;  } |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
|                     |                                                                                                                        |

假设光标处在第2行的行首，输入命令%后，光标将跳到第7行的行首。

如果当前光标没有停留在任何一个可用的括号字符上，命令%也会向前为它找到一个，但只会在当前行内查找，所以如果当前光标位于上例中第4行的x<=10上时，命令%还是会向前先找到第一个“(”的。

2.局部变量和函数名的跳转

命令gd可以在当前文件中对局部变量名或函数名进行搜索，并将光标定位在第一次出现的位置上，如图1-13所示，在代码第12行的sum变量上使用命令gd后，光标将定位在第4行的sum上。

 ![vi_edit_Program_1](/Volumes/╬╚┤µ/gmx/images_linux/vi_edit_Program_1.png)

这项功能对查找一些静态的变量或函数比较有用。

3.查找全局标识符

当在编辑程序时，经常会想知道一个变量是被声明为int型还是unsigned。解决这个问题的快速办法就是使用命令[I，命令会列出所有包含该标识符的行，不光在当前文件中，也查找当前文件所包含的头文件，以及被头文件所包含的文件，以此类推。看下面例子：

| 1  2  3  4  5  6  7  8  9  10 | /*file1.c*/  #include<stdio.h>  #include"yanyb.h"  int main ()  {      int x;      x=a;      printf("%d\n",x);      return 0;  } |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|                               |                                                                                                                                                       |

file1.c中包含了头文件yanyb.h文件。

| 1  2 | /*yanyb.h*/  int a=1; |
| ---- | ------------------------ |
|      |                          |

在file1.c中的a上使用命令[I，会在窗口下方给出如下信息。

| 1  2  3  4 | yanyb.h      1:   1 int a=1;  file1.c      2:   6 x=a; |
| ---------- | ----------------------------------------------------------------- |
|            |                                                                   |

上面列出的列表中每一行都有一个标号，如果要跳转到某一项只要先输入对应的标号即可：

3[`<Tab>`

### 2.2程序编辑过程中的关键字补全

很多的程序编辑器都提供了关键字补全功能，vi编辑器也不例外，相应的命令为Ctrl+p和Ctrl+n，这两个命令之间的差别只是在于搜索的顺序。

在源程序中输入printf函数时，只输入其中一部分，如图1-14所示。

 ![vi_edit_Program_2](/Volumes/╬╚┤µ/gmx/images_linux/vi_edit_Program_2.png)

此时输入Ctrl+n，屏幕中会出现相应的函数选项，此时可以使用上下方向键进行选择，如下图：

 ![vi_edit_Program_3](/Volumes/╬╚┤µ/gmx/images_linux/vi_edit_Program_3.png)

除了关键字补全外，还可以补全前面定义的变量或函数名。

### 2.3源代码的缩进

缩进不仅可以增强代码的可读性，也利于错误的排除，vi编辑器中提供了自动缩进和手动缩进两种功能，请看下面。

1.自动缩进

vi编辑器默认情况下可以自动完成缩进功能，对于缩进量可以在命令模式下使用如下命令进行设置。

: setcindent shiftwidth=2

这里将缩进设置为2个空格，即输出的文件格式如下。

| 1  2  3  4  5  6  7 | int main()  {    int x;    for(x=1;x<=10;x++)      printf("%d\n",x);    return 0;  } |
| ------------------- | ------------------------------------------------------------------------------------------------- |
|                     |                                                                                                   |

如果设置为4，则输出结果如下：

| 1  2  3  4  5  6  7 | int main()  {      int x;      for(x=1;x<=10;x++)          printf("%d\n",x);      return 0;  } |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
|                     |                                                                                                                       |

2.手动缩进

如果接手一些缩进格式相当槽糕的代码，或者要已有的代码里增删修补时，可能需要重新对代码的缩进进行整理，这时可以使用命令“=”来实现。

看下面的例子：

| 1  2  3  4  5  6  7 | int main()  {  int x;  for(x=1;x<=10;x++)  printf("%d\n",x);  return 0;  } |
| ------------------- | ----------------------------------------------------------------------------- |
|                     |                                                                               |

对于上面的代码，可以在光标所在行执行==操作，对该行进行缩进。也可以使用命令=G，对当前所在行到文件底部所有进行缩进，输出结果如下：

| 1  2  3  4  5  6  7 | int main()  {      int x;      for(x=1;x<=10;x++)          printf("%d\n",x);      return 0;  } |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
|                     |                                                                                                                       |

可以看到，整段代码实现了良好的缩进。

# 系统监视

- 内存查看命令free

  ![command_free](/Volumes/╬╚┤µ/gmx/images_linux/command_free.png)
- 磁盘空间用量查看命令df

 ![command_df](/Volumes/╬╚┤µ/gmx/images_linux/command_df.png)

- 系统监控命令top ：

   能显示实时的进程列表，而且还能实时监视系统资源，包括内存、交换分区和CPU的使用率等。

- top命令的一般格式是：

```
top  [d <间隔秒数>] [n <执行次数>]
```

 ![command_top](/Volumes/╬╚┤µ/gmx/images_linux/command_top.png)

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
