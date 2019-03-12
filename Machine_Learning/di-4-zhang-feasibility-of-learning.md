

本讲主要来探讨一下Learning到底是不是可行的。通过上一节知道我们主要focused on使用a batch of supervised数据，数据都是concrete feature，来做二元分类以及回归分析。但是即使是在这样核心的条件下，有可能Learning也是做不到的。如果做不到，那么我们能否再加入一些假设或者用些什么方法让它大部分的时候是做得到的。

Lecture 4 : Feasibility of Learning

> learning is impossible?
learning is PAC-possible if enough statistical data and finite |H|

- Learning is impossible?

    absulutely no free lunch outside D
- Probability to the Rescue

    probably approximately correct outside D
- Connection to Learning

    verification possible if Ein(h) small for fixed h
- Connection to Real Learning

    learning possible if |H| finite and Ein(g) small