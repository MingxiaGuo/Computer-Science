> [官方文档 https://docs.nginx.com](https://docs.nginx.com)
> 
> [官方文档 https://nginx.org/en/docs/](https://nginx.org/en/docs/)

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