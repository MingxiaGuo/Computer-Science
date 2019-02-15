### 4.5.1 有关路由选择协议的几个基本概念

### 4.5.2 内部网关协议 RIP

### 4.5.3 内部网关协议 OSPF

### 4.5.4 外部网关协议 BGP

4.5.1、路由选择协议的基本概念
1、理想的路由算法
①.算法必须是正确的和完整的分组能到达目的主机；
②.算法在设计上应简单网络通讯量尽可能小；
③.算法应具有自适应性应能适应通信量和网络拓扑的变化；
④.算法应具有稳定性算法收敛性好；
⑤.算法应该是公平的除优先级高的用户外，算法对所有用户都是公平的；
⑥.算法应是最佳的所谓“最佳”只是对于某一特定要求较为合理 
路由选择的复杂性高是因为  ①.它是使网络中的所有结点共同协调工作的结果。
②.路由选择的环境往往不断变化。
依据算法能否随网络的通信量和拓扑自适应调整变化划分：
①.静态路由：非自适应路由选择，简单，适合小型网络
②.动态路由：自适应路由选择，复杂，开销大，适合大型网络
2、分层次的路由选择协议
因特网主要采用动态的分布式路由选择协议，由于以下两个原因，因特网采用分层次的路由选择协议。
①.因特网规模太大有几百万个路由器互连。如果让所有路由器知道所有网络怎么样到达，则这种路由表将非常大，处理起来太花时间。所有路由器之间交换信息所需带宽，就会使因特网通信链路饱和。
②.许多单位不愿意外界了解自己单位网路的布局细节，但同时希望连接Internet为此，因特网将整个互联网划分为许多小的自治系统，记为AS ；AS是单一技术管理下的一组路由器，而这些路由器使用一种AS内部的路由选择协议和共同的度量，以确定分组在该AS内的路由，同时还使用一种AS之间的路由选择协议，用以确定分组在AS之间的路由；即：一个AS内部可使用多种路由协议和度量，但对其它AS表现出的是一个单一的和一致的路由选择策略；
内部网关协议IGP (Interior Gateway Protocol) 一个AS内使用的路由选择协议，如RIP（Routing information Protocol路由信息协议）、OSPF（Open Shortest Path First开放式最短路径优先）等；
外部网关协议EGP (External Gateway Protocol) 不同自治系统之间使用的路由选择协议，如BGP（Border Gateway Protocol,边界网关协议）等；
 
对于大的AS，还可将所有网络再划分成区域网和主干网。
4.5.2、内部网关协议之一路由信息协议（RIP）
1、RIP的工作原理：
⑴、分布式路由选择协议就是每一个路由器都要不断地和其它路由器交换信息，交换信息的三个要点：①.和哪些路由器交换信息；②.交换什么信息；③.什么时候交换信息；
⑵、RIP的距离概念从一个路由器到直连网络的距离定义为1（也可定义为0，不常用），从一路由器到非直连网络的距离定义为所经过的路由器数加1，从网络A经N个路由器到达网络B的距离为N+1；
RIP协议的距离也称为跳数，RIP允许一条路径最多只能包含15个路由器。因此距离为16即表示不可达。故RIP只适用于小型互联网。 
⑶、RIP的工作原理简述最大的优点就是简单；
RIP是一种分布式距离向量路由选择协议，RIP协议要求网络中每一个路由器都要维护从它自己到每一个目标网络的距离记录，形成距离向量，距离向量的集合称之为“路由表”（路由表的最主要信息：目的网络、最短距离、下一跳）；
路由器开始工作时，只知道自己直连的网络距离。通过与相邻路由器的不断交换信息，最终都会知道到达本AS中任何一个网络的最短距离和下一跳路由器地址。
RIP选择一条具有最短距离的路由，且不能在两个网络之间同时使用多条路由。
⑵、RIP协议的三个要点：
①.仅和相邻路由器交换信息；
②.交换的信息是当前路由器所知道的全部信息，即路由表；
③.按固定时间间隔交换信息，例如30秒一次；
2、距离向量算法：
对每一个相邻路由器发过来的RIP报文，进行以下步骤： 
⑴、对地址X的相邻路由器发过来的RIP报文，先修改此报文中所有项目把下一跳字段中地址都改为X，并把所有距离字段值加1；
⑵、针对修改后的RIP报文中每一表项进行以下操作
若：原来的路由表中没有目的网络N，则把该项目添加到路由表中；
否则：查看原表项的下一跳路由地址是否为X：
若：下一跳是X，则把收到的表项替换原表项（取用最新消息）；
否则：比较距离大小：
若收到的表项距离小于原表项的距离，则更新，
否则什么也不做；
⑶、若3分钟还没收到相邻路由器更新的路由表，则视该路由器不可达，把以此路由器为下一跳的表项距离置16； 
⑷、返回；
【例题4.14】已知路由器R1，有表Ra所示的路由表。现收到相邻路由器R2发来的更新信息如表Rb所示，试写出R1更新后的路由表
表Ra	表Rb	结果R1a
目的网络	下一跳	距离	目的网络	下一跳	距离	目的网络	下一跳	距离
Net2	R4	3	Net1	R1	3	Net1	R4	4
Net3	R5	4	Net2	R2	4	Net2	R4	5
…	…	…	Net3	直接交付	1	Net3	R4	2
…	…	…	…	…	…	…	…	…
RIP协议让一个自治系统中的所有路由器都和自己相邻路由器定期交换路由信息，并不断更新其路由表，使得从每一个路由器到每一目的网络的路由都最短
3、RIP协议报文格式：
RIP2较RIP1协议本身并无多大变化，但性能上有改进；RIP2使用运输层的用数据报UDP进行传送。
 
