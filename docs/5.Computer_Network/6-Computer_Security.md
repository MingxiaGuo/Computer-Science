Computer Security / Cyber Security / Digital Security / IT Security



## Aspects of Network Security:

Privacy

Encryption/Decryption

Data Excryption Standard



Message Integrity

End-point authentication

Non-Repudiation


## Vulnerabilities

A vulnerability is a weakness in design, implementation, operation, or internal control of a computer or system. Most of the vulnerabilities that have been discovered are documented in the [Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures "Common Vulnerabilities and Exposures") (CVE) database

Vulnerabilities scanner: 
- Nessus: 个人免费，商业收费。web网站形式的漏洞扫描工具。发现web网站，web服务器，服务器操作系统等的漏洞

# Basic Network Attacks/Threats

计算机网络面临的安全性威胁：

* 被动攻击：**被动攻击**的攻击者只是观察和分析某一个协议数据单元 PDU 而不干扰信息流。
	* 截获 interception：攻击者从网络上窃听他人的通信内容。这种被动攻击又叫流量分析
* 主动攻击：
	- 中断 interruption：攻击者有意中断他人在网络上的通信
	- 篡改 modification：攻击者故意篡改网络上传送的报文
	- 伪造 fabrication：攻击者伪造信息在网络上传送
	- 恶意程序 rogue program 攻击：
		- 计算机病毒：狭义的计算机病毒是一种会传染其他程序的程序，传染通过修改其他程序来把自身或其变种复制进去完成
		- 计算机蠕虫：一种通过网络的通信功能将自身从一个结点发送到另一个结点并自动启动运行的程序
		- 特洛伊木马：一种程序，它执行的功能超出所声称的功能。
		- 逻辑炸弹：一种当运行环境满足某种特定条件时执行其他特殊功能的程序。

**主动攻击**指攻击者对某个连接中通过的 PDU 进行各种处理，如：

- 更改报文流
- 拒绝报文服务
- 伪造连接初始化

**计算机网络通信安全的目标**

(1) 防止析出报文内容；

(2) 防止通信量分析；

(3) 检测更改报文流；

(4) 检测拒绝报文服务；

(5) 检测伪造初始化连接。

对付被动攻击可采用各种数据加密技术，对付主动攻击，需将加密技术与适当鉴别技术相结合。





计算机网络安全的内容，三个都用到密码技术：

1. 保密性：密码机制
2. 安全协议设计
3. 访问控制 Access Control





密码机制：

对成密钥

公钥密码




# 因特网中的安全协议

## 网络层安全协议

IPsec

AH

ESP

## 运输层安全协议

## 应用层安全协议

# 防火墙

防火墙是一种特殊编程的路由器，安装在一个网点或网络的其余部分之间。



attacks