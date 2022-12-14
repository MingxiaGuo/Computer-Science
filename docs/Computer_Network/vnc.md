# VNC

## 简介

VNC，为一种使用RFB协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。VNC与操作系统无关，因此可跨平台使用，例如可用Windows连线到某Linux的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持JAVA的浏览器，也可使用。-- 维基百科

VNC: virtual network computing. This is a desktop sharing network that allows you to remotely control another computer.

VNC is a client-server GUI-based tool that allows you to connect via remote-desktop to your  Linux  host.

安装、使用
以下操作均为centos系统。

1. 个人认为tigervnc比较好用，示例为tigervnc

yum install tigervnc-server
2. 启用vnc，登陆账号执行命令，会反馈一个ID并提示设置vnc密码，ID默认从1开始。在vnc client端直接输入IP:ID即可。

vncserver
3. 配置防火墙，将对应的vnc端口开放

firewall-cmd --add-port=5901/tcp --permanent
firewall-cmd --reload
VNC server 监听的端口从 5900 开始，display:1 的监听 5901，display:2 监听 5902，以此类推。

 4. 检查是否有相关进程

ps aux | grep vnc
lsof -i:5901
5. vnc常用命令
列出当前账号的vnc信息：

vncserver -list
删除对应的ID：

vncserver -kill :1
设置开机自启动
1. 建立vnc服务

复制vncserver的服务。"@:2"指，该service启用vnc的2号端口，对应的系统port为5902。如果有多个账号，那么每个账号都需要建立一个service。

cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:2.service
修改复制后的文件，将username改为正确的账号名称

  [Unit]
  Description=Remote desktop service (VNC)
  After=syslog.target network.target

  [Service]
  Type=forking

  # Clean any existing files in /tmp/.X11-unix environment
  ExecStartPre=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
  ExecStart=/usr/bin/vncserver_wrapper username %i -geometry 1280x720 -depth 24
  ExecStop=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'

  [Install]
  WantedBy=multi-user.target
————————————————
版权声明：本文为CSDN博主「Saber Li」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_41351504/article/details/122036880