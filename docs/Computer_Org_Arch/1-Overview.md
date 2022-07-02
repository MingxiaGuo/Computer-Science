## What is Computer Architecture and Organization?

使用计算机的目的是为了提高手工作业的效率。但还有很多手工作业无法直接由计算机处理。

In general terms, the architecture of a computer system can be considered as a catalogue of tools or attributes that are visible to the user such as instruction sets, number of bits used for data, addressing techniques, etc.

Whereas, Organization of a computer system defines the way system is structured so that all those catalogued tools can be used. The significant components of Computer organization are ALU, CPU, memory and memory organization.

# Computer Architecture VS Computer Organization

| Computer Architecture                                        | Computer Organization                                        |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Computer Architecture is concerned with the way hardware components are connected together to form a computer system. | Computer Organization is concerned with the structure and behaviour of a computer system as seen by the user. |
| It acts as the interface between hardware and software.      | It deals with the components of a connection in a system.    |
| Computer Architecture helps us to understand the functionalities of a system. | Computer Organization tells us how exactly all the units in the system are arranged and interconnected. |
| A programmer can view architecture in terms of instructions, addressing modes and registers. | Whereas Organization expresses the realization of architecture. |
| While designing a computer system architecture is considered first. | An organization is done on the basis of architecture.        |
| Computer Architecture deals with high-level design issues.   | Computer Organization deals with low-level design issues.    |
| Architecture involves Logic (Instruction sets, Addressing modes, Data types, Cache optimization) | Organization involves Physical Components (Circuit design, Adders, Signals, Peripherals) |







History of Computer

https://www.javatpoint.com/history-of-computer

Type of Computer





计算机发展历程


冯诺伊曼机
	冯诺伊曼体系
		采用存储程序工作方式
		计算机硬件系统由运算(运算器，控制器，存储器)，输入设备，输出设备组成
		采用二进制表示信息
	现代计算机
第一代：电子管计算机
第二代：晶体管计算机
第三代：中小规模集成电路计算机
第四代



第一代：电子管计算机

1946-1957：电子管作为开关元件，使用机器语言，可以存储信息，输入输出很慢。
最初计算机发明是解决第二次世界大战时美国国防部弹道研究室开发新武器射程和检测模拟元算表的难题。
虽然当时电子管计算机耗电高，占地面积大，使用不方便，但比当时任何机械计算机快得多，每秒5000多次加法运算。

第二代：晶体管计算机

1958-1964: 晶体管替代电子管，采用磁芯存储器，汇编语言取代机器语言

1947年在贝尔实验室用半导体硅作为基片，制成第一个晶体管，它的体积小，低耗电，载流子高速运行的特点，使真空管望尘莫及。

第三代：中小规模集成电路计算机

1965-1971: 中小规模集成电路
1972-1977：大规模集成电路 （采用集成度很高的电路，出现了微处理器等）
1977-now：超大规模集成电路（采用集成度很高的电路，出现了微处理器等）

光刻技术和设备成熟

## 计算机工作过程

​	把程序和数据装入到主存储器中
​	从程序的起始地趾运行程序
​	用程序的首地址从存储器中取出第一条指令，经过译码、执行步骤等控制计算机各功能部件协同运行，完成指令功能，并计算下一条指令的地址
​	用新得到的指令地址继续读出第二天指令并执行之，直到程序结束为止；每一条指令都是在取指、译码、执行的循环过程中完成的。





## 计算机三大基本原则

* 计算机是执行输入、运算、输出的机器 （硬件）   计算机是执行程序的机器：计算机是执行程序的机器
* 程序是指令和数据的集合 （软件） 
* 计算机的处理方式有时与人们的思维习惯不同
* 计算机是由硬件和软件组成的

![image-20220702193924166](/Users/gmx/Library/Application Support/typora-user-images/image-20220702193924166.png)



软件：即程序的基础。
指令：控制计算机进行输入、运算、输出的命令。
把向计算机发出的指令一条条列出来，就得到了程序。

在程序设计中，会为一组指令赋予一个名字，可以称之为 函数、语句、方法、子例程、子程序。

程序中数据分为两类，一类是作为指令执行对象的输入数据，一类是从指令的执行结果得到的输出数据。
在编程时程序员会为数据赋予名字，称其为 变量。



用数字表示所有信息，是一个很具有代表性的计算机式处理方法，这一点正是和人类的思维习惯最不一样的地方。

计算机内部先把文字转换尘封相应的数字再处理，这样的数字叫“字符编码”，总之计算机会把什么都用数字来表示。



## 计算机组成

* 硬件(物理)系统

  * 主机/机箱
    * CPU
    * 电源
    * 声卡
    * 显卡
    * 调制解调器
    * 网卡
    * 系统单元
    * 主板
      * 桥接器：桥接器：主機板上面溝通各部元件的晶片組，其設計優劣，就會影響效能。
        * 北桥
        * 南桥：负责连接速度较慢的装置介面，包括硬盘、USB、网卡等
  * 存储器
  * 输入单元
  * 输出单元
  * 总线

* 软件(逻辑)系统

  * 操作系统软件：管理整个计算机系统，监视服务，使系统资源得到合理调度，高效运行

    * 操作系统(DOS, Windows, UNIX, Linux等)： 批处理系统，分时系统，实时系统
    * 标准程序库
    * 语言处理程序：将汇编语言翻译成机器语言的汇编程序，将高级语言翻译成机器语言的编译程序
      * 机器语言
      * 汇编语言
      * 高级语言(C, C++, Fortran, Pascal)
    * 服务程序：诊断程序，调试程序，连接程序
    * 数据库管理系统
    * 网络软件

  * 应用软件：用户根据任务需要所编制的各种程序

    * 文字处理软件(Microsoft Word, WPS)
    * 表格处理软件(Microsoft Excel, WPS)
    * 辅助设计软件(AutoCAD, Mastercam)
    * 科学计算程序
    * 过程控制程序
    * 事务管理程序
      			

    

硬件系统：

计算机硬件由大量的IC(Integrated Circuit, 集成电路)组成，每块IC上带有许多引脚。这些引脚由的用于输入有的用于输出。IC会在其内部对外部输入对信息进行运算，并把运算结果输出到外部。

\1. 如何进行输入
\2. 如何获取输出
\3. 进行怎样的运算才能从输入得到输出

输入，运算，输出必须成套出现，缺一不可



北桥：

负责连接速度较快的CPU、主存与显卡等元件。

由於北橋最重要的就是 CPU 與主記憶體之間的橋接，因此目前的主流架構中， 大多將北橋記憶體控制器整合到 CPU 封裝當中了。所以上圖你只會看到 CPU 而沒有看到以往的北橋晶片喔！

早期晶片組分南北橋，北橋可以連接 CPU、主記憶體與顯示卡。只是 CPU 要讀寫到主記憶體的動作，還需要北橋的支援，也就是 CPU 與主記憶體的交流， 會瓜分掉北橋的總可用頻寬，真浪費！因此目前將記憶控制器整合到 CPU 後，CPU與主記憶體之間的溝通是直接交流，速度較快之外，也不會消耗更多的頻寬！

## 常用计算单位

​	容量
​		bit, byte; GB为10进位, GiB为2进位
​	速度
​		Hz：CPU运算速度，Hz: 秒分之一
​		Mbps：网络每秒传输的字节数 Mbps = Mbits per second，