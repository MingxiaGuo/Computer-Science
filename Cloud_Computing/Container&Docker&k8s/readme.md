
https://yeasy.gitbooks.io/docker_practice/

Docker简介
1. 什么是Docker
2. Dokcer的优势
3. Dokcer基本概念






容器技术是近几年开源社区和云计算的新贵。
容器引擎，https://docs.docker.com/

What is Container?
* A group of processes run in isolaAon
    * Similar to VMs but managed at the **process level**
    * All processes MUST be able to run on the **shared kernel**
* Each container has its own set of "namespaces" (isolated view)
    * PID - process IDs
    * USER - user and group IDs
    * UTS - hostname and domain name
    * NS - mount points
    * NET - Network devices, stacks, ports
    * IPC - inter-process communications, message queues 
    * cgroups - controls limits and monitoring of resources
* Docker gives it its own root filesystem

VM vs Container

Why Containers?
* Fast startup Ame - only takes milliseconds to: 
    * Create a new directory
    * Lay-down the container's filesystem
    * Setup the networks, mounts, ...
    * Start the process
* Better resource uAlizaAon
    * Can fit far more containers than VMs into a host

What is Docker?
* Docker is tooling to manage containers
    * Docker is not a technology, it’s a tool or plaQorm
    * Simplified exisAng technology to enable it for the masses
    * Containers are not new, Docker just made them easy to use
* Docker creates and manages the lifecycle of containers
    * Setup filesystem
    * CRUD container 
        * Setup networks
        * Setup volumes / mounts
        * Create: start new process telling OS to run it in isolaAon

Docker images
* Tar file containing a container's filesystem + metadata 
* For sharing and redistribuAon
    * Global/public registry for sharing: DockerHub 
* Similar, in concept, to a VM image


Our First Container
$ docker run ubuntu echo Hello World
Hello World
•  What happened?
•  Docker created a directory with a "ubuntu" filesystem (image) •  Docker created a new set of namespaces
•  Ran a new process: echo Hello World
•  Using those namespaces to isolate it from other processes
•  Using that new directory as the "root" of the filesystem (chroot)
•  That's it!
•  NoAce as a user I never installed "ubuntu"
•  Run it again - noAce how quickly it ran

ssh-ing into a container - fake it...
$ docker run -ti ubuntu bash
root@62deec4411da:/# pwd
/
•  Now the process is "bash" instead of "echo"
•  But it’s sAll just a process
•  Look around, mess around, it’s totally isolated •  rm /etc/passwd – no worries!
•  MAKE SURE YOU'RE IN A CONTAINER!

A look under the covers
$ docker run ubuntu ps -ef
UID         PID   PPID  C STIME TTY
root          1      0  0 14:33 ?
•  Things to noAce with these examples
•  Each container only sees its own process(es) •  Each container only sees its own filesystem •  Running as "root"
•  Running as PID 1
    TIME CMD
00:00:00 ps -ef


Docker 使用 Google 公司推出的 Go 语言 进行开发实现，基于 Linux 内核的 cgroup，namespace，以及 AUFS 类的 Union FS 等技术，对进程进行封装隔离，属于 操作系统层面的虚拟化技术。由于隔离的进程独立于宿主和其它的隔离的进程，因此也称其为容器。最初实现是基于 LXC，从 0.7 版本以后开始去除 LXC，转而使用自行开发的 libcontainer，从 1.11 开始，则进一步演进为使用 runC 和 containerd。

Docker 在容器的基础上，进行了进一步的封装，从文件系统、网络互联到进程隔离等等，极大的简化了容器的创建和维护。使得 Docker 技术比虚拟机技术更为轻便、快捷。

为什么使用Docker？
1. 更

传统虚拟机技术是虚拟出一套硬件后，在其上运行一个完整操作系统，在该系统上再运行所需应用进程；而容器内的应用进程直接运行于宿主的内核，容器内没有自己的内核，而且也没有进行硬件虚拟。因此容器要比传统虚拟机更为轻便。