（1）定义

位图[数据结构](http://lib.csdn.net/base/datastructure)，就是用一块内存区域的每个比特表示一个对象的数据结构，叫做 bitmap 或者 bitplane。

优点是速度快，内存空间占用小，能表示大范围的数据。

《Programming Pearls》里面举了一个例子，假设要对0到一千万范围内的、没有重复元素的正整数排序，

则利用位图数据结构很合适。

Abitsetstores bits \(elements with only two possible values: 0 or 1,`true`or`false`, ...\).

The class emulates an array of`bool`elements, but optimized for space allocation: generally, each element occupies only one bit \(which, on most systems, is eight times less than the smallest elemental type:`char`\).

Each bit position can be accessed individually: for example, for a given bitset named`foo`, the expression`foo[3]`accesses its fourth bit, just like a regular array accesses its elements. But because no elemental type is a single bit in most C++ environments, the individual elements are accessed as special references type \([http://www.cplusplus.com/reference/bitset/bitset/\](http://www.cplusplus.com/reference/bitset/bitset/\)\)

（2）适用范围

位图数据结构在排序算法中的特殊应用是利用排序问题中不常见的三个属性：

第一：输入数据限制在相对较小的范围内 （这也是编写软件时最多的设计方法）；

第二：数据没有重复；

第三：对于每条记录而言，除了单一数据外（此题为单一的整数），没有任何其他关联数据。

从而达到写算法时能根据实际问题实现最有效的时间─空间折中与双赢。

\(3\)位图数据结构的实现

（a）比特的编号机制

下面过一个示例来帮助大家理解比特的编号方法，在这里，从低字节的高位比特位开始，第一个bit为0，最后一个bit为 n-1（大端模式）

例如：现有数组为int a\[3\]表示一块内存区域，共3*4=12个字节，共12*8=96个比特，因此a\[0\]对应的bit位0-31，a\[1\]对应32-63，a\[2\]对应64-95。a[0]的高比特（从左边数，第1个字节，第1个比特）为第0个比特。
因此，上述程序与机器是大端还是小端模式无关。

从低字节的低位比特位开始，第一个bit为0，最后一个bit为 n-1（大端模式）

    #include<iostream>
    using namespace std;  
    int main(int argc,char *argv)  
    {  
        int a[3];  
        for(int i=0;i=3;i++)  
        {  
            a[i]=1;  
        }  
        for(int i=0;i<3;i++)  
        {  
            a[i]=a[i]<<5;  //左移5位
            cout<<a[i]<<endl;  
        }  
        return 0;  
    }  

输出结果如下图所示

![](http://img.blog.csdn.net/20170611132807503?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzM1OTI1ODM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

**由此可知原来数据存放如下    
**

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |


经过经过位运算后，也即左移5位后为，即对应的数为32

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |


\(b\)位图实现

要使用位图数据结构，就必须熟悉位操作。

以下是已经写好的操作位图数据结构的实用函数

	#define BITS_PER_BYTE 8
	#define BITS_PER_INT (BITS_PER_BYTE * 4)
	// set the bit of the int specified by index to 1.
	// the index is zero-based, counting from the left(the higher end)
	inline void pearl_int_set(int* data, int index)
	{
		int mask = 1 << (BITS_PER_INT - 1 - index);
		*data |= mask;
	}
	
	// test whether a bit of the int specified by index is 1.
	// the index is zero-based, counting from the left(the higher end)
	inline int pearl_int_test(int* data, int index)
	{
		int mask = 1 << (BITS_PER_INT - 1 - index);
		return (*data) & mask;
	}
	
	// set a bit of the int specified by bit_index to 0.
	// the index is zero-based, counting from the left(the higher end)
	inline void pearl_int_clear(int *data, int bit_index)
	{
		int mask = ~(1 << (BITS_PER_INT - 1 - bit_index));
		*data &= mask;
	}
	
	// get the right(lower) part of the int.
	inline int pearl_int_right(int *data, int count)
	{
		int mask = 1;
		while(count > 0) {
			mask = mask << 1 + 1;
		}
		return *data & mask;	
	}
	
	// get the left(upper) part of the int value
	inline int pearl_int_left(int *data, int count)
	{
		int mask = 1;
		count = BITS_PER_BYTE - count;
		while (count > 0) {
			mask = mask << 1 + 1;
		}
	
		mask = ~mask;
		return *data & mask;
	}
	
	// set a bit of the speicified memory area to 1.
	// @warning this function does NOT perform error checking.
	inline void pearl_set(int *bitplane, int index)
	{
		int offset = index / BITS_PER_INT;
		int pos = index - offset * BITS_PER_INT;
	
		pearl_int_set(bitplane + offset, pos);
	}
	
	// set a bit of the specified memory area to 0.
	// @warning this function does NOT perform error checking.
	inline void pearl_clear(int *bitplane, int index)
	{
		int offset = index / BITS_PER_INT;
		int pos = index - offset * BITS_PER_INT;
	
		pearl_int_clear(bitplane + offset, pos);
	}
	
	// test if a bit of the specified memory area is 1.
	// @warning this function does NOT perform error checking.
	inline int pearl_test(int *bitplane, int index)
	{
		int offset = index / BITS_PER_INT;
		int pos = index - offset * BITS_PER_INT;
	
		return pearl_int_test(bitplane + offset, pos);
	}

用法举例：
	
	int main(int argc, char* argv[]) {
	    int* bitplane = (int*)malloc(sizeof(int)*SIZE);
	    pearl_set(bitplane, n); // 0 <= n <= SIZE * 4 * 8 - 1
	    if ( pearl_test(bitplane, n) ) {
	        printf("bit(%d) is set\n", n);
	    }
	    pearl_clear(bitplane, n);
	    if ( pearl_test(bitplane, n) ) {
	        printf("bit(%d) is cleared\n", n);
	    }
	    return 0;
	}