> [官方文档 https://docs.nginx.com](https://docs.nginx.com)
> 
> [官方文档 https://nginx.org/en/docs/](https://nginx.org/en/docs/)

## 介绍
Nginx (engine x) 是一个高性能的Web[服务器](https://cloud.tencent.com/product/cvm/?from_column=20065&from=20065)和反向代理服务器，也是一个IMAP/POP3/SMTP服务器

## 架构

**框架模型：**

![](https://ask.qcloudimg.com/http-save/3421842/2btcjhgdri.jpeg)

- master进程
	- 监视工作进程的状态
	- 当工作进程死掉后重启一个新的
	- 处理信号和通知工作进程
- worker进程
	- 处理客户端请求
	- 从主进程处获得信号做相应的事情
- cache loader进程
	- 加载缓存索引文件信息，然后退出
- cache manager进程
	- 管理磁盘的缓存大小，超过预定值大小后最少使用数据将被删除

**框架模型流程：**

![](https://ask.qcloudimg.com/http-save/3421842/gclrhcm0lq.jpeg)

**框架模型流程：**

![](https://ask.qcloudimg.com/http-save/3421842/3vm93r7olg.jpeg)

![](https://ask.qcloudimg.com/http-save/3421842/p0h9top5dx.jpeg)

**核心流程图：**

![](https://ask.qcloudimg.com/http-save/3421842/ew1ppajtyt.jpeg)

![](https://ask.qcloudimg.com/http-save/3421842/tcwbe5cb9j.jpeg)

**核心流程图：**

![](https://ask.qcloudimg.com/http-save/3421842/nsbrympoyp.jpeg)

![](https://ask.qcloudimg.com/http-save/3421842/wa62qxw1zd.jpeg)

**http请求流程：**

![](https://ask.qcloudimg.com/http-save/3421842/08v6bego60.jpeg)

![](https://ask.qcloudimg.com/http-save/3421842/sqf2kh7syi.jpeg)

**Upstream设计：**

- 访问第三方Server服务器
- 底层HTTP通信非常完善
- 异步非阻塞
- 上下游内存零拷贝，节省内存
- 支持自定义模块开发

![](https://ask.qcloudimg.com/http-save/3421842/fut27ddedg.jpeg)

**upstream流程：**

![](https://ask.qcloudimg.com/http-save/3421842/rcuv79xjem.jpeg)

![](https://ask.qcloudimg.com/http-save/3421842/diafdfxbcf.jpeg)

**4. Nginx定制化模块开发**

**Nginx的模块化设计特点：**

- 高度抽象的模块接口
- 模块接口非常简单，具有很高的灵活性
- 配置模块的设计
- 核心模块接口的简单化
- 多层次、多类别的模块设计

![](https://ask.qcloudimg.com/http-save/3421842/3oc3nxd5va.jpeg)

**核心模块：**

![](https://ask.qcloudimg.com/http-save/3421842/bh3fdxydj5.jpeg)

**handler模块：**

接受来自客户端的请求并构建响应头和响应体。

![](https://ask.qcloudimg.com/http-save/3421842/zv5guvwulw.jpeg)

**filter模块：**

过滤（filter）模块是过滤响应头和内容的模块，可以对回复的头和内容进行处理。它的处理时间在获取回复内容之后，向用户发送响应之前。

![](https://ask.qcloudimg.com/http-save/3421842/rjg01n7s0u.jpeg)

**upstream模块：**

使nginx跨越单机的限制，完成网络数据的接收、处理和转发，纯异步的访问后端服务。

![](https://ask.qcloudimg.com/http-save/3421842/6yzrrcsgk3.jpeg)

**load_balance：**

负载均衡模块，实现特定的算法，在众多的后端服务器中，选择一个服务器出来作为某个请求的转发服务器。

![](https://ask.qcloudimg.com/http-save/3421842/8yfqntqlb6.jpeg)

**ngx_lua模块：**

- 脚本语言
- 内存开销小
- 运行速度快
- 强大的 Lua 协程
- 非阻塞
- 业务逻辑以自然逻辑书写

![](https://ask.qcloudimg.com/http-save/3421842/9tlrpj97s0.jpeg)




## 反向代理(Reverse Proxy)

正向代理是 将所有的请求交给某个端口处理
反向代理是将 某个请求交给 代理服务器处理, 由其来确定使用哪一台服务器
```json
server {
    listen 80;
    server_name www.example.com example.com;

    location /app {
	    proxy_pass http://127.0.0.1:8080;
    }
    
    location / {
	    proxy_set_header Host $host;
	    proxy_set_header Accept-Encoding "";
	    proxy_pass http://localhost:3000;
	}
}
```


## 负载均衡(load balance)
```json

http {
    upstream backend {
        server backend1.example.com weight=5;
        server backend2.example.com;
        server 192.0.0.1 backup;
    }
}

server {
    location / {
        proxy_pass http://backend;
    }
}

```


## **Nginx应用场景**

**场景如下：**

- 静态文件服务器
- 反向代理，[负载均衡](https://cloud.tencent.com/product/clb?from_column=20065&from=20065)
- 安全防御
- 智能路由(企业级灰度测试、地图POI一键切流)
- 灰度发布
- 静态化
- 消息推送
- 图片实时压缩
- 防盗链


## **Nginx源码结构**

- 代码量大约11万行C代码
- 源代码目录结构
- core （主干和基础设置）
- event （事件驱动模型和不同的IO复用模块）
- http （HTTP服务器和模块）
- mail （邮件代理服务器和模块）
- os （操作系统相关的实现）
- misc （杂项）

## **Nginx特点**

- 反向代理，[负载均衡器](https://cloud.tencent.com/product/clb?from_column=20065&from=20065)
- 高可靠性、单master多worker模式
- 高可扩展性、高度模块化
- 非阻塞
- 事件驱动
- 低内存消耗
- 热部署

## 面试题
https://javabetter.cn/interview/nginx-40.html