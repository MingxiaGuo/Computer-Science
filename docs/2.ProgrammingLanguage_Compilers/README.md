# Computer Language

1] TIOBE（http://www.tiobe.com）是一家评估编程语言流行度的权威机构，每月公布一次编程语言排行榜。

[2] 一个能计算出每个图灵可计算函数（Turing-computable function）的计算系统被称为图灵完备的。一个语言是图灵完备的，意味着该语言的计算能力与一个通用图灵机（Universal Turing Machine）相当，这也是现代计算机语言所能拥有的最高能力。

**好的语言就是适合编程者和解决对象的语言**


这门语言是什么，为什么要创造这门语言，以及这门语言要解决什么问题。

[Computer Language](https://www.wikiwand.com/en/Computer_language):  a [formal language](https://www.wikiwand.com/en/Formal_language) used to communicate with a [computer](https://www.wikiwand.com/en/Computer).


计算机语言：语言发展离机器语言越远，离人类语言更近，易读写维护安全通行可移植，开发效率高更抽象和宏观，但运行速度和效率下降用法和功能上局限性更大。中低级语言更适合中小型或底层应用，高级语言更适合大型应用
* 第一代：机器语言；由0和1组成，计算机能直接读懂，但对程序员来说难以记忆和阅读，维护费时
* 第二代：汇编语言 Assembly；用接近英语单词的助记码替代0和1，减轻程序员负担，由汇编器(assember)转为机器语言来再执行。但是汇编器是针对特定机器类型的，不可移植。汇编器只能一对一翻译，程序员依然需要编写硬件操作的细节。
* 第三代：高级语言 Fortran，Pascal，C，Java，VB；引入编译器(Compiler)和解释器(Interpreter)，使代码更简洁抽象，且能对一些指令做优化处理，减轻程序员负担。有时C被称为中级语言
* 第四代：面向问题语言：SQL，SAS，SPSS；专注业务逻辑和问题领域，程序员主要分析和描述问题，不需花大量时间考虑具体算法和逻辑。但是第四代语言过于局限于特定领域，属于领域特定语言，而不是通用编程语言。SQL用于数据库操作，SAS和SPSS用于统计分析，Mathematica用于科学计算。LaTeX是专门用于排版的语言，正则表达式（regular expression）是专门处理字符匹配的语言但是疑问系统往往横跨多个领域，这些不同领域的语言是很难整合的。
* 第五代：人工智能语言：Prolog，Mercury，OPSS；保持第三代通用性和第四代的重目标轻过程，重描述轻实现，
* 


* Construction Language
  * Command language: is interpreted languages

    * shell
    * [batch programming languages](https://www.wikiwand.com/en/Batch_programming_language).
  * [Programming language](https://www.wikiwand.com/en/Programming_language)
  
    * [Machine code](https://www.wikiwand.com/en/Machine_code)
    * [Assembly language](https://www.wikiwand.com/en/Assembly_language)
    * [C](https://www.wikiwand.com/en/C_(programming_language)); 在2000年前的单机时代，C语言是编程之王； 静态类型/弱类型/非脚本型/通用语言
    * [C++](https://www.wikiwand.com/en/C++)
    * [Java](https://www.wikiwand.com/en/Java_(programming_language)): 静态类型/强类型/非脚本型/通用语言
    * [Go](https://www.wikiwand.com/en/Go_(programming_language))：静态类型/强类型/非脚本型/通用语言
    * [Python](https://www.wikiwand.com/en/Python_(programming_language))：动态类型/强类型/脚本型/通用语言
    * [JavaScript](https://www.wikiwand.com/en/JavaScript)：动态类型/弱类型/脚本型/通用语言
    * Scripting language
      * Bash: Unix shell , Command language
      * Python
      * Javascript
  * [Query language](https://www.wikiwand.com/en/Query_language): 
    * SQL： 领域专用语言
* Data exchange Language: 

  * JSON, 
  * [XML](https://www.wikiwand.com/en/XML) (Extensible Markup Language)
  * [YAML](https://www.wikiwand.com/en/YAML) (YAML Ain't Markup Language) https://yaml.org/
* [Markup language](https://www.wikiwand.com/en/Markup_language)

  * [HTML](https://www.wikiwand.com/en/HTML) (Hyper Text Markup Language) https://html.spec.whatwg.org/multipage/
* [style sheet language](https://www.wikiwand.com/en/Style_sheet_language)

  * [CSS](https://www.wikiwand.com/en/CSS) (Cascading Style Sheets)
* Modeling Language

  * [Architecture description language](https://www.wikiwand.com/en/Architecture_description_language) : UML
  * [Hardware description language](https://www.wikiwand.com/en/Hardware_description_language)



编程语言分类：

* 动态类型/静态类型: Dynamic programming language/Static program language 
* 强类型/弱类型
* 脚本型/非脚本型
* 通用语言/领域专用语言
* 不能用编译型/解释型来分类语言，编译型/解释型只用来修饰实现，而不用来修饰语言



函数式 声明式

字节码 机器码

[Compiled language](https://www.wikiwand.com/en/Compiled_language): C, C++, Java, Go, Objective-C, Swift

[interpreted languages](https://www.wikiwand.com/en/Interpreted_language): Command Langauge




面向过程编程
C
Fortran
面向对象编程
C++
C#
Java
函数式编程
面向消息编程



在一般的编程过程中，都要先编译再执行。所谓编译就是把用C语言等编程语言编写的文件(源文件)转换成用机器语言(原生代码)编写的文件。









程序一般由关键字、常量、变量、运算符、类型和函数组成。

程序中可能会使用到这些分隔符：括号 ()，中括号 [] 和大括号 {}。

程序中可能会使用到这些标点符号：.、,、;、: 和 …。

程序的代码通过语句来实现结构化。每个语句不需要像 C 家族中的其它语言一样以分号 ; 结尾，因为这些工作都将由 Go 编译器自动完成。

如果你打算将多个语句写在同一行，它们则必须使用 ; 人为区分，但在实际开发中我们并不鼓励这种做法。



