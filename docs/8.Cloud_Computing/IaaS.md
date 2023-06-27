基础设施资源，主要包括三个方面：计算、存储、网络。说通俗点，就是CPU，硬盘，网卡。
Openstack就是一个云计算的底层操作系统，一套软件，一套IaaS软件。
## 1. Compute
计算的最小单元叫“实例(instance)“, 三种计算实例：裸机，虚机，容器.
### 裸机
### 虚拟机
底层实现：qemu + kvm；vmware的esxi
### 容器
## 2. Storage
存储后端：Ceph
存储模块类型：
* 块：设备资源叫做“卷volume
* 文件
* 对象
## 3.Network
LBaaS 服务
DNS服务
防火墙服务
VPN 服务

在网络方面我更喜欢 openstack 的网络设计，几乎是参照标准模型来实现的，使用 network 来实现二次隔离，subnet 和 router 提供三层功能，在配合 vpnaas，fwaas，octavia 使永和很容易在 openstack 云上打造一套专属的数据中心。