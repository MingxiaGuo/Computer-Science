# Prerequsite
## 读数据
https://blog.csdn.net/TomorrowAndTuture/article/details/137657143

### bufio.NewReader
逐行读取输入，并且处理每行的数据
ReadLine 是一个低级的行读取原语。大多数调用者应该使用 ReadBytes(‘\n’) 或 ReadString(‘\n’)，或者使用 Scanner。


```go

reader := bufio.NewReader(os.Stdin)

// ********** 按行读取，读取的行不包括换行符本身 ***********
data, _, _ := reader.ReadLine() // 读取第一行； 
inputStr1 = string(data) 
data, _, _ := reader.ReadLine()  // 读取第二行
inputStr2 = string(data) 

// 按自己指定的分隔符如\n 读取，读取的结果包含\n本身，如果按\n读取后需要使用strings.TrimSpace去掉字符串两端的空白
data, _, _ := reader.ReadString("\n")

// **************** 读取多行 *******************
reader := bufio.NewReader(os.Stdin)
for {
	
	line, _, err := reader.ReadLine()
	if err != nil {
		break
	}
	parts := strings.Fields(cmd)
	
}


// 
reader := bufio.NewReader(os.Stdin)
for {
	line, err := reader.ReadString('\n')
	if err != nil {
		break // EOF or other error
	}
	line = strings.TrimSpace(line) // 去除换行符等首尾的空白字符
	parts := strings.Fields(cmd)
}	
```


### bufio.NewScanner
和NewReader不同在于scanner读取多行

```go
scanner := bufio.NewScanner(os.Stdin)
// scanner.Split(bufio.ScanLines) // 如果保持默认可不写这一行
scanner.Scan()  // 读取第一行； 默认一次Scan()读取一行数据
inputStr1 := scanner.Text()
scanner.Scan()  // 读取第二行
inputStr2 := scanner.Text()


scanner := bufio.NewScanner(os.Stdin)
for scanner.Scan(){
	line := scanner.Text()
	parts := strings.Fileds(line)
}

```

### fmt.Scan

会读取标准输入直到遇到空格、制表符或换行符，并且不会读取这些分隔符。这适合读取一行中的多个单词或命令。

读取由空白符分割的值保存到传递给参数，换行符视为空白符

```go
var (
	name string
	age int
	married bool
)
fmt.Scan(&name, &age, &married) //读取由空白符分割的值保存到传递给参数，换行符视为空白符

fmt.Scanf("1:%s 2:%d 3:%t",&name,&age,&married) // 根据format参数指定的格式去读取值保存传递给参数

fmt.Scanln(&name, &age, &married) // 与Scan类似，它在遇到换行时才停止扫描



var N,num int
fmt.Scan(&N)
for i := 0; i < N; i++ {
	fmt.Scan(&num)
}
```

## 格式化输出


|格  式|描  述|
|---|---|
|%v|按值的本来值输出|
|%+v|在 %v 基础上，对结构体字段名和值进行展开|
|%#v|输出 Go 语言语法格式的值|
|%T|输出 Go 语言语法格式的类型和值|
|%%|输出 % 本体|
|%b|整型以二进制方式显示|
|%o|整型以八进制方式显示|
|%d|整型以十进制方式显示|
|%x|整型以十六进制方式显示|
|%X|整型以十六进制、字母大写方式显示|
|%U|Unicode 字符|
|%f|浮点数|
|%p|指针，十六进制方式显示|

## 值与地址
在 Golang 中，int，float，bool，string，array，struct 都属于值类型，数据拷贝时都是值拷贝，拷贝副本过来。

## 指针与地址

 &t取struct t的指针地址，通过\*取指针变量的值
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


```go

func main() {
    type data struct{ a int }
    var d = data{1234}
    var p *data
	p = &d
	fmt.Printf("%p, %v\n", p, p.a) // 直接⽤用指针访问⺫⽬目标对象成员，⽆无须转换。 
}

```

