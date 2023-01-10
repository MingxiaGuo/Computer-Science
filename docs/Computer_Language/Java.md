2000年后，随着机器性能的提升、软件规模与复杂度的提 高，Java逐步取代了C的位置。
多数系统级语言(包括Java和C#)的根本编程哲学来源于C++，将C++的面向对象进一步发扬光大。





java
	javase
		概述
			特点
				面向对象
				跨平台
				分布式
				多线程，并发编程
				安全性
				支持函数式编程
				JIT编译
			术语
				JDK
					javac
					java
					javadoc
					javap
					javah
					jar
					jdb
					native2ascii
				JRE
					API
						java.lang
						java.net
						java.io
						java.nio
						java.util
						java.time
						java.text
						java.sql
				JVM
					HotSpot
			执行方式
				1.编译
					将源代码（.java）处理成字节码（.class）
				2.解释
					将字节码加载到jvm中执行（JIT编译）
			开发环境
				JDK
					javac
					java
					javadoc
				IDE
					IntelliJ IDEA
					Eclipse
					NetBeans
			程序结构
				package
					方便管理
					避免命名冲突
				import
					将java.lang包其他包中的内容需要先导入
				class/interface/enum/@interface
					被publuc修饰的类/接口/枚举/注解最多只有一个
					建议：一个源文件中只写一个类/接口/枚举/注解
				注释
					行注释 - //
					块注释（多行注释） - /*...*/
					文档注释 - /**...*/
						@author
						@since
						@param
						@return
						@throws
						@see
						@deprecated
		基本语法
			数据类型
				基本数据类型
					byte
					short
					int
					double
					long
					float
					char
					boolean
				引用数据类型
					数组
					类
					接口
					枚举
				基本数据类型的转换
					自动转换
					强制转换
				8种基本数据类型对应的包装类
			标识符
				

			关键字
			运算符
				算术运算符
					+ - * / % ++ --
				比较运算符
					&gt; &gt;= &lt; &lt;= != ==
						所以比较都可用到int short byte long float double char
						boolean只能使用==和!=
						引用数据类型只能使用==和!=
				赋值运算符
					= += -= *= /= %=
				逻辑运算符
					&amp;&amp; 短路
					&amp; 非短路
					|| 短路
					| 非短路
					! 非
			字面量
			分隔符
			变量和常量
		程序流程结构
			顺序结构
			分支结构（选择结构）
				if...else...
				switch...case...default...
			循环结构（重复结构）
				while
				do...while
				for
					两个分号分隔三个部分
					for-each
		面向对象
			特点
				抽象
				封装
				继承
				多态
			三大特性
				封装
				继承
				多态
			重载
			重写
		访问修饰符
			public
			private
			protected
		特殊修饰符
			static
			final
			abstract
		集合
	前端
		html
		css
		javascript
		jquery
	javaee
		jsp
		servlet
	框架
		ssh
		ssm
		bootstrap

# java开发环境下载安装

# JDK&JRE&JVM

![](/Users/gmx/Documents/workspace/note/Computer-Science/docs/Computer_Language/assets/QQ截图20170304212135.png)

* JDK

  ```
    Java Development kit java开发工具包
  ```

* JRE

  ```
    java Runtime Environment java运行时环境
  ```

* JVM
      java virtual machine java虚拟机

  # java执行过程

  ![](/Users/gmx/Documents/workspace/note/Computer-Science/docs/Computer_Language/assets/QQ截图20170304214031.png)

* 下载JDK1.7

* 安装JDK

* 配置环境变量

  * JAVA\_HOME ：C:\Program FIles\Java\jdk1.6.0\_14
  * Path: %JAVA\_HOME%\bin;%JAVA\_HOME%\jre\bin;”

* 打开cmd 输入java验证是否安装成功





Java后端框架：

1. Spring：是 Java 后端框架家族里面最强大的一个框架，其拥有 IOC（控制反转） 和 AOP（面向切面） 两大利器，大大简化了软件开发复杂性。并且，Spring 现在能与所有主流开发框架集成，可谓是一个万能框架，Spring 让 JAVA 开发变得更多简单。
2. SpringMVC：API层，处理|响应请求，获取表单参数，表单校验等。HTTP协议中的请求/响应特性，在该框架中，用户的每一个请求都声明了一个需要执行的动作。而这主要是通过将每个请求URI映射到一个可执行的方法来实现。同时，也将请求参数映射到对应方法的参数。
3. SpringBoot：Spring 组件一站式解决方案，简化使用 Spring 框架的难度，简省繁重的配置。
4. SpringCloud：微服务框架首选，它利用Spring Boot 的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中心、消息总线、负载均衡、断路器、数据监控等
5. Mybatis：一种轻量级的对象关系映射持久层（ORM）框架，数据层，数据库相关，连接、处理、映射。
6. Swagger-UI：前后端协作的利器，解析代码里的注解生成JSON文件，通过Swagger UI生成网页版的接口文档，可以在上面做简单的接口调试 。
7. ApachePOI：POI提供API给Java程序对Microsoft Office格式档案读和写的功能。
