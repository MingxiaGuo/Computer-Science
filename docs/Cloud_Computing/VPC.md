

VPC(Virtual private cloud)

A VPC is a public cloud offering that lets an enterprise establish its own private cloud-like computing environment on shared [public cloud](https://www.ibm.com/cloud/public) infrastructure. A VPC gives an enterprise the ability to define and control a virtual network that is logically isolated from all other public cloud tenants, creating a private, secure place on the public cloud.

Imagine that a cloud provider’s infrastructure is a residential apartment building with multiple families living inside. Being a public cloud tenant is akin to sharing an apartment with a few roommates. In contrast, having a VPC is like having your own private condominium—no one else has the key, and no one can enter the space without your permission.

A VPC’s logical isolation is implemented using virtual network functions and security features that give an enterprise customer granular control over which IP addresses or applications can access particular resources. It is analogous to the “friends-only” or “public/private” controls on social media accounts used to restrict who can or can’t see your otherwise public posts.







## VPC vs. …

### VPC vs. virtual private network (VPN)

A virtual private network (VPN) makes a connection to the public Internet as secure as a connection to a private network by creating an encrypted tunnel through which the information travels. You can deploy a VPN-as-a-Service (VPNaaS) on your VPC to establish a secure site-to-site communication channel between your VPC and your on-premises environment or other location. Using a VPN, you can connect subnets in multiple VPCs so that they function as if they were on a single network.

### VPC vs. private cloud

Private cloud and virtual private cloud are sometimes—and mistakenly—used interchangeably.  In fact, a virtual private cloud is actually a *public cloud* offering. A *private cloud* is a single-tenant cloud environment owned, operated, and managed by the enterprise, and hosted most commonly on-premises or in a dedicated space or facility. By contrast, a VPC is hosted on multi-tenant architecture, but each customer’s data and workloads are logically separate from those of all other tenants. The cloud provider is responsible for ensuring this logical isolation.

### VPC vs. public cloud

A virtual private cloud is a single-tenant concept that gives you the opportunity to create a private space within the public cloud’s architecture. A VPC offers greater security than traditional multi-tenant public cloud offerings but still lets customers take advantage of the high availability, flexibility, and cost-effectiveness of the public cloud. In some cases, there may be different ways of how you scale a VPC and a public cloud account. For instance, additional storage volumes may only be available in blocks of a certain size for VPCs. Not all public cloud features are supported in all VPC offering



region

Zone: availability zone