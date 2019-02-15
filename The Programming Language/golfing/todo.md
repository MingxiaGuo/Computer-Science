## 框架

* [Gin —— a HTTP web framework written in Go \(Golang\)](https://github.com/gin-gonic)

impot

导入本地：`import  "fmt"`

导入远程包：`import “github.com/mattn/go-sqlite3”`   //计算CRC32的包托管于Github

                然后，在执行go build或者go install之前，只需要加这么一句：`go get github.com/mattn/go-sqlite3`

                go get下来的源码位置应为：¥GOPATH/src/github.com/mattn/go-sqlite3\(这里是物理路径\)

                  若网络问题导致无法使用go get下载，则需要手动下载包那就应该在src目录下建立同样的子目录将包存放到此处。

                 例如你的报错信息中有golang.org/x/net/context这个包，

                 因为golang.org的服务器是谷歌公司的，IP被封，你通过手动等方式下载回来的包因该存放到此处:

                 $GOPATH/src/golang.org/x/net/context

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



