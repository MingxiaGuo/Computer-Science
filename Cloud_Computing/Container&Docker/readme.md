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