arch: 
block:

crypto:
drivers
fs: 文件系统管理
init:
kernel：内核核心代码


> Documentation, README ---- 帮助、说明文档。
> 
> arch// ---- 体系结构相关的代码，例如arm, x86等等。 
> 	- arch//mach- ---- 具体的machine/board相关的代码。  
> 	- arch//boot/dts ---- 设备树（Device Tree）文件。  
> 	- arch//include/asm ---- 体系结构相关的头文件。  
> 	- arch//mach- ---- 具体的machine/board相关的代码。  
> block/ ---- 提供块设备的层次。  
> certs:
> crypto/ ----- 加密、解密相关的库函数。  
> drivers/ ---- 设备驱动（在Linux kernel 3.10中，设备驱动占了49.4的代码量）。  
> fs/ ---- VFS子系统（3.4小节）。  
> 
> include/ ---- 内核头文件，需要提供给外部模块（例如用户空间代码）使用。  
>  init/ ---- Linux系统启动初始化相关的代码。  
>  ipc/ ---- IPC（进程间通信）子系统。  
> kernel/ ---- Linux内核的核心代码，包含了3.2小节所描述的进程调度子系统，以及和进程调度相关的模块。  
> lib/ ---- 实现需要在内核中使用的库函数，例如CRC、FIFO、list、MD5等。  
> mm/ ---- 内存管理子系统（3.3小节）。  
> net/ ---- 不包括网络设备驱动的网络子系统（3.5小节）。  
>
>  
> 
> 
> 
>samples/ ---- 一些示例代码。  
> security/ ---- 提供安全特性（SELinux）。  
> sound/ ---- 音频相关的驱动及子系统，可以看作“音频子系统”。  
> tools/ ---- 一些常用工具，如性能剖析、自测试等。  
> usr/ ---- 用于生成initramfs的代码。  
> virt/ ---- 提供虚拟机技术（KVM等）的支持。  
> 
> firmware/ ---- 保存用于驱动第三方设备的固件。  
> 
> Kconfig, Kbuild, Makefile, scripts/ ---- 用于内核编译的配置文件、脚本等。  
> COPYING ---- 版权声明。  
> MAINTAINERS ----维护者名单。  
> CREDITS ---- Linux主要的贡献者名单。  
> REPORTING-BUGS ---- Bug上报的指南。  
> 