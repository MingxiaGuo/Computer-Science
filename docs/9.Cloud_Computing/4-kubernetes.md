# Container Orchestration

Everyone’s container journey starts with one container. At first the growth is easy to handle, but soon you have many applications, many instances… And that is why we have Container orchestration.

![](image/Container_orchestration.png)

## 1 Container Orchestration Functionality

![](image/container_orchestration_2.png)

* Container Orchestration Functionality
  * Scheduling: Distributes containers across nodes
  * Cluster Management: Federates multiple hosts into one target
  * Service Discovery:
    * Knows where the containers are located
    * Distributes client requests across the containers
  * Provisoning
  * Monitoring
  * Configuration Management
  * Auto-scalling
  * Networking
  * load balancing
  * Policy
  * Replication: Ensures the right number of nodes and containers
  * Health management
  * Replaces unhealthy containers and nodes

特性：
scalable, reliable, stable, efficient, and performant.

## 2 Container ecosystem layers

![](image/container_ecosystem_layers.png)

## 3 **资源管理器**

* Apache mesos: 开源分布式资源管理框架
* Docker Swarm: docker 集群化方案
* K8s: from Borg. 轻量级，资源消耗小；开源；弹性伸缩；负载均衡(IPVS)
* Borg: 谷歌内部容器管理器
* Omega：


# [Kubernetes](https://kubernetes.io/)

