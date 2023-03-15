# Bus

Basics of Bus
	波特率
	比特率
	总线宽度
	总线带宽
	总线的传输周期
	主设备
	从设备
	总线复用

## Bus Types

* 片内总线：芯片内部的总线，如CPU芯片内部，寄存器与寄存器之间，寄存器与与算逻单元ALU之间都由片内总线连接。
* 系统总线：系统总线是指CPU，主存、I/O设备各大部件之间的信息传输线。这些部件通常安在主板或各个插板上，又称板级总线或板间总线。
  * 数据总线DBUS：ISA、EISA、VESA、PCI
  * 地址总线ABUS
    * 专门用来传送地址的
    * 总是单向三态的，地址只能从CPU传向外部存储器或I/O端口
    * 地址总线的位数决定了CPU可直接寻址的内存空间大小
  * 控制总线CBUS
    * 用来传送控制信号和时序信号
    * 控制信号中，有的是微处理器送往存储器和I/O接口电路的
    * 也有是其它部件反馈给CPU的，比如：中断申请信号、复位信号、总线请求信号、设备就绪信号等
* 通信总线


![Image](https://mmbiz.qpic.cn/mmbiz_png/OhzPdhKPG8QZqdnKnL9NNDkQwnb7req982CuzjkS7bTEZuTciaOnghK0a4v8yeDCIOkNOk52OQcfiasYPP27cOog/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

https://mp.weixin.qq.com/s?__biz=MzI1OTExNzkzNw==&mid=2650457527&idx=2&sn=953f947e20f93ef44042dc5cd02d0b7d&chksm=f273a3a9c5042abf6d9908884dcd51b0c8d97f16925c779751c91f671e24cff636507c60909e&scene=27

## Bus performance

    总线宽度
	总线频率
	总线带宽
	寻址能力
	负载能力
	是否支持并行传输

## 总线的组成

    总线的物理连接和逻辑连接
	结构
		单总线结构
		多总线结构

## 总线标准

    ISA总线
	EISA
	VESA局部总线
	PCI局部总线
	AGP
	PCI-Express
	RS-23C
	USB
	PCMCIA
	IDE
	SCSI
	SATA
