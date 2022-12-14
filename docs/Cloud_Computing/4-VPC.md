

# VPC

Amazon VPC: https://docs.aws.amazon.com/vpc/index.html

IBM Cloud VPC: https://cloud.ibm.com/docs/vpc?topic=vpc-getting-started

VPC (Virtual private cloud)

Virtual Private Cloud (Amazon VPC) enables you to provision a **logically isolated** section of the AWS Cloud where you can launch AWS resources in a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in **your own data center**, with the benefits of using the scalable infrastructure of AWS.

**VPC**: A virtual private cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can specify an IP address range for the VPC, add subnets, add gateways, and associate security groups.

VPC is your own space in the IBM Cloud that allows you to define a virtual private network where you deploy, secure, control and manage cloud resource dedecated to your business.

**Subnet**: A subnet is a range of IP addresses in your VPC. You launch AWS resources, such as Amazon EC2 instances, into your subnets. You can connect a subnet to the internet, other VPCs, and your own data centers, and route traffic to and from your subnets using route tables.

A VPC is a public cloud offering that lets an enterprise establish its own private cloud-like computing environment on shared [public cloud](https://www.ibm.com/cloud/public) infrastructure. A VPC gives an enterprise the ability to define and control a virtual network that is logically isolated from all other public cloud tenants, creating a private, secure place on the public cloud.

Imagine that a cloud provider’s infrastructure is a residential apartment building with multiple families living inside. Being a public cloud tenant is akin to sharing an apartment with a few roommates. In contrast, having a VPC is like having your own private condominium—no one else has the key, and no one can enter the space without your permission.

A VPC’s logical isolation is implemented using virtual network functions and security features that give an enterprise customer granular control over which IP addresses or applications can access particular resources. It is analogous to the “friends-only” or “public/private” controls on social media accounts used to restrict who can or can’t see your otherwise public posts.

一个VPC ---> 一个租户

Cloud Data Center(Insfrustracture) is hosted in multiple locations world-wide. These locations are composed of Regions, Availability Zones, Local Zones, AWS Outposts, and Wavelength Zones. 

* **Regions**: Each Region is a separate geographic area. Regions are isolated from each other. This achieves the greatest possible fault tolerance and stability. 一个region是多个数据中心的集群，到2021年为止AWS全球有25个region，AWS服务分布在世界各地。

* **Availability Zones**: Availability Zones are multiple, isolated locations within each Region. The code for Availability Zone is its Region code followed by a letter identifier. For example, `us-east-1a` 每个region中包含数个独立的、物理分离的AZ，每个AZ有独立的供电，制冷，安保，同一region内AZ之间有高带宽，极低延时的光纤网络相连，数据以加密形式传输。每个AZ下包含一个或多个数据中心，每个数据中心有独立的供电、制冷、网络。

* **Local Zones**: Local Zones provide you the ability to place resources, such as compute and storage, in multiple locations closer to your end users.

- **AWS Outposts**: AWS Outposts brings native AWS services, infrastructure, and operating models to virtually any data center, co-location space, or on-premises facility.
- **Wavelength Zones**: Wavelength Zones allow developers to build applications that deliver ultra-low latencies to 5G devices and end users. Wavelength deploys standard AWS compute and storage services to the edge of telecommunication carriers' 5G networks.
- 



AWS Global Infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/



* **Regions**: Each Region is a separate geographic area. Regions are isolated from each other. This achieves the greatest possible fault tolerance and stability. 一个region是多个数据中心的集群，到2021年为止AWS全球有25个region，AWS服务分布在世界各地。
* **Availability Zones**: Availability Zones are multiple, isolated locations within each Region. The code for Availability Zone is its Region code followed by a letter identifier. For example, `us-east-1a` 每个region中包含数个独立的、物理分离的AZ，每个AZ有独立的供电，制冷，安保，同一region内AZ之间有高带宽，极低延时的光纤网络相连，数据以加密形式传输。每个AZ下包含一个或多个数据中心，每个数据中心有独立的供电、制冷、网络。
* VPC：Virtual Private Cloud, 是用户在region中自定义的虚拟网络，是一个整体概念，用户可在region中创建多个VPC。我们可以在VPC中选择IP网段，创建subnet，指定route table，控制ACL，设置网关。大部分AWS服务都需要以VPC为基础进行构建，入EC2，ALB，及无服务器服务ECS Fargate。VPC只能属于一个region
* Subnet：当我们在一个VPC中创建subnet时需要给subnet选择一个AZ，一个subnet只能选择在一个AZ中。Subnet是VPC中的子网络建立在特定的AZ中，subnet是最终承载大部分AWS服务的组件，如EC2，ECS Fargate，RDS。subnet分为private subnet(不能直接访问intenet)和public subnet(可直接访问internet)，private subnet也可通过NAT的方式访问internet
* Security Group：Security Group通过控制IP和端口来控制出站入站规则，可以用于EC2，RDS及VPC Endpoint。
* VPC Endpoint//