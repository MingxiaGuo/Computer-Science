# 1. Physical Layer

物理层主要目的：在传输媒体上透明传输比特流；物理层不是指具体的传输媒体 

物理层的主要任务：确定与传输媒体的接口的一些特性：

- **机械特性** 指明接口所用接线器的形状和尺寸、引线数目和排列、固定和锁定装置等等。

- **电气特性** 指明在接口电缆的各条线上出现的电压的范围。

- **功能特性** 指明某条线上出现的某一电平的电压表示何种意义。

- **过程特性** 指明对于不同功能的各种可能事件的出现顺序。

物理层L1：在网卡中实现，传送比特

* **传输媒体**：决定电信号0和1的传输方式，物理介质不同决定了电信号的传输带宽，速率，传输距离以及抗干扰性
  * 有线(网线)：双绞线，同轴电缆，光纤；
  * 无线：无线电波，微波，红外线，光波；
* **设备**：集线器hub，中继器，调制解调器, 
  * 集线器：这种设备有多个口，可以将宿舍里的多台电脑连接起来。但是，和交换机不同，集线器没有大脑，它完全在物理层工作。它会将自己收到的每一个字节，都复制到其他端口上去。这是第一层物理层联通的方案。Hub采用的是广播方式。工作在半双工模式，即可能同时发送和接收数据，会将数据包广播到所有集线 器端口，适合用于抓包。
* **传输单元**：比特流；

数据在计算机中多采用并行传输，在通信线路上，一般都是串行传输，主要出于经济上考虑； 

物理层的PDU(协议数据单元)由专门的串行信号模式组成，这些模式对应于数据链路层的帧的位模式。

用集线器和网线连接多个电脑，配置IP，子网掩码，默认网关可以组成一个最小的**局域网**，也即**LAN。**可以玩联机局域网游戏啦！

---

Hub采用 的是广播方式，如果每一台电脑发出的包，宿舍的每个电脑都能收到，那就麻烦了。这就需要解决几个问题：

1. 这个包是发给谁的？谁应该接收？
2. 大家都在发，会不会产生混乱？有没有谁先发、谁后发的规则？
3. 如果发送的时候出现了错误，怎么办？

这几个问题，都是**第二层，数据链路层**，也即MAC层要解决的问题