在Go中，切片的本质是一个结构体，包含一个指向底层数组的指针(prt)，长度（len），容量（cap）。所以，切片本身包含一个指针，将切片按值传递给函数，在函数内对其修改，影响将会传递到函数外。因为底层的数组被修改了。  
但当对切片进行`append()`操作，若是元素数量超过原有切片的容量，将会使得切片容量增大，这就是问题所在。扩容后的切片，本质上是产生一个新的底层数组。如果在函数内对切片添加元素导致扩容，会导致元素内的切片指向一个新的数组，但是函数外的切片仍然指向原来旧的数组，则将会导致影响无法传递到函数外。如果希望函数内对切片扩容作用于函数外，就需要以指针形式传递切片。

```go

// ************************* 数组指针 *********************


                     // 数组指针，是一个指针 ，*表示定义一个指针
var arrPtr *[4]int  // 创建一个指针 arrPtr，指向一个数组
var arr = [4]int{1,2,3,4}  // 创建一个数组并初始化
arrPtr = &arr              // 将数组 arr的地址赋值给arrPtr
                        //&t取struct t的指针地址，通过\*取指针变量的值

(*arrPtr)[0] // 通过指针访问数组

// ************************* 指针数组 *********************
var ptrArr [4]*int  
a, b, c, d := 1, 2, 3, 4

arr2 := [4]int{a, b, c, d}  // 拷贝四个变量的值为函数组元素
fmt.Println("数组 arr2 :", arr2)

ptrArr = [4]*int{&a, &b, &c, &d} // 存的都是内存地址
fmt.Println("指针数组 ptrArr :", ptrArr)



```



## 类型转换


```go
// ********************* 其他类型转字符串 *************************
// int转字符串
str := fmt.Sprintf("%d", numInt)
str := strconv.Itoa(numInt)

// []byte 转字符串
String s = new String(bytes)
s := string(num16[i])

// float 转字符串
s := fmt.Sprintf("%f", input)
s := strconv.FormatFloat(f, 'f', -1, 64)

// ********************* 字符串转其他类型 *************************
// 字符串转int
strInt, _ := strconv.Atoi(str)

// 字符串转字节切片[]byte
b := []byte(s)

```

## 流程控制

```go


// ************** 循环 *******************

for {

}


// ****************** switch ******************
switch key {
case "a", "b":
	fmt.Print(key+"ab")
case "c":
	fmt.Print(key+"c")
}

```

# 字符串 
```go

str = strings.TrimSpace(str) // 去除字符串首尾的空格，制表符，换行符等字符

words := strings.Fields(str) // 将字符串按空格分割成一个字符串切片

strLen := len(str) // 字符串长度

wordlen := len(words) // 单词数组长度

len(words[len(words)-1] // 最后一个单词的长度

inputStr = strings.ToLower(inputStr) // 统一为小写

for _, s := range inputStr { // 挨个读取字符串里每个字符
	if string(s) == inputS {
		count++ 
	}
}

sArr := strings.Split(s, ".") // 按. 分隔字符串为数组

str[i] //  字符串中第i个字符	
	
```


# 数组

```go

arr := make([]int, 0) // 创建数组

arr = append(arr, num)

```

# 哈希

应用：
* 去重：定义map
* 
# 排序

go sort 排序库函数

```go
ints := []int{1, 4,3, 2}
sort.Ints(ints) // 默认升序
sort.Sort(sort.Reverse(sort.IntSlice(ints))) // 降序排序

sort.Strings()
sort.Float64s()

sort.Slice()
sort.SearchInts()
sort.Search()
```

## 选择排序

在未排序的部分找到最小或最大的元素，将其放到已排序部分的末尾。
```go

for i := 0; i < len(arr); i++ {
	for j := i; j < len(arr); j++ {
		if arr[i] > arr[j] {
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
}

```