- kubernetes - [Tutorials - Kuberneteshttps://kubernetes.io/docs/tutorials/](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=11&cad=rja&uact=8&ved=2ahUKEwjD9dHigubfAhWO1FkKHUMkA_kQFjAKegQIFBAB&url=https%3A%2F%2Fkubernetes.io%2Fdocs%2Ftutorials%2F&usg=AOvVaw10KC1WIqEEhUnwj_VnX0g6)
- Kubectl command: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands
- git repo: https://github.com/kubernetes/kubernetes
- client-go: https://github.com/kubernetes/client-go
- sample-controller: https://github.com/kubernetes/sample-controller

## 1 kubernetes overview

### 1.1 what is Kubernetes

谷歌开源的容器集群管理系统，是google多年大规模容器管理技术Brog的开源版本
一个集群管5000台机器

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) is an open source **container orchestration engine** for **automating deployment**, **scaling**, and **management of containerized applications(workloads and services)** based on Borg and Omega, that facilitates both declarative configuration and automation. The open source project is hosted by the Cloud Native Computing Foundation ([CNCF](https://www.cncf.io/about)).

The name Kubernetes originates from **Greek**, meaning **helmsman(舵手)** or **pilot(飞行员)**.

Kubernetes不仅仅支持Docker，还支持Rocket，这是另一种容器技术。

Kubernetes 为什么要用“舵手”来命名呢？大家可以看一下这张图：这是一艘载着一堆集装箱的轮船，轮船在大海上运着集装箱奔波，把集装箱送到它们该去的地方。我们之前其实介绍过一个概念叫做 container，container 这个英文单词也有另外的一个意思就是“集装箱”。Kubernetes 也就借着这个寓意，希望成为运送集装箱的一个轮船，来帮助我们管理这些集装箱，也就是管理这些容器。

<img src="./assets/轮船.png" style="zoom:30%;" />

why k8s： Going back in time: https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/#going-back-in-time

k8s是声明式系统

### 1.2 Kubernetes feature

* 基于容器的应用部署，维护和滚动升级
* Intelligent Scheduling: 把一个容器放到一个集群的某一个机器上，跨机器和跨地域集群调度
* Self-healing: 在一个集群中，经常会出现宿主机的问题或者说是 OS 的问题，导致容器本身的不可用，Kubernetes 会自动地对这些不可用的容器进行恢复. Kubernetes will **ALWAYS** try and steer the cluster to its desired state.
* Horizontal scaling: scale up and down dynamically 自动伸缩
* Service discovery & load balancing：负载均衡和服务发现
* Automated rollouts and rollbacks:
* Secret and configuration management
* 无状态服务和有状态服务
* 插件机制保证扩展性

实际上，使用Kubernetes只需一个[部署文件](https://github.com/kubernetes/kubernetes/blob/master/examples/guestbook/all-in-one/guestbook-all-in-one.yaml)，使用一条命令就可以部署多层容器（前端，后台等）的完整集群：kubectl是和Kubernetes API交互的命令行程序。现在介绍一些核心概念。

下面，我们希望以三个例子跟大家更切实地介绍一下 Kubernetes 的能力。
![](image/kubelet.png)

#### 集群管理

#### 服务发现

#### 1.2.1 资源调度

<img src="" style="zoom: 33%;" />
![](./assets/调度.png)
Kubernetes 可以把用户提交的容器放到 Kubernetes 管理的集群的某一台节点上去。Kubernetes 的调度器是执行这项能力的组件，它会观察正在被调度的这个容器的大小、规格。

比如说它所需要的 CPU以及它所需要的 memory，然后在集群中找一台相对比较空闲的机器来进行一次 placement，也就是一次放置的操作。在这个例子中，它可能会把红颜色的这个容器放置到第二个空闲的机器上，来完成一次调度的工作。

#### 1.2.2 自动修复

<img src="./assets/自动修复.png" style="zoom: 33%;" />

Kubernetes 有一个节点健康检查的功能，它会监测这个集群中所有的宿主机，当宿主机本身出现故障，或者软件出现故障的时候，这个节点健康检查会自动对它进行发现。

下面 Kubernetes 会把运行在这些失败节点上的容器进行自动迁移，迁移到一个正在健康运行的宿主机上，来完成集群内容器的一个自动恢复。

#### 1.2.3 水平伸缩

<img src="./assets/水平伸缩.png" style="zoom:50%;" />

Kubernetes 有业务负载检查的能力，它会监测业务上所承担的负载，如果这个业务本身的 CPU 利用率过高，或者响应时间过长，它可以对这个业务进行一次扩容。

比如说在下面的例子中，黄颜色的过度忙碌，Kubernetes 就可以把黄颜色负载从一份变为三份。接下来，它就可以通过负载均衡把原来打到第一个黄颜色上的负载平均分到三个黄颜色的负载上去，以此来提高响应的时间。

以上就是 Kubernetes 三个核心能力的简单介绍。

### 1.3. Kubernetes Strengths

* **Kubernetes has a clear governance model** managed by the Linux Foundation. Google is actively driving the product features and roadmap, while allowing the rest of the ecosystem to participate.
* **A growing and vibrant Kubernetes ecosystem** provides confidence to enterprises about its long-term viability.  IBM, Huawei, Intel, and Red Hat are some of the companies making prominent contributions to the project.
* **The commercial viability of Kubernetes makes it an interesting choice for vendors.**  We expect to see new offerings announced over the next several months.
* **Despite the expected growth in commercial distributions, Kubernetes avoids dependency and vendor lock-in** through active community participation and ecosystem support.
* **Kubernetes supports a wide range of deployment options.** Customers can choose between bare metal, virtualization, private, public, and hybrid cloud deployments. It enjoys a wide range of delivery models across on-premises and cloud-based services.
* **The design of Kubernetes is more operations-centric** than developer-orientated, which makes it the first choice of DevOps teams.

### 命令式与声明式

命令式系统关注“如何做”：命令式系统写出解决某个问题，完成某个任务或达到某个目标的明确步骤。此方法明确写出系统应该执行某些命令，并期待系统返回期望结果

声明式系统关注“做什么”，声明式系统指程序代码描述系统应该做什么而不是怎么做，仅限于描述达到什么目的 ，如何达到目的交给系统。直接声明：直接告诉你我需要什么。间接声明：不直接告诉你我的需求，会把需求放在特定的地方，请在方便时候拿出处理

幂等性：状态固定，每次我要你做事，请返回相同结果

面向对象：把一切抽象成对象。

### k8s 生态系统

![](image/k8s生态系统.png)

### k8s设计理念

![](image/k8s设计理念.png)
分层架构:

- 核心层: Kubernetes 最核心的功能，对外提供 API 构建高层的应用，对内提供插件式应用执行环境。
- 应用层: 部署(无状态应用、有状态应用、批处理任务、集群应用等)和路由(服务发现、DNS 解析等)。
- 管理层: 系统度量(如基础设施、容器和网络的度量)、自动化(如自动扩展、动态 Provision 等)、 策略管理(RBAC、Quota、PSP、NetworkPolicy 等)。
- 接口层: Kubectl 命令行工具、客户端 SDK 以及集群联邦。
- 生态系统: 在接口层之上的庞大容器集群管理调度的生态系统，可以划分为两个范畴:
  - Kubernetes 外部: 日志、监控、配置管理、CI、CD、Workflow、FaaS、OTS 应用、 ChatOps 等;
  - Kubernetes 内部: CRI、CNI、CVI、镜像仓库、Cloud Provider、集群自身的配置和管理等。

![](image/k8s分层架构.png)

**API 设计原则:**

- 所有 API 都应是声明式的
  - 相对于命令式操作，声明式操作对于重复操作的效果是稳定的，这对于容易出现数据丢失或重复的分布式环境来说是很重要的。
  - 声明式操作更易被用户使用，可以使系统向用户隐藏实现的细节，同时也保留了系统未来持续优化的可能性。
  - 此外，声明式的 API 还隐含了所有的 API 对象都是名词性质的，例如 Service、Volume 这些 API 都是名词，这些名词描述了用户所期望得到的一个目标对象。
- API 对象是彼此互补而且可组合的
  * 这实际上鼓励 API 对象尽量实现面向对象设计时的要求，即 `<mark>`“高内聚，松耦合”`</mark>`，对业务相关的概念有一个合适的分解，提高分解出来的对象的可重用性。

* 高层 API 以操作意图为基础设计

  - 如何能够设计好 API，跟如何能用面向对象的方法设计好应用系统有相通的地方，高层设计一定是从业务出发，而不是过早的从技术实现出发。
  - 因此，针对 Kubernetes 的高层 API 设计，一定是以 Kubernetes 的业务为基础出发，也就是以系统调度管理容器的操作意图为基础 设计。
* 低层API根据高层API的控制需要设计

  * 设计实现低层 API 的目的，是为了被高层 API 使用，考虑减少冗余、提高重用性的目的，低层 API的设计也要以需求为基础，要尽量抵抗受技术实现影响的诱惑。
* 尽量避免简单封装，不要有在外部API无法显式知道的内部隐藏的机制

  * 简单的封装，实际没有提供新的功能，反而增加了对所封装 API 的依赖性。
  * 例如 StatefulSet 和 ReplicaSet，本来就是两种 Pod 集合，那么 Kubernetes 就用不同 API 对象 来定义它们，而不会说只用同一个 ReplicaSet，内部通过特殊的算法再来区分这个 ReplicaSet 是 有状态的还是无状态。
* API操作复杂度与对象数量成正比

  * API 的操作复杂度不能超过 O(N)，否则系统就不具备水平伸缩性了。
* API对象状态不能依赖于网络连接状态

  * 由于众所周知，在分布式环境下，网络连接断开是经常发生的事情，因此要保证 API 对象状态能应对网络的不稳定，API 对象的状态就不能依赖于网络连接状态。
* 尽量避免让操作机制依赖于全局状态

  * 因为在分布式系统中要保证全局状态的同步是非常困难的。

Kubernetes 如何通过对象的组合完成业务描述:

<img src="/Users/gmx/Documents/workspace/note/Computer-Science/docs/Cloud_Computing/assets/对象组合.png" style="zoom:30%;" />

service按label组合pod

**架构设计原则:**

- 只有 APIServer 可以直接访问 etcd 存储，其他服务必须通过 Kubernetes API 来访问集群状态;
- 单节点故障不应该影响集群的状态;
- 在没有新请求的情况下，所有组件应该在故障恢复后继续执行上次最后收到的请求 (比如网络分区或服务重启等);
- 所有组件都应该在内存中保持所需要的状态，APIServer 将状态写入 etcd 存储，而其 他组件则通过 APIServer 更新并监听所有的变化; 不应该频繁去查api-server
- 优先使用事件监听而不是轮询。

**引导(Bootstrapping)原则:** kublet是k8s的初始化系统

* Self-hosting 是目标。
* 减少依赖，特别是稳态运行的依赖。
* 通过分层的原则管理依赖。
* 循环依赖问题的原则:

  - 同时还接受其他方式的数据输入(比如本地文件等)，这样在其他服务不可 用时还可以手动配置引导服务;
  - 状态应该是可恢复或可重新发现的;
  - 支持简单的启动临时实例来创建稳态运行所需要的状态，使用分布式锁或文件锁等来协调不同状态的切换(通常称为 pivoting 技术);
  - 自动重启异常退出的服务，比如副本或者进程管理器等。

### 1.4 Kubernetes Certified Service Providers(KCSP)

The KCSP program is a vetted tier of service providers who have deep experience helping enterprises successfully adopt Kubernetes. KCSP partners offer Kubernetes support, consulting, professional services and training for organizations embarking on their Kubernetes journey.

* KCSP is managed by the Cloud Native Computing Foundation
* IBM is a KCSP Partner

  * IBM Container Service is a managed k8s environment with built-in cluster security and isolation while leveraging services including Waston, IoT, Weather, etc.

## 2 K8s Cluster Architecture

### 2.1 Architecture Overview

![](image/k8s-arch.svg)

* **Cluster**: 集群是一组节点，这些节点可以是物理服务器或者虚拟机，之上安装了Kubernetes平台. A cluster is a set of resources, worker nodes, networks, and storage devices that keep apps highly available
* [Node](https://kubernetes.io/docs/concepts/architecture/nodes/): a node is a worker machine in k8s
	* master node
	* worker node
* [Pods](https://kubernetes.io/docs/concepts/workloads/pods/): A pod represents a set of running containers in your cluster. The worker node(s) host the Pods that are the components of the application workload
* The [Control Plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) manages the worker nodes and the Pods in the cluster. Control Plane=**Master node** that manages the cluster
  * Scheduling, replication & control
  * Multiple nodes for HA
* **Worker nodes**
  * Node where pods are run
  * Docker engine
  * kubelet agent accepts & executes commands from the master to manage pods
  * cAdvisor – Container Advisor provides resource usage and performance statistics
  * kube-proxy – routes inbound or ingress traffic

```sh
mguo@dal1-qz2-sr3-rk095-s04:~$ kubectl get pod -n kube-system
NAME                                             READY   STATUS    RESTARTS      AGE
coredns-7c88f46b5-9cnxj                          1/1     Running   0             38d
coredns-7c88f46b5-c7rnj                          1/1     Running   0             38d
coredns-7c88f46b5-lqrf4                          1/1     Running   0             38d
coredns-7c88f46b5-rfsjd                          1/1     Running   0             38d
etcd-backup-operator-5567446cd4-nnmbp            1/1     Running   0             99m
kube-apiserver-dal1-qz2-sr3-rk180-s18            1/1     Running   0             38d
kube-controller-manager-dal1-qz2-sr3-rk180-s18   1/1     Running   0             38d
kube-proxy-69sf6                                 1/1     Running   0             36d
kube-proxy-7hkvm                                 1/1     Running   0             38d
kube-proxy-99w2s                                 1/1     Running   0             3d21h
kube-proxy-bb5ct                                 1/1     Running   0             38d
kube-proxy-bp4sk                                 1/1     Running   0             17h
kube-scheduler-dal1-qz2-sr3-rk180-s18            1/1     Running   1 (38d ago)   38d
```

### 2.2 Control Plane Components

Kubernetes 的 **Master Node** 包含四个主要的组件：API Server、Controller manager、Scheduler 以及 etcd。Control Plane = Master Node

![](image/control-plane-components.png)

#### 2.2.1 API Server

**Kube-apiserver** 是 Kubernetes 最重要的核心组件之一，这是k8s控制平面唯一带有用户可访问API并使用JSON格式的清单文件(manifest files)。主要提供以下功能:

* 提供集群管理的 REST API 接口，包括:认证授权，数据校验，集群状态变更等
  * 认证 Authentication;
  * 授权 Authorization;
  * 准入：访问控制 Admission(Mutating & Valiating)。（request validation, mutation,）
* 提供其他模块之间的数据交互和通信的枢纽(其他模块通过 APIServer 查询或 修改数据，只有 APIServer 才直接操作 etcd，**Kubernetes 中所有的组件都会和 API Server 进行连接**，组件与组件之间一般不进行独立的连接，都**依赖于 API Server 进行消息的传送**)。

- APIServer 提供 etcd 数据缓存以减少集群对 etcd 的访问
- Used by kubectl CLI

![](image/kube-apiserver.png)

![](image/kube-apiserver展开.png)

rate limit：限流

自定义的对象走Aggregated APIServer

Aggregater是对APIserver的扩展方式

AggregationServer即extenisonServer。

#### 2.2.2 ETCD

* **Etcd**: A highly-available key value store. All cluster data is stored here. https://etcd.io/ 长久存储所有API对象
	* etcd acts as the cluster Distributed backing datastore for kubernetes.
	* provide a strong, consistent and **highly available key-value store** for persisting cluster state.
	* Stores objects(API对象) and config information.
	* The apiserveris the only thing that talks to itUses *“Raft Consensus”* among a quorum of systems to create a fault-tolerant consistent *“view”* of the cluster. https://raft.github.io/
	* ![](image/etcd.png)
  * etcd 是 CoreOS 基于 **Raft协议** 开发的分布式 key-value 存储，可用于**服务发现**、**共享配置**以及**一致性保障**(如 数据库选主、分布式锁等)。 异步消息机制，使得集群通过etcd的event联系起来。
    * 基本的 key-value 存储;
    * **监听机制**;
    - key 的过期及续约机制，用于监控和服务发现;
    - 原子 CAS 和 CAD，用于分布式锁和 leader 选举。
    - ![](image/etcd-cluster.png)
  * 直接访问 etcd 的数据
    * 通过 etcd 进程查看启动参数
    * 进入容器 `kubectl exec -it etcd-cadmin bash -n kube-system`
	    * ps -ef|grep etcd
	    * sh: ps: command not found
    * 怎么办?到主机 Namespace 查看 cert 信息
    * 进入容器查询数据

      export ETCDCTL_API=3

      etcdctl --endpoints https://localhost:2379 --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key --cacert /etc/kubernetes/pki/etcd/ca.crt get --keys-only --prefix / # 查询以/开头的key`
    * 监听对象变化

      etcdctl --endpoints https://localhost:2379 --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes/pki/etcd/server.key --cacert /etc/kubernetes/pki/etcd/ca.crt watch --prefix /registry/services/specs/default/mynginx



#### 2.2.3 Controller Manager

Controller Manager:

- Controller Manager 是集群的大脑，是确保整个集群动起来的关键;
- 作用是确保 Kubernetes 遵循 `<mark>`声明式系统规范 `</mark>`，确保系统的真实状态(Actual State)与用户定义的期望状态(Desired State)一致;
- Controller Manager 是**多个控制器的组合**，每个 Controller 事实上都是一个 control loop，负责侦听其管控的对象，当对象发生变更时完成配置; 每个controller是一个生产者-消费者模型，它监控apiserver的变化(apiserver支持watchable)，当检测到对象发生变化，controler的生产者观测到其变化并将其放入队列，消费者从队列取出数据进行处理。
- Controller 配置失败通常会触发自动重试，整个集群会在控制器不断重试的机 制下确保最终一致性( Eventual Consistency)

控制器工作流程：

![](image/控制器工作流程.png)

Informer 的内部机制:

![](image/Informer的内部机制.png)

控制器的协同工作原理:

![](image/控制器的协同工作原理.png)

* **Kube-controller-manager**: 控制管理器，它用来完成**对集群状态的一些管理**。比如刚刚我们提到的两个例子之中，第一个自动对容器进行修复、第二个自动进行水平扩张，都是由 Kubernetes 中的 Controller 来进行完成的。它运行着处理集群日常任务的控制器，包括：节点控制器，副本控制器，端点(endpoint)控制器及服务账户等

  * The home of the core controllers,
  * Daemon that runs controllers, which are the background threads that handle routine tasks in the cluster
  * Monitors the cluster state via the apiserver and **steers the cluster towards the desired state**. Does NOT handle scheduling,
  * Some types of these controllers are:
    * **Node Controller**: Responsible for noticing and responding when nodes go down.
    * **Job controller**: Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion.
    * **Endpoints Controller:** Populates the Endpoints object (that is, joins Services & Pods).
    * **Service Account & Token Controllers**: Create default accounts and API access tokens for new namespaces.
* **cloud-controller-manager**

  * The following controllers can have cloud provider dependencies:

    * **Node controller**: For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding

    - **Route controller**: For setting up routes in the underlying cloud infrastructure
    - **Service controller**: For creating, updating and deleting cloud provider load balancers
    - **Volume Controller**: For creating, attaching, and mounting volumes, and interacting with the cloud provider to orchestrate volumes

我们刚刚提到的 API Server，它本身在部署结构上是一个可以水平扩展的一个部署组件；Controller 是一个可以进行热备的一个部署组件，它只有一个 active，它的调度器也是相应的，虽然只有一个 active，但是可以进行热备。

#### 2.2.4 Scheduler

**kube-scheduler**: 调度器，完成调度操作，特殊的 Controller，工作原理与其他控制器无差别。

* 负责分配调度pod到集群内的节点上，它监听kube-apiserver, 查询还未分配Node的pod（NodeName为空的pod），并且获取当前集群所有节点的健康状况和资源使用情况，根据调度策略，依据Container对 CPU、对 memory 请求大小，为这些pod找一台合适的节点，进行放置（更新Pod的NodeName字段）；
* k8s 工作机制是基于event的，任何组件都是生产者-消费者模型。生产者是listInformer，消费者是一堆worker。
* 调度器需要充分考虑诸多因素：
  * 公平调度：优先级高先调度，同一优先级先进先出
  * 资源高效利用：可压缩与不可压缩，cpu可压缩，memory不可压缩，不同资源如何考虑高效利用，多元资源调度问题
  * QoS：保证质量
  * include individual and collective resource requirements,
  * hardware/software/policy constraints
  * affinity和anti-affinity
  * 数据本地化(data locality)：大数据领域
  * 内部负载干扰(inter-workload interference)
  * Deadlines

kube-scheduler 调度阶段分为:

* Predict: 过滤不能满足业务需求的节点，如资源不足、端口冲突等。 有一堆插件组合，有些是默认开启的
* Priority: 按既定要素将满足调度需求的节点评分，按优先级排序，选择最佳节点。 有一堆插件组合，有些是默认开启的
* Bind: 将计算节点与 Pod 绑定，完成调度

![](image/调度器.png)

**Predicates策略**：过滤策略。 有一堆插件组合，有些是默认开启的

* PodFitsHostPorts: 检查是否有Host Ports冲突。 docker -p可将容器里参数映射出来，k8s设hostport意味着要在主机起一个端口
* PodFitsPorts: 同PodFitsHostPorts
* PodFitsResources: 检查Node的资源是否充足，包括允许的Pod数量、CPU、内存、CPU个数及其他OpaqueIntResources
* HostName: 检查pod.Spec.NodeName是否与候选节点一致
* MatchNodeSelector: 检查候选节点的pod.Spec.NodeSelector是否匹配。Selector与label匹配
* NoVolumeZoneCOnflict: 检查Volume zone是否冲突
* MatchInterPodAffinity: 检查是否匹配Pod的亲和性要求
* NoDiskConflict：检查是否存在volume冲突，仅限于GCE PD、AWS EBS、Ceph RBD以及iSCSI
* PodToleratesNodeTaints: 检查pod是否容忍Node taints
* CheckNodeMemoryPressure: 检查pod是否可以调度到MemoryPressure的节点上
* CheckNodeDiskPressure: 检查pod是否可以调度到DiskPressure的节点上
* NoVolumeNodeConflict：检查节点是否满足Pod所引用的volume的条件
* ........还有很多策略，你也可以编写自己的策略

Predicates plugin工作原理：

![](image/predicates_plugin工作原理.png)
**Priorities策略**：打分策略， 每个plugin有一个权重

* SelectorSpreadPriority: 优先减少节点上属于同一个service或Replication controller的Pod数量
* InterPodAffinityProority: 优先将Pod调度到相同的拓扑上(如同一个节点、Rack、Zone等)
* LeastRequestPriority：优先调度到请求资源少的节点上，适用于批次作业
* BalanceResourceAllocation：优先平衡各节点的资源使用，适用于long running service
* NodePreferAvoidPodsPriority：alpha.kubernetes.io/preferAvoidPods字段判断，权重为10000，避免其他优先级策略的影响
* NodeAffinityPriority: 优先调度搭配匹配NodeAffinity的节点上
* TaintTolerationPriority：优先调度到匹配TaintToleration的节点上
* ServiceSpreadingPriority：尽量将同一个service的pod分布到不同节点上，已经被SelectorSpreadPriority替代(默认未使用)
* EqualPriority：将所有节点到优先级设置为1(默认未使用)
* ImageLocalityPriority：尽量将使用大镜像的容器调度到已经下拉了该镜像的节点上(默认未使用)
* MostRequestedPriority: 尽量调度到已经使用过的Node上，特别适用于cluster-autoscaler (默认未使用)

**资源需求**：

* CPU
  * requests：k8s调度pod时，会判断当前节点正在运行的pod的CPU request的总和，再加上当前调度pod的CPU request，计算其是否超过节点的CPU的可分配资源，至少需要的资源
  * limits：配置cgroup以限制资源上限
* 内存
  * requests：判断节点的剩余内存是否满足pod的内存请求量，以确定是否可以将pod调度到该节点
  * limits：配置cgroup以限制资源上限
* 磁盘资源需求
  * 容器临时存储(ephemeral storage) 包含日志和可写层数据，可通过定义Pod spec中的limits.ephemeral-storage和request.ephemeral-storage来申请。
  * pod调度完后，计算节点对临时存储的限制不是基于cgroup的，而是由kubelet定时获取容器的日志和容器可写层的磁盘使用情况，如果超过限制，会对pod进行驱逐。
* Init container的资源需求

```yaml

spec:
	containers:
		- image: nginx
		  name: nginx
		  ........
		  resources:
				Limits:
			      cpu:     1
			      memory:  2Gi
			    Requests:
			      cpu:      1m   # 千分之一的cpu，相当于10万微秒时间片可以用100微秒
			      memory:   2Gi
```

```sh

$ docker inspect <container_ID>
.....
"cgroupsPath": "/kubepods/burstable/pode0c242ef-ed83-466b-9ffd-f643129704f7/bf1414765b20999f1e31a25e6efe87154fbf14e1470fb1b0f28a1485398e6164"
.....
.....

$ cd /sys/fs/cgroup/kubepods/burstable/pode0c242ef-ed83-466b-9ffd-f643129704f7/bf1414765b20999f1e31a25e6efe87154fbf14e1470fb1b0f28a1485398e6164
$  
cx

```

LimitRange 对象: 不常用

```yaml
apiVersion: v1 
kind: LimitRange 
metadata:
	name: mem-limit-range 
spec:
	limits:
		- default:
				memory: 512Mi
			defaultRequest:
				memory:256Mi
			type: Container
```

### 2.3 Node Components

Kubernetes 的 **Node** 包含四个主要的组件：kubelet, kube-proxy, Container Runtime Engine:

![](image/node-components.png)

<img src="./assets/k8s-node.png" style="zoom: 33%;" />

#### 2.3.1 kubelet

* **kubelet**
  * An agent that runs on each [node](https://kubernetes.io/docs/concepts/architecture/nodes/) in the cluster. It makes sure that [containers](https://kubernetes.io/docs/concepts/containers/) are running in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/).
  * The kubelet takes a set of PodSpecs that are provided through various mechanisms and ensures that the containers described in those PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by Kubernetes
  * 负责调度到对应节点的 Pod 的生命周期管理，执行任务并将 Pod 状态报告给主节点的渠道，通过容器运行时(拉取镜像、启动和停止容器等)来运行这些容器。它 还会定期执行被请求的容器的健康探测程序。

Kubernetes 的初始化系统(init system): 每个节点上都有kubelet

* 从不同源获取 Pod 清单，并按需求启停 Pod 的核心组件:

  - Pod 清单可从本地文件目录，给定的 HTTPServer 或 Kube-APIServer 等源头获取;
  - Kubelet 将运行时，网络和存储抽象成了 CRI，CNI，CSI。
* 负责汇报当前节点的资源信息和健康状态;
* 负责 Pod 的健康检查和状态汇报。

![](image/kubelet%201.png)


PodWorker: 负责起停pod

OOMwatcher：管理内存情况

ProbManager：应用健康检查

ContainetGC：回收不用的容器

ImageGC：回收不用的镜像




#### 2.3.2 kube-proxy

* **kube-proxy**: 用来搭负载均衡，让用户通过service的ip访问服务

  * 它负责节点的网络，在主机上维护网络规则并执行连接转发。它还负责对正在服务 的 pods 进行负载平衡
  * kube-proxy is a network proxy that runs on each [node](https://kubernetes.io/docs/concepts/architecture/nodes/) in your cluster, implementing part of the Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/) concept.
  * [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/) maintains network rules on each nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster.
  * kube-proxy uses the operating system packet filtering layer if there is one and it's available. Otherwise, kube-proxy forwards the traffic itself.
  * Performs connection forwarding or load balancing for Kubernetes cluster services.
* 监控集群中用户发布的服务，并完成负载均衡配置。
* 每个节点的 Kube-Proxy 都会配置相同的负载均衡策略，使得整个集群的服务发现建立在分布式负载 均衡器之上，服务调用无需经过额外的网络跳转(Network Hop)。
* 负载均衡配置基于不同插件实现:

  * userspace。
  * 操作系统网络协议栈不同的 Hooks 点和插件:
    * iptables;
    * ipvs。

![](image/kube-proxy.png)

* **Container runtime Engine**

  * The **container runtime** is the CRI compatible application(software) that is responsible for running and managing containers.
  * Kubernetes supports container runtimes such as [containerd](https://containerd.io/docs/), [CRI-O](https://cri-o.io/#what-is-cri-o), and any other implementation of the [Kubernetes CRI (Container Runtime Interface)](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md).

    * Containerd (docker)
    * Cri-o
    * Rkt
    * Kata (formerly clear and hyper)
    * Virtlet (VM CRI compatible runtime)

**Kubernetes 的 Node** 是真正运行业务负载的，每个业务负载会以 Pod 的形式运行。等一下我会介绍一下Pod 的概念。一个 Pod 中运行的一个或者多个容器，真正去运行这些 Pod 的组件的是叫做 **kubelet**，也就是 Node 上最为关键的组件，它通过 API Server 接收到所需要 Pod 运行的状态，然后提交到我们下面画的这个 Container Runtime 组件中。

在 OS 上去创建容器所需要运行的环境，最终把容器或者 Pod 运行起来，也需要对存储跟网络进行管理。Kubernetes 并不会直接进行网络存储的操作，他们会靠 Storage Plugin 或者是网络的 Plugin 来进行操作。用户自己或者云厂商都会去写相应的 **Storage Plugin** 或者 **Network Plugin**，去完成存储操作或网络操作。

在 Kubernetes 自己的环境中，也会有 Kubernetes 的 Network，它是为了提供 Service network 来进行搭网组网的。（等一下我们也会去介绍“service”这个概念。）真正完成 service 组网的组件的是 **Kube-proxy**，它是利用了 **iptable** 的能力来进行组建 Kubernetes 的 Network，就是 cluster network，以上就是 Node 上面的四个组件。

Kubernetes 的 Node 并不会直接和 user 进行 interaction，它的 interaction 只会通过 Master。而 User 是通过 Master 向节点下发这些信息的。Kubernetes 每个 Node 上，都会运行我们刚才提到的这几个组件。

### 2.4 Add-ons

* DNS: kube-dns:负责为整个集群提供 DNS 服务;
* Ingress Controller:为服务提供外网入口;
* MetricsServer:提供资源监控; Container Resource Monitoring
* Dashboard:提供Web GUI;
* Fluentd-Elasticsearch:提供集群日志采集、存储与查询。Cluster-level Logging

### 2.5 Communication of components

![](image/k8s例子.png)

下面我们以一个例子再去看一下 Kubernetes 架构中的这些组件，是如何互相进行 interaction 的。

 用户可以通过 UI 或者 CLI 提交一个 Pod 给 Kubernetes 进行部署，这个 Pod 请求首先会通过 CLI 或者 UI 提交给 Kubernetes API Server，下一步 API Server 会把这个信息写入到它的存储系统 etcd，之后 Scheduler 会通过 API Server 的 watch 或者叫做 notification 机制得到这个信息：有一个 Pod 需要被调度。

这个时候 Scheduler 会根据它的内存状态进行一次调度决策，在完成这次调度之后，它会向 API Server report 说：“OK！这个 Pod 需要被调度到某一个节点上。”

这个时候 API Server 接收到这次操作之后，会把这次的结果再次写到 etcd 中，然后 API Server 会通知相应的节点进行这次 Pod 真正的执行启动。相应节点的 kubelet 会得到这个通知，kubelet 就会去调 Container runtime 来真正去启动配置这个容器和这个容器的运行环境，去调度 Storage Plugin 来去配置存储，network Plugin 去配置网络。

这个例子我们可以看到：这些组件之间是如何相互沟通相互通信，协调来完成一次Pod的调度执行操作的。

### 2.6 kubectl & kubeconfig

#### kubectl 
Kubectl

- kubectl是一个Kubernetes的命令行工具，它允许 Kubernetes 用户以命令行的方式与 Kubernetes 交 互，其默认读取配置文件 ~/.kube/config。
- kubectl会将接收到的用户请求转化为rest调用以 rest client 的形式与 apiserver 通讯。
- apiserver的地址，用户信息等配置在kube config。
- kubectl 使用kubeconfig认证文件连接k8s cluster

kubeconfig

```yaml
apiVersion: v1 
clusters:
- cluster:
	certificate-authority-data: REDACTED
	server: https://127.0.0.1:54729 
	name: kind-kind
contexts: 
- context:
	cluster: kind-kind
	user: kind-kind 
	name: kind-kind
current-context: kind-kind 
kind:Config
users:
- name: kind-kind
	user:
		client-certificate-data: REDACTED 
		client-key-data: REDACTED
```

**kubectl 常用命令**

```sh
kubectl get po –oyaml -w # kubectl 可查看对象。 -oyaml 输出详细信息为yaml格式 -w watch该对象的后续变化。 -owide 以详细列表的格式查看对象。
kubectl get ns
```

```sh
# kubectl describe 展示资源的详细信息和相关Event。

kubectl describe po ubuntu-6fcf6c67db-xvmjh ....
Events:
Message
Type Reason Age From
---- ------ ---- ---- ------- Normal Scheduled 8m13s default-scheduler
Normal Pulling Normal Pulled Normal Created Normal Started
Successfully assigned ubuntu-6fcf6c67db-xvmjh to k8smaster 7m56s kubelet, k8smaster pulling image "ubuntu:16.04"
7m50s kubelet, k8smaster Successfully pulled image "ubuntu:16.04" 7m50s kubelet, k8smaster Created container
7m50s kubelet, k8smaster Started container
```

```sh
# kubectl exec 提供进入运行容器的通道，可以进入容器进行 debug 操作。

kubectl exec -it ubuntu-6fcf6c67db-xvmjh -- bash 
root@ubuntu-6fcf6c67db-xvmjh:/# hostname -f 
ubuntu-6fcf6c67db-xvmjh 
root@ubuntu-6fcf6c67db-xvmjh:/#
```

```sh
# Kubectl logs 可查看 pod 的标准输入(stdout, stderr)，与 tail 用法类似。

kubectl logs ubuntu-6fcf6c67db-xvmjh Mon Mar 25 14:56:02 UTC 2019
Mon Mar 25 14:56:05 UTC 2019
Mon Mar 25 14:56:08 UTC 2019
Mon Mar 25 14:56:11 UTC 2019 Mon Mar 25 14:56:14 UTC 2019 ...

kubectl exec -it xx -- tail -f /xx.log # 如果应该将log转存到容器里的某个文件
```


#### kubeconfig

kubeconfig: kubeconfig描述集群配置信息。kubelet 使用kubeconfig认证文件连接k8s cluster,使用kubectl config命令生成kubeconfig文件。 


![](image/kubeconfig.png)

kubeconfig 配置文件默认地址 master节点的  /etc/kubernetes/admin.conf

如果不在master节点在其他机器上执行kubectl的方法

```sh
scp user@remote-server:/etc/kubernetes/admin.conf ~/.kube/config
# scp /etc/kubernetes/admin.conf root@<其他机器ip>:~
kubectl get node

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

scp /etc/kubernetes/admin.conf root@<其他机器ip>:~
kubectl --kubeconfig=admin.conf get node

export KUBERNETES_MASTER=http://127.0.0.1:8080
kubectl get node



```


```
[root@c61148v1 ~]# kubectl config get-contexts
CURRENT   NAME                          CLUSTER      AUTHINFO           NAMESPACE
*         kubernetes-admin@kubernetes   kubernetes   kubernetes-admin
* 
```

## 3. K8s Core Objects and API

https://kubernetes.io/docs/concepts/overview/working-with-objects/

### 3.1 k8s API

https://kubernetes.io/docs/concepts/overview/kubernetes-api/

Kubernetes API 是由 **HTTP+JSON** 组成的：用户访问的方式是 HTTP，访问的 API 中 content 的内容是 JSON/YAML 格式的。Kubernetes 的 **kubectl** 也就是 command tool，**Kubernetes UI**，或者有时候用 **curl**，直接与 Kubernetes 进行沟通，都是使用 HTTP + JSON 这种形式。

下面有个例子：比如说，对于这个 Pod 类型的资源，它的 HTTP 访问的路径，就是 API，然后是 apiVesion: V1, 之后是相应的 Namespaces，以及 Pods 资源，最终是 Podname，也就是 Pod 的名字。

如果我们去提交一个 Pod，或者 get 一个 Pod 的时候，它的 content 内容都是用 JSON 或者是 YAML 表达的。在这个 yaml file 中，对 Pod 资源的描述也分为几个部分。

### 3.2 k8s API object

<img src="/Users/gmx/Documents/workspace/note/Computer-Science/docs/Cloud_Computing/assets/常用k8s对象及分组.png" style="zoom:40%;" />

API 对象是 Kubernetes 集群中的管理操作单元。k8s 的所有管理能力构建在对象抽象的基础上。核心对象包括：

* Node:计算节点的抽象，用来描述计算节点的资源抽象、健康状态等。
* Namespace:资源隔离的基本单位，可以简单理解为文件系统中的目录结构。
* Pod:用来描述应用实例，包括镜像地址、资源需求等。 Kubernetes 中最核心 的对象，也是打通应用和基础架构的秘密武器。
* Service:服务如何将应用发布成服务，本质上是负载均衡和域名服务的声明

Kubernetes 集群系统每支持一项新功能，引入一项新技术，一定会新引入对应的 API 对象，支持对该功能的管理操作。

每个 API 对象都有四大类属性:

* TypeMeta
* MetaData
* Spec
* Status

**TypeMeta**：Kubernetes对象的最基本定义，它通过引入GKV(Group，Kind，Version)模型定义了一个对象的类型。

* Group：Kubernetes 定义了非常多的对象，如何将这些对象进行归类是一门学问，将对象依据其功能范围归入不同的分组， 比如把支撑最基本功能的对象归入 core 组，把与应用部署有关的对象归入 apps 组，会使这些对象的可维护性和可 理解性更高。
* Kind：定义一个对象的基本类型，比如 Node、Pod、Deployment 等。
* Version： **apiVesion**：为了向下兼容。社区每个季度会推出一个 Kubernetes 版本，随着 Kubernetes 版本的演进，对象从创建之初到能够完全生产化就 绪的版本是不断变化的。与软件版本类似，通常社区提出一个模型定义以后，随着该对象不断成熟，其版本可能会 从 v1alpha1 到 v1alpha2，或者到 v1beta1，最终变成生产就绪版本 v1。

**Metadata**：

* Namespace和Name：Metadata 中有两个最重要的属性: Namespace和Name，分别定义了对象的Namespace 归属及名字，这两个属性唯一定义了某个对象实例。 Node是non-Namespace的，所以name不能重名
* Label：用于识别资源，顾名思义就是给对象打标签，一个对象可以有任意对标签，其存在形式是键值对。 Label 定义了对象的可识别属性，Kubernetes API 支持以 **Label 作为过滤条件 查询对象**。
* Annotation：用于描述资源，Annotation 与 Label 一样用键值对来定义，但 Annotation 是作为属性扩展， 更多面向于系统管理员和开发人员，因此需要像其他属性一样做合理归类。当对象属性不够用时，可以将附加属性放到annotation。对资源的额外的一些用户层次的描述。https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
* Finalizer：Finalizer 本质上是一个资源锁，Kubernetes 在接收某对象的删除请求时，会检 查 Finalizer 是否为空，如果不为空则只对其做逻辑删除，即只会更新对象中的 metadata.deletionTimestamp 字段。
* ResourceVersion：ResourceVersion 可以被看作一种乐观锁，每个对象在任意时刻都有其 ResourceVersion，当 Kubernetes 对象被客户端读取以后，ResourceVersion 信息也被一并读取。此机制确保了分布式系统中任意多线程能够无锁并发访问对 象，极大提升了系统的整体效率。
* OwnerReference：用于多个资源相互关系

**Spec**：Spec 和 Status 才是对象的核心。Spec 是用户的期望状态，由创建对象的用户端来定义。与 TypeMeta 和 Metadata 等通用属性不同，Spec 和 Status 是每个对象独有的。

* Containers: 内部需要有哪些 container 被运行

  * name:
  * image: 它的 image 是什么
  * ports: 它暴露的 port 是什么？

**Status**：Status 是对象的实际状态，由对应的控制器收集实际状态并更新。

#### 3.2.2 Finalizer

Finalizer: https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/

Using Finalizers to Control Deletion: https://kubernetes.io/blog/2021/05/14/using-finalizers-to-control-deletion/

[Using Finalizers](https://book.kubebuilder.io/reference/using-finalizers.html#using-finalizers)

[Kubernetes: emptying the finalizers for a namespace that will not delete](https://fabianlee.org/2022/03/08/kubernetes-emptying-the-finalizers-for-a-namespace-that-will-not-delete/)

```
kubectl patch networkinterface 02d7-cb04699a-24e7-4cf8-abe2-f14e8cc5b8bc-b7mfx -p '{"metadata":{"finalizers":[]}}' --type=merge -n b423ad88b6f76fc60d40120bfec62c6d
```

#### 3.2.3 Labels

A label is a key/value pair that is attached to a resource, such as a pod, to convey a user-defined identifying attribute.

- **key-value** pairs that are used to i**dentify,** **describe** and **group** together related sets of objects or resources.
- **NOT** characteristic of uniqueness.
- Have a strict syntax with a slightly limited character set.
- https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set

<img src="./assets/labels.png" alt="image-20220418184741120" style="zoom:30%;" />

作用：

* 对k8s中各种资源进行分类、分组，添加一个具有特别属性的标签
* 用于筛选资源: 可以使用selector查询：类似于SQL ‘select * where ...
* 唯一的组合资源的方法
* 这些 label 是可以被 selector，也就是选择器所查询的。

通过 label，kubernetes 的 API 层就可以对这些资源进行一个筛选，那这些筛选也是 kubernetes 对资源的集合所表达默认的一种方式。

例如说，我们刚刚介绍的 Deployment，它可能是代表一组的 Pod，它是一组 Pod 的抽象，一组 Pod 就是通过 label selector 来表达的。当然我们刚才讲到说 service 对应的一组 Pod，就是一个 service 要对应一个或者多个的 Pod，来对它们进行统一的访问，这个描述也是通过 label selector 来进行 select 选取的一组 Pod。

所以可以看到 label 是一个非常核心的 kubernetes API 的概念

<img src="./assets/k8s-api-label.png" style="zoom:50%;" />

<img src="./assets/k8s-labels.png" style="zoom:50%;" />

上面是四个常用的标签。前三个标签打在pod上，最后一个标签打在node对象上。

k8s add label to nodes: https://www.golinuxcloud.com/kubectl-label-node/

k8s add label to pods: https://www.golinuxcloud.com/kubectl-label-node/

Kubernetes labels, selectors&annotations: https://www.golinuxcloud.com/kubernetes-labels-selectors-annotations/#Annotations

- Label是识别Kubernetes对象的标签，以key/value的方式附加到对象上。
- key最长不能超过63字节，value可以为空，也可以是不超过253字节的字符串。
- Label不提供唯一性，并且实际上经常是很多对象(如Pods)都使用相同的label来标志具 体的应用。
- Label定义好后其他对象可以使用LabelSelector来选择一组相同label的对象

* LabelSelector支持以下几种方式:

  * 等式，如 app=nginx 和 env!=production;

  - 集合，如 env in (production, qa);
  - 多个 label(它们之间是 AND 关系)，如 app=nginx,env=test。

![](/Users/gmx/Documents/workspace/note/Computer-Science/docs/Cloud_Computing/assets/label-example.png)

#### 3.2.4 Annotation

* Annotations 是 key/value 形式附加于对象的注解。
* 不同于 Labels 用于标志和选择对象，Annotations 则是用来记录一些附加信息，用来辅助应用部署、安 全策略以及调度策略等。
* 比如 deployment 使用 annotations 来记录 rolling update 的状态。

#### 3.2.4 Resource Model

* **Request**: amount of a resource allowed to be used, with a strong guarantee of availability.
  * CPU(seconds/second), RAM(bytes)
  * Scheduler will not over-commit requests
* **Limit**: max amount of a resource that can be used, regardless of guarantees.
  * scheduler ignores limits

<img src="./assets/resouece-model.png" alt="Screen Shot 2022-04-18 at 6.57.10 PM" style="zoom:90%;" />

#### 3.2.5 Selectors

Selectors use labels to filter or select objects, and are used throughout Kubernetes.

<img src="./assets/selectors.png" alt="image-20220418185913626" style="zoom:50%;" />

<img src="./assets/selectors-dia.png" alt="image-20220418185944036" style="zoom:40%;" />

**Selector Types**

<img src="./assets/selector-types.png" alt="image-20220418190042433" style="zoom:50%;" />

### 3.3 Namespace

Namespaces are a logical cluster or environment, and are the primary method of partitioning a cluster or scoping access.

资源隔离的基本单位，可简单理解为文件系统中的目录结构

k8s的对象分为namspace对象和非namspace对象

![image-20220418184210798](image/namespace.png)

Namespace 是用来做一个集群内部的逻辑隔离的，它包括鉴权、资源管理等。Kubernetes 的每个资源，比如刚才讲的 Pod、Deployment、Service 都属于一个 Namespace，同一个 Namespace 中的资源需要命名的唯一性，不同的 Namespace 中的资源可以重名。

kubectl get namespace

**Namespace 是对一组资源和对象的抽象集合**，比如可以用来将系统内部的对 象划分为不同的项目组或用户组。

常见的 pods, services, replication controllers 和 deployments 等都是属于 某一个 Namespace 的(默认是 default)，而 Node, persistentVolumes 等则不属于任何 Namespace。

### 3.3 Node

Node 是 Pod 真正运行的主机，可以物理机，也可以是虚拟机。为了管理 Pod，每个 Node 节点上至少要运行 container runtime (比如 Docker 或者 Rkt)、Kubelet 和 Kube-proxy 服务。

Node: 计算节点的抽象，用来描述计算节点的资源抽象，健康状态等。

```sh
kubectl get nodes -o wide # 查看所有节点
kubectl describe node <node_name> # 查看节点状态及节点其他详细信息
```

**Node status:** Node的一个属性，其记录了由系统最近观察到的节点状态

```yaml
kubectl describe node dal1-qz2-sr3-rk180-s18
Name:               dal1-qz2-sr3-rk180-s18
Roles:              control-plane,master
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=dal1-qz2-sr3-rk180-s18
                    kubernetes.io/os=linux
                    node-role.kubernetes.io/control-plane=
                    node-role.kubernetes.io/master=
                    node.kubernetes.io/exclude-from-external-load-balancers=
Annotations:        kubeadm.alpha.kubernetes.io/cri-socket: /var/run/dockershim.sock
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Fri, 09 Sep 2022 07:29:23 +0000
Taints:             node-role.kubernetes.io/master:NoSchedule
Unschedulable:      false
Lease:
  HolderIdentity:  dal1-qz2-sr3-rk180-s18
  AcquireTime:     <unset>
  RenewTime:       Fri, 04 Nov 2022 03:25:44 +0000
Conditions: # 描述了节点运行时的硬盘、内存、进程数等压力状态
  Type             Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----             ------  -----------------                 ------------------                ------                       -------
  MemoryPressure   False   Fri, 04 Nov 2022 03:24:51 +0000   Fri, 09 Sep 2022 07:29:20 +0000   KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure     False   Fri, 04 Nov 2022 03:24:51 +0000   Fri, 09 Sep 2022 07:29:20 +0000   KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure      False   Fri, 04 Nov 2022 03:24:51 +0000   Fri, 09 Sep 2022 07:29:20 +0000   KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready            True    Fri, 04 Nov 2022 03:24:51 +0000   Fri, 09 Sep 2022 07:38:36 +0000   KubeletReady                 kubelet is posting ready status. AppArmor enabled
Addresses: # 记录可访达节点的地址列表
  InternalIP:  10.12.11.66 # 内网IP
  ExternalIP：              # 外网IP
  Hostname:    dal1-qz2-sr3-rk180-s18
Capacity: # 节点拥有的资源总量
  cpu:                64
  ephemeral-storage:  50Gi
  hugepages-1Gi:      1Gi
  memory:             523371368Ki
  pods:               110 # 可运行的最大Pod个数
Allocatable: #  节点上可供普通 Pod使用的资源量，为了解决资源争夺问题，需要为系统守护进程以及k8s相关组件预留资源,因此allocatable != capacity. Allocatable(for pods)+kube-reserved+system-reserved+eviction-threshold=Node Capacity. Eviction Thresholds：驱逐阈值资源预留。系统预留一些内存资源，防止系统OOM，当系统可用资源小于驱逐阈值资源，节点为驱逐pod。allocatable 才是真正调度器调度 Pod 时的参考值（保证节点上所有 Pods 的 request 资源不超过Allocatable）
  cpu:                64
  ephemeral-storage:  48318382k
  hugepages-1Gi:      1Gi
  memory:             522220392Ki
  pods:               110     # 可运行的最大Pod个数
System Info:              # 描述了节点的基本信息
  Machine ID:                 534bf00c54374e23a39da7520647429b
  System UUID:                4C4C4544-004E-3810-8039-B1C04F484B32
  Boot ID:                    6780ee1c-7c5c-45b1-9888-212c22251ade
  Kernel Version:             4.15.0-1108-ibm-gt # Linux 内核版本
  OS Image:                   Ubuntu 18.04.6 LTS
  Operating System:           linux # 操作系统名称
  Architecture:               amd64
  Container Runtime Version:  docker://18.9.2 # Docker 版本
  Kubelet Version:            v1.22.8
  Kube-Proxy Version:         v1.22.8 # Kubernetes 版本、
PodCIDR:                      10.0.0.0/24
PodCIDRs:                     10.0.0.0/24 
Non-terminated Pods:          (13 in total)
  Namespace                   Name                                              CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                                              ------------  ----------  ---------------  -------------  ---
  kube-system                 coredns-6b8578cd59-4x2nd                          100m (0%)     0 (0%)      70Mi (0%)        8000Mi (1%)    14d
  kube-system                 coredns-6b8578cd59-chf2k                          100m (0%)     0 (0%)      70Mi (0%)        8000Mi (1%)    14d
  kube-system                 etcd-backup-operator-5b8c9c797-7q98r              0 (0%)        0 (0%)      0 (0%)           0 (0%)         20h
  kube-system                 kube-apiserver-dal1-qz2-sr3-rk180-s18             250m (0%)     0 (0%)      0 (0%)           0 (0%)         55d
  kube-system                 kube-controller-manager-dal1-qz2-sr3-rk180-s18    200m (0%)     0 (0%)      0 (0%)           0 (0%)         55d
  kube-system                 kube-proxy-xvmnv                                  0 (0%)        0 (0%)      0 (0%)           0 (0%)         55d
  kube-system                 kube-scheduler-dal1-qz2-sr3-rk180-s18             100m (0%)     0 (0%)      0 (0%)           0 (0%)         55d
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests     Limits
                #希望被分配到的额度  #最大被分配到的额度
  --------           --------     ------
  cpu                1950m (3%)   7 (10%)
  memory             1664Mi (0%)  24192Mi (4%)
  ephemeral-storage  0 (0%)       0 (0%)
  hugepages-1Gi      0 (0%)       0 (0%)
Events:              <none> # 最近发生过什么
```

资源预留配置示例：[www.qikqiak.com/k8strain/ma…](https://link.juejin.cn/?target=https%3A%2F%2Fwww.qikqiak.com%2Fk8strain%2Fmaintain%2Freserved%2F)

conditions描述节点运行时的一系列状态。一般有如下状态：

- Ready。True：表明节点是健康的并且可承载pod，False：节点不健康并且不能接受pod调度请求，Unknown：节点在规定时间内没有向节点控制器上传心跳。
- DiskPressure。True：表明磁盘大小存在压力（磁盘可用容量较小）。
- MemoryPressure。True：表明内存存在压力（内存容量过小）。
- PIDPressure。True：表明节点上存在大量的进程。
- NetworkUnavailable。True：表明节点的网络配置错误。

当节点的Ready属性为Unknow或者False时，并且持续时间超过pod-eviction-timeout（默认5分钟），节点控制器会计划将该节点的pod删除，但可能由于无法和节点建立通信导致删除失败。由于无法和节点建立通信，因此需要人工介入处理，手动删除节点。

**节点管理**

与 Pod 和 Service 不一样，节点并不是由 Kubernetes 创建的，节点由云供应商创建。向 Kubernetes 中创建节点时，仅仅是创建了一个描述该节点的 API 对象。节点 API 对象创建成功后，Kubernetes将检查该节点是否有效。例如，假设创建如下节点信息：

```yaml
kind: Node
apiVersion: v1
metadata:
  name: "10.240.79.157"
labels:
  name: "my-first-k8s-node"
```

Kubernetes 在 APIServer 上创建一个节点 API 对象（节点的描述），并且基于 metadata.name字段对节点进行健康检查。如果节点有效，则可以向该节点调度 Pod；否则，该节点 API 对象将被忽略，直到节点变为有效状态。 节点控制器（Node Controller） 节点控制器是一个负责管理节点的 Kubernetes master 组件。在节点的生命周期中，节点控制器起到了许多作用。

首先，节点控制器在注册节点时为节点分配 CIDR 地址块

第二，节点控制器通过云供应商（cloud-controller-manager）接口检查节点列表中每一个节点对象对应的虚拟机是否可用。在云环境中，只要节点状态异常，节点控制器检查其虚拟机在云供应商的状态，如果虚拟机不可用，自动将节点对象从 APIServer 中删除。

第三，节点控制器监控节点的健康状况。当节点变得不可触达时（例如，由于节点已停机，节点控制器不再收到来自节点的心跳信号），节点控制器将节点API对象的 NodeStatusCondition 取值从 NodeReady 更新为 Unknown；然后在等待 pod-eviction-timeout 时间后，将节点上的所有 Pod 从节点驱逐。

**节点自注册（Self-Registration）**

如果 kubelet 的启动参数 --register-node为 true（默认为 true），kubelet 会尝试将自己注册到 API Server。kubelet自行注册时，将使用如下选项：

--kubeconfig：向 apiserver 进行认证时所用身份信息的路径

--cloud-provider：向云供应商读取节点自身元数据

：自动向 API Server 注册节点

--register-with-taints：注册节点时，为节点添加污点（逗号分隔，格式为 `<key>`=`<value>`:`<effect>`

--node-ip：节点的 IP 地址

--node-labels：注册节点时，为节点添加标签

--node-status-update-frequency：向 master 节点发送心跳信息的时间间隔

如果 Node authorization mode (opens new window)和 NodeRestriction admission plugin (opens new window)被启用，kubelet 只拥有创建/修改其自身所对应的节点 API 对象的权限。

### 3.4 Pod

- Pod 是一组紧密关联的容器集合，是 Kubernetes 的一个**最小调度以及资源单元**, 它们共享 PID、IPC、Network 和 UTS namespace，是 Kubernetes 调度的基本单位。
- Pod 的设计理念是支持多个容器在一个 Pod 中共享网络和文件系统，可以通过进程间通信和文件共享这 种简单高效的方式组合完成服务。Each pod has its own IP
- 同一个 Pod 中的不同容器可共享资源:
  * 共享网络 Namespace;这些容器可以用 localhost 来进行直接的连接。而 **Pod 与 Pod 之间，是互相有 isolation 隔离的。**
  * 可通过挂载存储卷共享存储; •
  * 共享 Security Context。

```yaml
apiVersion: v1 
kind: Pod 
metadata:
	name: hello 
spec:
	containers:
	- image: nginx:1.15
		name: nginx
```

**如何通过 Pod 对象定义支撑应用运行**: 应用和配置分离，应用代码来自容器镜像，配置属性来自1.环境变量 2.读配置文件(外挂存储卷)

<img src="/Users/gmx/Documents/workspace/note/Computer-Science/docs/Cloud_Computing/assets/pod定义应用运行.png" style="zoom:30%;" />

存储卷

- 通过存储卷可以将外挂存储挂载到 Pod 内部使用。
- 存储卷定义包括两个部分: Volume 和 VolumeMounts。
  - Volume:定义 Pod 可以使用的存储卷来源;
  - VolumeMounts:定义存储卷如何 Mount 到容器内部。

```yaml
apiVersion: v1 
kind: Pod 
metadata:
	name: hello-volume 
spec:
	containers:
	- image: nginx:1.15
		name: nginx
		volumeMounts: 
		- name: data
			mountPath: /data 
	volumes:
	- name: data
		emptyDir: {}
```

**Pod 网络**

Pod的多个容器是共享网络 Namespace 的，这意味着:
 • 同一个 Pod 中的不同容器可以彼此通过 Loopback 地址访问:

- 在第一个容器中起了一个服务 http://127.0.0.1 。
- 在第二个容器内，是可以通过 httpGet http://127.0.0.1 访问到该地址的。 • 这种方法常用于不同容器的互相协作。

**资源限制**

Kubernetes 通过 Cgroups 提供容器资源管理的功能，可以限制每个容器的 CPU 和内存使用，比如对于刚才创建的 deployment，可以通过下面的命令限制 nginx 容器最多只用 50% 的 CPU 和 128MB 的内存:

```sh
$ kubectl set resources deployment nginx-app -c=nginx -- limits=cpu=500m,memory=128Mi

deployment "nginx" resource requirements updated
```

Memory

quota

等同于在每个 Pod 中设置 resources limits

```yaml
apiVersion: v1 
kind: Pod 
metadata:
	labels: 
		app: nginx
	name: nginx 
spec:
	containers:
	- image: nginx
		name: nginx 
		resources:
			limits:
				cpu: "500m" 
				memory: "128Mi"
```

Pods用来描述应用实例，包括镜像地址，资源需求等.k8s中最核心的对象，也是打通应用和基础架构的秘密武器。

比如像下面的这幅图里面，它包含了两个容器，每个容器可以指定它所需要资源大小。比如说，一个核一个 G，或者说 0.5 个核，0.5 个 G。

<img src="./assets/k8s-pod.png" style="zoom:50%;" />

当然在这个 Pod 中也可以包含一些其他所需要的资源：比如说我们所看到的 Volume 卷这个存储资源；比如说我们需要 100 个 GB 的存储或者 20GB 的另外一个存储。

在 Pod 里面，我们也可以去定义容器所需要运行的方式。比如说运行容器的 Command，以及运行容器的环境变量等等。Pod 这个抽象也给这些容器提供了一个共享的运行环境，它们会共享同一个网络环境，这些容器可以用 localhost 来进行直接的连接。而 **Pod 与 Pod 之间，是互相有 isolation 隔离的。**

A group of co-located containers: Pods are **one or MORE containers** that share volumes and namespace

* Smallest deployment unit – runs containers
* Each pod has its own IP
* Shares a PID namespace, network, and hostname, volumes
* **They are also ephemeral!**

<img src="./assets/pod.png" style="zoom:50%;" />

**Pod定义**

![image-20220418184313988](image/pod-example.png)

```yaml
apiVersion: v1 # 与k8s集群版本有关，使用 kubectl api-versions 即可查看当前集群支持的版本
kind: Pod # 该配置的类型，我们使用的是Pod
metadata: # 译名为元数据，即 Pod 的一些基本属性和信息
	name: nginx-pod # Pod 的名称
	labels: # 标签，可以灵活定位一个或多个资源，其中key和value均可自定义，可以定义多组，目前不需要理解
		app: nginx # 为该Deployment设置key为app，value为nginx的标签
spec: # 期望Pod实现的功能（即在pod中部署）
	containers: # 生成container，与docker中的container是同一种
	- name: nginx # container的名称
		image: nginx:1.7.9 # 使用镜像nginx:1.7.9创建container，该container默认80端口可访问
		ports: #  array of ports to expose. Can be granted a friendly name and protocol may be specified
		- containerPort: 80
		  name: http
      protocol: TCP
    env: # array of environment variables
    - name: MYVAR
      value: isAwesome
    command: [“/bin/sh”, “-c”] # Entrypoint array (equiv to Docker ENTRYPOINT)
    args: [“echo ${MYVAR}”] # Arguments to pass to the command (equiv to Docker CMD)
```

**Pod Template**

- Workload Controllers manage instances of Pods based off a provided template.
- Pod Templates are Pod specs with limited metadata.
- Controllers use Pod Templates to make actual pods.

```yaml
apiVersion: v1 
kind: Pod 
metadata: 
	name: nginx-pod 
	labels: 
		app: nginx 
spec: 
	template:
		metadata:
			labels:
				app: nginx
		spec:
			containers:
			- name: nginx
				image: nginx
```

**Pod description**

`kubectl describe pod nginx-deployment-67d4bdd6f5-w6kd7` configuration and status about the containers and Pod

````yaml
Name:         nginx-deployment-67d4bdd6f5-w6kd7 # below this line are basic data about the pod, such as the node it is running on, its labels and current status.
Namespace:    default
Priority:     0
Node:         kube-worker-1/192.168.0.113
Start Time:   Thu, 17 Feb 2022 16:51:01 -0500
Labels:       app=nginx
              pod-template-hash=67d4bdd6f5
Annotations:  <none>
Status:       Running # current state of the pod,which can be:1.Pending 2.Running 3.Succeeded 4.Failed 5.Unknown
IP:           10.88.0.3
IPs:
  IP:           10.88.0.3
  IP:           2001:db8::1
Controlled By:  ReplicaSet/nginx-deployment-67d4bdd6f5
Containers: # below this line is data about containers running on the pod (only one in this example, called nginx
  nginx:
    Container ID:   containerd://5403af59a2b46ee5a23fb0ae4b1e077f7ca5c5fb7af16e1ab21c00e0e616462a
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:2834dc507516af02784808c5f48b7cbe38b8ed5d0f4837f16e78d00deb7e7767
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running #the status of the container, which can be: 1.Waiting 2.Running 3.Terminated
      Started:      Thu, 17 Feb 2022 16:51:05 -0500
    Ready:          True # tells you whether the container passed its last readiness probe(n this case, the container does not have a readiness probe configured; the container is assumed to be ready if no readiness probe is configured.)
    Restart Count:  0 # how many times the container has been restarted,this information can be useful for detecting crash loops in containers that are configured with a restart policy of 'always.'
    Limits:
      cpu:     500m
      memory:  128Mi
    Requests:
      cpu:        500m
      memory:     128Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-bgsgp (ro)
Conditions: # which indicates that the pod is able to service requests and should be added to the load balancing pools of all matching services.
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes: # storage volumes, secrets or ConfigMaps mounted by containers in the pod
  kube-api-access-bgsgp:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events: # recent events occurring on the pod, such as images pulled, containers created and containers started
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  34s   default-scheduler  Successfully assigned default/nginx-deployment-67d4bdd6f5-w6kd7 to kube-worker-1
  Normal  Pulling    31s   kubelet            Pulling image "nginx"
  Normal  Pulled     30s   kubelet            Successfully pulled image "nginx" in 1.146417389s
  Normal  Created    30s   kubelet            Created container nginx
  Normal  Started    30s   kubelet            Started container nginx
  
 # "From" indicates the component that is logging the event, "SubobjectPath" tells you which object (e.g. container within the pod) is being referred to, and "Reason" and "Message" tell you what happened. 
````

**Pod lifecycle**

Pod state

- `Pending`：该阶段表示已经被 Kubernetes 所接受，但是容器还没有被创建，正在被 kube 进行资源调度。
- `1`：图中数字 1 是表示在被 kube 资源调度成功后，开始进行容器的创建，但是在这个阶段是会出现容器创建失败的现象
- `Waiting或ContainerCreating`：这两个原因就在于容器创建过程中**镜像拉取失败**，或者**网络错误**容器的状态就会发生转变。
- `Running`：该阶段表示容器已经正常运行。
- `Failed`：Pod 中的容器是以非 0 状态（非正常）状态退出的。
- `2`：阶段 2 可能出现的状态为 `CrashLoopBackOff`，表示容器正常启动但是存在异常退出。
- `Succeeded`：Pod 容器成功终止，并且不会再在重启。

container state

* Running
* 

### 3.7 **Ingress – Name Based Routing**

- An API object that manages external access to the services in a cluster
- Provides load balancing, SSL termination and name/path-based virtual hosting
- Gives services externally-reachable URLs

Steps to expose services using Kubernetes Ingress:  https://www.golinuxcloud.com/steps-to-expose-services-using-kubernetes-ingress/

### 3.8 Exploring the Core

Lab - github.com/mrbobbytables/k8s-intro-tutorials/blob/master/core



## 4 Workloads

### controller

A deep dive into Kubernetes controllers: https://docs.bitnami.com/tutorials/a-deep-dive-into-kubernetes-controllers/

### 4.1 **ReplicaSet**

- Pod 只是单个应用实例的抽象，要构建高可用应用，通常需要构建多个同样的副本，提供同一个服务。
- Kubernetes 为此抽象出副本集 ReplicaSet，其允许用户定义 Pod 的副本数，每一个 Pod 都会被当作一 个无状态的成员进行管理，Kubernetes 保证总是有用户期望的数量的 Pod 正常运行。
- 当某个副本宕机以后，控制器将会创建一个新的副本。
- 当因业务负载发生变更而需要调整扩缩容时，可以方便地调整副本数量。

![](image/replicaset-img.png)

- Primary method of managing pod replicas and their lifecycle.
- Includes their scheduling, scaling, and deletion.
- Their job is simple: **Always ensure the desired number of pods are running.**
- 
- ![](image/ReolicaSet.png)


![](image/ReplicaSet-example.png)
![image-20220418213531098](image/ReplicaSet-2.png)

### 4.2 **Deployment**

- 部署表示用户对 Kubernetes 集群的一次更新操作。
- 部署是一个比 RS 应用模式更广的 API 对象，可以是**创建一个新的服务**，**更新一个新的服务**，也可以是**滚动升级一个服务**。
- 滚动升级一个服务，实际是创建一个新的 RS，然后逐渐将新 RS 中副本数增加到理想状态，将旧 RS 中的副本数减小到 0 的 复合操作。
- 这样一个复合操作用一个 RS 是不太好描述的，所以用一个更通用的 Deployment 来描述。
- 以 Kubernetes 的发展方向，未来对所有长期伺服型的的业务的管理，都会通过 Deployment 来管理。

![](image/deployment-example.png)

```
通过类似 Docker run 的命令在 Kubernetes 运行容器
   kubectl run --image=nginx:alpine nginx-app --port=80 
   kubectl get deployment
   kubectl describe deployment/rs/pod

kubectl expose deployment nginx-app --port=80 --target-port=80 
	kubectl describe svc
	kubectl describe ep
```

- Way of managing Pods via **ReplicaSets.**
- Provide rollback functionality and update control.
- Updates are managed through the **pod-template-hash** label.
- Each iteration creates a unique label that is assigned to both the **ReplicaSet** and subsequent Pods.

![image-20220418213619710](image/Deployment.png)

Deployment 是在 Pod 这个抽象上更为上层的一个抽象，它可以定义一组 Pod 的副本数目、以及这个 Pod 的版本。一般大家用 Deployment 这个抽象来做应用的真正的管理，而 Pod 是组成 Deployment 最小的单元。Deployment用来描述一个应用的部署。
![](image/k8s-deployment.png)


Kubernetes 是通过 Controller，也就是我们刚才提到的控制器去维护 Deployment 中 Pod 的数目，它也会去帮助 Deployment 自动恢复失败的 Pod。

比如说我可以定义一个 Deployment，这个 Deployment 里面需要两个 Pod，当一个 Pod 失败的时候，控制器就会监测到，它重新把 Deployment 中的 Pod 数目从一个恢复到两个，通过再去新生成一个 Pod。通过控制器，我们也会帮助完成发布的策略。比如说进行滚动升级，进行重新生成的升级，或者进行版本的回滚。

```yaml
apiVersion: v1 
kind: Deployment
metadata: 
	name: nginx
spec: 
  replicas: 1
  selector:
  	matchLabels:
  		app: nginx
  template:
  	metadata:
  		labels:
  			app: nginx
  	spec:
  		containers:
  		- image: nginx
  			name: nginx
```

Pod是k8s最小调度单元，但是如果不小心删掉pod，服务将会中断，为了高可用使用deployment方式部署pod，保证pod出现问题后自动重启或恢复。做到了故障转移，

高可用最重要的点是冗余部署，可以将replicas大于1

对于高可用的应用一般要做负载均衡，冗余部署后是有多个IP的，这就用到了service

### 4.3 **DaemonSet**

后台支撑服务集
- 长期伺服型和批处理型服务的核心在业务应用，可能有些节点运行多个同类业务的 Pod，有些节点上又没有这类 Pod 运行;
- 而后台支撑型服务的核心关注点在 Kubernetes 集群中的节点(物理机或虚拟机)，要保证每个节点上都有一个此类 Pod 运行。
- 节点可能是所有集群节点也可能是通过 nodeSelector 选定的一些特定节点。
- 典型的后台支撑型服务包括存储、日志和监控等在每个节点上支撑 Kubernetes 集群运行的服务。

![](/Us/assets/daemonset-example.png)

- Ensure that all nodes matching certain criteria will run an instance of the supplied Pod.
- Are ideal for cluster wide services such as log forwarding or monitoring.

![image-20220418213752435](image/DaemonSet.png)

### 4.4 **StatefulSet**

A StatefulSet is a Controller that provides a unique identity to its Pods. It provides guarantees about the ordering of deployment and scaling.

- Tailored to managing Pods that must persist or maintain state.
- Pod lifecycle will be ordered and follow consistent patterns.
- Assigned a unique ordinal name following the convention of ‘*`<statefulset name>`-`<ordinal index>`*’.

有状态服务集
- 对于 StatefulSet 中的 Pod，每个 Pod 挂载自己独立的存储，如果一个 Pod 出现故障，从其他节点启动一个同样名字的 Pod，要挂载上原来 Pod 的存储继续以它的状态提供服务。
- 适合于 StatefulSet 的业务包括数据库服务 MySQL 和 PostgreSQL，集群化管理服务 ZooKeeper、etcd 等有状态服务。
- 使用 StatefulSet，Pod 仍然可以通过漂移到不同节点提供高可用，而存储也可以通过外挂的存储来提供高可靠性，

  StatefulSet 做的只是将确定的 Pod 与确定的存储关联起来保证状态的连续性。

![](image/statefulset.png)

Statefulset 与 Deployment 的差异

* 身份标识

  * StatefulSet Controller 为每个 Pod 编号，序号从0开始。
* 数据存储

  * StatefulSet 允许用户定义 volumeClaimTemplates，Pod 被创建的同时，Kubernetes 会以volumeClaimTemplates 中定义的模板创建存储卷，并挂载给 Pod。
* StatefulSet 的升级策略不同

  * onDelete
  * 滚动升级
  * 分片升级

### 4.5 **Job**

Deployment ，Service都是long running任务。Job用来支持一次性任务，短时任务，Job完成后pod时complete状态
- Job 是 Kubernetes 用来控制批处理型任务的 API 对象。
- Job 管理的 Pod 根据用户的设置把任务成功完成后就自动退出。
- 成功完成的标志根据不同的 spec.completions 策略而不同:
  - 单 Pod 型任务有一个 Pod 成功就标志完成;
  - 定数成功型任务保证有 N 个任务全部成功;
    • 工作队列型任务根据应用确认的全局成功而标志成功。


![](image/job.png)
### 4.6 **CronJob**

An extension of the Job Controller, it provides a method of executing jobs on a cron-like schedule.

### 3.5 Service

Service 是应用服务的抽象，通过 labels 为应用提供负载均衡和服务发现。匹配 labels 的 Pod IP 和端口列表组成 endpoints，由 Kube-proxy 负责将服务 IP 负载均衡到这些 endpoints 上。

每个 Service 都会自动分配一个 cluster IP(仅在集群内部可访问的虚拟地址) 和 DNS 名，其他容器可以通过该地址或 DNS 来访问服务，而不需要了解后端 容器的运行。

![](image/service-img.png)

Service Spec:

```yaml
apiVersion: v1 
kind: Service 
metadata:
	name: nginx 
spec:
	ports:
	- port: 8078 # the port that this service should serve on
		name: http
		# the container on each pod to connect to, can be a name 
		# (e.g. 'www') or a number (e.g. 80)
		targetPort: 80
		protocol: TCP
	selector: 
		app: nginx
```

Service 提供了一个或者多个 Pod 实例的稳定访问地址。

service：服务如何将应用发布成服务，本质上是负载均衡和域名服务的声明。

![](image/k8s-service.png)

比如在上面的例子中，我们看到：一个 Deployment 可能有两个甚至更多个完全相同的 Pod。对于一个外部的用户来讲，访问哪个 Pod 其实都是一样的，所以它希望做一次负载均衡，在做负载均衡的同时，我只想访问某一个固定的 VIP，也就是 Virtual IP 地址，而不希望得知每一个具体的 Pod 的 IP 地址。

我们刚才提到，这个 pod 本身可能 terminal go（终止），如果一个 Pod 失败了，可能会换成另外一个新的。

对一个外部用户来讲，提供了多个具体的 Pod 地址，这个用户要不停地去更新 Pod 地址，当这个 Pod 再失败重启之后，我们希望有一个抽象，把所有 Pod 的访问能力抽象成一个第三方的一个 IP 地址，实现这个的 Kubernetes 的抽象就叫 Service。

实现 Service 有多种方式，Kubernetes 支持 Cluster IP，上面我们讲过的 kuber-proxy 的组网，它也支持 nodePort、 LoadBalancer 等其他的一些访问的能力。

A service defines a set of pods and a means by which to access them, such as single stable IP address, static namespaces and corresponding DNS name. 1. Collection of pods exposed as an endpoint. 2. state and networking info propagated to all worker nodes

- **Unified method of accessing** the exposed workloads of Pods.
- **Durable resource** (unlike Pods)  , **NOT Ephemeral!**
  - static cluster-unique IP
  - static namespaced DNS name

* \<service name\>.\<namespace\>.svc.cluster.local

- Target Pods using **equality based selectors**.
- Uses **kube-proxy** to provide simple load-balancing.
- **kube-proxy** acts as a daemon that creates **local entries** in the host’s iptables for every service.

* Types of service exposure

  * **ClusterIP** (Default)– Exposes cluster-internal IP
  * **NodePort** – Exposes the service on each Node’s IP at a static port
  * **LoadBalancer** – Exposes externally using a cloud provider’s load balancer
  * **ExternalName** – Maps to an external name (such as foo.bar.example.com)

  <img src="./assets/services-2.png" alt="image-20220418175332944" style="zoom:30%;" />

  ![img](image/services.png)

#### 3.6.1 **ClusterIP Service**

**ClusterIP** services exposes a service on a strictly cluster internal virtual IP.
![](image/clusrerip-service.png)
![](image/cluster-ip-dia.png)

**ClusterIP Service Without Selector**

![](image/cluster-ip-no-selector.png)

#### 3.6.2 NodePort Service

- **NodePort** services extend the **ClusterIP** service.
- Exposes a port on every node’s IP.
- Port can either be statically defined, or dynamically taken from a range between 30000-32767.
  ![](image/nodeport-service.png)
  ![](image/nodeport-service-example.png)

#### 3.6.3 **LoadBalancer Service**

- **LoadBalancer** services extend **NodePort.**
- Works in conjunction with an external system to map a cluster external IP to the exposed service.

apiVersion: v1
kind: Service
metadata:
  name: example-prod
spec:
  type: LoadBalancer
  selector:
    app: nginx
    env: prod
  ports:
    protocol: TCP
    port: 80
    targetPort: 80

<img src="./assets/load-balance-service.png" alt="image-20220418192321568" style="zoom:50%;" />

<img src="./assets/load-balance-service-2.png" alt="image-20220418192321568" style="zoom:50%;" />

#### 3.6.4 **ExternalName Service**

- **ExternalName** is used to reference endpoints **OUTSIDE** the cluster.
- Creates an internal **CNAME** DNS entry that aliases another.

## 5. Security

权限管理：认证，授权，准入

Kubernetes 主要通过 API Server 对外提供服务，Kubernetes 对于访问 API 的用户提供了相应的安全控制：认证和授权。认证解决用户是谁的问题，授权解决用户能做什么的问题。只有通过合理的权限控制，才能够保证整个集群系统的安全可靠。

下图是 API 访问需要经过的三个步骤，它们分别是：认证、授权和准入，准入不在这章节讨论，它更多专注的是资源的管理。

![](image/access-control.png)

一个组件和apiserver通信时要做认证鉴权，要有一个身份，每个k8s pod 会分配一个service account，service account以volume形式mount到pod里，里面的应用读取service account 对应的文件来与apiserver通信

用户(User Account)& 服务帐户(Service Account)

* 用户帐户为人提供账户标识，而服务账户为计算机进程和 Kubernetes 集群中运行的 Pod 提供 账户标识。
* 用户帐户和服务帐户的一个区别是作用范围:
  * 用户帐户对应的是人的身份，人的身份与服务的 Namespace 无关，所以用户账户是跨Namespace 的;
  * 而服务帐户对应的是一个运行中程序的身份，与特定 Namespace 是相关的。

### Authentication

**Authentication** 认证是指用户是否可以登录 Kubernetes，即是否可以向 API Server 发送请求。

#### 认证用户

在 Kubernetes 中，有两类用户：

- Normal Users：外部用户
- Service Accounts：内部用户

Normal Users 独立于 Kubernetes，不归其管理，这类用户可以是：

- 可以分发 private keys 的管理员（真人）
- 提供用户服务的第三方厂商，比如 Google Accounts
- 保存用户名和密码的列表文件

**Normal Users**：

如果用户都不在 Kubernetes 中，都不归它管，那它是如何进行认证的呢？
对于一般的应用系统来说，用户提供用户名和密码，服务端收到过后会在数据库中进行检查是否存在并有效，如果有就表示鉴权成功，反之失败。

那对于 Kubernetes 来说，是如何实现的呢？
尽管无法通过 API 调用来添加普通用户，Kubernetes 巧妙的通过证书来进行用户认证。也就是说，不管任何用户，只要能提供有效的证书就能通过 Kubernetes 用户认证。

通过用户认证过后，Kubernetes 会把证书中的 CN 作为用户名（比如证书中”/CN=joker“，则用户名就是 Joker），把 Organization 作为用户组，然后由用户名和用户组绑定的 Role 来决定用户的权限。

**Service Accounts**：

Service Accounts 由 Kubernetes 管理，它们被绑定到特定的 namespace，其可以通过 API Server 自己创建，也可以通过调用 API 来创建，比如使用 kubectl 客户端工具。

与 Normal Users 不同，Service Accounts 存在对应的 Kubernetes 对象，当创建 Service Accounts，会创建相应的 Secret，里面保存对应的密码信息（在 1.24.x 版本中，不会创建对应的 secret）。当创建的 Pod 指定了一个 Service Account，其 Secret 会被 Mount 到 Pod 中，Pod 中的进程就可以访问 Kubernetes API 了。

#### 认证策略

Kubernetes 有以下几种鉴权方法：

- **X509 Client Certs** (CN used as user, Org fields as group) No way to revoke them!! – wip ☺ 客户端证书
- **Static Password File** (password,user,uid,"group1,group2,group3")
- **Static Token File** (token,user,uid,"group1,group2,group3")
- **Bearer Token** (Authorization: Bearer 31ada4fd-ade)
- **Bootstrap Tokens** (Authorization: Bearer 781292.db7bc3a58fc5f07e)
- **Service Account Tokens** (signed by API server’s private TLS key or specified by file)

**客户端证书**

当我们使用客户端证书进行认证时，需要向 Kubernetes 提供有效的证书，这个证书可以是外部证书，也可以是 Kubernetes 自己审批的证书。

如果是外部证书，就需要在 API Server 启动的时候用 `--client-ca-file=SOMEFILE`参数引入外部证书的 CA 等信息，用来验证客户端证书的有效性。

当认证通过后，Kubernetes 会把证书的 Subject CN 作为用户名，Organization 作为用户组（Group）。

**不记名令牌**

当使用不记名令牌（Bearer token）来对某 HTTP 客户端执行身份认证时，API 服务器希望看到一个名为 Authorization 的 HTTP 头，其值格式为 Bearer 。 不记名令牌（Bearer token）必须是一个可以放入 HTTP 头部值字段的字符序列，至多可使用 HTTP 的编码和引用机制。 例如：如果持有者令牌为 31ada4fd-adec-460c-809a-9e56ceb75269，则其出现在 HTTP 头部时如下所示：

```text
Authorization: Bearer 31ada4fd-adec-460c-809a-9e56ceb75269
```

在 Kubernetes 中，主要有以下几种使用不记名令牌（Bearer token）的方法：

- Static Token File（静态令牌）
- Service Account Tokens（服务账号令牌）
- OpenID Connect Tokens（OIDC 令牌）

**Static Token File**

当使用静态令牌的时候，API Server 会通过 `--token-auth-file=SOMEFILE`从外部引入一个 CSV 文件，API Server 会从这个文件中读取对应的用户名和用户组。

当客户端进行请求时，API Server 把请求 Header 中的 Bearer tokens 和文件中的 token 进行比较，然后判断 Token 是否有效。

**Service Account Tokens**

当手动或者自动创建 Service Account 的时候，Kubernetes 会自动创建一个 Service Account Token，在 v1.24 版本之前，会对应创建一个 secret 保存到对应的 namespace 中，在 v1.24 版本之后不会再单独创建 secret，而是在启动 Pod 的时候，由 kubelet 通过 TokenRequest API 生成一个 Token 挂载到 Pod 中。

上文提到，Service Account 主要是为 Pods 提供访问 API Server 的功能，当 Pod 创建过后，Service Account Token 就会被 Mount 到 Pod 中，此时 Pod 就拥有访问 API Server 的能力。

当然，Service Account Token 除了用在 Pod 上，在外部也可以使用，在《Kubernetes 集群管理》中的集群安装章节，有介绍使用 Token 访问 Kubernetes Dashboard，这时候使用的也是 Service Account Token。

**OpenID Connect Tokens**

OpenID Connect 是一种 OAuth2 认证方式，Kubernetes 可以利用 OAuth2 Token Response 中的 ID Token 作为 Bearer Token 进行认证访问。

其流程如下：

![img](https://pic3.zhimg.com/80/v2-9446775ae8fb5a5a6b5c7d396eaa4836_1440w.jpg)

1. 登录到你的身份服务（Identity Provider）
2. 你的身份服务将为你提供 access_token、id_token 和 refresh_token
3. 在使用 kubectl 时，将 id_token 设置为 --token 标志值，或者将其直接添加到 kubeconfig 中
4. kubectl 将你的 id_token 放到一个称作 Authorization 的头部，发送给 API 服务器
5. API 服务器将负责通过检查配置中引用的证书来确认 JWT 的签名是合法的
6. 检查确认 id_token 尚未过期
7. 确认用户有权限执行操作
8. 鉴权成功之后，API 服务器向 kubectl 返回响应
9. kubectl 向用户提供反馈信息

不管用户通过哪种方式进行认证，认证通过并不代表就有操作权限，仅仅只是通过第一条防线而已，下一步就要进行鉴权，用来决定用户是否有具体的操作权限。

### Authorization

鉴权

#### 鉴权流程

当请求通过认证（Authentication）过后，就会进入鉴权（Authorization）阶段。在这个阶段 Kubernetes 会检查请求是否有权限访问需要的资源，如果有权限则开始处理请求，反之则返回权限不足。

API Server 会检查所有 Policy 来检查是否存在 Policy 允许请求中的动作，存在则允许请求执行，否则会拒绝执行并返回 403 错误。当配置了多个授权模块的时候，请求会按顺序校验每一个模板，如果其中任一模块校验不通过，则请求会被拒绝，不再进行后续的校验。

Kubernetes 在做鉴权时，主要检查以下信息：

- user：同鉴权中检查的信息相同
- group：同鉴权中检查的信息相同
- extra：同鉴权中检查的信息相同
- API：是否为 Api 资源
- Request path：非资源（API 资源）endpoint，比如/healthz
- API request verb：API 动作，比如 get, list, create, update, patch，对某个资源的具体动作，比如，列出所有的 pod
- HTTP request verb：用于非资源的请求中的 HTTP 动作，比如 get, post, put
- Resource：请求访问的资源名字或 ID
- Subresource：请求访问的子资源名字或 ID
- Namespace：资源所在的名字空间
- API group：请求访问的 API group，API group 指控制相关资源的一组 Api，如果未指定则代表 core API group

#### 鉴权模块

Kubernetes 提供了以下 4 种鉴权模式：

- Node：一种特殊的授权模块，基于 Node 上运行的 Pod 为 Kubelet 授权
- ABAC：基于属性的访问控制
- RBAC：基于角色的访问控制
- Webhook：HTTP 请求回调，通过一个 WEB 应用鉴定是否有权限进行某项操作

这里只会介绍 RBAC——基于角色的访问控制。在实际中，这种模式使用的场景比较多。

**RBAC**

RBAC 是 Kubernetes 中常用的鉴权模式，其基本概念如下：

1. Rule：规则，一组属于不同 API Group 的操作集合；
2. Role：角色，用于定义一组对 Kubernetes API 对象操作的一组规则，作用于当个 namespace；
3. ClusterRole：集群角色，该角色不受 namespace 的限制；
4. Subject：被作用者，也就是规则作用的对象；
5. RoleBinding：将角色和被作用者进行绑定，作用于当个 namespace；
6. ClusterRoleBinding：将集群角色和作用者进行绑定，不受 namespace 限制；

Role 和 ClusterRole 中定义一组相关权限的规则，这些权限是累加的（不存在拒绝某操作的规则）。其中 Role 是 Namespace 级别的，而 ClusterRole 是集群级别的。

Role 的定义如下：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: role-demo
  namespace: devops
rules:
- apiGroups: [""]
  resources: ["pods", "deployment"]
  verbs: ["creat", "delete", "watch", "list", "get"]
```

其含义是：它允许被作用者在 devops 的 namespace 中对 pod 和 deployment 有 creat，delete，watch，list，get 操作。由于 Role 是 Namespace 级别，所以上面的规则只对 devops 的 namespace 有效。

ClusterRole 的定义如下：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-role-demo
rules:
- apiGroups: [""]
  resources: [""]
  verbs: ["watch", "list", "get"]
```

其含义是对所有资源都有 watch、list、get 的操作权限。

如果要定义所有权限，可以将 verbs 字段定义如下：

```yaml
verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

**RoleBinding 和 ClusterRoleBinding**

角色绑定将一个角色中定义的各种权限授予一个或者一组用户。 角色绑定包含了一组相关主体（即 subject, 包括用户——User、用户组——Group、或者服务账户——Service Account）以及对被授予角色的引用。 在命名空间中可以通过 RoleBinding 对象授予权限，而集群范围的权限授予则通过 ClusterRoleBinding 对象完成。

RoleBinding 可以引用在同一命名空间内定义的 Role 对象。 如下：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: joker-rolebinding
  namespace: devops
subjects:
  - kind: User
    name: joker
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: role-demo
  apiGroup: rbac.authorization.k8s.io
```

这就给 joker 用户和 role-demo 的 Role 建立了绑定关系，其中 joker 这个 User 只是一个授权系统中的逻辑概念，它需要通过外部认证服务，比如 Keystone，或者直接给 API Server 指定一个用户名，密码文件。

上面的 YAML 文件中其中一个重要的字段是 Subjects 字段，它定义"被作用者"，其中的 kind 表示被作用者的类型，其有以下三种类型：

- User：用户，这是由外部独立服务进行管理的，管理员进行私钥的分配，用户可以使用 KeyStone 或者 Goolge 帐号，甚至一个用户名和密码的文件列表，对于用户的管理集群内部没有一个关联的资源对象，所以用户不能通过集群内部的 API 来进行管理。
- Group：组，这是用来关联多个账户，集群中有一个默认的组，比如 cluster-admin。
- ServiceAccount：服务帐号，通过 Kubernetes API 来管理的一些用户帐号，和 namespace 进行关联的，适用于集群内部运行的应用程序，需要通过 API 来完成权限认证，所以在集群内部进行权限操作，我们都需要使用到 ServiceAccount。

另外一个重要字段是 roleRef，它定义 RoleBing 对象可以直接通过 Role 的名字来引用我们定义的 Role 对象，从而定义被作业者和角色之间的绑定关系。

RoleBinding 是 namespace 级别的，如果是集群级别则用 ClusterRoleBinding，如下：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: joker-clusterrolebinding
subjects:
  - kind: User
    name: joker
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-role-demo
  apiGroup: rbac.authorization.k8s.io
```

上面定义的就是 joker 这个用户对所有 namespace 里的资源都有 watch，list，get 的操作权限。

**Service Account**

Service Account 也是一种账号，但它并不是给 Kubernetes 集群的用户（系统管理员、运维人员、租户用户等）用的，而是给运行在 Pod 里的进程用的，它为 Pod 里的进程提供了必要的身份证明。

我们通过一个例子来了解 ServiceAccount 的授权过程。 1、首先定义一个 ServiceAccount：

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: devops
  name: sa-demo
```

一个简单的 ServiceAccount 只需要简单的 namespace 和 name 即可。

2、编写 RoleBinding 的 YAML 文件来为这个 ServiceAccount 分配权限：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: role-demo
  namespace: devops
rules:
  - apiGroups: [""]
    resources: ["pods", "deployment"]
    verbs: ["creat", "delete", "watch", "list", "get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: sa-rolebinding
  namespace: devops
subjects:
  - kind: ServiceAccount
    name: sa-demo
    namespace: devops
roleRef:
  kind: Role
  name: role-demo
  apiGroup: rbac.authorization.k8s.io
```

然后我们创建上面定义的 YAML 文件，查看创建完成后的信息：

```sh
$ kubectl get sa -n devops
NAME      SECRETS   AGE
default   0         6m25s
sa-demo   0         6m25s
$ kubectl get role -n devops
NAME        CREATED AT
role-demo   2022-07-06T04:27:02Z
$ kubectl get rolebinding -n devops
NAME             ROLE             AGE
sa-rolebinding   Role/role-demo   6m50s
```

现在创建一个 Pod 并使用 sa-demo Service Account。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-sa-demo
  namespace: devops
spec:
  serviceAccountName: sa-demo # pod 使用service account
  containers:
  - name: pod-sa-demo
    image: nginx
    imagePullPolicy: IfNotPresent
```

查看 Pod 信息如下：

```sh
$ kubectl get po -n devops pod-sa-demo -oyaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    cni.projectcalico.org/containerID: c0820de4319bb6915602c84132ff83a63f62abaa1e9c706bad04e64661455d30
    cni.projectcalico.org/podIP: 172.16.51.225/32
    cni.projectcalico.org/podIPs: 172.16.51.225/32
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{},"name":"pod-sa-demo","namespace":"devops"},"spec":{"containers":[{"image":"nginx","imagePullPolicy":"IfNotPresent","name":"pod-sa-demo"}],"serviceAccountName":"sa-demo"}}
  creationTimestamp: "2022-07-06T04:30:13Z"
  name: pod-sa-demo
  namespace: devops
  resourceVersion: "192831"
  uid: 4f4c7c5a-53ca-45f7-94ad-63e546cfcc62
spec:
  containers:
  - image: nginx
    imagePullPolicy: IfNotPresent
    name: pod-sa-demo
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-vxrcd
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: kk-node01
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: sa-demo
  serviceAccountName: sa-demo
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: kube-api-access-vxrcd
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
```

从上面可以看到 Service Account Token 被挂载到 Pod 中了。

```sh
$ kubectl exec -it -n devops pod-sa-demo -- /bin/sh
# ls /var/run/secrets/kubernetes.io/serviceaccount
ca.crt  namespace  token
```

其中 ca.crt 就是用来访问 API Server 的。

如果一个 Pod 在定义时没有指定 spec.serviceAccountName 属性，则系统会自动为其赋值为 default，即大家都使用同一个 Namespace 下的默认 Service Account。

Subjects 的 kind 类型除了 User，ServiceAccount 之外，还有一个 Group，就是一组用户的意思。如果你为 Kubernetes 配置了外部认证服务的话，这个用户组就由外部认证服务提供。而对于 Kubernetes 内置用户 ServiceAccount 来说，其也有用户和用户组的概念，其中对于一个 ServiceAccount，其在 Kubernetes 中对应的用户是：

```text
system:serviceaccount:<ServiceAccount名字>
```

而对于其用户组是：

```text
system:serviceaccounts:<Namespace名字>
```

比如我们定义下面这个 RoleBinding:

```yaml
subjects:
  - kind: Group
    name: system:serviceaccounts:devops
    apiGroup: rbac.authorization.k8s.io
```

这就意味着 Role 这个角色的权限规则作用与 devops 的 namespace 中的所有 ServiceAccount。

再比如：

```yaml
subjects:
  - kind: Group
    name: system:serviceaccounts
    apiGroup: rbac.authorization.k8s.io
```

这就意味着 Role 这个角色规则作用与整个集群的所有 ServiceAccount。

kubernetes 已经内置了许多 ClusterRole，以 system:开头，可以用 kubectl get clusterrole 查看。

另外，Kubernetes 还提供了四个预先定义好的 ClusterRole 来供用户直接使用，它们是：

- cluster-admin：超管
- admin：普通管理权限
- edit：修改权限
- view：只读权限

我们在定义 RoleBinding 或 ClusterRolebinding 的时候可以直接使用。

**Role - Authorization**

![image-20220418183514597](image/role-auth.png)

**RoleBinding - Authorization**

`<img src="/Users/guomingxia/Library/Application Support/typora-user-images/image-20220418182604251.png" alt="image-20220418182604251" style="zoom:50%;" />`

`<img src="/Users/guomingxia/Library/Application Support/typora-user-images/image-20220418182837085.png" alt="image-20220418182837085" style="zoom:55%;" />`

### Admission Control

- AlwaysPullImages
- DefaultStorageClass
- DefaultTolerationSeconds
- DenyEscalatingExec
- EventRateLimit
- ImagePolicyWebhook
- LimitRanger/ResourceQuota
- PersistentVolumeClaimResize
- PodSecurityPolicy

`<img src="/Users/guomingxia/Library/Application Support/typora-user-images/image-20220418182931121.png" alt="image-20220418182931121" style="zoom:50%;" />`

`<img src="/Users/guomingxia/Library/Application Support/typora-user-images/image-20220418182957776.png" alt="image-20220418182957776" style="zoom:50%;" />`

**Request/Response**

`<img src="/Users/guomingxia/Library/Application Support/typora-user-images/image-20220418183041455.png" alt="image-20220418183041455" style="zoom:50%;" />`

## 6. Networking

- k8s组网要求：
  - Pod 中的所有容器都可以不受阻碍地相互通信。
  - 所有的Pods之间可以在不使用[NAT网络地址转换](https://links.jianshu.com/go?to=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F网络地址转换)的情况下相互通信
  - 所有的Nodes之间可以在不使用NAT网络地址转换的情况下相互通信
  - 每个Pod自己看到的自己的ip和其他Pod看到的一致
- k8s网络模型设计原则
  - 每个Pod都拥有一个独立的 IP地址，而且 假定所有 Pod 都在一个可以直接连通的、扁平的网络空间中 。
  - 不管它们是否运行在同 一 个 Node (宿主机)中，都要求它们可以直接通过对方的 IP 进行访问。
  - 设计这个原则的原因 是，用户不需要额外考虑如何建立 Pod 之间的连接，也不需要考虑将容器端口映射到主机端口等问题。
    需要解决的网络问题：

* Container-to-Container的网络
  - Containers within a pod exist within the **same network namespace** and share an IP.
  - Enables intrapod communication over *localhost*.

- Pod-to-Pod
  - Allocated **cluster unique IP** for the duration of its life cycle.
  - Pods themselves are fundamentally ephemeral.
  - **pod与pod之间的网络：首先pod自身拥有一个IP地址，不同pod之间直接使用IP地址进行通信即可**
  - 同一台node节点上pod和pod通信
    - veth对就是一个成对的端口，所有从这对端口一端进入的数据包，都将从另一端出来。
    - **为了让多个Pod的网络命名空间链接起来，我们可以让veth对的一端链接到root网络命名空间（宿主机的），另一端链接到Pod的网络命名空间。**
    - **还需要用到一个Linux以太网桥，它是一个虚拟的二层网络设备，目的就是把多个以太网段连接起来，它维护一个转发表，通过查看每个设备mac地址决定转发，还是丢弃数据**
    - pod1-->pod2（同一台node上），pod1通过自身eth0网卡发送数据，eth0连接着veth0，网桥把veth0和veth1组成了一个以太网，然后数据到达veth0之后，网桥通过转发表，发送给veth1，veth1直接把数据传给pod2的eth0。
  - 不同node节点上pod和pod通信

* Pod-to-Service
  * managed by **kube-proxy** and given a **persistent cluster unique IP**
  * exists beyond a Pod’s lifecycle.
* External-to-Service 的网络
  * Handled by **kube-proxy**.
  * Works in cooperation with a cloud provider or other external entity (load balancer).
* 

k8s网络分三个层面（由里到外）：

1. 容器网络（不同容器之间怎么相互访问）
2. 集群内网络（不同节点之间怎么相互访问）
3. 集群外网络（集群外怎么访问到集群内的服务）

### 6.1 Container-to-Container 网络

**pod中每个docker容器和pod在一个网络命名空间内，所以ip和端口等等网络配置，都和pod一样**，这是通过docker的一种网络模式：container 模式来实现的。新创建的Docker容器不会创建自己的网卡，配置自己的 IP，而是和一个指定的容器共享 IP、端口范围等。
同一个pod内共享网络命名空间，容器之间通过访问127.0.0.1:（端口）即可。

container模式是bridge和host模式的合体，优先以bridge方式启动启动第一个容器，后面的所有容器启动时，均指定网络模式为container，它们均共享第一个容器的网络资源，除了网络资源，其他资源，容器彼此之间依然是相互隔离的。

图中的veth\*即指veth对的一端（另一端未标注，但实际上是成对出现），该veth对是由Docker Daemon挂载在docker0网桥上，另一端添加到容器所属的网络命名空间，图上显示是容器中的eth0。
图中演示了bridge模式下的容器间通信。docker1向docker2发送请求，docker1，docker2均与docker0建立了veth对进行通讯。

当请求经过docker0时，由于容器和docker0同属于一个子网，因此请求经过docker2与docker0的veth\*对，转发到docker2，该过程并未跨节点，因此不经过eth0。

### 6.2 Pod to Pod 网络

#### 6.2.1 同一台节点上pod和pod通信

同一Node中Pod的默认路由都是docker0的地址，由于它们关联在同一个docker0网桥上，地址网段相同，所以它们之间应当是能直接通信的。来看看实际上这一过程如何实现。对pod外的请求通过pod1和Docker0网桥的veth对（图中挂在eth0和ethx上）实现。访问另一个pod内的容器，其请求的地址是PodIP而非容器的ip，实际上也是同一个子网间通信，直接经过veth对转发即可。

#### 6.2.2 不同节点上pod和pod通信

### 6.1 容器网络

熟悉docker的同学会知道，docker创建的容器之间会通过一张docker0的网卡相互通信。而k8s社区为了方便用户适应各自的网络情况，暴露出一套api接口——cni，用户只要实现了这套接口就可以自定义容器网络配置策略。

CNI（Container Network Interface）是由一组用于配置Linux容器的网络接口的规范和库组成，同时还包含了一些插件。CNI仅关心容器创建时的网络分配，和当容器被删除时释放网络资源。通过此链接浏览该项目：https://github.com/containernetworking/cni。

1 cni设计考量点
容器运行时必须在调用任何插件之前为容器创建一个新的网络命名空间。
然后，运行时必须确定这个容器应属于哪个网络，并为每个网络确定哪些插件必须被执行。
网络配置采用JSON格式，可以很容易地存储在文件中。网络配置包括必填字段，如name和type以及插件（类型）。网络配置允许字段在调用之间改变值。为此，有一个可选的字段args，必须包含不同的信息。
容器运行时必须按顺序为每个网络执行相应的插件，将容器添加到每个网络中。
在完成容器生命周期后，运行时必须以相反的顺序执行插件（相对于执行添加容器的顺序）以将容器与网络断开连接。
容器运行时不能为同一容器调用并行操作，但可以为不同的容器调用并行操作。
容器运行时必须为容器订阅ADD和DEL操作，这样ADD后面总是跟着相应的DEL。 DEL可能跟着额外的DEL，但是，插件应该允许处理多个DEL（即插件DEL应该是幂等的）。
容器必须由ContainerID唯一标识。存储状态的插件应该使用（网络名称，容器ID）的主键来完成。
运行时不能调用同一个网络名称或容器ID执行两次ADD（没有相应的DEL）。换句话说，给定的容器ID必须只能添加到特定的网络一次。

2 cni插件
bridge：创建网桥，并添加主机和容器到该网桥
ipvlan：在容器中添加一个ipvlan接口
ipvlan类似于macvlan，区别在于端点具有相同的mac地址。 ipvlan支持L2（链路层）和L3（网络层）模式。 在ipvlan L2模式下，每个端点获得相同的mac地址但不同的ip地址。 在ipvlan l3模式下，数据包在端点之间路由，提供了更好的可伸缩性。
loopback：创建一个回环接口
macvlan：创建一个新的MAC地址，将所有的流量转发到容器
以往，我们只能为一块以太网卡添加多个IP地址，却不能添加多个MAC地址，因为MAC地址正是通过其全球唯一性来标识一块以太网卡的，即便你使用了创建ethx:y这样的方式，你会发现所有这些“网卡”的MAC地址和ethx都是一样的，本质上，它们还是一块网卡，这将限制你做很多二层的操作。有了MACVLAN技术，你可以这么做了。
MACVLAN技术是一种将一块以太网卡虚拟成多块以太网卡的极简单的方案。
ptp：创建veth对
vlan：分配一个vlan设备
VLAN 技术主要就是在二层数据包的包头加上tag 标签，表示当前数据包归属的vlan 号。VLAN的主要优点: (1)广播域被限制在一个VLAN内,节省了带宽,提高了网络处理能力。 (2)增强局域网的安全性:VLAN间不能直接通信,即一个VLAN内的用户不能和其它VLAN内的用户直接通信,而需要通过路由器或三层交换机等三层设备。 (3)灵活构建虚拟工作组:用VLAN可以划分不同的用户到不同的工作组,同一工作组的用户也不必局限于某一固定的物理范围,网络构建和维护更方便灵活。

3 ip分配
作为容器网络管理的一部分，CNI插件需要为接口分配（并维护）IP地址，并安装与该接口相关的所有必要路由。这给了CNI插件很大的灵活性，但也给它带来了很大的负担。众多的CNI插件需要编写相同的代码来支持用户需要的多种IP管理方案（例如dhcp、host-local）。
为了减轻负担，使IP管理策略与CNI插件类型解耦，我们定义了IP地址管理插件（IPAM插件）。CNI插件的职责是在执行时恰当地调用IPAM插件。 IPAM插件必须确定接口IP/subnet，网关和路由，并将此信息返回到“主”插件来应用配置。 IPAM插件可以通过协议（例如dhcp）、存储在本地文件系统上的数据、网络配置文件的“ipam”部分或上述的组合来获得信息。



#### calico

#### VCN
### 6.2 集群内网络

**pod的ip地址是不持久的，当集群中pod的规模缩减或者pod故障或者node故障重启后，新的pod的ip就可能与之前的不一样的。所以k8s中衍生出来Service来解决这个问题。**

k8s定义了一种资源Service，Kubernetes Service 定义了这样一种抽象：一个 Pod 的逻辑分组，一种可以访问它们的策略 —— 通常称为微服务。 这一组 Pod 能够被 Service 访问到，通常是通过 Label Selector实现的。

对 Kubernetes 集群中的应用，Kubernetes 提供了简单的 Endpoints API，只要 Service 中的一组 Pod发生变更，应用程序就会被更新。 对非 Kubernetes 集群中的应用，Kubernetes 提供了基于 VIP（虚拟IP） 的网桥的方式访问 Service，再由 Service 重定向到相应的 Pod。

在 Kubernetes 集群中，每个 Node 运行一个 **kube-proxy**(服务代理) 进程。kube-proxy 负责为 Service 实现了一种 VIP（虚拟 IP）的形式，而不是 ExternalName 的形式。

服务代理模式主要分三种：

**1 userspace 代理模式**
kube-proxy 会监视 Kubernetes master 对 Service 对象和 Endpoints 对象的添加和移除。 对每个 Service，它会在本地 Node 上打开一个端口（随机选择）。 任何连接到“代理端口”的请求，都会被代理到 Service 的 Pods 中的某个上面。 使用哪个 Pod，是基于 Service 的 SessionAffinity 来确定的。 最后，它安装 iptables 规则，捕获到达该 Service 的 clusterIP（是虚拟 IP）和 Port 的请求，并重定向到代理端口，代理端口再代理请求到 backend Pod。

**2 iptables代理模式**
kube-proxy 会监视 Kubernetes master 对 Service 对象和 Endpoints 对象的添加和移除。 对每个 Service，它会安装 iptables 规则，从而捕获到达该 Service 的 clusterIP（虚拟 IP）和端口的请求，进而将请求重定向到 Service 的一组 backend 中的某个上面。 对于每个 Endpoints 对象，它也会安装 iptables 规则，这个规则会选择一个 backend Pod。

**3 ipvs代理模式**
kube-proxy会监视Kubernetes Service对象和Endpoints，调用netlink接口以相应地创建ipvs规则并定期与Kubernetes Service对象和Endpoints对象同步ipvs规则，以确保ipvs状态与期望一致。访问服务时，流量将被重定向到其中一个后端Pod。

---

pod to service
**pod的ip地址是不持久的，当集群中pod的规模缩减或者pod故障或者node故障重启后，新的pod的ip就可能与之前的不一样的。所以k8s中衍生出来Service来解决这个问题。**

Service管理了多个Pods，每个Service有一个虚拟的ip,要访问service管理的Pod上的服务只需要访问你这个虚拟ip就可以了，这个虚拟ip是固定的，当service下的pod规模改变、故障重启、node重启时候，对使用service的用户来说是无感知的，因为他们使用的service的ip没有变。

**当数据包到达Service虚拟ip后，数据包会被通过k8s给该servcie自动创建的负载均衡器路由到背后的pod容器。**

- 在k8s里，iptables规则是由kube-proxy配置，kube-proxy监视APIserver的更改，因为集群中所有service（iptables）更改都会发送到APIserver上，所以每台kubelet-proxy监视APIserver，当对service或pod虚拟IP进行修改时，kube-proxy就会在本地更新，以便正确发送给后端pod
- **pod到service包的流转：**

### 6.3 External-to-Service

让Internet流量进入k8s集群，这特定于配置的网络，可以在网络堆栈的不同层来实现：
（1） [NodePort](#### 3.6.2 NodePort Service)
（2）Service LoadBalancer
（3）Ingress控制器

Ingress 是从Kubernetes集群外部访问集群内部服务的入口。

通常情况下，service和pod仅可在集群内部网络中通过IP地址访问。所有到达边界路由器的流量或被丢弃或被转发到其他地方。Ingress是授权入站连接到达集群服务的规则集合。

你可以给Ingress配置提供外部可访问的URL、负载均衡、SSL、基于名称的虚拟主机等。用户通过POST Ingress资源到API server的方式来请求ingress。 Ingress controller负责实现Ingress，通常使用负载平衡器，它还可以配置边界路由和其他前端，这有助于以HA方式处理流量。

通过一个公开的ip地址来公开多个服务，第7层网络流量入口是在网络堆栈的HTTP / HTTPS协议范围内运行，并建立在service之上。

**工作**：客户端现针对www.1234.com执行dns解析，DNS服务器返回ingress控制器的ip，客户端拿到ip后，向ingress控制器发送http的get请求，将域名加在host头部发送。控制器接收到请求后，**从host头部就知道了该访问哪一个服务，通过与该service关联的endpoint对象查询podIP地址，将请求进行转发**

第7层负载均衡器的一个好处是它们具有HTTP感知能力，因此它们了解URL和路径。 这允许您按URL路径细分服务流量。 它们通常还在HTTP请求的X-Forwarded-For标头中提供原始客户端的IP地址。

## 7. Storage object

Pods by themselves are useful, but many workloads require **exchanging data** between containers, or **persisting** some form of **data**.

For this we have 4 ‘types’ of storage

* **Volumes**
* **PersistentVolumes**
* **PersistentVolumeClaims**
* **StorageClasses**

> ●PV’s and PVCs work great together, but still require some manual provisioning under the hood.
>
> ●What if we could do all that dynamically? Well, you can with StorageClasses
>
> ●Act as an abstraction on top of a external storage resource that has dynamic provisioning capability
>
> ○usually the cloud providers, but others work like ceph

### 7.1 Volumes

Volume 就是卷的概念，它是用来**管理 Kubernetes 存储的**，是**用来声明在 Pod 中的容器可以访问文件目录的**，一个卷可以被挂载在 Pod 中一个或者多个容器的指定路径下面。

<img src="./assets/k8s-volume.png" style="zoom:50%;" />

而 Volume 本身是一个抽象的概念，一个 Volume 可以去**支持多种的后端的存储。**比如说 Kubernetes 的 Volume 就支持了很多存储插件，它可以支持**本地的存储**，可以支持**分布式的存储**，比如说像 ceph，GlusterFS ；它也可以支持云存储，比如说阿里云上的云盘、AWS 上的云盘、Google 上的云盘等等。

A volume is a directory, possibly with some data in it, which is accessible to a Container as part of its  filesystem.

* Storage that is tied to the **Pod’s Lifecycle**. A Volume is defined in the pod Spec and tied to its lifecycle
* A pod can have one or more types of volumes attached to it.
* Can be consumed by any of the containers within the pod

  * web server
  * pre-process data
  * socket files
  * logs
* Survive Pod restarts; however their durability beyond that is dependent on the Volume Type.
* **Volume Types**

  * Current list of in-tree volume types supported, with more being added through the “Container Storage Interface”
    * essentially storage plugin system supported by multiple container orchestration engines (k8s and mesos)
  * The ones in blue support persisting beyond a pod’s lifecycle, but generally are not mounted directly except through a persistent volume claim
  * emptyDir is common for scratch space between pods
  * configMap, secret, downward API, and projected are all used for injecting information stored within Kubernetes directly into the Pod
  * <img src="./assets/volume-type.png" alt="image-20220418205851972" style="zoom:50%;" />
* Volume Example
* <img src="./assets/volume-example.png" alt="image-20220418210718174" style="zoom:50%;" />

### 7.2 Persistent Volumes

* A **PersistentVolume** (PV) are k8s objects that represent underlying storage resource.
* They don’t belong to any namespace, they are a global resource.
* PVs are a **cluster wide resource** linked to a backing storage provider: NFS, GCEPersistentDisk, RBD etc.
* Generally provisioned by an administrator. users aren’t usually the ones creating PVs
* Their lifecycle is handled independently from a pod
* **CANNOT** be attached to a Pod directly. Relies on a **PersistentVolumeClaim****.** users aren’t usually the ones creating PVs

<img src="./assets/persistentvolume.png" alt="image-20220418211757526" style="zoom:50%;" />

**PV Phases**: If you get or describe a PV, you will see that they have several different states.

* Available - The PV is ready and available to be consumed.
* Bound - The PV has been bound to a PVC and is not available.
* Released - The binding PVC has been deleted. The PV is in a state that (depending on reclaimPolicy) requires manual intervention
* Failed - For some reason, Kubernetes could not reclaim the PV from the stale or deleted PVC

### 7.3 Persistent Volume Claims

* A **PersistentVolumeClaim** (PVC) is a **namespaced** request for storage. a PVC is based within a namespace (with the pod)
* Satisfies a set of requirements instead of mapping to a storage resource directly. It is a one-to-one mapping of a user claim to a global storage offer.
* Ensures that an application’s ‘*claim*’ for storage is portable across numerous backends or providers.
* A user can define specific requirements for their PVC so it gets matched with a specific PV.

`<img src="/Users/guomingxia/Library/Application Support/typora-user-images/image-20220418212016521.png" alt="image-20220418212016521" style="zoom:50%;" />`

**PVs and PVCs with Selectors**

* This example defines a PV with 2Gi of space and a label.
* The PV is using the hostPath volume type, and thus they have a label of “type: hostpath”
* The PVC is looking for 1Gi of storage and is looking for a PV with a label of “type: hostpath”
* They will match and bind because the labels match, the access modes match, and the PVC storage capacity is <= PV storage capacity

<img src="./assets/PVs-and-PVCs.png" alt="image-20220418212331384" style="zoom:50%;" />

### 7.4 StorageClass

- Storage classes are an abstraction on top of an external storage resource (PV)
- Work hand-in-hand with the external storage system to enable **dynamic provisioning** of storage by eliminating the need for the cluster admin to pre-provision a PV
- <img src="./assets/storageclass-example.png" alt="image-20220418204704687" style="zoom:50%;" />

* **Available** **StorageClasses**

<img src="./assets/available-storageclass.png" alt="image-20220418204900166" style="zoom:50%;" />

### 7.5 Storageclass and PVC

* A PVC is created with a storage request and supplies the StorageClass ‘standard’
* The storageClass ‘standard’ is configured with some information to connect and interact with the API of an external storage provider
* The external storage provider creates a PV that strictly satisfies the PVC request. Really, it means it’s the same size as the request

  * The PV will be named pvc-\<uid of the pvc\>
* The PV is then bound to the requesting PVC

<img src="./assets/StorageClass-and-PVC.png" alt="image-20220418212844175" style="zoom:50%;" />

### 7.6 PV and PVC

- PersistentVolume(PV)是集群中的一块存储卷，可以由管理员手动设置， 或当用户创建 PersistentVolumeClaim(PVC)时根据 StorageClass 动 态设置。
- PV 和 PVC 与 Pod 生命周期无关。也就是说，当 Pod 中的容器重新启动、 Pod 重新调度或者删除时，PV 和 PVC 不会受到影响，Pod 存储于 PV 里 的数据得以保留。
- 对于不同的使用场景，用户通常需要不同属性(例如性能、访问模式等) 的 PV。

**Persistent Volumes and Claims**

* PVCs can be named the same to make things consistent but point to different storage classes
* In this example we have a dev and prod namespace. These PVCs are named the same, but reside within different namespaces and request different classes of storage.

![](image/PVs-and-PVCs.png)

### 7.5 **Working with Volumes**

Lab - github.com/mrbobbytables/k8s-intro-tutorials/blob/master/storage

## **资源管理

- 资源请求与限制（CPU、内存）
- QoS 类别


## 8. **Configuration**

Kubernetes has an integrated pattern for decoupling configuration from application or container.

This pattern makes use of two Kubernetes components: **ConfigMaps** and **Secrets.**

> There are instances in your application where you want to be able to store runtime-specific information.
> Things like connection info, SSL certs, certain flags that you will inevitably change over time.
> The Kubernetes takes that into account and has a solution with ConfigMaps and Secrets.

### 8.1 ConfigMap

- ConfigMap 用来将非机密性的数据保存到键值对中。
- 使用时， Pods 可以将其用作环境变量、命令行参数或者存储卷中的配置文件。
- ConfigMap 将环境配置信息和 容器镜像解耦，便于应用配置的修改。

* **ConfigMap**

  * Externalized data stored within kubernetes. Configmap data is stored “outside” of the cluster (in etcd)
* **ConfigMap Example**

  * **data**: Contains key-value pairs of ConfigMap contents.
    * ![](image/ConfigMap-example.png)
* Can be created from a manifest, literals, directories, or files directly.
	* ![](image/create-ConfigMap.png)

* Can be referenced through several different means:

  * environment variable at runtime
  * a command line argument (via env var)
  * injected as a file into a volume mount

### 8.2 **Secret**

- Secret 是用来保存和传递密码、密钥、证书这些敏感信息的对象。
- 使用 Secret 的好处是可以避免把敏感信息明文写在配置文件里。
- Kubernetes 集群中配置和使用服务不可避免的要用到各种敏感信息实现登录、认 证等功能，例如访问 AWS 存储的用户名密码。
- 为了避免将类似的敏感信息明文写在所有需要使用的配置文件中，可以将这些信息 存入一个 Secret 对象，而在配置文件中通过 Secret 对象引用这些敏感信息。
- 这种方式的好处包括:意图明确，避免重复，减少暴漏机会。

* **Secret**

  * Functionally identical to a ConfigMap.
  * Stored as **base64 encoded content.**
  * Encrypted at rest within etcd (**if configured!**).
  * Stored on each worker node in tmpfs directory.
  * Ideal for username/passwords, certificates or other sensitive information that should not be stored in a container.
  * and can be created the same way as configmaps
* **Secret Example**

<img src="./assets/secret-example.png" alt="image-20220418201946677" style="zoom:50%;" />

* **Secret Creation Example**
  * Manifest , literals, directories, or files.

<img src="./assets/create-secret.png" alt="image-20220418201802353" style="zoom:50%;" />

### 8.3 **Injecting Configuration**

![](image/inject-as-env.png)

![](image/inject-in-command.png)

![](image/inject-as-volume.png)
## 9. Scheduling, Preemption, eviction

- [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Pod Overhead](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/)
- [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [Scheduling Framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework)
- [Scheduler Performance Tuning](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
- [Resource Bin Packing for Extended Resources](https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/)

### Scheduling

### Node Affinity

https://www.golinuxcloud.com/kubernetes-node-affinity/

### Taint

```sh
kubectl taint nodes <node_name> key1=value1:NoSchedule # taint node, This means that no pod will be able to schedule onto node1 unless it has a matching toleration.
kubectl taint nodes <node_name> key1=value1:NoSchedule- # untaint node
```

Control scheduling with node taints: https://cloud.google.com/kubernetes-engine/docs/how-to/node-taints

### Toleration

You specify a toleration for a pod in the PodSpec. Both of the following tolerations "match" the taint created by the `kubectl taint` line above, and thus a pod with either toleration would be able to schedule onto `node1`:

```
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoSchedule"
  
-------------------------------------------------
  
tolerations:
- key: "key1"
  operator: "Exists"
  effect: "NoSchedule"
```

## Container Runtime

## 服务网格
    
    - Istio
    - Linkerd
    - Consul


## 9 健康检查

K8S中通过探针对容器执行定期诊断来判断容器的状态
* 探针类型:
	* LivenessProbe：探测应用是否处于健康状态，如果不健康则删除并重新创建容器。探测容器是否正在运行。如果存活探测失败，则 kubelet 会杀死容器，并且容器将受到其重启策略的影响。如果容器不提供存活探针，则默认状态为 Success。
	* ReadinessProbe：探测应用是否就绪并且处于正常服务状态，如果不正常则不会接收来自Kubernetes Service 的流量。 如果不正常不会重启容器。探测容器是否准备好服务请求。如果就绪探测失败，端点控制器将从与 Pod 匹配的所有Service的端点中删除该Pod的IP地址。初始延迟之前的就绪状态默认为 Failure。如果容器不提供就绪探针，则默认状态为 Success。
	* StartupProbe：探测应用是否启动完成，如果在 failureThreshold*periodSeconds 周期内未就绪，则会应用进程会被重启。
* 探活方式:
	* Command Exec
	* TCP socket: 端口检查，网络连通性检查
	* HTTP API: 

健康检查 spec:

```yaml
apiVersion: extensions/v1beta1 
kind: Deployment
metadata:
	labels: 
		app: nginx
	name: nginx-default 
spec:
	replicas: 3 
	selector:
		matchLabels: 
			app: nginx
	template: 
		metadata:
			labels: 
				app: nginx
		spec: 
			containers:
			- image: nginx 
				imagePullPolicy: Always 
				name: http
				resources: {} 
				terminationMessagePath:/dev/termination-log 
				terminationMessagePolicy: File resources:
					limits:
						cpu: "500m" 
						memory: "128Mi"
				livenessProbe: 
					httpGet: 
						path: /
						port: 80 
					failureThreshold: 10 # 出多少次错误才认为是fail
					initialDelaySeconds: 15 # 等几秒做检查
					periodSeconds: 15 # 间隔多少秒
					successThreshold: 1
					timeoutSeconds: 1 # 多少时间超时
				readinessProbe: 
					httpGet:
						path: /ping
						port: 80 
					initialDelaySeconds: 5 
					timeoutSeconds: 1
```


 diagnostics

k8s Liveness Probe

Kubernetes Liveness Probes | Practical Guide and Best Practices: https://komodor.com/learn/kubernetes-liveness-probes-a-practical-guide/

## 9. Metrics and Monitoring

**Metrics API server**

* Metric server collects metrics such as **CPU** and **Memory** by each pod and node from the Summary API, exposed by [Kubelet](https://kubernetes.io/docs/admin/kubelet/) on each node.
* Metrics Server registered in the main API server through [Kubernetes aggregator](https://kubernetes.io/docs/concepts/api-extension/apiserver-aggregation/), which was introduced in Kubernetes 1.7

**HPA (horizontal pod** **autoscaler**)

<img src="./assets/hpa.png" alt="image-20220418194256223" style="zoom:50%;" />

<img src="./assets/HPA-example.png" alt="image-20220418194429824" style="zoom:70%;" />

**Prometheus** & **Grafana (dashboards)**

![image-20220418194546676](image/prometheus.png)

**Fluentd** **(log shipping)**

![image-20220418194623430](image/fluentd.png)

![image-20220418194703160](image/logging-33.png)

## 9 Extend k8s

1. **kubectl plugins**: Users often interact with the Kubernetes API using `kubectl`. [Kubectl plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/) extend the kubectl binary. They only affect the individual user's local environment, and so cannot enforce site-wide policies.
2. **API server extensions** : The apiserver handles all requests. Several types of extension points in the apiserver allow authenticating requests, or blocking them based on their content, editing content, and handling deletion. These are described in the API Access Extensions section.
3. **Custom resources** : The apiserver serves various kinds of resources. Built-in resource kinds, like pods, are defined by the Kubernetes project and can't be changed. You can also add resources that you define, or that other projects have defined, called Custom Resources, as explained in the Custom Resources section. Custom Resources are often used with API Access Extensions.
4. **Scheduler extensions**: The Kubernetes scheduler decides which nodes to place pods on. There are several ways to extend scheduling. These are described in the Scheduler Extensions section.
5. **Controller extensions**: Much of the behavior of Kubernetes is implemented by programs called Controllers which are clients of the API-Server. Controllers are often used in conjunction with Custom Resources.
6. **kubelet network plugins**: The kubelet runs on servers, and helps pods appear like virtual servers with their own IPs on the cluster network. Network Plugins allow for different implementations of pod networking.
7. **kubelet storage plugins**: The kubelet also mounts and unmounts volumes for containers. New types of storage can be supported via Storage Plugins.

[Extending Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/)

### 9.1 API Extensions

[CustomResourceDefinitions](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#customresourcedefinition-v1beta1-apiextensions)

[Extend the Kubernetes API with CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)

[Custom Resources concept guide](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

**kubernetes二次开发（主要是开发满足自己业务的api）: client-go**

使用 client-go 控制原生及拓展的 Kubernetes API | PPT 实录: https://www.kubernetes.org.cn/1309.html

如何基于Kubernetes开发自定义的Controller: [https://www.kubernetes.org.cn/3655.html](https://www.kubernetes.org.cn/3655.html)

### 9.2 Infrastructure Extensions

Go clients for talking to a [kubernetes](http://kubernetes.io/) cluster:https://github.com/kubernetes/client-go

[源码分析] client-go的使用及源码分析: https://www.huweihuang.com/article/source-analysis/client-go-source-analysis/

## 9.K8s Pluggability

Kubernetes is highly configurable and extensible.

**Kubernetes extension points**：

* k8s Extensibility -- Infrastructure
  * Container Runtime (CRI)
  * Network Plugin (CNI)
  * Volumes (CSI)
  * Cloud Controller Manager (AWS, GCP, Azure)
  * Device Plugins (GPU, FPGAs, QRNGs)
  * Secret Backend (Vault, Azure, AWS, GCP, KMS)
  * Replace scheduler
  * Multiple scheduler
  * Schduler Extender
  * Custom Controller
* k8s Extensibility -- API
  * API(-server) Aggregation
  * Custom Resource Definition

Operator Pattern

### 9.1 CRD

CustomResourceDefinition

**Custom resources** : The apiserver serves various kinds of resources. Built-in resource kinds, like pods, are defined by the Kubernetes project and can't be changed. You can also add resources that you define, or that other projects have defined, called Custom Resources, as explained in the Custom Resources section. Custom Resources are often used with API Access Extensions.

- CRD是对k8s对象的扩展
- CRD 就像数据库的开放式表结构，允许用户自定义 Schema。
- 有了这种开放式设计，用户可以基于 CRD 定义一切需要的模型，满足不同 业务的需求。
- 社区鼓励基于 CRD 的业务抽象，众多主流的扩展应用都是基于 CRD 构建 的，比如 Istio、Knative，Calico。
- 甚至基于 CRD 推出了 Operator Mode 和 Operator SDK，可以以极低的 开发成本定义新对象，并构建新对象的控制器

### 9.2 Custom Controller

Create sample controller: [https://github.com/kubernetes/sample-controller/blob/master/controller.go](https://github.com/kubernetes/sample-controller/blob/master/controller.go)

clinet-go:

client-go 是 Kubernetes 官方推出的一个库，方便我们来调用 Kubernetes 的 RESTful API。

### 什么是 Informer 机制

Informer 是 client-go 中的核心工具包，已经被 kubernetes 中众多组件所使用。所谓 Informer，其实就是一个带有本地缓存和索引机制的、可以注册 EventHandler 的 client，本地缓存被称为 Store，索引被称为 Index。使用 informer 的目的是为了减轻 apiserver 数据交互的压力而抽象出来的一个 cache 层, 客户端对 apiserver 数据的 "读取" 和 "监听" 操作都通过本地 informer 进行。

Informer 的主要功能：

* 同步数据到本地缓存
* 根据对应的事件类型，触发事先注册好的 ResourceEventHandle

我们知道Kubernetes各个组件都是通过REST API跟API Server交互通信的，而如果每次每一个组件都直接跟API Server交互去读取/写入到后端的etcd的话，会对API Server以及etcd造成非常大的负担。 而Informer机制是为了保证各个组件之间通信的实时性、可靠性，并且减缓对API Server和etcd的负担。

### Informer 需要满足哪些要求？

* 消息可靠性
* 消息实时性
* 消息顺序性
* 高性能

Controller 流程

* 典型的 controller 一般会有一个或者多个 informer 来跟踪 resource，把最新的状态反映到本地的 cache 中。
* Informer 首先会 list/watch apiserver，Informer 所使用的 Reflector 包负责与 apiserver 建立连接，Reflector 使用 ListAndWatch 的方法，会先从 apiserver 中 list 该资源的所有实例，list 会拿到该对象最新的 resourceVersion，然后使用 watch 方法监听该 resourceVersion 之后的所有变化，若中途出现异常，reflector 则会从断开的 resourceVersion 处重现尝试监听所有变化，一旦该对象的实例有创建、删除、更新动作，Reflector 都会收到"事件通知"，这时，该事件及它对应的 API 对象这个组合，被称为增量（Delta），它会被放进 DeltaFIFO 中。
* Informer 会不断地从这个 DeltaFIFO 中读取增量，每拿出一个对象，Informer 就会判断这个增量的时间类型，然后创建或更新本地的缓存，也就是 store。
* 如果事件类型是 Added（添加对象），那么 Informer 会通过 Indexer 的库把这个增量里的 API 对象保存到本地的缓存中，并为它创建索引，若为删除操作，则在本地缓存中删除该对象。
* DeltaFIFO 再 pop 这个事件到 controller 中，controller 会调用事先注册的 ResourceEventHandler 回调函数进行处理。
* 在 ResourceEventHandler 回调函数中，其实只是做了一些很简单的过滤，然后将关心变更的 Object 放到 workqueue 里面。
* Controller 从 workqueue 里面取出 Object，启动一个 worker 来执行自己的业务逻辑，业务逻辑通常是计算目前集群的状态和用户希望达到的状态有多大的区别，然后孜孜不倦地让 apiserver 将状态演化到用户希望达到的状态，比如为 deployment 创建新的 pods，或者是扩容/缩容 deployment。
* **在**worker**中就可以使用** lister **来获取** resource**，而不用频繁的访问** apiserver**，因为** apiserver **中** resource **的变更都会反映到本地的** cache **中。**

client 类型

下面介绍 client-go 中的三种 client。

**Clientset**

Clientset 是我们最常用的 client，你可以在它里面找到 kubernetes 目前所有原生资源对应的 client。 获取方式一般是，指定 group 然后指定特定的 version，然后根据 resource 名字来获取到对应的 client。

**Dynamic Client**

Dynamic client 是一种动态的 client，它能同时处理 kubernetes 所有的资源。并且同时，它也不同于 clientset，dynamic client 返回的对象是一个 map[string]interface{}，如果一个 controller 中需要控制所有的 API，可以使用dynamic client，目前它被用在了 garbage collector 和 namespace controller。

**RESTClient**

RESTClient 是 clientset 和 dynamic client 的基础，前面这两个 client 本质上都是 RESTClient，它提供了一些 RESTful 的函数如 Get()，Put()，Post()，Delete()。由 Codec 来提供序列化和反序列化的功能。

**如何选择 Client 的类型呢?**
如果你的 Controller 只是需要控制 Kubernetes 原生的资源，如 Pods，Nodes，Deployments等，那么 clientset 就够用了。

如果你需要使用 ThirdPartyResource 来拓展 Kubernetes 的 API，那么需要使用 Dynamic Client 或 RESTClient。

需要注意的是，Dynamic Client 目前只支持 JSON 的序列化和反序列化。

在1.7+版本需要将 ThirdPartyResource 迁移到 CustomResourceDefinition

## 10 垃圾回收
https://cloud.tencent.com/developer/article/1880506
镜像回收
容器回收
## 12. K8s 升级策略

通过 k8s 的服务发现机制能容易地获得 Service 对应 IP 和 Port。k8s 支持 2 种基本的服务发现模式：环境变量和 DNS。


##  滚动升级&回滚部署
滚动升级：不中断服务情况下对应用程序进行升级，通过控制器逐步将旧版本的pod替换为新版本的pod，减少服务中断时间，同时保证应用程序的稳定性。

https://blog.csdn.net/weixin_36755535/article/details/129855972
Kubernetes升级策略有
1. 滚动更新（Rolling Update）：这是最常见的更新策略。它允许逐步替换旧版本的Pod实例，确保应用程序在更新过程中保持可用。滚动更新适用于无状态应用，并且允许您指定更新速率和同时更新的Pod数量。
2. 蓝绿部署（Blue/Green Deployment）：蓝绿部署是一种在新旧版本之间进行切换的策略。在蓝绿部署中，您先部署一个全新的版本（绿色），然后在切换时将流量从旧版本（蓝色）切换到新版本。这种策略允许您在部署过程中立即回滚到旧版本，以应对意外问题。
3. 金丝雀发布（Canary Release）：金丝雀发布是一种渐进性更新策略。它允许您在生产环境中逐渐引入新版本的应用程序，只将少量流量路由到新版本，以评估其性能和稳定性。如果新版本稳定，可以逐渐增加流量份额，直至完全替换旧版本。
4. 滚动回滚（Rolling Rollback）：当滚动更新出现问题或新版本存在严重错误时，滚动回滚策略允许您回滚到之前的版本，以恢复到一个稳定的状态。
5. 逐一替换（Recreate）：逐一替换策略简单粗暴，它直接删除旧版本的Pod并创建新版本的Pod。这种策略会导致应用程序在更新过程中短暂的不可用，因为所有Pod都会同时停止和重新创建。
6. 资源限制策略：除了更新策略本身，Kubernetes还支持使用资源限制来控制更新过程中的资源消耗。您可以在更新期间指定资源限制，以确保集群资源的稳定分配。


## 10 k8s Troubleshooting

### command

* The Ultimate Kubectl Commands Cheat Sheet: https://komodor.com/learn/the-ultimate-kubectl-cheat-sheet/
* Kubernetes Troubleshooting – The Complete Guide: https://komodor.com/learn/kubernetes-troubleshooting-the-complete-guide/
* Debugging Your Kubernetes Cluster, Pods, and Containers | Tutorial & Kubectl Examples: https://www.containiq.com/post/debugging-your-kubernetes-cluster-pods-and-containers

### 0. The Three Pillars of k8s Troubleshooting

There are three aspects to effective troubleshooting in a Kubernetes cluster: understanding the problem, managing and remediating the problem, and preventing the problem from recurring.

**understanding**

In a Kubernetes environment, it can be very difficult to understand what happened and determine the root cause of the problem. This typically involves:

- Reviewing recent changes to the affected cluster, pod, or node, to see what caused the failure.
- Analyzing YAML configurations, Github repositories, and logs for VMs or bare metal machines running the malfunctioning components.
- Looking at Kubernetes events and metrics such as disk pressure, memory pressure, and utilization. In a mature environment, you should have access to dashboards that show important metrics for clusters, nodes, pods, and containers over time.
- Comparing similar components behaving the same way, and analyzing dependencies between components, to see if they are related to the failure.

To achieve the above, teams typically use the following technologies:

- **Monitoring Tools:** Datadog, Dynatrace, Grafana, New Relic
- **Observability Tools:** Lightstep, Honeycomb
- **Live Debugging Tools:** OzCode, Rookout
- **Logging Tools:** Splunk, LogDNA, Logz.io

**Management**

In a microservices architecture, it is common for each component to be developed and managed by a separate team. Because production incidents often involve multiple components, collaboration is essential to remediate problems fast.

Once the issue is understood, there are three approaches to remediating it:

- **Ad hoc solutions**—based on tribal knowledge by the teams working on the affected components. Very often, the engineer who built the component will have unwritten knowledge on how to debug and resolve it.
- **Manual runbooks**—a clear, documented procedure showing how to resolve each type of incident. Having a runbook means that every member of the team can quickly resolve the issue.
- **Automated runbooks**—an automated process, which could be implemented as a script, infrastructure as code (IaC) template, or Kubernetes operator, and is triggered automatically when the issue is detected. It can be challenging to automate responses to all common incidents, but it can be highly beneficial, reducing downtime and eliminating human error.

To achieve the above, teams typically use the following technologies:

- **Incident Management:** PagerDuty, Kintaba
- **Project Management:** Jira, Monday, Trello
- **Infrastructure as Code:** Amazon CloudFormation, Terraform

**Prevention**

Successful teams make prevention their top priority. Over time, this will reduce the time invested in identifying and troubleshooting new issues. Preventing production issues in Kubernetes involves:

- Creating policies, rules, and playbooks after every incident to ensure effective remediation
- Investigating if a response to the issue can be automated, and how
- Defining how to identify the issue quickly next time around and make the relevant data available—for example by instrumenting the relevant components
- Ensuring the issue is escalated to the appropriate teams and those teams can communicate effectively to resolve it

To achieve the above, teams commonly use the following technologies:

- **Chaos Engineering:** Gremlin, Chaos Monkey, ChaosIQ
- **Auto Remediation:** Shoreline, OpsGenie

### 1 Troubleshooting Pods

If you’re experiencing an issue with a Kubernetes pod, and you couldn’t find and quickly resolve the error in the section above, here is how to dig a bit deeper. The first step to diagnosing pod issues is running `kubectl describe pod [name]`.

**Understanding the Output of the kubectl describe pod Command**:

Here is example output of the describe pod command, provided in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application-introspection/):

```yaml

Name:		nginx-deployment-1006230814-6winp #below this line are basic data about the pod, such as the node it is running on, its labels and current status.
Namespace:	default
Node:		kubernetes-node-wul5/10.240.0.9
Start Time:	Thu, 24 Mar 2016 01:39:49 +0000
Labels:		app=nginx,pod-template-hash=1006230814
Annotations:    kubernetes.io/created-by={"kind":"SerializedReference","apiVersion":"v1","reference":{"kind":"ReplicaSet","namespace":"default","name":"nginx-deployment-1956810328","uid":"14e607e7-8ba1-11e7-b5cb-fa16" ...
Status:		Running # current state of the pod,which can be:1.Pending 2.Running 3.Succeeded 4.Failed 5.Unknown
IP:		10.244.0.6
Controllers:	ReplicaSet/nginx-deployment-1006230814
Containers: #below this line is data about containers running on the pod (only one in this example, called nginx
  nginx:
    Container ID:	docker://90315cc9f513c724e9957a4788d3e625a078de84750f244a40f97ae355eb1149
    Image:		nginx
    Image ID:		docker://6f62f48c4e55d700cf3eb1b5e33fa051802986b77b874cc351cce539e5163707
    Port:		80/TCP
    QoS Tier:
      cpu:	Guaranteed
      memory:	Guaranteed
    Limits:
      cpu:	500m
      memory:	128Mi
    Requests:
      memory:		128Mi
      cpu:		500m
    State:		Running #the status of the container, , which can be: 1.Waiting 2.Running 3.Terminated
      Started:		Thu, 24 Mar 2016 01:39:51 +0000
    Ready:		True
    Restart Count:	0
    Environment:        [none]
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-5kdvl (ro)
Conditions:
  Type          Status
  Initialized   True
  Ready         True
  PodScheduled  True
Volumes: # storage volumes, secrets or ConfigMaps mounted by containers in the pod
  default-token-4bcbi:
    Type:	Secret (a volume populated by a Secret)
    SecretName:	default-token-4bcbi
    Optional:   false
QoS Class:      Guaranteed
Node-Selectors: [none]
Tolerations:    [none]
Events: # recent events occurring on the pod, such as images pulled, containers created and containers started
  FirstSeen	LastSeen	Count	From					SubobjectPath		Type		Reason		Message
  ---------	--------	-----	----					-------------		--------	------		-------
  54s		54s		1	{default-scheduler }						Normal		Scheduled	Successfully assigned nginx-deployment-1006230814-6winp to kubernetes-node-wul5
  54s		54s		1	{kubelet kubernetes-node-wul5}	spec.containers{nginx}	Normal		Pulling		pulling image "nginx"
  53s		53s		1	{kubelet kubernetes-node-wul5}	spec.containers{nginx}	Normal		Pulled		Successfully pulled image "nginx"
  53s		53s		1	{kubelet kubernetes-node-wul5}	spec.containers{nginx}	Normal		Created		Created container with docker id 90315cc9f513
  53s		53s		1	{kubelet kubernetes-node-wul5}	spec.containers{nginx}	Normal		Started		Started container with docker id 90315cc9f513
```

We bolded the most important sections in the `describe pod` output:

- `Name`—below this line are basic data about the pod, such as the node it is running on, its labels and current status.
- Status -- this is the current state of the pod, which can be:
  - Pending
    - Running
    - Succeeded
    - Failed
    - Unknown
- `Containers`—below this line is data about containers running on the pod (only one in this example, called nginx),
- Containers:State  —this indicates the status of the container, which can be:
  - Waiting
  - Running
  - Terminated
- `Volumes`—storage volumes, secrets or ConfigMaps mounted by containers in the pod.
- `Events`—recent events occurring on the pod, such as images pulled, containers created and containers started.

Continue debugging based on the pod state.

#### 1. CreateContainerConfigError

This error is usually the result of a missing Secret or ConfigMap. Secrets are Kubernetes objects used to store sensitive information like database credentials. ConfigMaps store data as key-value pairs, and are typically used to hold configuration information used by multiple pods.

**How to identify the issue**

Run `kubectl get pods` .

Check the output to see if the pod’s status is `CreateContainerConfigError`

```
$ kubectl get pods 
NAME                 READY   STATUS                       RESTARTS   AGE
pod-missing-config   0/1     CreateContainerConfigError   0          1m23s
```

**Getting detailed information and resolving the issue**

To get more information about the issue, run `kubectl describe [name]` and look for a message indicating which ConfigMap is missing:

```
$ kubectl describe pod pod-missing-config 
Warning Failed 34s (x6 over 1m45s) kubelet 
Error: configmap "configmap-3" not found
```

Now run this command to see if the ConfigMap exists in the cluster.

For example `$ kubectl get configmap configmap-3`

If the result is `null`, the ConfigMap is missing, and you need to create it. See the [documentation](https://kubernetes.io/docs/concepts/configuration/configmap/) to learn how to create a ConfigMap with the name requested by your pod.

Make sure the ConfigMap is available by running `get configmap [name]` again. If you want to view the content of the ConfigMap in YAML format, add the flag `-o yaml`.

Once you have verified the ConfigMap exists, run `kubectl get pods` again, and verify the pod is in status `Running`:

```
$ kubectl get pods
NAME                 READY   STATUS    RESTARTS   AGE
pod-missing-config   0/1     Running   0          1m23s
```

#### 2. ImagePullBackOff

This status means that a pod could not run because it attempted to pull a container image from a registry, and failed. The pod refuses to start because it cannot create one or more containers defined in its manifest.

**How to identify the issue**

Run the `command kubectl get pods`

Check the output to see if the pod status is `ImagePullBackOff` or `ErrImagePull`:

```
$ kubectl get pods
NAME       READY    STATUS             RESTARTS   AGE
mypod-1    0/1      ImagePullBackOff   0          58s
```

**Getting detailed information and resolving the issue**

Run the `kubectl describe pod [name]` command for the problematic pod.

The output of this command will indicate the root cause of the issue. This can be one of the following:

- **Wrong image name or tag**—this typically happens because the image name or tag was typed incorrectly in the pod manifest. Verify the correct image name using `docker pull`, and correct it in the pod manifest.
- **Authentication issue in Container registry**—the pod could not authenticate with the registry to retrieve the image. This could happen because of an issue in the Secret holding credentials, or because the pod does not have an RBAC role that allows it to perform the operation. Ensure the pod and node have the appropriate permissions and Secrets, then try the operation manually using `docker pull`.

#### 3. CrashLoopBackOff

This issue indicates a pod cannot be scheduled on a node. This could happen because the node does not have sufficient resources to run the pod, or because the pod did not succeed in mounting the requested volumes.

**How to identify the issue**

Run the command `kubectl get pods`.

Check the output to see if the pod status is `CrashLoopBackOff`

```
$ kubectl get pods
NAME       READY    STATUS             RESTARTS   AGE
mypod-1    0/1      CrashLoopBackOff   0          58s
```

**Getting detailed information and resolving the issue**

Run the `kubectl describe pod [name]` command for the problematic pod:

The output will help you identify the cause of the issue. Here are the common causes:

- **Insufficient resources**—if there are insufficient resources on the node, you can manually evict pods from the node or scale up your cluster to ensure more nodes are available for your pods.
- **Volume mounting**—if you see the issue is mounting a storage volume, check which volume the pod is trying to mount, ensure it is defined correctly in the pod manifest, and see that a storage volume with those definitions is available.
- **Use of hostPort**—if you are binding pods to a hostPort, you may only be able to schedule one pod per node. In most cases you can avoid using hostPort and use a Service object to enable communication with your pod.

#### 4. Terminating

```sh
mguo@dal3-qz2-sr1-rk403-s04:~$ kubectl get pod -n genctl -o wide | grep compute-agent-z
compute-agent-z-xn4nc   1/1  Terminating   0    25d     11.87.142.16  dal3-qz2-sr1-rk350-s14   <none>   <none>
```

```sh
mguo@dal3-qz2-sr1-rk403-s04:~$ kubectl get node | grep dal3-qz2-sr1-rk350-s14
NAME                     STATUS     ROLES                     AGE   VERSION
dal3-qz2-sr1-rk350-s14   NotReady   compute,worker            67d   v1.21.8
```

Go to 2.Troubleshooting Nodes

#### 5. Evicted

##### 5.1 Node DiskPressure

To troubleshoot the issue of node disk pressure, you need to figure out what files are taking up the most space

```kubernetes
kubectl describe pod <pod_name> -n <namespace>

Events:
  Type     Reason     Age   From               Message
  ----     ------     ----  ----               -------
  Normal   Scheduled  40m   default-scheduler  Successfully assigned genctl/image-spec-projection-controller-6bb9f79fcd-7wcdj to dal3-qz2-sr1-rk358-s07
  Warning  Evicted    40m   kubelet            The node had condition: [DiskPressure].

```

Kubernetes has not cleaned up any unused images. By default, this shouldn’t happen, as Kubernetes routinely checks whether there are any images not in use, and deletes any unused images that it finds. This is an unlikely source of node disk pressure; however, it should be kept in mind.

```sh
sudo cat /proc/meminfo
sudo df -hT
sudo free -g
sudo crictl imagefsinfo
sudo crictl image list
```

```sh
sudo du -sh /var/lib/containerd 
sudo crictl imagefsinfo 
sudo crictl rmi --prune 
pause_version=$(sudo crictl images | grep pause | awk '{print $2}') 
pause=$(ls /tmp/kube | grep pause | grep ${pause_version}) 
sudo ctr -n k8s.io image import /tmp/kube/$pause 
sudo du -sh /var/lib/containerd 
sudo crictl imagefsinfo
```

logs building up. The [default behavior in Kubernetes](https://www.airplane.dev/blog/kubernetes-logging) is to save logs in two cases: It’ll save the logs of any running containers, and it’ll save the logs of the most recently exited container to aid in troubleshooting. This is an attempt to strike a balance between keeping important logs, and getting rid of logs that aren’t useful by deleting them over time. However, if you have a long-running container with a lot of logs, they may build up enough that it overloads the capacity of the node disk.

#### 6. ContainerStatusUnknown

```sh

kubectl describe pod <pod_name> -n <namespace>

Warning  Evicted    4m55s  kubelet            The node was low on resource: ephemeral-storage. Container copy-secrets-sidecar was using 36Ki, which exceeds its request of 0. Container image-spec-projection-controller was using 22548Ki, which exceeds its request of 0. Container vault-agent was using 4Ki, which exceeds its request of 0.
```

##### low on resource: ephemeral-storage
问题：Kubernetes使用的系统盘容量不足，触发项如下：
1. image镜像太多，耗用太多ephemeral-storage；查证时无意中发现pod在启动时要重新下载相关镜像，说明由于磁盘容量不够时，kubernetes会清理镜像文件去腾空磁盘，省出资源去优先启动pod。符合上述1中所述的“镜像层占用ephemeral-storage”。因为笔者机器打算做一个单节点的kubernetes集群，去部署微服务的allinone环境，image会很多，占用空间会很大。原有的20G根本不够用。
2. 本地pv存储全部挂载了系统盘目录下；kubernetes中的allinone的各个组件的持久化存储都是用的本地盘(系统盘)，都开的是1G，那么原有的20G更不够了。
3. 有些容器没有使用持久化存储，日志等全部打印到了ephemeral-storage。造成应用的日志全部打印到了容器里，也就是/var/log目录下，耗用了ephemeral-storage。
解决方案：原则 - 让ephemeral-storage只存储kubernetes体系下的日志，系统盘容量要充足。
* 清理磁盘资源
* 通过可修改kubelet的配置参数imagefs.available 来提高阈值，重启kubelet
* 1. image镜像层的存储指定非系统盘；
2. 本地pv存储挂载非系统盘；**(生产环境禁止使用本地磁盘，必须使用**[**云存储**](https://cloud.tencent.com/product/cos?from_column=20065&from=20065)**)**
3. 容器必须都使用持久化存储，禁止把日志都打到容器里。

ephemeral-storage 用于管理和调度k8s 中运行的应用的短暂存储。每个k8s 节点上，kubelet的根目录(默认/var/lib/kubelet)和日志目录(/var/log)保存在节点的主分区上，这个分区同时也会被Pod的EmptyDir类型的volume、容器日志、镜像的层、容器的可写层所占用。ephemeral-storage便是对这块主分区进行管理，通过应用定义的需求(requests)和约束(limits)来调度和管理节点上的应用对主分区的消耗。
使用df -h可以看到/var/lib下有很多容器相关的目录，这些都是ephemeral-storage：

临时存储，节点上kubelet的配置路径超过阈值会触发驱逐，默认情况下阈值是85%

```sh

sudo df -hT /
sudo du -xhd1 /   ## cd / && du -h -x --max-depth=1，进入根目录查磁盘占用过大的文件夹，删除不需要的文件
# df -h
# df -h /
# df -h /tmp
# df -h | grep /var/lib
sudo free -g
sudo du -sh /var/log
sudo du -sh /var/lib/containerd


sudo cat /proc/meminfo
sudo crictl imagefsinfo
sudo top
df -h | grep /var/lib/


# ************************** cleanup unused images ************************** #
# ********** docker
docker system prune --all
# ********** containerd 
sudo crictl rmi --prune
ctr -n k8s.io images export pause.tar-v3.7 registry.k8s.io/pause:3.7
ctr -n k8s.io image import pause.tar-v3.7
pause_image_version=$(cat /etc/containerd/config.toml| grep /pause:|awk -F'"' '{print $2}'|awk -F':' '{print $2}')
# crictl images | awk '$1 == "k8s.gcr.io/pause" { print $0 }'
# in_use_images_id=$(crictl ps -a | grep -Ev 'CONTAINER' | awk '{ print $2 }')


# ****************** clean up containerd exited containers ****************** #
crictl ps --state exited -q | xargs -n1 crictl rm
gt all 'sudo -i bash -c "crictl ps --state exited -q | xargs -n1 crictl rm"'


kubectl rollout restart deployment <deployment-name> -n genctl

```




### 2. Troubleshooting Nodes

Debugging Your Kubernetes Nodes in the ‘Not Ready’ State | nodenotready: https://www.containiq.com/post/debugging-kubernetes-nodes-in-not-ready-state

如何将我的节点的状态从 NotReady 或 Unknown 状态更改为 Ready 状态？: https://aws.amazon.com/cn/premiumsupport/knowledge-center/eks-node-status-ready/

As mentioned earlier, each node in a cluster is used to run pods. Before a pod is scheduled on a node, Kubernetes checks whether the node is capable of running the pod or not. The STATUS column in the output of kubectl get nodes represents the status. The possible values in this column are:

1. Ready: The node is healthy and ready to accept pods.
2. NotReady: The node has encountered some issue and a pod cannot be scheduled on it.
3. SchedulingDisabled: The node is marked as unschedulable. This can be done using the [kubectl cordon](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#cordon) command.
4. Unknown: The node is unreachable by the control plane.

Having a node in the NotReady state means that the node is effectively unused and will accumulate costs without participating in running pods. Furthermore, losing a node can negatively impact your production workload.

When a worker node shuts down or crashes, all stateful pods that reside on it become unavailable, and the node status appears as `NotReady`.

If a node has a `NotReady` status for over five minutes (by default), Kubernetes changes the status of pods scheduled on it to `Unknown`, and attempts to schedule it on another node, with status `ContainerCreating`.

**How to identify the issue**

Run the command `kubectl get nodes`.

Check the output to see is the node status is `NotReady`

```
NAME        STATUS      AGE    VERSION
mynode-1    NotReady    1h     v1.2.0
```

To check if pods scheduled on your node are being moved to other nodes, run the command `get pods`.

Check the output to see if a pod appears twice on two different nodes, as follows:

```
NAME       READY    STATUS               RESTARTS      AGE    IP        NODE
mypod-1    1/1      Unknown              0             10m    [IP]      mynode-1
mypod-1    0/1      ContainerCreating    0             15s    [none]    mynode-2
```

**Resolving the issue**

If the failed node is able to recover or is rebooted by the user, the issue will resolve itself. Once the failed node recovers and joins the cluster, the following process takes place:

1. The pod with Unknown status is deleted, and volumes are detached from the failed node.
2. The pod is rescheduled on the new node, its status changes from `Unknown` to `ContainerCreating` and required volumes are attached.
3. Kubernetes uses a five-minute timeout (by default), after which the pod will run on the node, and its status changes from `ContainerCreating` to `Running`.

If you have no time to wait, or the node does not recover, you’ll need to help Kubernetes reschedule the stateful pods on another, working node. There are two ways to achieve this:

- **Remove failed node from the cluster**—using the command `kubectl delete node [name]`
- **Delete stateful pods with status unknown**—using the command `kubectl delete pods [pod_name] --grace-period=0 --force -n [namespace]`

Learn more about [Node Not Ready issues](https://komodor.com/learn/how-to-fix-kubernetes-node-not-ready-error/) in Kubernetes.

**Toubleshotting the issue**


### 3. Troubleshooting kubelet

#### 3.1 connection refused
kubelet 无法连接到kube-apiserver
```
kubectl get node 

The connection to the server 10.11.52.238:6443 was refused - did you specify the right host or port?

or 

failed to list bootstrap tokens: Get "https://10.11.52.238:6443/api/v1/namespaces/kube-system/secrets?fieldSelector=type%3Dbootstrap.kubernetes.io%2Ftoken": dial tcp 10.11.52.238:6443: connect: connection refused
```

1. Check kubelet status

```bash
systemctl status kubelet

```

2. check kubelet log 
```sh

journalctl -xefu kubelet 

Get \"https://10.11.52.238:6443/api/v1/nodes/c61148v1.fyre.ibm.com?timeout=10s\": dial tcp 10.11.52.238:6443: connect: connection refused"

```





3 check kube-apiserver status
```

Login on master node
crictl ps -a | grep kube-apiserver


```


```sh
Issue ：kube-apiserver exited 

crictl logs <kube-apiserver container ID>

"ContainerStatus from runtime service failed"

解决方案：
rm /etc/containerd/config.toml

cat > /etc/containerd/config.toml <<EOF
[plugins."io.containerd.grpc.v1.cri"]
  systemd_cgroup = true
EOF

systemctl restart containerd
crictl ps 
```


```sh
Issue ：kube-apiserver exited 

crictl logs <kube-apiserver container ID>

Err: connection error: desc = "transport: Error while dialing: dial tcp 127.0.0.1:2379: connect: connection refused"

2379 是etcd的服务

连不上etcd

crictl ps -a ｜ grep etcd

etcd exited

crictl logs -f <etcd container id>

{"level":"info","ts":"2024-08-08T15:18:22.085935Z","caller":"osutil/interrupt_unix.go:64","msg":"received signal; shutting down","signal":"terminated"}

{"level":"warn","ts":"2024-08-08T14:16:08.594749Z","caller":"embed/serve.go:212","msg":"stopping secure grpc server due to error","error":"accept tcp 10.11.52.238:2379: use of closed network connection"}



```



```sh 

Issue: kube-apiserver exited 

cat /var/log/messages|grep kube-apiserver|grep -i error
kubelet log 显示以下错误：
CreateContainerError: failed to get sandbox container task: no running task found: task 85a5cdddc59dc126b40781c0814ff3d94ea5ab1df88662a3bfb5eef8e58fbf6a not found: not found

通常意味着 `kubelet` 或者 `containerd`（作为容器运行时）在处理 Pod 的 Sandbox 容器时遇到了问题。Sandbox 容器是为每个 Pod 创建的基础容器，用于运行 Pod 中的其他容器。


解决方案：
清理旧的exited 容器
crictl ps --state exited -q | xargs -n1 crictl rm

```


```

Issue: kube-apiserver exited 

cat /var/log/messages|grep kube-apiserver|grep -i error
kubelet log 显示以下错误：

Error syncing pod, skipping


Aug  8 07:13:04 localhost kubelet[82226]: E0808 07:13:04.587402   82226 pod_workers.go:1298] "Error syncing pod, skipping" err="failed to \"StartContainer\" for \"kube-apiserver\" with CrashLoopBackOff: \"back-off 2m40s restarting failed container=kube-apiserver pod=kube-apiserver-c61148v1.fyre.ibm.com_kube-system(1e9303fda845580bc2a856ae1bd25102)\"" pod="kube-system/kube-apiserver-c61148v1.fyre.ibm.com" podUID="1e9303fda845580bc2a856ae1bd25102"


k8s etcd 挂了

crictl ps -a ｜ grep etcd

etcd exited

crictl logs -f <etcd container id>

{"level":"warn","ts":"2024-08-08T14:16:08.594749Z","caller":"embed/serve.go:212","msg":"stopping secure grpc server due to error","error":"accept tcp 10.11.52.238:2379: use of closed network connection"}


解决方案：
检查防火墙是否关闭，如果没有则关闭
systemctl stop firewalld && systemctl disable firewalld


```


#### 3.2 failed to verify certificate
```sh


[root@c61148v1 ~]# kubectl get node
Unable to connect to the server: tls: failed to verify certificate: x509: certificate signed by unknown authority (possibly because of "crypto/rsa: verification error" while trying to verify candidate authority certificate "kubernetes")

solution:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config


```
### 5. Troubleshooting Pods

Troubleshooting Kubernetes Pods: A Quick Guide

**Pod Stays Pending**:

If a pod’s status is Pending for a while, it could mean that it cannot be scheduled onto a node. Look at the describe pod output, in the Events section. Try to identify messages that indicate why the pod could not be scheduled. For example:

- **Insufficient resources in the cluster**—the cluster may have insufficient CPU or memory resources. This means you’ll need to delete some pods, add resources on your nodes, or add more nodes.
- **Resource requirements**—the pod may be difficult to schedule due to specific resources requirements. See if you can release some of the requirements to make the pod eligible for scheduling on additional nodes.

**Pod Stays Waiting**:

If a pod’s status is Waiting, this means it is scheduled on a node, but unable to run. Look at the `describe pod` output, in the ‘Events’ section, and try to identify reasons the pod is not able to run.

Most often, this will be due to an error when fetching the image. If so, check for the following:

- **Image name**—ensure the image name in the pod manifest is correct
- **Image available**—ensure the image is really available in the repository
- **Test manually**—run a docker pull command on the local machine, ensuring you have the appropriate permissions, to see if you can retrieve the image

**Pod Is Running but Misbehaving**:

If a pod is not running as expected, there can be two common causes: error in pod manifest, or mismatch between your local pod manifest and the manifest on the API server.

**Checking for an error in your pod description:**

It is common to introduce errors into a pod description, for example by nesting sections incorrectly, or typing a command incorrectly.

Try deleting the pod and recreating it with `kubectl apply --validate -f mypod1.yaml`

This command will give you an error like this if you misspelled a command in the pod manifest, for example if you wrote `continers` instead of `containers`:

```
46757 schema.go:126] unknown field: continers
46757 schema.go:129] this may be a false alarm, see https://github.com/kubernetes/kubernetes/issues/5786
pods/mypod1
```

**Checking for a mismatch between local pod manifest and API Server:**

It can happen that the pod manifest, as recorded by the Kubernetes API Server, is not the same as your local manifest—hence the unexpected behavior.

Run this command to retrieve the pod manifest from the API server and save it as a local YAML file:

```
kubectl get pods/[pod-name] -o yaml > apiserver-[pod-name].yaml
```

You will now have a local file called `apiserver-[pod-name].yaml`, open it and compare with your local YAML. There are three possible cases:

- **Local YAML has the same lines as API Server YAML, and more**—this indicates a mismatch. Delete the pod and rerun it with the local pod manifest (assuming it is the correct one).
- **API Server YAML has the same lines as local YAML, and more**—this is normal, because the API Server can add more lines to the pod manifest over time. The problem lies elsewhere.
- **Both YAML files are identical**—again, this is normal, and means the problem lies elsewhere.

**Diagnosing Other Pod Issues:**

If you weren’t able to diagnose your pod issue using the methods above, there are several additional methods to perform deeper debugging of your pod:

- Examining Pod Logs
- Debugging with Container Exec
- Debugging with an Ephemeral Debug Container
- Running a Debug Pod on the Node

**Examining Pod Logs:**

You can retrieve logs for a malfunctioning container using this command:

```
kubectl logs [pod-name] [container-name]
```

If the container has crashed, you can use the `--previous` flag to retrieve its crash log, like so:

```
kubectl logs --previous [pod-name] [container-name]
```

**Debugging with Container Exec:**

Many container images contain debugging utilities—this is true for all images derived from Linux and Windows base images. This allows you to run commands in a shell within the malfunctioning container, as follows:

```
kubectl exec [pod-name] -c [container-name] -- [your-shell-commands]
```

**Debugging with an Ephemeral Container:**

There are several cases in which you cannot use the `kubectl exec` command:

- The container has already crashed
- The container image is distroless, or purposely does not include a debugging utility

The solution, supported in Kubernetes v.1.18 and later, is to run an “ephemeral container”. This is a container that runs alongside your production container and mirrors its activity, allowing you to run shell commands on it, as if you were running them on the real container, and even after it crashes.

Create an ephemeral container using `kubectl debug -it [pod-name] --image=[image-name] --target=[pod-name]`.

The `--target` flag is important because it lets the ephemeral container communicate with the process namespace of other containers running on the pod.

After running the debug command, kubectl will show a message with your ephemeral container name—take note of this name so you can work with the container:

```
Defaulting debug container name to debugger-8xzrl
```

You can now run `kubectl exec` on your new ephemeral container, and use it to debug your production container.

**Running a Debug Pod on the Node:**

If none of these approaches work, you can create a special pod on the node, running in the host namespace with host privileges. This method is not recommended in production environments for security reasons.

Run a special debug pod on your node using `kubectl debug node/[node-name] -it --image=[image-name]`.

After running the debug command, kubectl will show a message with your new debugging pod—take note of this name so you can work with it:

```
Creating debugging pod node-debugger-mynode-pdx84 with container debugger on node [node-name]
```

Note that the new pod runs a container in the host IPC, Network, and PID namespaces. The root filesystem is mounted at /host.

When finished with the debugging pod, delete it using `kubectl delete pod [debug-pod-name]`.

### 6. Troubleshooting Clusters

Troubleshooting Kubernetes Clusters: A Quick Guide

**Viewing Basic Cluster Info:**

The first step to troubleshooting container issues is to get basic information on the Kubernetes worker nodes and Services running on the cluster.

To see a list of worker nodes and their status, run `kubectl get nodes --show-labels`. The output will be something like this:

```
NAME      STATUS    ROLES    AGE     VERSION        LABELS
worker0   Ready     [none]   1d      v1.13.0        ...,kubernetes.io/hostname=worker0
worker1   Ready     [none]   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
worker2   Ready     [none]   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
```

To get information about Services running on the cluster, run:

```
kubectl cluster-info
```

The output will be something like this:

```
Kubernetes master is running at https://104.197.5.247
elasticsearch-logging is running at https://104.197.5.247/api/v1/namespaces/kube-system/services/elasticsearch-logging/proxy
kibana-logging is running at https://104.197.5.247/api/v1/namespaces/kube-system/services/kibana-logging/proxy
kube-dns is running at https://104.197.5.247/api/v1/namespaces/kube-system/services/kube-dns/proxy
```

**Retrieving Cluster Logs:**

To diagnose deeper issues with nodes on your cluster, you will need access to logs on the nodes. The following table explains where to find the logs.

| NODE TYPE | COMPONENT          | WHERE TO FIND LOGS                     |
| :-------- | :----------------- | :------------------------------------- |
| Master    | API Server         | `/var/log/kube-apiserver.log`          |
| Master    | Scheduler          | `/var/log/kube-scheduler.log`          |
| Master    | Controller Manager | `/var/log/kube-controller-manager.log` |
| Worker    | Kubelet            | `/var/log/kubelet.log`                 |
| Worker    | Kube Proxy         | `/var/log/kube-proxy.log`              |

**Common Cluster Failure Scenarios and How to Resolve Them:**

Let’s look at several common cluster failure scenarios, their impact, and how they can typically be resolved. This is not a complete guide to cluster troubleshooting, but can help you resolve the most common issues.

**API Server VM Shuts Down or Crashes:**

- **Impact:** If the API server is down, you will not be able to start, stop, or update pods and services.
- **Resolution:** Restart the API server VM.
- **Prevention:** Set the API server VM to automatically restart, and set up high availability for the API server.

**Control Plane Service Shuts Down or Crashes:**

- **Impact:** Services like the Replication Controller Manager, Scheduler, and so on are collocated with the API Server, so if any of them shut down or crashes, the impact is the same as shutdown of the API Server.
- **Resolution:** Same as API Server VM Shuts Down.
- **Prevention:** Same as API Server VM Shuts Down.

**API Server Storage Lost:**

- **Impact:** API Server will fail to restart after shutting down.
- **Resolution:** Ensure storage is working again, manually recover the state of the API Server from backup, and restart it.
- **Prevention:** Ensure you have a readily available snapshot of the API Server. Use reliable storage, such as Amazon Elastic Block Storage (EBS), which survives shut down of the API Server VM, and prefer highly available storage.

**Worker Node Shuts Down:**

- **Impact:** Pods on the node stop running, the Scheduler will attempt to run them on other available nodes. The cluster will now have less overall capacity to run pods.
- **Resolution:** Identify the issue on the node, bring it back up and register it with the cluster.
- **Prevention:** Use a replication control or a Service in front of pods, to ensure users are not impacted by node failures. Design applications to be fault tolerant.

**Kubelet Malfunction:**

- **Impact:** If the kubelet crashes on a node, you will not be able to start new pods on that node. Existing pods may or may not be deleted, and the node will be marked unhealthy.
- **Resolution:** Same as Worker Node Shuts Down.
- **Prevention:** Same as Worker Node Shuts Down.

**Unplanned Network Partitioning Disconnecting Some Nodes from the Master:**

- **Impact:** The master nodes think that nodes in the other network partition are down, and those nodes cannot communicate with the API Server.
- **Resolution:** Reconfigure the network to enable communication between all nodes and the API Server.
- **Prevention:** Use a networking solution that can automatically reconfigure cluster network parameters.

**Human Error by Cluster Operator:**

- **Impact:** An accidental command by a human operator, or misconfigured Kubernetes components, can cause loss of pods, services, or control plane components. This can result in disruption of service to some or all nodes.
- **Resolution:** Most cluster operator errors can be resolved by restoring the API Server state from backup.
- **Prevention:** Implement a solution to automatically review and correct configuration errors in your Kubernetes clusters.




## Setup and Run k8s

https://kubernetes.io/docs/setup/
* [Download Kubernetes](https://kubernetes.io/releases/download/)
* [install tools](https://kubernetes.io/docs/tasks/tools/)
* Select a [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) for your new cluster

Install Kubernetes Cluster: https://github.com/cncamp/101/tree/master/k8s-install

kubeadm: 部署一个正式的k8s cluster
minikube：部署一个最小的 local  k8s cluster
kind: 
### Create k8s cluster with kubeadm

https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/

Prerequisite：
```
OS: linuxos, such centos ubuntu
RAM: >=2GB
CPU: >=2CPUs

```


```sh
# 服务器规划：（本实验采用虚拟机）
## k8s-master：192.168.239.137
## k8s-node1：192.168.239.138
## k8s-node2：192.168.239.139

master: 10.11.52.238
node1: 10.11.56.39
node2: 10.11.56.81

```

Config all hosts
```bash

# 关闭swap交换分区, 否则kubeadm 时会失败
swapoff -a 

# 时间同步

# 修改为静态ip

# 永久关闭防火墙,否则etcd 会挂掉
systemctl stop firewalld && systemctl disable firewalld

# 永久关闭selinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
setenforce 0
getenforce

# 永久设置hostname

# 将桥接ipv4流量设置到iptables的链，否则kubeadm join时会失败
modprobe br_netfilter

cat > /etc/sysctl.d/k8s.conf <<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

# net.ipv4.ip_forward = 1 打开ip转发

sysctl -p /etc/sysctl.d/k8s.conf


```

Install container runtime (docker)  kubeadm, kubelet, kubectl on all hosts

```sh
## Install containerd 
https://github.com/containerd/containerd/blob/main/docs/getting-started.md

sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo 
sudo yum install -y containerd.io

# 
#containerd config default > /etc/containerd/config.toml
#vim /etc/containerd/config.toml #将SystemdCgroup = false修改为SystemdCgroup = true
# 上面两行命令有问题

cat > /etc/containerd/config.toml <<EOF
[plugins."io.containerd.grpc.v1.cri"]
  systemd_cgroup = true
EOF


sudo systemctl enable containerd


cat > /etc/crictl.yaml <<EOF
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
debug: false
EOF



```

```sh

## Install docker
https://docs.docker.com/engine/install/centos/

sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo 

sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin # Install latest version
sudo yum list docker-ce.x86_64 --showduplicates | sort -r  # listing the available versions
sudo yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io docker-buildx-plugin docker-compose-plugin # Install a specific version

sudo systemctl enable docker && sudo systemctl start docker # 设置开机自启动并start docker

sudo docker --version
sudo systemctl status docker


```




```sh
# Set k8s yum repo
# Install kubectl kubeadm kubelet
# https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-using-native-package-management


cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.30/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.30/rpm/repodata/repomd.xml.key
EOF

```

```bash

# Install kubectl kubeadm kubelet
# https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-using-native-package-management

sudo yum install -y kubectl kubeadm kubelet
sudo yum list kubelet --showduplicates
sudo yum install -y kubelet-1.30.3 kubeadm-1.30.3 kubectl-1.30.3

sudo systemctl enable kubelet # 仅设置开机自启动，这时是不启动的，初始化master后才启动

```


```sh
# Init master node
## 仅master 节点执行

kubeadm init \
  --apiserver-advertise-address=10.11.52.238 \
  --pod-network-cidr=10.244.0.0/16

# kubernetes-version： 可选
# apiserver-advertise-address：设置k8s API 服务器的对外通信的IP地址，如果未指定，将使用第一个非-loopback、非点对点网络接口的 IP 地址。这个 IP 地址应该是集群中其他节点可以访问到的地址，通常是在你的网络环境中可以路由的公网或私网 IP 地址。可使用命令 ip addr show 查看
# pod-network-cidr： 指定 Pod 网络的 CIDR 范围。用于 Pod 的 IP 地址分配的，它应该独立于节点的网络配置，并且与其他网络组件如服务（Services）的地址空间分离。
# service-cidr: Kubernetes 集群中为 Service 类型的对象保留的 IP 地址范围.当创建一个类型为 ClusterIP、NodePort 或 LoadBalancer 的 Service 时，Kubernetes 会从 `service-cidr` 中分配一个 IP 地址给这个 Service。 默认值是 `10.96.0.0/12`，这在大多数情况下已经足够

如果命令执行失败可以加参数 --v=5

kubeadm init \
  --kubernetes-version 1.30.3 \
  --apiserver-advertise-address=0.0.0.0 \
  --service-cidr=10.96.0.0/16 \
  --pod-network-cidr=10.244.0.0/16 \
  --image-repository registry.aliyuncs.com/google_containers


# k8s version: https://kubernetes.io/releases/download/#binaries


如果kubeadm init 失败，问题fix完以后执行 kubeadm reset ，再执行kubeadm init。




```


> 为了选择一个合适的 `pod-network-cidr`，你可以遵循以下步骤：
1. **理解需求**:确定你的集群可能需要多少个 Pod。这有助于你计算 CIDR 块的大小。例如，如果你预计有数千个 Pod，那么一个较小的 /24 网段可能不足以容纳所有的 Pod。
2. **选择地址空间**:
    - 选择一个不会与现有网络重叠的地址空间。通常，人们会使用 RFC 1918 中定义的私有 IP 地址范围，例如 `10.0.0.0/8`, `172.16.0.0/12`, 或 `192.168.0.0/16`。
    - 从所选的地址池中，分割出一部分作为 Pod 的网络地址范围。例如，你可以从 `10.0.0.0/8` 中选择 `10.244.0.0/16` 作为 Pod 网络的 CIDR。
3. **考虑未来扩展**:
    - 留有足够的空间以应对未来的增长。如果预期会有大量的 Pod，选择一个较大的 CIDR 块。例如，对于成千上万的 Pod，可能需要一个 /16 或 /17 的 CIDR 块。
4. **避免冲突**:
    - 确保你选择的 CIDR 不会与任何其他网络配置冲突，比如你的数据中心网络、节点的网络、服务的网络等。
5. **配置网络插件**:
    - 根据你选择的网络插件（如 Calico, Flannel, Cilium, Weave Net 等），确保网络插件的配置与你选定的 `pod-network-cidr` 匹配。
- kubeadm init --pod-network-cidr=10.244.0.0/16
- 此外，你还应该在后续的网络插件配置中使用相同的 CIDR 值。通常，在初始化完控制平面之后，你需要安装网络插件来实现 Pod 间的网络连通性。例如，对于 Flannel，你可能会运行类似这样的命令：`kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml`  但如果你使用的是其他网络插件，可能需要通过其特定的配置文件或参数来指定 pod-network-cidr。

> 选择 `service-cidr` 的方法如下：
1. **理解 Service 的作用**:
    - Service 允许你定义一组逻辑上的后端 Pods 并为它们提供一个稳定的网络入口。因此，`service-cidr` 应该是一个与 Pod 网络和其他网络组件隔离的地址空间。
2. **选择地址空间**:
    - 和 `pod-network-cidr` 一样，`service-cidr` 也应该位于 RFC 1918 定义的私有 IP 地址范围内，例如 `10.0.0.0/8`, `172.16.0.0/12`, 或 `192.168.0.0/16`。
    - 选择一个不与 `pod-network-cidr` 重叠的 CIDR 块，以避免网络冲突。
3. **考虑范围大小**:
    - 评估你集群中可能创建的 Service 数量。一个较小的 CIDR 块（如 `/24`）可以支持大约 254 个 Service，而更大的 CIDR 块（如 `/16`）可以支持多达 65534 个 Service。
4. **避免冲突**:
    - 确保 `service-cidr` 不会与任何其他网络配置冲突，比如你的数据中心网络、节点的网络、Pod 的网络等。
5. **配置 `kubeadm init` 命令**: 将你选择的 `service-cidr` 作为参数传递给 `kubeadm init` 命令，例如：kubeadm init --service-cidr=10.96.0.0/12
6. `service-cidr` 的默认值是 `10.96.0.0/12`，这在大多数情况下已经足够。但是，如果你的集群规模非常大，或者你有特定的网络规划需求，你可能需要选择一个更合适的 CIDR 块。
7. 注意，一旦你为集群设置了 `service-cidr`，在不重新初始化集群的情况下，就无法更改这个值。因此，在集群初始化时选择一个合适的 `service-cidr` 是很重要的。


```
# Check cluster
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

#  if you are the root user
export KUBECONFIG=/etc/kubernetes/admin.conf 

kubectl get node
node notready是正常的

```

```bash
# Join worker to master
## 仅在work节点执行, master不执行

kubeadm join 10.11.52.238:6443 --token a3diy7.53mlamfxrsbjpdkj       --discovery-token-ca-cert-hash sha256:a1993ae8836c9d99e196121e8fe5949154f3edb62d6cce7b58e4396c5773678a


```

```bash
# Install network plugin



```


Issue 1

kubeadm init --v=5 --apiserver-advertise-address=10.11.52.238   --pod-network-cidr=10.244.0.0/16

```
[preflight] Some fatal errors occurred:
	[ERROR CRI]: container runtime is not running: output: time="2024-08-08T04:07:58-07:00" level=fatal msg="validate service connection: validate CRI v1 runtime API for endpoint \"unix:///var/run/containerd/containerd.sock\": rpc error: code = Unimplemented desc = unknown service runtime.v1.RuntimeService"
, error: exit status 1


```

This problem related to errors in CRI plugins. You can check the status of the CRI plugin

```
ctr plugin ls
```

In the past I got the same problem due to devmapper problem, since devmapper is configured as default CRI snapshotter, CRI got error as well.

```
TYPE                                  ID                       PLATFORMS      STATUS
io.containerd.snapshotter.v1          devmapper                linux/amd64    error
io.containerd.grpc.v1                 cri                      linux/amd64    error
```

The problem gone after I reconfigure the devmapper snapshotter.

Removing the config (/etc/containerd/config.toml) works as well, but the containerd runs with default configuration, which was not what I wanted.

```bash
cat > /etc/containerd/config.toml <<EOF
[plugins."io.containerd.grpc.v1.cri"]
  systemd_cgroup = true
EOF
systemctl restart containerd
```


```
# Backup old containerd config (optional)
sudo mv /etc/containerd/config.toml /etc/containerd/config.bak

# Regenerate containerd config
sudo containerd config default | sudo tee /etc/containerd/config.toml

# Restart containerd
sudo systemctl restart containerd

# The above got it to work for me; but with some warnings 
# and ignorable errors that looked this this: 
sudo crictl ps
# WARN[0000] runtime connect using default endpoints: [unix:///var/run/dockershim.sock unix:///run/containerd/containerd.sock unix:///run/crio/crio.sock]. As the default settings are now deprecated, you should set the endpoint instead.
# ERRO[0002] connect endpoint 'unix:///var/run/dockershim.sock', make sure you are running as root and the endpoint has been started: context deadline exceeded
# WARN[0002] image connect using default endpoints: [unix:///var/run/dockershim.sock unix:///run/containerd/containerd.sock unix:///run/crio/crio.sock]. As the default settings are now deprecated, you should set the endpoint instead.
# ERRO[0004] connect endpoint 'unix:///var/run/dockershim.sock', make sure you are running as root and the endpoint has been started: context deadline exceeded
# CONTAINER           IMAGE               CREATED             STATE               NAME                ATTEMPT             POD ID
# ^-- The last line represents correct output, which is why 
# I say ignorable warnings/errors, even the post command 
# exit code seeable using 'echo $?' exit code shows success

# What cleaned up the errors for me was copy pasting the following
echo """
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
""" | sudo tee /etc/crictl.yaml

docker ps
# ^-- no more errors :)

# Note others may need to run one of these instead, based on their
# system's config, keep trying docker ps until one config works
echo """
runtime-endpoint: unix:///var/run/crio/crio.sock
image-endpoint: unix:///var/run/crio/crio.sock
""" | sudo tee /etc/crictl.yaml

echo """
runtime-endpoint: unix:///var/run/dockershim.sock
image-endpoint: unix:///var/run/dockershim.sock
""" | sudo tee /etc/crictl.yaml
```

### Create k8s cluster with minikube

minikube

安装Kubernetes 沙箱环境，主要有三个步骤：

- 安装一个虚拟机，在虚拟机中启动 Kubernetes。推荐
- 在虚拟机中启动 Kubernetes，Kubernetes 有一个非常有意思的项目，叫 minikube，也就是启动一个最小的 local 的 Kubernetes 的一个环境。我们推荐使用阿里云版本的minikube，它和官方 minikube 的主要区别就是把 minikube 中所需要的 Google 上的依赖换成国内访问比较快的一些镜像，这样就方便了大家的安装工作；安装 MiniKube（中国版）: 
- 对 minikube 进行启动。启动命令：`minikube start —vm-driver virtualbox` . 如果大家不是 Mac 系统，其他操作系统请访问下面这个链接，查看其它操作系统如何安装 minikube 沙箱环境。 [https://kubernetes.io/docs/tasks/tools/install-minikube/](https://kubernetes.io/docs/tasks/tools/install-minikube，)

当大家安装好之后，我会跟大家一起做一个例子，来做三件事情：

1. 提交一个 nginx deployment；

   kubectl apply  -f  https://k8s.io/examples/application/deployment.yaml
2. 升级 nginx deployment，也就是改变它中间 Pod 的版本；

   kubectl apply -f  https://k8s.io/examples/application/deployment-update.yaml
3. 扩容 nginx deployment，进行一次水平的伸缩。

   kubectl apply -f  https://k8s.io/examples/application/deployment-update.yaml

首先，我们先看一下 minikube 的 status，可以看到 kubelet master 和 kubectl 都是配置好的。

```
minikube status
```

下一步我们利用 kubectl 来看一下这个集群中节选的状态，可以看到这个master 的节点已经是running状态：

```
kubectl get nodes
```

我们就以这个为节点，下面我们尝试去看一下现在集群中 Deployment 这个资源：

```
kubectl get deployments
```

可以看到集群中没有任何的 Deployment，我们可以利用 watch 这个语义去看集群中 Deployment 这个资源的变化情况。

```
kubectl get --watch deployments
```

下面我们去做刚才想要的三个操作：第一个操作是去创建一个 Deployment。可以看到下面第一个图，这是一个 API 的 content，它的 kind 是 Deployment，name 是 nginx-deployment, 有图中它的 replicas 数目是2，它的镜像版本是 1.7.9。

```
cat deploymeny.yaml
```

我们下面还是回到 kubectl 这个 commnd 来执行这次 Deployment 的真正的操作。我们可以看到一个简单的操作，就会去让 Deployment 不停地生成副本。

```
lubectl apply -f deployment.yaml
```

Deployment 副本数目是 2 个，下面也可以 describe 一下现在的 Deployment 的状态。我们知道之前是没有这个 Deployment 的，现在我们去 describe 这个 nginx-deployment。

```
kubectl describe nginx-deployment
```

下图中可以看到：有一个 nginx-deployment 已经被生成了，它的 replicas 数目也是我们想要的、selector 也是我们想要的、它的 image 的版本也是 1.7.9。还可以看到，里面的 deployment-controller 这种版本控制器也是在管理它的生成。

下面我们去升级这个 Deployment 版本，首先下载另外一个 yaml 文件 deployment-update.yaml，可以看到这里面的 image 本身的版本号从 1.7.9 升级到 1.8。

```
cat deployment-update.yaml
```

接下来我们重新 apply 新的 deployment-update 这个 yaml 文件。

```
lubectl apply -f deployment-update.yaml
```

可以看到，在另一边的屏幕上显示出了这个 Deployment 升级的一些操作，最终它的 up-to-date 值从 0 变成了 2，也就是说所有的容器都是最新版本的，所有的 Pod 都是最新版本的。我们也可以 discribe 具体去看一下是不是所有 Pod 的版本都被更新了，可以看到这个 image 的版本由 1.7.9 真正更新到了 1.8。

```
kubectl describe nginx-deployment
```

最后，我们也可以看到 controller 又执行了几次新的操作，这个控制器维护了整个 Deployment 和 Pod 状态。

最后我们演示一下给 Deployment 做水平扩张，下载另一个 yaml 文件 deployment-scale.yaml，这里面的 replicas 数目已经从 2 改成了 4。

```
cat deployment-scale.yaml
```

回到最开始的窗口，用 kubectl 去 apply 这个新的 deployment-scale.yaml 文件，在另外一个窗口上可以看到，当我们执行了 deployment-scale 操作之后，它的容器 Pod 数目从 2 变成了 4。我们可以再一次 describ 一下当前集群中的 deployment 的情况，可以看到它的 replicas 的数目从 2 变到了 4，同时也可以看到 controller 又做了几次新的操作，这个 scale up 成功了。

```
kubectl apply -f deployment-scale.yaml
kubectl describe nginx-deployment
```

最后，让我们利用 delete 操作把我们刚才生成的 Deployment 给删除掉。kubectl delete deployment，也是刚才我们本身的 deployment name，当我们把它删除掉之后，我们今天所有的操作就完成了。

```
kubectl delete deployment nginx-deployment
```

我们再去重新 get 这个 Deployment，也会显示这个资源不再存在，这个集群又回到了最开始干净的状态。

```
kubectl get deployments
```


### Create k8s cluster with kind


### Kops/Kubespray


## References

* **Kubernetes concept** https://kubernetes.io/docs/concepts/
* **Kubernetes tutorial** –https://kubernetes.io/docs/tutorials/kubernetes-basics/
* Introduction to container orchestration –https://www.exoscale.ch/syslog/2016/07/26/container-orch/
* TNS Research: The Present State of Container Orchestration –https://thenewstack.io/tns-research-present-state-container-orchestration/
* Large-scale cluster management at Google with Borg –https://research.google.com/pubs/pub43438.html
* kubernetes 中文社区： https://www.kubernetes.org.cn/
* Free Kubernetes Courses https://www.edx.org/
* Interactive Kubernetes Tutorials https://www.katacoda.com/courses/kubernetes
* Learn Kubernetes the Hard Way https://github.com/kelseyhightower/kubernetes-the-hard-way
* Official Kubernetes Youtube Channel https://www.youtube.com/c/KubernetesCommunity
* Official CNCF Youtube Channel https://www.youtube.com/c/cloudnativefdn
* Track to becoming a CKA/CKAD (Certified Kubernetes Administrator/Application Developer) https://www.cncf.io/certification/expert/
* Awesome Kubernetes https://www.gitbook.com/book/ramitsurana/awesome-kubernetes/details
* **Kubernetes中文指南/云原生应用架构实战手册** - https://jimmysong.io/kubernetes-handbook


# 问题
## 高可用的集群中 一般几个master节点？

在高可用（HA）的Kubernetes集群中，Master节点的数量通常是奇数个，最常见的是3个或5个。选择奇数个Master节点的主要原因是与选举机制有关，特别是涉及到Leader选举时。以下是不同数量的Master节点的一些考虑因素：

3个Master节点
- **常见选择**：适用于大多数生产环境。
- **成本效益**：相对于5个Master节点，3个节点的成本更低，同时也能提供足够的冗余和高可用性。
- **容错能力**：可以容忍一个节点故障，集群仍然可以正常运行。
- **性能**：对于大多数中小型集群来说，3个Master节点的性能已经足够。

5个Master节点
- **高可用性**：适用于大型或关键业务的集群，需要更高的容错能力和稳定性。
- **成本较高**：增加了硬件和维护成本。
- **容错能力**：可以容忍两个节点故障，集群仍然可以正常运行。
- **性能**：对于非常大的集群，5个Master节点可以提供更好的负载均衡和响应速度。

更多Master节点
- **极端情况**：在极少数情况下，可能会使用7个或更多Master节点，但这通常只适用于非常大规模的集群或有特殊需求的场景。
- **复杂性和成本**：随着Master节点数量的增加，管理和维护的复杂性也会增加，同时成本也会显著上升。

考虑因素
- **集群规模**：小型集群可能只需要3个Master节点，而大型集群可能需要5个或更多。
- **业务重要性**：关键业务系统可能需要更高的冗余和可用性。
- **预算**：更多的Master节点意味着更高的硬件和运维成本。
- **性能要求**：高并发请求和大数据量的集群可能需要更多的Master节点来保证性能。

总之，3个Master节点是大多数生产环境中最常见的选择，既提供了足够的高可用性，又保持了成本效益。如果业务需求特别高或集群规模非常大，可以考虑使用5个Master节点。


# 高可用的集群中 一般几个worker节点


在高可用（HA）的Kubernetes集群中，Worker节点的数量取决于多个因素，包括应用规模、资源需求、可用性要求和成本预算。以下是一些常见的配置和考虑因素：

 常见的Worker节点数量范围

1. **小型高可用集群**：5-10个Worker节点
   - **适用场景**：小型生产环境、初创公司、中小型企业。
   - **特点**：能够提供基本的高可用性和容错能力，成本相对较低。

2. **中型高可用集群**：10-50个Worker节点
   - **适用场景**：中等规模的企业、互联网应用、企业内部应用。
   - **特点**：能够处理中等规模的工作负载，具备较高的可用性和扩展性。

3. **大型高可用集群**：50-200个Worker节点
   - **适用场景**：大型企业、互联网公司、高流量网站。
   - **特点**：能够处理大规模的工作负载，具备高可用性和扩展性。

4. **超大型高可用集群**：200个以上Worker节点      1600
   - **适用场景**：超大型企业、云计算提供商、大型互联网公司。
   - **特点**：能够处理极其大规模的工作负载，具备高度的扩展性和容错能力。

具体考虑因素

1. **应用规模和资源需求**：
   - **无状态应用**：可以更容易地水平扩展，通常需要更多的Worker节点。
   - **有状态应用**：可能需要更少的Worker节点，但每个节点的资源需求更高。

2. **可用性要求**：
   - **高可用性**：更多的Worker节点可以提供更高的容错能力，确保即使部分节点故障，集群仍能正常运行。
   - **低可用性**：较少的Worker节点可能在成本上更有优势，但容错能力较弱。

3. **成本预算**：
   - **成本敏感**：可以选择较少的Worker节点，通过优化资源利用来降低成本。
   - **预算充足**：可以部署更多的Worker节点，以提高性能和可用性。

4. **扩展性**：
   - **未来扩展**：如果预计未来会有较大的扩展需求，可以提前规划并部署更多的Worker节点。
   - **静态需求**：如果应用需求相对稳定，可以按需配置Worker节点。

5. **管理复杂性**：
   - **简单管理**：少量的Worker节点更容易管理和维护。
   - **复杂管理**：大量的Worker节点需要更复杂的管理和监控工具。

最佳实践

- **容量规划**：根据应用的实际资源需求和预期工作负载进行详细的容量规划。
- **性能测试**：在部署前进行性能测试，确保集群能够满足业务需求。
- **自动伸缩**：使用Kubernetes的自动伸缩功能（如HPA和VPA），根据实际负载动态调整Worker节点的数量。
- **监控和告警**：部署监控和告警系统，及时发现和处理潜在的问题。

总结

在高可用的Kubernetes集群中，通常推荐的Worker节点数量范围是10-50个，这能够满足大多数企业的需求，提供良好的可用性和扩展性。如果业务规模较大或对高可用性有特殊要求，可以考虑更多的Worker节点。具体数量应根据实际需求和资源情况进行详细规划和测试。


## 为什么kubernetes 所有请求都要经过kube-apiserver
Kubernetes 是一个用于自动化部署、扩展和管理容器化应用程序的平台。Kubernetes 集群的核心组件之一是 `kube-apiserver`，它是 Kubernetes 控制平面的主要入口点。所有对集群状态的请求和操作都必须通过 `kube-apiserver` 进行，原因如下：

1. **单一入口点**：
   - `kube-apiserver` 提供了一个统一的入口点，使得所有客户端（如 `kubectl`、控制平面组件、外部系统等）都可以通过一致的 API 访问集群资源。
   - 这种设计简化了客户端的开发和维护，因为它们只需要与一个 API 交互，而不需要了解集群内部的具体实现细节。

2. **安全性**：
   - `kube-apiserver` 负责认证和授权。它验证客户端的身份，并确保它们具有执行特定操作的权限。
   - 通过集中管理认证和授权，可以更有效地保护集群的安全性。

3. **一致性**：
   - `kube-apiserver` 确保所有对集群状态的更改都是原子的、一致的，并且遵循 ACID 属性（原子性、一致性、隔离性、持久性）。
   - 这种一致性保证了集群状态的一致性和可靠性，避免了因并发操作导致的不一致问题。

4. **版本控制**：
   - `kube-apiserver` 支持多个 API 版本，允许客户端选择适合自己的 API 版本。
   - 这种版本控制机制使得 Kubernetes 可以平滑地演进，而不会影响现有的客户端。

5. **资源管理和调度**：
   - `kube-apiserver` 与 `etcd`（Kubernetes 的分布式键值存储）交互，管理集群的状态。
   - 它负责将客户端的请求转换为对 `etcd` 的操作，并将结果返回给客户端。
   - 通过 `kube-apiserver`，可以集中管理资源的创建、更新和删除操作，确保集群资源的一致性和完整性。

6. **事件和通知**：
   - `kube-apiserver` 支持 Watch 机制，允许客户端订阅资源的变化。
   - 这种机制使得客户端可以实时接收资源状态的变化通知，从而及时做出反应。

7. **可扩展性**：
   - `kube-apiserver` 设计为高度可扩展的，可以通过水平扩展（增加更多的 `kube-apiserver` 实例）来提高其处理能力。
   - 这种设计使得 Kubernetes 可以轻松应对大规模集群的需求。

总结来说，`kube-apiserver` 在 Kubernetes 中扮演着核心角色，它不仅提供了统一的入口点和安全性保障，还确保了集群状态的一致性和可靠性。通过集中管理认证、授权、资源管理和调度，`kube-apiserver` 使得 Kubernetes 成为一个强大且可靠的容器编排平台。

## 这么多都调kuber-api ，不会压力大吗


虽然所有的请求都需要通过 kube-apiserver 处理，但 Kubernetes 架构的设计考虑到了性能和可扩展性的需求。以下是一些缓解 kube-apiserver 压力的方式：

1. **负载均衡**:
   - kube-apiserver 可以配置为高可用集群，通过负载均衡器分发请求到多个实例上。这样即使单个实例出现故障，整个系统的可用性也不会受到影响。

2. **缓存机制**:
   - Kubernetes 内部使用了多种缓存机制来减少对 kube-apiserver 的直接访问次数。例如，kubelet 和 controller manager 组件会定期从 kube-apiserver 获取资源列表，并在本地缓存这些信息。当需要获取资源状态时，优先从本地缓存读取，而不是每次都向 kube-apiserver 发送请求。

3. **API 请求限制**:
   - kube-apiserver 支持配置请求速率限制，防止恶意或意外的大流量请求对其造成过大负担。通过设置合理的限流策略，可以有效降低 kube-apiserver 的压力。

4. **优化 API 设计**:
   - Kubernetes API 设计尽可能减少了不必要的网络通信开销。例如，批量操作（如创建多个 Pod）、Watch 机制以及使用标签选择器等功能，都旨在提高效率和减少请求次数。

5. **异步处理**:
   - 对于一些耗时较长的操作，如滚动升级、Pod 创建等，Kubernetes 通常采用异步处理的方式来减轻 kube-apiserver 的即时压力。控制器（如 Deployment 控制器）会在后台逐步完成这些任务，而无需等待 kube-apiserver 返回响应。

6. **水平扩展**:
   - 当集群规模增大时，可以通过增加 kube-apiserver 实例的数量来进行水平扩展。这样可以分散请求负载，保持良好的性能表现。

尽管如此，在实际应用中仍需关注 kube-apiserver 的性能指标，合理规划资源分配和请求频率，以确保 Kubernetes 集群能够稳定高效地运行。
