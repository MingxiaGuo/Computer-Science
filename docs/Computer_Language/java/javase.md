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