命令字段指出报文的意义，比如：1表示请求路由信息，2表示对请求路由信息的响应或更新报文；
必为0字段为凑足4字节；
地址族标记（地址类别）字段标示所用的地址协议，比如:2表示IP地址
路由标记字段填入自治系统号ASN；其后便是路由表项（如下所示）
表项头部信息（4B）	目的网络（8B）	下一跳（4B）	距离（4B）
地址族标记(2B)	路由标记(2B)	IP地址	子网掩码	下一跳路由器地址	到此网络的距离
2	65535	192.168.6.3	255.255.255.0	168.62.3.1	3
…	…	…	…	…	…
RIP2报文中的路由部分由若干条路由信息组成，每一条路由信息长20B，最多路由信息不超过25条，RIP报文的最大长度=4+20*25=504B，一个RIP报文不够可再用一个或多个RIP报文；
RIP2还具有简单鉴别功能。若使用该功能，则将原来的第一个路由的20字节用作鉴别，此时地址族标识符全置1，路由标记写入鉴别类型，剩下16B鉴别数据。
4、RIP 协议的优缺点 
⑴、最大的优点实现简单，开销较小。 
⑵、缺点之一好消息传播快，坏消息传播慢（典型特点），即：当网络出现故障时，要经过比较长的时间才能将此信息传送到所有的路由器；
⑶、缺点之二RIP 限制了网络的规模：可使用的最大距离为 15（16 表示不可达）
⑷、缺点之三网络规模大，开销就大：路由器之间交换的信息是完整路由表；
【例题4.14】好消息传播快，坏消息传播慢的实例分析：
下图说明：	 表示达到网络1的距离为16，直接到达；
 表示达到网络1的距离为3，下一跳为R2；

 
 
4.5.3、内部网关协议之二开放式最短路径优先（OSPF）
1、OSPF协议的特点：
事实上，所有自治系统内部使用的路由选择协议都是要寻找一条最短的路径；
OSPF最主要的特征就是使用分布式链路状态路由选择协议，其特点是 
①.使用洪泛法向本自治系统中的所有路由器发信息即：每个路由器向所有相邻路由器发送信息，而每一个相邻路由器又将此信息发送给与他所有相邻路由器（除刚发来信息的路由器）。
②.发送的信息就是与相路由器相邻的所有路由器的链路状态。
链路状态就是说明本路由器和哪些路由器相邻，以及该链路的“度量”或者说“代价“（表示费用、距离、时延带宽等等）。
③.只有链路状态发生变化时，路由器才对外用洪泛法发送此信息。
2、OSPF协议的原理：
所有路由器通过洪泛法发送链路状态信息，最终都能建立一个链路状态数据库（数据库实质上就是全网络拓扑结构图），每个路由器根据链路状态数据库中的数据，利用一定的算法（比如Dijkstra算法）构建一个到达每个网络的单源最短路径树，最后构造路由表； 
说明 	⑴、OSPF的链路状态数据库更新较快，收效也快。  
⑵、为使OSPF能适用于大规模网络，OSPF将一个AS划分成若干个更小范围，称作“域”。每一个域都有一个32位的区域标识符。一个区域不能太大，最好不超过200个路由器。  
划分区域的好处就是将洪泛法范围局限于一个区域内，而不是整个AS，这样可减少整个网络通信量。因而每个区域内的路由器仅知道本区域内完整网络拓扑。
⑶、为使每一区域能与本AS内其他区域通信，OSPF使用层次结构的区域划分。上层区域叫主干区域，标识符是0.0.0.0，主干区域的作用是用来联通其它在下层的区域。每个区域至少一个区域边界路由器。主干区域中的路由器叫主干路由器。主干路由器中还要有个路由器专门和其它AS交换路由信息，这样的路由器称作自治系统边界路由器。
 
