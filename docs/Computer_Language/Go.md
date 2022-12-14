# The Go Programming Language

- golang - [A Tour of Gohttps://tour.golang.org/](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwierJvygubfAhXupVkKHboyCv8QFjAAegQIChAB&url=https%3A%2F%2Ftour.golang.org%2F&usg=AOvVaw1_8r9p82VJ6ungPMSEYhqa)

## Contents
* [初识GO](1.初识Go.md)
* [顺序编程](2.顺序编程.md)
* 面向对象编程
* 并发编程
* 网络编程
* 安全编程
* 工程管理

## materials

[系统学习GO，推荐几本靠谱的书? - 知乎]([https://www.zhihu.com/question/30461290\](https://www.zhihu.com/question/30461290%29)

相关网站

* Go 编程语言的维基百科： [en.wikipedia.org/wiki/Go\_\(programming\_language\)](http://en.wikipedia.org/wiki/Go_%28programming_language%29)

* 可以到http://code.google.com/p/go/ 4 直接下载最新代码。这里持续对Go资料进行了整理:http://github.com/wonderfo/wonderfogo/wiki。

* Official website:[The Go Programming Language](https://golang.org/). for basic knowlwdge


* Official Github: [github.com/golang/go](https://github.com/golang/go)

* Go 项目 Bug 追踪和功能预期详见 [github.com/golang/go/issues](https://github.com/golang/go/issues)

* go语言谷歌邮件列表  [golang-nuts](http://groups.google.com/group/golang-nuts/)  非常活跃，每天的讨论和问题解答数以百计。
Go的中文邮件组为http://groups.google.com/group/golang-china

* go语言在Google App Engine的应用的单独邮件列表 [google-appengine-go](https://groups.google.com/forum/#!forum/google-appengine-go)

> 以上 2 个邮件列表的讨论内容并不是分得很清楚，都会涉及到相关的话题。

* Go 语言开发社区的资源站 [go-lang.cat-v.org/](#)

* 官方的 Go IRC 频道 [irc.freenode.net](http://irc.freenode.net/)  的#go-nuts

* Go 语言相关资源的搜索引擎页面： [gowalker.org](https://gowalker.org/)

* Go语言运行在 Google App Engine 上的  [Go Tour](http://tour.golang.org/) ，也可通过执行命令go install go-tour.googlecode.com/hg/gotour 安装到本地机器上。  
  对于中文读者，可以访问该指南的[中文版本](http://go-tour-zh.appspot.com/) ，或通过命令 go install 行安装。

* Linked-in 的小组： [www.linkedin.com/groups?gid=2524765&trk=myg\_ugrp\_ovr](http://www.linkedin.com/groups?gid=2524765&trk=myg_ugrp_ovr)

* Go 语言在 Twitter 的官方帐号 [@golang](https://twitter.com/golang) 大家一般使用\#golang作为话题标签。

书籍

* Go 指南：[https://tour.go-zh.org/welcome/1](https://tour.go-zh.org/welcome/1)

* Go语言圣经：[https://legacy.gitbook.com/book/yar999/gopl-zh/details](https://legacy.gitbook.com/book/yar999/gopl-zh/details)

* Go in Action.\(Go 语言实战\)

  * 笔记 [Go语言环境搭建详解\|飞雪无情的博客](http://www.flysnow.org/2017/01/05/install-golang.html)

* [GitHub《The Way to Go》中文译本，中文正式名《Go 入门指南》](https://github.com/Unknwon/the-way-to-go_ZH_CN)   ——内容较旧




Go mindmap: https://github.com/gocn/knowledge







Doc: https://go.dev/doc/

* Download and Install Go: https://go.dev/doc/install
* The Go Programming Language Specification: https://go.dev/ref/spec
* Tutorial: Get started with Go: https://go.dev/doc/tutorial/getting-started
* [Tour of Go](https://go.dev/tour/)
* [How to Write Go Code](https://go.dev/doc/code.html)
* Effective Go: https://go.dev/doc/effective_go
* 



问题追踪和调试

工程管理



尽管看起来Java已经深获人心，但Java编程的体验并未尽如人意。
之所以开发Go 语言，是因为“近10年来开发程序之难让我们有点沮丧”。 这一定位暗示了Go语言希望取代C和Java的地位，成为最流行的通用开发语言。
Go语言设计者认为值得学习的是C语言，而不是C++。
互联网时代的C语言需要考虑哪些关键问题呢?

- 并行与分布式支持。必须要让这门语言操作多核计算机与计算机集群如同操作单机一样容易。
- 软件工程支持。工程规模不断扩大是产业发展的必然趋势。单机时代语言可以只关心 问题本身的解决，而互联网时代的C语言还需要考虑软件品质保障和团队协作相关的话题。
- 编程哲学的重塑。计算机软件经历了数十年的发展，形成了面向对象等多种学术流派。 什么才是最佳的编程实践?作为互联网时代的C语言，需要回答这个问题。

融合各家之长，极力维持语言特性的简洁，力求小而精。
2012年发布正式版



# Go

Code example: https://github.com/cncamp/golang

## 1. Go Introduction

### 1.1 思想

构建高可用微服务：**统一思想-12 factors**

* I. 基准代码： 一份基准代码，多份部署；讲究代码驱动
* II. 依赖： 显式声明依赖关系；go有专门的依赖管理工具
* III. 配置： 在环境中存储配置
* IV. 后端服务： 把后端服务当作附加资源
* V. 构建，发布，运行 严格分离构建和运行
* VI. 进程 以一个或多个无状态进程运行应用
* VII. 端口绑定 通过端口绑定提供服务
* VIII. 并发 通过进程模型进行扩展
* IX. 易处理 快速启动和优雅终止可最大化健壮性
* X. 开发环境与线上环境等价 尽可能的保持开发，预发布，线上环境相同
* XI. 日志 把日志当作事件流
* XII. 管理进程 后台管理任务当作一次性进程运行

### 1.2 Why Go语言

Go语言的原则

* Less is exponentially more.  裁掉很多不重要的功能
* Do less, Enable More.

其他语言弊端：

* 硬件发展速度远超软件
* C语言等原生语言缺乏好的依赖管理(依赖头文件) ， 依赖管理混乱，没有声明关系要依赖哪个.h的什么版本
* Java和C++等语言过于笨重，J2EE笨重
* 系统语言(如C语言)对**垃圾回收**和并行计算等基础功能缺乏支持，虽然性能好，但不高效，导致内存泄漏，非法访问
* 对多核计算机缺乏支持，并行计算，对线程的支持，已有语言的线程其实都是线程，开销大，且线程数量是有限的，

Go语言主要特性：全新的静态类型开发语言（强类型语言）

* 自动垃圾回收
* 更丰富的内置类型
* 函数多返回值
* 错误处理
* 匿名函数和闭包 
* 类型和接口
* 并发编程 
* 反射
* 语言交互性

Go语言：编译高效，支持高并发，面向垃圾回收的新语言

* 秒级完成大型程序单节点编译，
* 依赖管理清晰
* 不支持继承，程序员无需花费时间定义不同类型间的关系
* 支持垃圾回收，支持并罚执行，支持多线程通讯
* 对多核计算机支持友好

Go语言不支持的特性

* 不支持函数重载和操作符重载
* 为了避免C/C++开发中的bug和混乱，不支持隐式转换，
* 支持**接口抽象**，不支持继承；多用组合，少用继承，继承会提升系统复杂性；
* 不支持动态加载代码
* 不支持动态链接库；go编译成二进制文件，放在哪都能运行，不会因缺少依赖而无法运行
* 通过recover和panic替代异常机制
* 不支持断言
* 不支持静态变量

语言层面解决软件工程问题的设计哲学： 

* 不得包含在源代码文件中没有用到的包，否则Go编译器会报编译错误。
* 强制左花括号{的放置位置
* 函数名的大小写规则，

与C语言相比，Go语言摒弃了语句必须以分号作为语句结束标记的习惯。

go语言特性来源:

![](/Users/gmx/Documents/workspace/note/Computer-Science/docs/Computer_Language/assets/go语言特性来源.png)



### 1.3 Go 语言环境搭建

下载 Go：https://go.dev/doc/install

* Go 安装文件以及源代码 https://golang.google.cn/dl/

* 下载对应平台的二进制文件并安装

* 环境变量

  * GOROOT: go的安装目录; 将GOROOT加到/etc/profile环境变量后，在IDE看源码跳转到go本身的源码 
  * GOPATH：可以设成IDE的workspace
    * src:存放源代码  `/Users/gmx/go/src/github.com/<project_name>`
    * pkg:存放依赖包
    * bin:存放可执行文件

  * 其他常用变量
    * GOOS，GOARCH，GOPROXY
    * 国内用户建议设置 goproxy:export GOPROXY=https://goproxy.cn (七牛云提供的代理)

IDE 设置(VS Code)：

* 下载并安装VisualStudioCode https://code.visualstudio.com/download
* 安装Go语言插件 https://marketplace.visualstudio.com/items?itemName=golang.go
* 其他可选项
  * Intellj goland，收费软件 
  * vim，sublime等

### 1.5 Go环境变量

* **$GOROOT** 表示 Go 在你的电脑上的安装位置，它的值一般都是 $HOME/go，当然，你也可以安装在别的地方。
* **$GOARCH** 表示目标机器的处理器架构，它的值可以是 386、amd64 或 arm。
* **$GOOS** 表示目标机器的操作系统，它的值可以是 darwin、freebsd、linux 或 windows。
* **$GOBIN** 表示编译器和链接器的安装位置，默认是 $GOROOT/bin，如果你使用的是 Go 1.0.3 及以后的版本，一般情况下你可以将它的值设置为空，Go 将会使用前面提到的默认值
* **GoPATH**：允许多个目录，当有多个目录时，请注意分隔符，多个目录的时候Windows是分号;当有多个GOPATH时默认将go get获取的包存放在第一个目录下。GoPATH目录约有三个子目录：

  * Src：存放源代码(比如：.go .c .h .s等)   按照golang默认约定，go run，go install等命令的当前工作路径（即在此路径下执行上述命令）。开发程序的主要目录，所有的源码都是放在这个目录下面。，那么一般我们的做法就是一个目录一个项目，
  * Pkg：编译时生成的中间文件（比如：.a）
  * Bin : 编译后的可执行文件，为了方便，可把此目录加入到$PATH变量中，如果有多个gopath，那么使用
    ${GOPATH//://bin:}/bin添加所有的bin目录

### 1.4 Go基本命令

Go command: https://pkg.go.dev/cmd/go

* bug：start a bug report
* **build：compile packages and dependencies**  e.g. go build main.go ; GOOS=linux GOARCH=amd64 go build main.go
* clean：remove object files and cached files 
* doc：show documentation for package or symbol 
* env：print Go environment information
* fix：update packages to use new APIs
* **fmt：gofmt (reformat) package sources** e.g. go fmt main.go
* generate ：generate Go files by processing source 
* **get：add dependencies to current module and install them**
* **install：compile and install packages and dependencies**
* list：list packages or modules
* **mod：module maintenance** 依赖管理
* run：compile and run Go program
* **test：test packages** 
* **tool： run specified go tool** 
* version：print Go version 
* vet： report likely mistakes in packages

```sh
bug       # start a bug report
build     # compile packages and dependencies          e.g. go build main.go ; GOOS=linux GOARCH=amd64 go build main.go
clean     # remove object files and cached files
doc       # show documentation for package or symbol
env       # print Go environment information
fix       # update packages to use new APIs
fmt       # gofmt (reformat) package sources          e.g. go fmt main.go
generate  # generate Go files by processing source
get       # add dependencies to current module and install them
install   # compile and install packages and dependencies
list      # list packages or modules
mod       # module maintenance
run       # compile and run Go program
test      # test packages
tool      # run specified go tool
version   # print Go version
vet       # report likely mistakes in packages
```



Go build

* Go 语言不支持动态链接，因此编译时会将所有依赖编译进同一个二进制文件。 

* 指定输出目录。

  * go build –o bin/mybinary .

* 常用环境变量设置编译操作系统和 CPU 架构。

  * GOOS=linux GOARCH=amd64 go build 

* 全支持列表。

  * $GOROOT/src/go/build/syslist.go

* 适用情况： 测试编译，检查是否有编译错误，直接生产可执行程序(只生成编译结果而不自动运行 )

* 特点：只生成编译结果而不自动运行

* 简介：

  1. package name 为main的文件才能产生可执行文件，否则不会产生任何变化

  2. 执行该命令且以若干源码文件作为参数时，只有这些文件会被编译。列出代码运行所需全部源码文件，否则可能产生编译错误

  3. 执行该命令且不追加任何参数时，它会试图把当前目录作为代码包并编译

  4. 执行该命令且以代码包的导入路径作为参数时，该代码包及其依赖会被编译  
     1. 加入-a标记后所有涉及到的代码包都会被重新编译  
     2. 不加入-a标记，则只会编译归档文件中不是最新的代码包

* 使用

  1. 编译源码文件：go build [fileName].go

  2. 编译代码包：go build [代码包的导入路径]

* 常见标记

  | 标记  | 描述                                                         |
  | :---- | :----------------------------------------------------------- |
  | -o    | 指定输出文件。                                               |
  | -a    | 强行对所有涉及到的代码包（包括标准库中的代码包）进行重新构建，即使它们已经是最新的了。 |
  | -n    | 打印构建期间所用到的其它命令，但是并不真正执行它们。         |
  | -p n  | 构建的并行数量（n）。默认情况下并行数量与CPU数量相同。       |
  | -race | 开启数据竞争检测。此标记目前仅在linux/amd64、darwin/amd64和windows/amd64平台下被支持。 |
  | -v    | 打印出被构建的代码包的名字。                                 |
  | -work | 打印出临时工作目录的名字，并且取消在构建完成后对它的删除操作。 |
  | -x    | 打印出构建期间所用到的其它命令。                             |

  例如：go build -a [代码包的导入路径]

Go test

* go技术栈目标是把自动化流水线构建出来，所有代码经过自动化测试，通过自动化流水线到生产系统，测试用例到覆盖度非常重要

* Go 语言原生自带测试

  ```go
  import "testing"
  
  func TestIncrease(t *testing.T) { 
  	t.Log("Start testing") 
  	increase(1, 2)
  }
  ```

* go test ./... -v 运行测试

* go test 命令扫描所有*_test.go为结尾的文件，惯例是将测试代码与正式代码放在同目录， 如 foo.go 的测试代码一般写在 foo_test.go

Go vet: 代码静态检查，发现可能的 bug 或者可疑的构造

* Example: https://github.com/cncamp/golang/blob/master/examples/module1/govet/main.go

- Print-format 错误，检查类型不匹配的print 

  str := “hello world!”

  fmt.Printf("%d\n", str)

- Boolean 错误，检查一直为 true、false 或者冗余的表达式

  fmt.Println(i != 0 || i != 1)

- Range 循环，比如如下代码主协程会先退出，go routine无法被执行

  ```go
  words := []string{"foo", "bar", "baz"} 
  for _, word := range words {
  	go func() { 
  		fmt.Println(word).
  	}() 
  }
  ```

- Unreachable的代码，如 return 之后的代码

- 其他错误，比如变量自赋值，error 检查滞后等

  ```go
  res, err := http.Get("https://www.spreadsheetdb.io/") 
  defer res.Body.Close()
  if err != nil {
  	log.Fatal(err) 
  }
  ```

* 



1. $ go install 编译包文件并编译整个程序

   1. 用于编译并安装代码包或源码文件
      1. 安装代码包会在当前工作区的pkg/&lt;平台相关目录&gt;下生成归档文件
      2. 安装命令源码文件会在当前工作区的bin目录或$GOBIN目录下生成可执行文件
   2. 执行该命令且不追加任何参数时，它会试图把当前目录作为代码包并安装
      执行该命令且以代码包的导入路径作为参数时，该代码包及其依赖会被安装
      执行该命令且以命令源码文件及相关库源码文件作为参数时，只有这些文件会被编译并安装

2. $ go run 直接运行程序，方便调试 (将编译、链接和运行3个步骤合为一步 ,运行完后在当前目录下也看不 到任何中间文件和最终的可执行文件)

   1. 使用

      1. go run [fileName].go                    用于执行go的源代码 如go run helloworld.go

      2. go run [fileName].go -p [argu]            带参数[argu]执行go的源代码

   2. 常用标记

      -a：强制编译相关代码，无论是否编译过  
      -v：列出被编译的代码包的名称

      -a -v：列出所有被编译的代码包的名称

      -p n：并行编译，其中n为并行的数量 如-p 2

      -n：打印编译过程中所需运行的命令，但并不执行这些命令

      -x：打印编译过程中所需运行的命令，并执行这些命令

      -work：显示编译时创建的临时工作目录的路径，并且不删除这个临时工作目录

      使用方式：如go run -v [fileName].go

3. $ go get 获取远程包(需提前安装git或hg)

   1. 简介

      1. 用于从远程代码仓库（如Github）上**下载并安装**代码包
         支持的代码版本控制系统有：Git、Mercurial(hg)、SVN、Bazaar
      2. 指定的代码包会被下载到$GOPATH中包含的第一个工作区的src目录中

   2. 使用

      如`go get github.com/go-errors/errors`

   3. 常用标记

      | 标记 | 描述                                                         |
      | :--- | :----------------------------------------------------------- |
      | -d   | 只执行下载动作，而不执行安装动作                             |
      | -u   | 利用网络来更新已有的代码包及其依赖包                         |
      | -fix | 在下载代码包后先执行修正动作（版本兼容问题），而后再进行编译和安装 |

      例如：`go get -d github.com/go-errors/errors`

4. $ go fmt  格式化源码（部分IDE在保存时自动调用）

5. $ go test  运行测试文件（以_test.go结尾的文件）

6. $ go doc 查看文档（CHM手册）

   $ go doc  -http

### 1.5 代码版本控制

- 下载并安装 Git Command Line
  - https://git-scm.com/downloads
- Github
  * 本课程示例代码均上传在 https://github.com/cncamp/golang

- 创建代码目录
  - mkdir –p $GOPATH/src/github.com/cncamp
  - cd $GOPATH/src/github.com/cncamp
- 代码下载
  * git clone https://github.com/cncamp/golang.git

- 修改代码
- 上传代码
  - git add filename
  - git commit –m 'change logs'
  - git push

```sh
git init            # initiates git in the current directory
git remote add origin https://github.com/repo_name.git        # add remote reposiory
```

### 1.6 Golang playground

* 官方 playground：https://play.golang.org/
* 可直接编写和运行 Go 语言程序 
* 国内可直接访问的 playground https://goplay.tools/

## 代码格式

```
package PackageName

import （

）

func main() {

}
```

* 当你导入多个包时，最好按照字母顺序排列包名，这样做更加清晰易读。

* **每一段代码只会被编译一次**

* **如果对一个包进行更改或重新编译，所有引用了这个包的客户端程序都必须全部重新编译。**

* 如果包名不是以 . 或 / 开头，如 “fmt” 或者 “container/list”，则 Go 会在全局文件进行查找；如果包名以 ./ 开头，则 Go 会在相对目录中查找；如果包名以 / 开头（在 Windows 下也可以这样使用），则会在系统的绝对路径中查找。

* 除了符号 _，包中所有代码对象的标识符必须是唯一的，以避免名称冲突。但是相同的标识符可以在不同的包中使用，因为可以使用包名来区分它们。

* 你可以通过使用包的别名来解决包名之间的名称冲突，或者说根据你的个人喜好对包名进行重新设置，如：import fm “fmt”。

* main 函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的函数（如果有 init() 函数则会先执行该函数）

* 多行注释一般用于包的文档描述或注释成块的代码片段。

所有的结构将在这一章或接下来的章节中进一步地解释说明，但总体思路如下：

* 在完成包的 import 之后，开始对常量、变量和类型的定义或声明。

* 如果存在 init 函数的话，则对该函数进行定义（这是一个特殊的函数，每个含有该函数的包都会首先执行这个函数）。

* 如果当前包是 main 包，则定义 main 函数。

* 然后定义其余的函数，首先是类型的方法，接着是按照 main 函数中先后调用的顺序来定义相关函数，如果有很多函数，则可以按照字母顺序来进行排序。

反斜杠  可以在常量表达式中作为多行的连接符使用。

数字型的常量是没有大小和符号的，并且可以使用任何精度而不会导致溢出：

所有的内存在 Go 中都是经过初始化的。

所有的内存在 Go 中都是经过初始化的。

%s 代表字符串标识符、%v 代表使用类型的默认输出格式的标识符。这些标识符所对应的值从格式化字符串后的第一个逗号开始按照相同顺序添加

函数 fmt.Sprintf 与 Printf 的作用是完全相同的，不过前者将格式化后的字符串以返回值的形式返回给调用者，因此你可以在程序中使用包含变量的字符串，具体例子可以参见示例 15.4  [simple\_tcp\_server.go](https://github.com/Unknwon/the-way-to-go_ZH_CN/blob/master/eBook/examples/chapter_15/simple_tcp_server.go)

函数 fmt.Print 和 fmt.Println 会自动使用格式化标识符 %v 对字符串进行格式化，两者都会在每个参数之间自动增加空格，而后者还会在字符串的最后加上一个换行符

*标识符*：有效的标识符必须以字符（可以使用任何 UTF-8 编码的字符或 _）开头，然后紧跟着 0 个或多个字符或 Unicode 数字，如：X56、group1、_x23、i、өԑ12。无效的标识符：以数字开头、go语言关键字、包含运算符。

_ 本身就是一个特殊的标识符，被称为空白标识符。它可以像其他标识符那样用于变量的声明或赋值（任何类型都可以赋值给它），但任何赋给这个标识符的值都将被抛弃，因此这些值不能在后续的代码中使用，也不可以使用这个标识符作为变量对其它变量进行赋值或运算。在编码过程中，你可能会遇到没有名称的变量、类型或方法。虽然这不是必须的，但有时候这样做可以极大地增强代码的灵活性，这些变量被统称为匿名变量。

```
func GetName\(\) \(firstName, lastName, nickName string\){
  ...
return ”May”, “Chan”, “Chibi Maruko”
  ...
}
```

若只想获得nickName，则函数调用语句可以用如下方式编写:

_, _, nickName := GetName()



----





**Golang import**导入包语法介绍

[https://blog.csdn.net/u010649766/article/details/79458004](https://blog.csdn.net/u010649766/article/details/79458004)

写 Go 代码的时经常用到 import 这个命令用来导入包，参考如下：

```
import(
"fmt"
)
```

然后在代码里面可以通过如下的方式调用：

```fmt.Println( "我爱北京天安门" )```


fmt 是 Go 的标准库，它其实是去 GOROOT 下去加载该模块，当然 Go 的 import 还支持如下两种方式来加载自己写的模块：

相对路径

import  "./model" // 当前文件同一目录的 model 目录，但是不建议这种方式 import

1

绝对路径

import  "shorturl/model" // 加载 GOPATH/src/shorturl/model 模块

1

package 的导入的特殊用法

上面展示了一些 import 常用的几种方式，但是还有一些特殊的 import ，让很多新手很费解，下面是三种导入包的使用方法。

点操作

有时候会看到如下的方式导入包：

```
import(

. "fmt"

)
```

这个点操作的含义就是这个包导入之后在你调用这个包的函数时，你可以省略前缀的包名，也就是前面你调用的：

fmt.Println\( "我爱北京天安门" \)



可以省略的写成：

Println\( "我爱北京天安门" \)

1

别名操作

别名操作顾名思义可以把包命名成另一个用起来容易记忆的名字：

import\(

f "fmt"

\)

1

2

3

别名操作调用包函数时前缀变成了重命名的前缀，即：

f.Println\( "我爱北京天安门" \)

1

下划线操作

这个操作经常是让很多人费解的一个操作符，请看下面这个 import

import \(

“database/sql”

\_ “github.com/ziutek/mymysql/godrv”

\)

下滑线 “\_” 操作其实只是引入该包。当导入一个包时，它所有的 init\(\) 函数就会被执行，但有些时候并非真的需要使用这些包，仅仅是希望它的 init\(\) 函数被执行而已。这个时候就可以使用 “\_” 操作引用该包了。即使用 “\_” 操作引用包是无法通过包名来调用包中的导出函数，而是只是为了简单的调用其 init\(\) 函数。



impot

导入本地：`import  "fmt"`

导入远程包：`import “github.com/mattn/go-sqlite3”`   //计算CRC32的包托管于Github

                然后，在执行go build或者go install之前，只需要加这么一句：`go get github.com/mattn/go-sqlite3`
    
                go get下来的源码位置应为：¥GOPATH/src/github.com/mattn/go-sqlite3\(这里是物理路径\)
    
                  若网络问题导致无法使用go get下载，则需要手动下载包那就应该在src目录下建立同样的子目录将包存放到此处。
    
                 例如你的报错信息中有golang.org/x/net/context这个包，
    
                 因为golang.org的服务器是谷歌公司的，IP被封，你通过手动等方式下载回来的包因该存放到此处:
    
                 $GOPATH/src/golang.org/x/net/context



## Write a example

* $ cd /Users/guogmx/Documents/workspace/workspace_go

* $ mkdir src/hello

* $ vim hell.go

```
package main

import "fmt"

func main(){
   ...
   fmt.Printf("hello, world")
   ...
}
```

* $ go build

* $ ./hello

* hello, world

* $ go install

> You can run go install to install the binary into your workspace’s bin directory or go clean -I to remove it.



## 2. 顺序编程

### 2.1 流程控制

* if
* switch
* for
* For-range

#### 2.1.1 If

基本形式

```go
if condition1 {
	// do something
} else if condition2 {
	// do something else
} else {
	// catch-all or default
}
```

if 的简短语句同 for 一样， if 语句可以在条件表达式前执行一个简单的语句。

```go
if v := x - 100; v < 0{ 
	return v
}
```

#### 2.1.2 Switch

当分支很多时选switch

```go
switch var1 {
	case val1: //空分支 
	case val2:
		fallthrough //执行case3中的f() 
	case val3:
		f()
	default: //默认分支
	... 
}
```

#### 2.1.3 For

Example: https://github.com/cncamp/golang/blob/master/examples/module1/forloop/main.go

Go 只有一种循环结构:for 循环。

* 计入计数器的循环

  for 初始化语句; 条件语句; 修饰语句 {}

  ```go
  for i := 0; i < 10; i++ { 
  	sum += i
  }
  ```

* 初始化语句和后置语句是可选的，此场景与 while 等价(Go 语言不支持 while)

  ```go
  for ; sum < 1000; { 
  	sum += sum
  }
  ```

* 无限循环

  ```go
  for {
  	if condition1 {
  		break
  	} 
  }
  ```

#### 2.1.4 for-range

遍历数组，切片，字符串，Map 等 

```go
for index, char := range myString { 
	...
}
for key, value := range MyMap {
	...
}
for index, value := range MyArray { 
	...
}
```

需要注意:如果 for range 遍历指针数组，则 value 取出的指 针地址为原指针地址的拷贝。

### 2.2 常量

const identifier type

常量是指编译期间就已知且不可改变的值。常量可以是数值类型(包括整型、
浮点型和复数类型)、布尔类型、字符串类型等。

* 字面常量：程序中硬编码的常量，

  ```go
  -12
  3.14159265358979323846 // 浮点类型的常量 
  3.2+12i // 复数类型的常量 
  true // 布尔类型的常量 
  "foo" // 字符串常量
  ```

  > 在其他语言中，常量通常有特定的类型，比如12在C语言中会认为是一个int类型的常量。 如果要指定一个值为12的long类型常量，需要写成12l，这有点违反人们的直观感觉。Go语言 的字面常量更接近我们自然语言中的常量概念，它是无类型的。只要这个常量在相应类型的值域 范围内，就可以作为该类型的常量，比如上面的常量12，它可以赋值给int、uint、int32、 int64、float32、float64、complex64、complex128等类型的变量

* 常量定义

  ```go
  const Pi float64 = 3.14159265358979323846
  const zero = 0.0 // 无类型浮点常量 
  const (
      size int64 = 1024
      eof = -1 // 无类型整型常量
  )
  const u, v float32 = 0, 3 // u =0.0, v = 3.0,常量的多重赋值
  const a, b, c = 3, 4, "foo" //a=3,b=4,c="foo", 无类型整型和字符串常量
  ```

  > Go的常量定义可以限定常量类型，但不是必需的。如果定义常量时没有指定类型，那么它 与字面常量一样，是无类型常量。常量定义的右值也可以是一个在编译期运算的常量表达式，比如```const mask = 1 << 3``` .由于常量的赋值是一个编译期行为，所以右值不能出现任何需要运行期才能得出结果的表达式

* 预定义常量

### 2.3 变量

 var identifier type

变量相当于是对一块数据存储 空间的命名，程序可以通过定义一个变量来申请一块数据存储空间，之后可以通过引用变量名来 使用这块存储空间。

* 变量声明

  ```
  var v1 int
  var v2 string 
  var v3 [10]int // 数组
  var v4 []int // 数组切片
  var v5 struct {
      f int 
  }
  var v6 *int // 指针
  var v7 map[string]int // map，key为string类型，value为int类型
  var v8 func(a int) int
  ```

  ```go
  var (
      v1 int
      v2 string
  )
  ```

* 变量初始化

  ```go
  var v1 int = 10 // 正确的使用方式1
  var v2 = 10 // 正确的使用方式2，编译器可以自动推导出v2的类型,如果初始化值已存在，则可以省略类型;变量会从初始值中获得类型。 
  v3 := 10 // 正确的使用方式3，编译器可以自动推导出v3的类型
  ```

* 变量赋值

  ```go
  var v10 int 
  v10 = 123
  ```

  ```go
  i,j = j, i // 多重赋值：交换i和j变量
  ```

* 匿名变量:短变量声明, 为了让代码行数变少

  * 在函数中，简洁赋值语句 := 可在类型明确的地方代替 var 声明。
  * 函数外的每个语句都必须以关键字开始(var, func 等等)，因此 := 结构不能在函数外使用。

  ```go
  func GetName() (firstName, lastName, nickName string) {    
      return "May", "Chan", "Chibi Maruko"
  } 
  若只想获得nickName，则函数调用语句可以用如下方式编写:
  _, _, nickName := GetName()
  
  c, python, java := true, false, "no!"
  ```

* 类型转换与推导

  * 类型转换: 表达式 T(v) 将值 v 转换为类型 T。

    * 一些关于数值的转换: 
      * var i int=42 
      * var f float64 = float64(i)
      * var u uint = uint(f) l 

    * 或者，更加简单的形式:
      * i:=42
      * f := float64(i) 
      * u := uint(f)

  * 类型推导

    * 在声明一个变量而不指定其类型时(即使用不带类型的 := 语法或 var = 表达式语法)，变量的类型由右值推导得出。

      ```go
      * var i int
      * j:=i     // j也是一个int
      ```

### 2.4 类型

Go语言内置以下这些基础类型:

* 布尔类型:bool。
* 整型:int8、byte、int16、int、uint、uintptr等。 
* 浮点类型:float32、float64。
* 复数类型:complex64、complex128。 
* 字符串:string。
* 字符类型:rune。
* 错误类型:error。

此外，Go语言也支持以下这些复合类型: 

* 指针(pointer)
* 数组(array)
* 切片(slice)
* 字典(map)
* 通道(chan)
* 结构体(struct) 
* 接口(interface)

#### 2.4.1 数组

* 相同类型且长度固定<mark>连续内存片段</mark> : <mark>固定长度</mark>

* 以编号访问每个元素

* 定义方法 

  ```go
  var identifier [len]type`
  ```

* 示例 

  ```go
  myArray:=[3]int{1,2,3}
  ```

#### 2.4.2 切片(slice)

- 切片是对数组一个连续片段的引用, 切片也是连续的内存片段，但是不定长度，数组必须固定长度

- 数组定义中不指定长度即为切片

  ```go
  var identifier []type
  ```

- 切片在未初始化之前默认为nil，长度为0

- 常用方法：https://github.com/cncamp/golang/blob/master/examples/module1/slice/main.go

  ```go
  func main() {
  	myArray := [5]int{1, 2, 3, 4, 5}
  	mySlice := myArray[1:3] 
  	fmt.Printf("mySlice %+v\n", mySlice) 
  	fullSlice := myArray[:]
  	remove3rdItem := deleteItem(fullSlice, 2) 
  	fmt.Printf("remove3rdItem %+v\n", remove3rdItem)
    
    mySlice1 := []int{} // go语言里用slice多用array少
    mySlice1 = append(mySlice1, 1)
    mySlice1 = append(mySlice1, 2)
    mySlice1 = append(mySlice1, 3)
    mySlice1 = append(mySlice1, 4)
  }
  func deleteItem(slice []int, index int) []int { // 删除，go没有提供原生的slice删除方法
  	return append(slice[:index], slice[index+1:]...) 
  }
  ```

- 构造slice可以通过make或new方式

  * New返回指针地址

  * Make返回第一个元素，可预设内存空间，避免未来的内存拷贝

  * 示例 https://github.com/cncamp/golang/blob/master/examples/module1/slice/makenew/main.go

    ```go
    mySlice1 := new([]int) 
    mySlice2 := make([]int, 0) 
    mySlice3 := make([]int, 10) 
    mySlice4 := make([]int, 10, 20) //初始给10空间。最多给20
    ```

​			<img src="/Users/gmx/Documents/workspace/note/Computer-Science/docs/Computer_Language/assets/make_new.png" style="zoom:50%;" />

* 关于切片的常见问题

  * 切片是连续内存并且可以动态扩展，由此引发的问题? 

    ```go
    a := []int{}
    b := []int{1,2,3} 
    c := a
    a = append(b, 1) //如果b的连续空间已用完，append时需要重新寻找一块连续的内存空间，地址和原来不一样，导致a与c 不相等，解决方法：append b 后赋值给b
    ```

  * 修改切片的值? https://github.com/cncamp/golang/blob/master/examples/module1/slice/forrange/main.go

    ```go
    mySlice := []int{10, 20, 30, 40, 50} 
    for _, value := range mySlice {
    	value *= 2  // vaule时临时变量，所以这里vaule*2不影响myslice的值，go语言任何地方都是值传递
    }
    fmt.Printf("mySlice %+v\n", mySlice) 
    for index, _ := range mySlice {
    	mySlice[index] *= 2 // 解决方法：用下标访问slice
    }
    fmt.Printf("mySlice %+v\n", mySlice)
    ```

#### 2.4.3 Map

* 声明方法

  ```go
  var map1 map[keytype]valuetype //key只能是int string 这种简单类型
  ```

* 示例: https://github.com/cncamp/golang/blob/master/examples/module1/map/main.go

  ```go
  myMap := make(map[string]string, 10)  
  myMap["a"] = "b"
  myFuncMap := map[string]func() int{ 
    	"funcA": func() int { return 1 },
  }
  fmt.Println(myFuncMap)
  f := myFuncMap["funcA"] 
  fmt.Println(f())
  ```

* 访问 Map 元素

  * 按 Key 取值

    ```go
    value, exists := myMap["a"] 
    if exists {
    	println(value)
    }
    ```

  * 遍历 Map: for-range

    ```go
    for k, v := range myMap { 
    	println(k, v)
    }
    ```

#### 2.4.4 指针

指针是一个代表着某个内存地址的值, 这个内存地址往往是在内存中存储的另一个变量的值的起始位置.

Go语言对指针的支持介于Java语言和 C/C++ 语言之间, 它既没有像Java那样取消了代码对指针的直接操作的能力, 也避免了 C/C++ 中由于对指针的滥用而造成的安全和可靠性问题.

指针的copy比struct的copy成本更小

https://www.cnblogs.com/cheyunhua/p/16652003.html

#### 2.4.5 结构体和指针

- 通过 type ... struct 关键字自定义结构体

- Go 语言支持指针，但不支持指针运算 

  - 指针变量的值为内存地址
  - 未赋值的指针为 nil

- 示例：https://github.com/cncamp/golang/blob/master/examples/module1/struct/main.go

  https://github.com/cncamp/golang/blob/master/examples/module1/pointer/main.go

  ```go
  type MyType struct { 
  	Name string
  }
  
  func printMyType(t *MyType){  // (t *MyType)为了声明参数t是struct MyType的指针，是一个固定语法
    println(t.Name)             // 指针 方法定义用*，取地址用&
  } 
  
  func main(){
  	t := MyType{Name: "test"}  //t是struct
    printMyType(&t)  // &t取struct的指针地址，//通过*取指针变量的值
  }
  ```

* struct 只能包含属性，interface是一组函数方法的抽象，只能定义行为:https://github.com/cncamp/golang/blob/master/examples/module1/interface/main.go

  ```go
  type IF interface {
  	getName() string
  }
  
  type Human struct {
  	firstName, lastName string
  }
  ```

* 结构体标签

  * 结构体中的字段除了有名字和类型外，还可以有一个可选的标签(tag)

  * 使用场景:Kubernetes APIServer 对所有资源的定义都用 Json tag 和 protoBuff tag, yaml 首先转成json，json与go的struct转换

    ```go
    NodeName string `json:"nodeName,omitempty" protobuf:"bytes,10,opt,name=nodeName"`
    ```

  * ```go
    type MyType struct {
    	Name string `json:"name"` 
    }
    
    func main() {
    	mt := MyType{Name: "test"} 
    	myType := reflect.TypeOf(mt) 
    	name := myType.Field(0)
    	tag := name.Tag.Get("json")  //通过反射机制把这个属性的json标签拿出来
    	println(tag)
    }
    //通过序列化和反序列化把json string变成内存空间的一个变量值
    ```

* 类型重命名 ：做了枚举类型变量，定义这种类型的变量时不会滥用，不会随便去写

  ```go
  // Service Type string describes ingress methods for a service
  type ServiceType string 
  
  const (
  	// ServiceTypeClusterIP means a service will only be accessible inside the 
    // cluster, via the ClusterIP.
  	ServiceTypeClusterIP ServiceType = "ClusterIP"
  
  	// ServiceTypeNodePort means a service will be exposed on one port of 
    // every node, in addition to 'ClusterIP' type.
  	ServiceTypeNodePort ServiceType = "NodePort"
  
  	// ServiceTypeLoadBalancer means a service will be exposed via an
  	// external load balancer (if the cloud provider supports it), in addition 
    // to 'NodePort' type.
  	ServiceTypeLoadBalancer ServiceType = "LoadBalancer"
  
  	// ServiceTypeExternalName means a service consists of only a reference to 
    // an external name that kubedns or equivalent will return as a CNAME
  	// record, with no exposing or proxying of any pods involved.
  	ServiceTypeExternalName ServiceType = "ExternalName" 
  )
  ```

### 2.5 函数

Main 函数: https://github.com/cncamp/golang/blob/master/examples/module1/map/main.go

- 每个 Go 语言程序都应该有个 main package

- Main package 里的 main 函数是 Go 语言程序入口 

  ```go
  package main
  func main() {
  	args := os.Args 
    if len(args) != 0 {
  		println("Do not accept any argument")
  		os.Exit(1) 
    }
  	println("Hello world") 
  }
  ```

参数解析

* 请注意main函数与其他语言不同，没有类似java的[]stringargs参数

* Go语言如何传入参数呢? 

  * 方法1:

    ```go
     fmt.Println("osargsis:",os.Args)
    ```

  * 方法2:

    ```go
    name:=flag.String("name","world","specify the name you want to say hi")
    flag.Parse()
    ```

Init 函数：https://github.com/cncamp/golang/blob/master/examples/module1/init/main.go

* Init函数:会在包初始化时运行, 包被第一次加载时，所有程序运行之前运行init

* 有些包是被调用的没有main函数，这是就需要init来执行初始化的操作

* 谨慎使用init函数

  * 当多个依赖项目引用统一项目，且被引用项目的初始化在 init 中完成，并且不可重复运行时，会导致启动错误

  ```go
  package main
  var myVariable = 0 
  func init() {
  	myVariable = 1 
  }
  ```

返回值 

* 多值返回：异常处理更简洁，error 是一个返回值

  * 函数可以返回任意数量的返回值 • 

* 命名返回值

  * Go 的返回值可被命名，它们会被视作定义在函数顶部的变量。
  * 返回值的名称应当具有一定的意义，它可以作为文档使用。
  * 没有参数的 return 语句返回已命名的返回值。也就是直接返回。

* 调用者忽略部分返回值

  ```go
   result, _ = strconv.Atoi(origStr)
  ```

传递变长参数

* Go 语言中的可变长参数允许调用方传递任意多个相同类型的参数 • 

* 函数定义

  ```go
  func append(slice []Type, elems ...Type) []Type
  ```

* 调用方法

  ```go
  myArray := []string{}
  myArray = append(myArray, "a","b","c")
  ```

内置函数: 不加包名，引用名 直接用

| 函数名              | 作用                             |
| :------------------ | -------------------------------- |
| close               | 管道关闭                         |
| len, cap            | 返回数组、切片，Map 的长度或容量 |
| new, make           | 内存分配                         |
| copy, append        | 操作切片                         |
| panic, recover      | 错误处理                         |
| print, println      | 打印                             |
| complex, real, imag | 操作复数                         |

回调函数(Callback)

* 函数作为参数传入其它函数，并在其他函数内部调用执行

  - strings.IndexFunc(line, unicode.IsSpace)

  - Kubernetes controller的leaderelection

* 示例：https://github.com/cncamp/golang/blob/master/examples/module1/callbacks/main.go

  ```go
  func main() {
  	DoOperation(1, increase)
  	DoOperation(1, decrease) 
  }
  func increase(a, b int) { 
  	println(“increase result is:”, a+b)
  }
  func DoOperation(y int, f func(int, int)) {
  	f(y, 1) 
  }
  func decrease(a, b int) { 
  	println("decrease result is:", a-b)
  }
  ```

闭包

* 实际是个匿名函数：定义函数是为了逻辑抽象，为了易于阅读，提高重用性； 当想要某段逻辑独立 运行且不想起个函数名字

  * 不能独立存在

  * 可以赋值给其他变量  x:=func(){}  // 函数的声明

  * 可以直接调用  func(x,yint){println(x+y)}(1,2) //运行函数

  * 可作为函数返回值  func Add() (func(b int) int) 

  * 使用场景

    ```go
    defer func() {
    	if r := recover(); r != nil {
    		println(“recovered in FuncX”) 
      }
    }()
    ```











### 2.6 反射机制

* reflect.TypeOf ()返回被检查对象的类型 

* reflect.ValueOf()返回被检查对象的值

* 示例

  ```
  myMap := make(map[string]string, 10) myMap["a"] = "b"
  t := reflect.TypeOf(myMap) fmt.Println("type:", t)
   v := reflect.ValueOf(myMap) fmt.Println("value:", v)
  ```

* 基于 struct 的反射

  ```go
  // struct
  myStruct := T{A: "a"}
  v1 := reflect.ValueOf(myStruct)
  for i := 0; i < v1.NumField(); i++ { 
    fmt.Printf("Field %d: %v\n", i, v1.Field(i))
  }
  for i := 0; i < v1.NumMethod(); i++ { 
    fmt.Printf("Method %d: %v\n", i, v1.Method(i)) 
  }
  // 需要注意 receive 是 struct 还是指针
  result := v1.Method(0).Call(nil) 
  fmt.Println("result:", result)
  ```

### 2.6 错误处理



## 3. 面向对象编程

Go 语言中的面向对象编程

* 可见性控制

  - public - 常量、变量、类型、接口、结构、函数等的名称大写

  - private - 非大写就只能在包内使用

* 继承

  - 通过组合实现，内嵌一个或多个 struct

* 多态
  * 通过接口实现，通过接口定义方法集，编写多套实现

Json 编解码

* Unmarshal:从string转换至struct
  func unmarshal2Struct(humanStr string)Human {

h := Human{}
 err := json.Unmarshal([]byte(humanStr), &h) if err != nil {

println(err)
 }}
 return h return string(updatedBytes)



• •

json 包使用 map[string]interface{} 和 []interface{} 类型保存任意对象 可通过如下逻辑解析任意 json

var obj interface{}
 err := json.Unmarshal([]byte(humanStr), &obj) objMap, ok := obj.(map[string]interface{})
 for k, v := range objMap {

switch value := v.(type) { case string:

fmt.Printf("type of %s is string, value is %v\n", k, value) case interface{}:

fmt.Printf("type of %s is interface{}, value is %v\n", k, value) default:

fmt.Printf("type of %s is wrong, value is %v\n", k, value) }

}

### 方法

* 方法:作用在接收者上的函数

  * func (recv receiver_type) methodName(parameter_list) (return_value_list) • 使用场景

* 很多场景下，函数需要的上下文可以保存在receiver属性中，通过定义 receiver 的方法，该方法可以直接 访问 receiver 属性，减少参数传递需求

  ```go
  // StartTLS starts TLS on a server from NewUnstartedServer. 
  func (s *Server) StartTLS() {
  	if s.URL != “” {
  		panic(“Server already started”)
  }
   	if s.client == nil {
  		s.client = &http.Client{Transport: &http.Transport{}
    } 
  }
  ```

方法与函数：

接受者传递了一些信息，从程序设计层面设计接口抽象出一些行为，可以定义一些方法，从程序实现层面，一个函数有时需要几十个参数，不通过如参，把参数定义成属性。



传值还是传指针：https://github.com/cncamp/golang/blob/master/examples/module1/pointer/main.go

- Go语言只有一种规则-传值
- 函数内修改参数的值不会影响函数外原始变量的值
- 可以传递指针参数将变量地址传递给调用函数，Go语言会 复制该指针作为函数内的地址，但指向同一地址
- 思考:当我们写代码的时候，函数的参数传递应该用struct 还是pointer?

如果变量是struct，想要改变这个变量，传变量的地址, 不想改变传值



#### 接口

* 接口定义一组方法集合, 接口是一个逻辑抽象，把一个对象的行为抽象出来但不写具体实现

  ```go
  type IF interface {
  	Method1(param_list) return_type 
  }
  ```

* 适用场景:Kubernetes中有大量的接口抽象和多种实现

* Struct无需显示声明实现interface，只需直接实现方法

* Struct除实现interface定义的接口外，还可以有额外的方法 

* 一个类型可实现多个接口(Go语言的多重继承)

* Go语言中接口不接受属性定义

* 接口可以嵌套其他接口

* 示例：k8s service需要适配不同cloud：AWS Azure openstack, service有个类型loadBalanceType，要与不同的云厂商对接loadBalance管理接口，从service的语义来说就是定义负载均衡，操作也是固定的：配置删除更新；所以可以抽象一个loadBalanceTyper servcie，不同厂商去实现这个interface。对于service controller只需要调用接口，

  https://github.com/cncamp/golang/blob/master/examples/module1/interface/main.go

```go
type IF interface { 
  getName() string
}
type Human struct {
	firstName, lastName string
}
func (h *Human) getName() string { 
  return h.firstName + "," + h.lastName
}
type Car struct {
	factory, model string
}
func (c *Car) getName() string { 
  return c.factory + "-" + c.model
}
func main() {
	interfaces := []IF{}
	h := new(Human)
	h.firstName = "first"
	h.lastName = "last"
	interfaces = append(interfaces, h) 
  c := new(Car)
	c.factory = "benz"
	c.model = "s"
	interfaces = append(interfaces, c) 
  for _, f := range interfaces {
		fmt.Println(f.getName()) 
  }
}
```

注意事项

* Interface是可能为nil的，所以针对interface的使用一定要预 先判空，否则会引起程序 crash(nil panic)

* Struct初始化意味着空间分配，对struct的引用不会出现空指针

## 4. 并发编程

并发编程：多线程

并发和并行：

* 并发(concurrency)：两个或多个事件在同一时间间隔发生 
* 并行(parallellism)：两个或者多个事件在同一时刻发生

## 5. 网络编程

## 6. 安全编程

## 7. 工程管理















### 常用语法





## 包管理

go包管理与java类似，java包管理需要写全路径，go只需要写最后一个包名

* 标准库包

  * log: 基本的日志功能

  * os

  * sync

  * fmt :格式化IO

    ```go
    fmt.Println("aa", "bb", "cc")
    fmt.Printf("message, %+v%s%s\n", "a", "b", "c")
    fmt.Sprintf() //拼接字串时候用
    fmt. Errorf()
    ```

  * flag：命令行参数的规则定义以及获取和解析命令行参数; https://github.com/cncamp/golang/blob/master/examples/module1/helloworld/main.go

* 第三方包





### 

## 框架

* [Gin —— a HTTP web framework written in Go \(Golang\)](https://github.com/gin-gonic)

## **Go**跨平台编译

Golang支持交叉编译，也就是说你在32位平台的机器上开发，可以编译生成64位平台上的可执行程序。

交叉编译依赖下面几个环境变量：

$GOARCH    目标平台（编译后的目标平台）的处理器架构（386、amd64、arm）  
 $GOOS          目标平台（编译后的目标平台）的操作系统（darwin、freebsd、linux、windows）

执行下面命令：

$ cd /usr/local/go/src  
 $ sudo CGO\_ENABLED=0 GOOS=linux GOARCH=amd64 ./make.bash

这里 额外多一个环境变量 CGO\_ENABLED 是因为 交叉编译不支持 CGO，我们这里禁用它。

**\[shell\]shell**中**\| &&\|\| \(\) {}**用法以及**shell**的逻辑与或非

[**https://www.cnblogs.com/aaronLinux/p/8340281.html**](https://www.cnblogs.com/aaronLinux/p/8340281.html)

Golang 支持在一个平台下生成另一个平台可执行程序的交叉编译功能。


Mac下编译Linux, Windows平台的64位可执行程序：

CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build test.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build test.go
Linux下编译Mac, Windows平台的64位可执行程序：


CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build test.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build test.go

GOOS：目标可执行程序运行操作系统，支持 darwin，freebsd，linux，windows
GOARCH：目标可执行程序操作系统构架，包括 386，amd64，arm






 go编译器

目前Go语言有2套编译器:GC和gccgo。其中GC提供的cgo支持C语言,gccgo支持C/C++。

golang 项目的工程组织规范：

```
$GOPATH
├─bin
├─pkg
└─src
    └─github.com(远程包)
    └─golang.org(远程包)
    └─your_pkg_src(本地包)
```

## go工具

 bin/ 目录下主要包括以下几个工具：

dlv.exe	go 语言调试工具
gocode.exe	go语言代码检查，自动补全
godef.exe 	go语言代码定义和引用的跳转
golint.exe 	go语言代码规范检查
go-outline.exe 	用于在Go源文件中提取JSON形式声明的简单工具
gopkgs.exe 	快速列出可用包的工具
gorename.exe 	在Go源代码中执行标识符的精确类型安全重命名
goreturns.exe 	类似fmt和import的工具，使用零值填充Go返回语句以匹配func返回类型
go-symbols.exe 	从go源码树中提取JSON形式的包符号的工具
gotour.exe 	go语言指南网页版
guru.exe 	go语言源代码有关工具，如代码高亮等
————————————————
版权声明：本文为CSDN博主「阿龙哥哥」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/v6543210/article/details/84504460

## Go编译顺序

Go命令行工具只是一个源代码管理工具，或者说是一个前端。真正的Go编译 器和链接器被Go命令行工具隐藏在后面，我们可以直接使用它们:

```
$ 6g helloworld.go

$ 6l helloworld.6

$ ./6.out

Hello, world. 你好，世界!
```

6g和6l是64位版本的Go编译器和链接器，对应的32位版本工具为8g和8l。Go还有另外一个 GCC版本的编译器，名为 gccgo，但不在本书的讨论范围内。



## 问题追踪和调试

1. 打印日志：fmt包或log包
2. GDB调试 ```$ gdb softwareName```

