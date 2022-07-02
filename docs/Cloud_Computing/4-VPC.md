

# VPC

Amazon VPC: https://docs.aws.amazon.com/vpc/index.html

IBM Cloud VPC: https://cloud.ibm.com/docs/vpc?topic=vpc-getting-started

VPC (Virtual private cloud)

Virtual Private Cloud (Amazon VPC) enables you to provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**VPC**: A virtual private cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can specify an IP address range for the VPC, add subnets, add gateways, and associate security groups.

**Subnet**: A subnet is a range of IP addresses in your VPC. You launch AWS resources, such as Amazon EC2 instances, into your subnets. You can connect a subnet to the internet, other VPCs, and your own data centers, and route traffic to and from your subnets using route tables.

A VPC is a public cloud offering that lets an enterprise establish its own private cloud-like computing environment on shared [public cloud](https://www.ibm.com/cloud/public) infrastructure. A VPC gives an enterprise the ability to define and control a virtual network that is logically isolated from all other public cloud tenants, creating a private, secure place on the public cloud.

Imagine that a cloud provider’s infrastructure is a residential apartment building with multiple families living inside. Being a public cloud tenant is akin to sharing an apartment with a few roommates. In contrast, having a VPC is like having your own private condominium—no one else has the key, and no one can enter the space without your permission.

A VPC’s logical isolation is implemented using virtual network functions and security features that give an enterprise customer granular control over which IP addresses or applications can access particular resources. It is analogous to the “friends-only” or “public/private” controls on social media accounts used to restrict who can or can’t see your otherwise public posts.



Cloud Data Center(Insfrustracture) is hosted in multiple locations world-wide. These locations are composed of Regions, Availability Zones, Local Zones, AWS Outposts, and Wavelength Zones. 

* **Regions**: Each Region is a separate geographic area. Regions are isolated from each other. This achieves the greatest possible fault tolerance and stability.

* **Availability Zones**: Availability Zones are multiple, isolated locations within each Region. The code for Availability Zone is its Region code followed by a letter identifier. For example, `us-east-1a`

* **Local Zones**: Local Zones provide you the ability to place resources, such as compute and storage, in multiple locations closer to your end users.

- **AWS Outposts**: AWS Outposts brings native AWS services, infrastructure, and operating models to virtually any data center, co-location space, or on-premises facility.
- **Wavelength Zones**: Wavelength Zones allow developers to build applications that deliver ultra-low latencies to 5G devices and end users. Wavelength deploys standard AWS compute and storage services to the edge of telecommunication carriers' 5G networks.
- 



AWS Global Infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/