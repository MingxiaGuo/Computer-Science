
**库**和**工具包**：开发者摆脱底层编码，专注于特定问题和业务逻辑。**库**和**工具包**是为程序员带来自由，**框架**是为程序员带来约束的。具体地说，库和工具包提供武器装备，框架则利用控制反转（IoC）机制实现对各模块的统一调度，从而剥夺了程序员对全局的掌控权，使他们成为手执编程武器、随时听候调遣的士兵。

**框架**： 可以是协同工作的类，也可以是协同工作的函数。设计者在特定领域的整体设计上不必重新发明轮子。一个足够复杂的应用软件开发，为确保快速有效，通常采取的方式是：在宏观上选取一些框架以控制整体的结构和流程在微观实现上利用库和工具包来解决具体的细节问题。

**编程范式**：是计算机编程的基本风格或典范模式

**设计模式**：是软件的战术思想，是针对某些经常出现的问题提出的行之有效的设计解决方案，而它侧重思想重用，因此比框架更更抽象、更普适，但多限于局部解决方案，没有框架的整体性。与之相似的还有惯用法（idiom），也是针对常发问题的解决方案，侧重实现而非设计，与实现语言密切相关，是一种更底层更具体的编程技巧。

**架构**：是软件的战略决策。一般指一个软件系统的最高层次的整体结构和规划，一个架构可能包含多个框架，而一个框架可能包含多个设计模式

Software Design & Architecture

* Enterprise Patterns
* Architectural Patterns
* Architectural Styles
* Architectural Principles
* Design Patterns
* Design Principles
* Object-Oriented Programming
* Programming Paradigms
* Clean Code

![](https://user-images.githubusercontent.com/6892666/65833569-bb34fc00-e29f-11e9-8516-79cbd9f8f07b.png)

![](https://user-images.githubusercontent.com/6892666/65896069-834eb700-e37a-11e9-95be-7ae2300d5d50.png)

Architecture

* Architectural Styles
  * structural
    * Component-based architectures
    * Layered Architectures
    * Monolithic Architectures
  * Message-based
    * Event-Driven Architectures
    * Publish-Subscribe Architectures
  * Distributed
    * Client-server Architectures
    * Peer-to-peer Architectures
* Architectural Patterns
  * Layered(n-tier) Architecture
    * Layers
      * Domain layer
      * Application Architectures
      * Infrastructure layer
      * Adapter layer
    * Similar Architectures
      * Ports & adapters
      * Vertical-slice Architecture
  * Event sourcing
  * Microkernels
  * Microservices
  * Space-based

Common architectural pattern

* **Layered pattern**
* **Client-server pattern**
* Master-slave pattern
* Pipe-filter pattern
* Broker pattern
* **Peer-to-peer pattern**
* Event-bus pattern
* Model-view-controller pattern
* Blackboard pattern
* Interpreter pattern
