# Ceph
https://docs.ceph.com/en/quincy/

CEPH is a free and open-source software defined storage system designed to allow block, file and object storage from a unified system.

Ceph is software defined storage, a form of storage virtualization to separate the storage hardware from the software that manages the storage infra structure.

## Ceph Arch
https://docs.ceph.com/en/quincy/architecture/
### 基本结构

![](image/ceph.png)

* ***RADOS**:  Reliable Autonomous Distributed Object Store. Base layer that stores all the data. Its software based, self-healing, intelligent and lightweight. Ceph的底层是**RADOS**，RADOS本身也是分布式存储系统，Ceph所有的存储功能都是基于RADOS实现的。RADOS采用C++开发，所提供的原生Librados API包括C和C++两种。
* **LIBRADOS**: Client library that allows apps to access RADOS (supports C++, Java, Python, Ruby). Ceph的上层应用调用本机上的librados API，再由后者通过socket与RADOS集群中的其他节点通信并完成各种操作。
* **RADOSGW**: Rados Gateway for object store.  A bucket-based REST gateway, compatible with Amazon S3 and Swift . RADOS GateWay、RBD其作用是在librados库的基础上提供抽象层次更高、更便于应用或客户端使用的上层接口。其中RADOS GW是一个提供与Amazon S3和Swift兼容的RESTful API的gateway，以供相应的对象存储应用开发使用。
* **RBD**: Rados Block Device. Reliable fully distributed Block device with Cloud Platform Integration(a linux kernel client and a QEMU/KVM driver). RBD则提供了一个标准的块设备接口，常用于在虚拟化的场景下为虚拟机创建volume。目前，RedHat已经将RBD驱动集成在KVM/QEMU中，以提供虚拟机访问性能。这两种方式目前在云计算中应用的比较多。
* **CEPHFS**: A POSIX-compliant distributed file system, with a linux kernel client and support for FUSE. CephFS则提供了POSIX接口，用户可直接通过客户端挂载使用。它是内核态的程序，所有无需调用用户空间的librados库。它通过内核中的net模块来与RADOS进行交互。



With recent versions of Ceph, native support for iSCSI have been added to expose block storage to non-native clients like VMWare/ Windows.

### Ceph storage cluster
![](https://pic1.zhimg.com/80/v2-0d79db0bc30af7216d14a63f43f353e0_1440w.webp)
A Ceph storage cluster consists of multiple types of daemons:
* Monitor: 监控整个集群的状态，维护集群的cluster MAP二进制表，保证集群数据的一致性。ClusterMAP描述了对象块存储的物理位置，以及一个将设备聚合到物理位置的桶列表。
* OSD: Ceph OSD(Object Storage Devices) Daemon, 用于集群中所有数据与对象的存储。处理集群数据的复制、恢复、回填、再均衡。并向其他osd守护进程发送心跳，然后向Mon提供一些监控信息。当Ceph存储集群设定的数据有两个副本时（一共存两份），则至少需要两个OSD守护进程，即两个OSD节点，集群才能到达active+clean状态。
* MDS:  Ceph Metadata Server (可选). 为Ceph文件系统提供元数据计算、缓存与同步。在Ceph中，元数据也是存储在osd节点中的，mds类似于元数据的代理缓存服务器。MDS进程并不是必须的进程，只有需要使用CephFS时，才需要配置MDS节点。

A Ceph OSD Daemon checks its own state and the state of other OSDs and reports back to monitors.

A Ceph Manager acts as an endpoint for monitoring, orchestration, and plug-in modules.

A Ceph Metadata Server (MDS) manages file metadata when CephFS is used to provide file services.