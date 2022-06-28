# Agile Software Development

## Software Development

1. ### 传统软件开发模式

### 瀑布模型

![20180808152613545.jpg](blob:file:///72a72872-fbcc-484b-bb5f-5ad26fcbd73e)

![20180808152613545.jpg](blob:file:///2b28e7ac-738c-4f96-b3fa-06b9331feef8)

- 以文档为驱动

形式化的软件开发方法 (Formal Method)”, “里程碑式的开发 (Plan-driven development)”

### 迭代开发

**迭代开发将一个大任务，分解成多次连续的开发，本质就是逐步改进。**开发者先快速发布一个有效但不完美的最简版本，然后不断迭代。每一次迭代都包含规划、设计、编码、测试、评估五个步骤，不断改进产品，添加新功能。通过频繁的发布，以及跟踪对前一次迭代的反馈，最终接近较完善的产品形态。

### 增量开发

**所谓****"****增量开发****"****，指的是软件的每个版本，都会新增一个用户可以感知的完整功能。也就是说，按照新增功能来划分迭代。**

### Agile **敏捷开发**

**增量开发加上迭代开发，才算真正的敏捷开发**

**每次迭代都是一个完整的软件开发周期，必须按照软件工程的方法论，进行正规的流程管理。**

具体来说，每次迭代都必须依次完成以下五个步骤。

1. 需求分析（requirements analysis）
2. 设计（design）
3. 编码（coding）
4. 测试（testing）
5. 部署和评估（deployment / evaluation）



Agile Manifesto 敏捷的价值观：

* **Individuals and interactions** over processes and tools   **个人和交互** 重于 过程和工具

* **Working software** over comprehensive documentation  **可用的软件** 重于 完备的文档  

* **Customer collaboration** over contract negotiation  **和客户协作**重于 合同谈判

* **Responding to change** over following a plan  **响应变化** 重于 遵循计划

 

**六、十二条原则**

该宣言还提出十二条敏捷开发的原则。

1. 通过早期和持续交付有价值的软件，实现客户满意度。
2. 欢迎不断变化的需求，即使是在项目开发的后期。要善于利用需求变更，帮助客户获得竞争优势。
3. 不断交付可用的软件，周期通常是几周，越短越好。
4. 项目过程中，业务人员与开发人员必须在一起工作。
5. 项目必须围绕那些有内在动力的个人而建立，他们应该受到信任。
6. 面对面交谈是最好的沟通方式。
7. 可用性是衡量进度的主要指标。
8. 提倡可持续的开发，保持稳定的进展速度。
9. 不断关注技术是否优秀，设计是否良好。
10. 简单性至关重要，尽最大可能减少不必要的工作。
11. 最好的架构、要求和设计，来自团队内部自发的认识。
12. 团队要定期反思如何更有效，并相应地进行调整。

![Screen Shot 2022-03-15 at 3.51.17 AM](/Users/guomingxia/Documents/workspace/Computer-Science/docs/Project_Management/assets/agile.png)

- \# Agile history:

- \* 1910-1959

- ​	* Ford Scientific Management

- ​	* Mass Production

- ​	* PDCA (W.Edwards Deming)

- \* 1960s

- ​	* Toyota Production System(Taichi Ohno)

- ​	* Waterfall(Winston W Poyce)

- \* 1970s

- \* 1980s

- ​	* PC - application development crisis

- ​		* Business need validation => Production(3 yrs)

- ​		* Requirement changes => project cancellation

- ​		* Misinterpret requirements

- \* 1990s

- ​	* RAD (James Martin)

- ​	* Scrum(Ken Schwabar & Jeff Sutherland)

- ​	* DSDM

- ​	* FDD(Jeff De Luca)

- ​	* XP(Kent Beck)

- ​	* Crystal(Alistair Cockburn)

- ​	* Lean Thinking

- \* 2000s

- ​	* Agile

- \* 2010s

- 

- 

- - 

  - XP(Extreme programming，极限编程)：偏重实践。

  - - 最初形成于1996—1999年间，Kent Beck、Ward Cunninggham、Ron Jeffrey在开发C3项目（Chrysler Comprehensive Compensation）的实践中总结出了XP的基本元素。在此之后，Kent Beck和他的一些好朋友们一起在实践中完善提高，终于形成了极限编程方法论
    - https://blog.csdn.net/fw0124/article/details/48713959

  - FDD



- 比较有名的最佳实践

- - TDD
  - 





Scrum:

- 偏重过程。英文意思是橄榄球运动的一个专业术语，表示“争球”的动作；把一个开发流程的名字取名为Scrum，我想你一定能想象出你的开发团队在开发一个项目时，大家像打橄榄球一样迅速、富有战斗激情、人人你争我抢地完成它，你一定会感到非常兴奋的。而Scrum就是这样的一个开发流程，运用该流程，你就能看到你团队高效的工作。

- - - Sprint：是短距离赛跑的意思，这里面指的是一次迭代，而一次迭代的周期是1个月时间（即4个星期），也就是我们要把一次迭代的开发内容以最快的速度完成它，这个过程我们称它为 Sprint

Sprint：冲刺周期，通俗的讲就是实现一个“小目标”的周期。一般需要 2-6 周时间。

User Story：用户的外在业务需求。拿银行系统来举例的话，一个 Story 可以是用户的存款行为，或者是查询余额等等。也就是所谓的小目标本身。

Task：由 User Story 拆分成的具体开发任务。

Backlog：需求列表，可以看成是小目标的清单。分为 Sprint Backlog 和 Product Backlog。

Daily meeting：每天的站会，用于监控项目进度。有些公司直接称其为 Scrum。

Sprint Review meeting: 冲刺评审会议，让团队成员们演示成果。

Sprint burn down：冲刺燃尽图，说白了就是记录当前周期的需求完成情况。

Release：开发周期完成，项目发布新的可用版本。

Scrum开发流程中的三大角色 ：

- PO：product owner, **产品负责人**——主要负责确定产品的功能和达到要求的标准，指定软件的发布日期和交付的内容，同时有权力接受或拒绝开发团队的工作成果
- SM：scrum master，**流程管理员——**主要负责整个Scrum流程在项目中的顺利实施和进行，以及清除挡在客户和开发工作之间的沟通障碍，使得客户可以直接驱动开发。
- ST:scrum team，**开发团队——**主要负责软件产品在Scrum规定流程下进行开发工作，人数控制在5~10人左右，每个成员可能负责不同的技术方面，但要求每成员必须要有很强的自我管理能力，同时具有一定的表达能力；成员可以采用任何工作方式，只要能达到Sprint的目标。





Agile development guide: https://www.aha.io/roadmapping/guide/agile



Tool:

* Aha
* Trello
* Jira: https://www.atlassian.com/software/jira  Jira Software is built for every member of your software team to plan, track, and release great software. Jira Software is the project management tool for agile teams
* Confluence: https://www.atlassian.com/software/confluence  Confluence is your remote-friendly team workspace where knowledge and collaboration meet.