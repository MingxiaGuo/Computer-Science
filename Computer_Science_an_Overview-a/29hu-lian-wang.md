IP - 互联网协议 - Internet Protocol
UDP - 用户数据包协议 - User Datagram Protocol
校验和 - Checksum
TCP - 传输控制协议 - Transmission Control Protocol
DNS - 域名系统 - Domain Name System
OSI - 开放式互联通信参考模型 - Open System Interconnection


互联网由无数互联设备组成，而且日益增多。计算机为获取这些视频，首先要连到局域网，也叫LAN，家里wifi路由器连着的所以设备，组成了局域网。局域网再连到广域网，广域网也叫WAN。WAN的路由器一般属于你的"互联网服务提供商，ISP"。广域网里，先连到一个区域性路由器，这路由器可能覆盖一个街区，然后连到一个更大的WAN，可能覆盖整个城市。可能再跳几次，但最终会到达互联网主干。互联网主干由一群超大型、带宽超高路由器组成。

为从youtube获取视频，数据包(packet)要先到互联网主干，沿着主干到达有对应视频文件的youtube服务器。数据包从你的计算机条道YouTube服务器，可能要跳10次，先跳4次到主干网，2次穿过主干，主干出来可能再跳4次，然后到youtube服务器。如果使用windows，Mac OS 或linux系统，可以使用traceroute来看跳了几次。

在“印第安纳波利斯”的Chad&Stacy Emigholz工作室访问加州的DFTBA服务器经历了11次中转。

