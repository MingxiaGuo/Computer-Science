PLA什么时候会停下来？  
    PLA找到一条线使所有点都没有犯错误。

对于训练数据D，对于标记为叉叉的点与标记为圈圈的点如果存在一条直线将其分开，则认为D是线性可分的，如下图左。否则为线性不可分，如下图右两种情况。

![](/assets/图22.jpg)

在线性可分的前提下，PLA算法仅需要有限次的试错更新即可找到合适的超平面。

Linear Separability\(线性可分\) :存在一条线，使对D的分类完全正确，称D是线性可分的。

如果D是线性可分的&lt;=&gt;存在完全的$$W_f$$，使$$y_n=sign(W_f^T*X_n)$$

### 证明线性可分集D调用PLA后最后会停下来

1. 假设$$W_f$$ 即为完美的，使$$y_n = sign(W_f^T*X_n)$$ ：有 $$y_{n(t)}W_f^TX_{n(t)} ≥ min(y_{n(t)}W_f^TX_n)>0$$
2. $$W_t$$ 更新，当找到错误点，有$$sign(W_tX_{n(t)}) ≠ y_{n(t)}$$   &lt;=&gt;     $$y_{n(t)}W_t^TX_{n(t)} ≤0$$
3. 遇到错误点更新：$$W_{t+1} = W_t+y_{n(t)}X_{n(t)}$$  
   1. ![](/assets/图22.PNG)

   $$W_f^T$$与$$W_t$$的乘积越来越大，表示$$W_f^T$$与$$W_t$$越来越靠近，但是也有可能是因为$$W_t$$的长度在增大。  
   1. ![](/assets/图23.PNG)  
   2. ![](/assets/图24.PNG)

   正规化的两个向量相乘最多是1

总结

as long as linear separable and correct by mistake

* inner product of $$W_f$$ and $$W_t$$ grows fast; length of $$W_t$$ grows slowly

* PLA 'lines' are more and more aligned with $$W_f$$  =&gt;  halts

![](/assets/图25.PNG)

