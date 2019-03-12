
### 4.4.1 ICMP 报文的种类

### 4.4.2 ICMP 的应用举例

## 

4.4.1、ICMP（Internet Control Message Protocol）的简介
1、ICMP的作用  ⑴、更有效地转发IP数据报；  ⑵、提高成功交付的机会；
2、ICMP的特点 
⑴、ICMP是网络层协议它的报文不是直接传送给数据链路层，而是要封装成IP数据报后传送给数据链路层，目的是解决IP协议中可能出现的不可靠问题。
⑵、ICMP差错报告采用“路由器—源主机”模式即一旦路由器发现数据报传输错误，将通知源主机，通知报文独立选路。引入控制报文后，该模式被打破。
3、ICMP报文的格式 
 
4.4.2、ICMP报文的种类 ①.ICMP差错报告报文、②.查询报文；
1、ICMP差错报告报文
⑴、ICMP的5种差错报告报文 
①.终点不可达报文当路由器或者主机不能交付数据报时，就向源点发送终点不可达报文。
②.源点抑制报文当路由器或主机由于阻塞而丢弃数据时，就向源点发送源点抑制报文，使源点减慢数据发送速率。
③.超时报文当路由器收到生存时间为零的数据报时，除丢弃该数据报时，还要向源点发送时间超过报文。当终点在预先规定的时间内不能收到数据报全部数据报片时，就将已收到的数据报片丢弃，并向源点发送超时数据报文。
④.参数问题报文当路由器或者目的主机收到的数据报首部有字段值不正确时，丢弃该数据报，并向源点发送参数问题报文。
⑤.改变路由（重定向）报文路由器把改变路由报文发送给主机，通知主机下次将数据报发送给别的路由器。
⑵、ICMP差错报告报文的形成方法  所有ICMP首部包括类型、代码与检验和三部分共4个字节的信息字段。ICMP差错报文的数据字段格式相同，由收到的需要差错报告的数据报首部及其数据部分前8个字节组成。
 
⑶、不应发送ICMP差错报文的几种情况：
①.对ICMP差错报告报文不再发送ICMP差错报告报文；
②.对第一分片以后的所有数据报分片不发送ICMP差错报告报文；
③.对多播地址的数据报都不发送ICMP差错报告报文；
④.对具有特殊地址（如127.0.0.0或0.0.0.0）的数据报不发送ICMP差错报文；
2、ICMP的2种查询报文  
⑴、回送请求和回答报文ICMP回送请求报文是主机或者路由器向一个特定的目的主机发出的询问。收到此报文的主机必须给源主机或者路由器发送ICMP回答报文，目的是测试目的站是否可达以及了解其有关状态。
⑵、时间戳（chuō）请求与回答报文ICMP时间戳请求报文是请某个主机或者路由器回答当前日期和时间，目的是进行时钟同步和测量时间 
4.4.3、ICMP应用举例
【例题4.12】PING程序 使用ICMP回送请求与回送回答报文测试主机之间的连通性；
 
【例题4.13】traceroute程序 源主机依次发送TTL为1，2，…，的数据报，直到有一个数据报刚刚到达目的主机时，TTL为1，主机不转发数据报，TTL值也不减1。因为数据报封装着无法交付的UDP用户数据报，故目的主机向源主机发送目的不可达的差错控制报文。这其间的每个路由器都因数据报TTL为0发送超时控制报文。对于每个TTL值源主机发送三次同样数据报。
 

