# Kubernetes安装部署

## 准备
 
## 步骤
 1. 安装Etcd
 2. 安装kube-apiserver
 3. 安装kube-controller-manager服务
 4. kube-scheduler服务
 5. kubelet服务
 6. kube-proxy服务
 7. kube-dns
 8. kube-dashboard


## 1.安装Etcd
etcd服务作为kubernetes集群的主数据库，在安装kubernetes各服务之前需要首先安装和启动。


从Github官网下载etcd发布的二进制文件，将etcd和etcdctl文件复制到/usr/bin目录。
设置systemd服务文件/lib/systemd/system/etcd.service:
	
	[Unit]
	Description=Etcd Serverd
	After=network.target

	[Service]
	Type=notify
	WorkingDirectory=/var/lib/etcd
	EnvironmentFile=-/etc/etcd/etcd.conf
	ExecStart=/usr/local/bin/etcd
	Restart=on-failure
	RestartSec=10s
	LimitNOFILE=40000

	[Install]
	WantedBy=multi-user.target

	
## 2.安装kube-apiserver
## 3.安装kube-controller-manager服务
## 4.kube-scheduler服务
## 5.kubelet服务
## 6.kube-proxy服务
## 7.kube-dns
## 8.kube-dashboard