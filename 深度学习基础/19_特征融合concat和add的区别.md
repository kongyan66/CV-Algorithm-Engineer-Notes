## 问题

在网络模型当中，经常要进行不同通道特征图的信息融合相加操作，以整合不同通道的信息，在具体实现方面特征的融合方式一共有两种，一种是 ResNet 和 FPN 等当中采用的 element-wise add ，另一种是 DenseNet 等中采用的 concat 。他们之间有什么区别呢？

## add

举个例子：

```python
a = [[1,2], [3, 4]]
b =  [[11,12], [13, 14]]
c = add(a, b)  # c = [[12,14], [16, 18]]  这里add表示add层操作，把输出结果值相加了
```

从中可以很容易地看出，add 方式有以下特点：

1. 做的是对应通道对应位置的值的相加，**通道数不变**
2. 描述图像的特征个数不变，但是每个特征下的信息却增加了。

## concat

也举个例子

```python
a = [[1,2], [3, 4]]
b =  [[11,12], [13, 14]]
c = concat(a, b)  # c = [[1,2], [3, 4], [11,12], [13, 14]]  这里concat表示concat层操作，把输出结果级联，增加了维度
```

从中可以很容易地看出，concat 方式有以下特点：

1. 做的是**通道的合并**，通道数变多了
2. 描述图像的特征个数变多，但是每个特征下的信息却不变。

## 多一点理解

DenseNet和Inception中更多采用的是concatenate操作，而ResNet更多采用的add操作，Resnet是做值的叠加，通道数是不变的，DenseNet是做通道的合并。你可以这么理解，add是描述图像的特征下的信息量增多了，但是描述图像的维度本身并没有增加，只是每一维下的信息量在增加，这显然是对最终的图像的分类是有益的。而concatenate是通道数的合并，也就是说描述图像本身的特征增加了，而每一特征下的信息是没有增加。

>add相当于加了一种prior，当两路输入可以具有“对应通道的特征图语义类似”的性质的时候，可以用add来替代concat，这样更节省参数和计算量（concat是add的2倍）

## 参考资料

[理解concat和add的不同作用](https://blog.csdn.net/qq_32256033/article/details/89516738)

[卷积神经网络中的add和concatnate区别](https://blog.csdn.net/weixin_39610043/article/details/87103358)

[ShuffleNet中add层和concatenate层的区别](https://www.i4k.xyz/article/qq_26369907/89351328)

