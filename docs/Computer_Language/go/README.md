# The GO Programming Language

- golang - [A Tour of Gohttps://tour.golang.org/](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwierJvygubfAhXupVkKHboyCv8QFjAAegQIChAB&url=https%3A%2F%2Ftour.golang.org%2F&usg=AOvVaw1_8r9p82VJ6ungPMSEYhqa)

---

语言层面解决软件工程问题的设计哲学： 

* 不得包含在源代码文件中没有用到的包，否则Go编译器会报编译错误。
* 强制左花括号{的放置位置
* 函数名的大小写规则，

与C语言相比，Go语言摒弃了语句必须以分号作 为语句结束标记的习惯。

编译环境准备： https://go.dev/doc/install

Go集成开发环境(IDE)：VSCode

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





Doc: https://go.dev/doc/

* Download and Install Go: https://go.dev/doc/install

* The Go Programming Language Specification: https://go.dev/ref/spec
* Tutorial: Get started with Go: https://go.dev/doc/tutorial/getting-started

* [Tour of Go](https://go.dev/tour/)
* [How to Write Go Code](https://go.dev/doc/code.html)
* Effective Go: https://go.dev/doc/effective_go

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

