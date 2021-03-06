# 最大边界间隔超平面

在Perceptron中，针对如下图所示线性可分的训练数据，有可能会得到左/中/右这样的三条分隔线，而且Perceptron无法确定这三条线哪一条更好。凭直觉而言，最右边是最好的，因为其对噪声的容忍度最高。从点的角度来看，测试模型的时候由于测量误差或者收集的条件不同，即便应该与训练数据一模一样的数据在收集时也可能出现误差，图中圆形区域为噪声，区域越大表示能够容忍的噪声越大；另一方面，从线的角度来看，超平面分别向正负样本方向扩展到最近的正负样本得到的间隔，代表了超平面的鲁棒性，最右边的线得到的间隔也最大。

![](../assets/图39.png)
![](../assets/图40.png)
![](../assets/图41.png)

图 都线性可分,那么哪条直线是最好的？