3、OSPF的分组格式：
OSPF直接用IP数据报传送，不用UDP，OSPF数据报很短，可减少通信量，不必分片。  
 
⑴、OSPF的分组结构
①.版本当前版本号为2；
②.类型 5种类型中的一种；
③.分组长度包括OSPF首部在内的分组长度，以字节为单位；
④.区域标识符分组所属区域的标识符；
⑤.路由器标识符发送该分组的路由器接口的IP地址；
⑥.检验和检验分组中错；
⑦.鉴别类型 1口令，0不用；
⑧.鉴别鉴别类型为0时填入0，为1时填入8字符号令；
⑵、OSPF的五种分组类型：	
①.问候分组发现和维持邻站的可达性；
②.数据库描述分组向邻站给出自己链路状态数据库中所有链路状态项目的摘要信息；
③.链路状态请求分组请求对方发送某些链路状态项目的详细信息；
④.链路状态更新分组用洪泛法对全网更新链路状态；
⑤.链路状态确认分组对链路更新分组的确认；
相邻路由器每10秒交换一次问候分组，若40秒没有收到邻站问候分组，则认为邻站不可达，修改链路状态数据库，重新计算路由表。当路由器刚开始工作时，通过问候分组知晓邻站；
OSPF还规定每隔一段时间，如30分钟更新一次数据库
⑶、OSPF的基本操作：
 
4.5.4、外部网关协议 BGP（Border Gateway Protocol）边界网关协议
⑴、外部网关协议和内部网关协议的区别：
BGP是不同于AS的路由器之间交换路由信息的协议，内部网关协议主要是设法使数据报在一个AS中尽可能有效的从源站传送到目的站，在AS内部不需要考虑其他方面策略。然而BGP使用的环境却不同，主要原因是： 
①.因特网规模太大，AS之间路由选择困难； 
②.AS之间路由选择必须考虑有关策略，因此路由选择协议应当允许使用多种路由选择策略，使这些策略是为了找出“较好的路径”，而不是最佳路径； 
⑵、BGP采用了路径向量路由选择协议：
配置BGP时，每一个AS的管理员要选择至少一个路由器作为该AS的“BGP发言人”。BGP发言人往往就是BGP边界路由器，但也可以不是。
①.BGP发言人要交换路由信息，要先建立TCP连接，然后在此连接上交换BGP会话。每一个BGP发言人除了必须运行BGP协议外，还必须运行其所在AS使用的内部网关协议；
   ②.BGP所交换的网络可达性信息就是要到达某个网络所要经过的一系列AS。各BGP发言人根据采用的策略从收到的路由信息中找出到达各AS的较好路由；
   ③.BGP路由表结构（目的网络前缀、下一跳路由、到达该目的网络所经过的AS序列）。因为BGP发言人收到其他BGP发言人发来的路径通知，要检查自己是否在路径序列中，如果在则不采用这个路径序列，以避免兜圈子。 
   ④.BGP邻站刚开始工作时交换整个BGP路由表。以后只需在发生变化时更新有变化的部分，以减少路由器处理开销及带宽
⑵、四种BGP报文：
①.OPEN（打开）报文与相邻BGP发言人建立关系，初始化通信；
②.UPDATE（更新）报文用来通告某一路由信息以及要撤销的多条路由；
③.KEEPALIVE（保活）报文周期性证实邻站连通性；
④.NOTIFICATION（通知）报文用来发送检测到的差错；
4.5.5、路由器的构成
路由器结构可划分为两个部分：路由选择部分+分组转发部分
⑴、路由部分也称控制部分，核心部件是路由选择处理机。它是根据所选定的路由协议构造出路由表。
⑵、分组转发部分由三个部分组成：交换结构、一组输入端口、一组输出端口。
交换结构根据转发表对分组进行处理
 
⑶、转发表和路由表的区别路由表根据网络拓扑计算，转发表则由路由表得到。转发表每行必须括到目的网络的输出端口及某些MAC信息，以后不加区分。 
总结	①.为什么既要MAC地址又要IP地址？
②.什么是网关？

