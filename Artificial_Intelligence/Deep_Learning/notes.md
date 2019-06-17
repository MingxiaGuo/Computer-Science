
哺乳动物视觉处理机理：
图像分割
基于特征的目标识别 SIFT特征
1998
2012年ImageNet大赛 AlexNet 卷积神经网络胜出

googleNet vgg
msra
# What is Deep Learning?
# What are are neural networks and how they work?

Deep learning is about neural networks.
The structure of a neural network is like any other kind of network;there is an interconnected web of nodes, which are called neurons,and the edges that join them together.
A neural network's main function is to receive a set of inputs,perform progressively complex calculations,
and then use the output to solve a problem.
Neural networks are used for lots of different applications, but in this series we will focus on classification.

If you wanna learn about neural nets in a bit more detail, including the math,
my two favourite resources are Michael Nielsen's book, and Andrew Ng's class.



Classification is the process of categorizing a group of objects, while only using some basic data features that describe them.
There are lots of classifiers available today - like Logistic Regression, Support Vector Machines, Naive Bayes, and of course, neural networks.
The firing of a classifier, or activation as its commonly called, produces a score.
For example, say you needed to predict if a patient is sick or healthy, and all you have are their height, weight, and body temperature. The classifier would receive this data about the patient, process it, and fire out a confidence score. A high score would mean a high confidence that the patient is sick, and a low score would suggest that they are healthy.
Neural nets are used for classification tasks where an object can fall
into one of at least two different categories.
Unlike other networks like a social network,
a neural network is highly structured and comes in layers.
The first layer is the input layer,
the final layer is the output layer,
and all layers in between are referred to as hidden layers.
A neural net can be viewed as the result of spinning classifiers together in a layered web.
This is because each node in the hidden and output layers has its own classifier.
Take that node for example -
it gets its inputs from the input layer, and activates.
Its score is then passed on as input to the next hidden layer for further activation.
So,
let’s see how this plays out end to end across the entire network.
A set of inputs is passed to the first hidden layer,
the activations from that layer are passed to the next layer and so on,
until you reach the output layer,
where the results of the classification are determined by the scores at each node.
This happens for each set of inputs.
Here's another one...
like so.
This series of events starting from the input where each activation is sent to the next layer,
and then the next, all the way to the output,
is known as forward propagation, or forward prop.
Forward prop is a neural net's way of classifying a set of inputs.
Have you wanted to learn more about neural nets?
Please comment and let me know your thoughts?
The first neural nets were born out of the need to address the inaccuracy of an early classifier, the perceptron.
It was shown that by using a layered web of perceptrons,
the accuracy of predictions could be improved.
As a result, this new breed of neural nets was called a Multi-Layer Perceptron or MLP.
Since then, the nodes inside neural nets have replaced perceptrons with more powerful classifiers,
but the name MLP has stuck.
Here's forward prop again.
Each node has the same classifier, and none of them fire randomly;
if you repeat an input, you get the same output.
So if every node in the hidden layer received the same input,
why didn’t they all fire out the same value?
The reason is that each set of inputs is modified by unique weights and biases.
For example, for that node,
the first input is modified by a weight of 10,
the second by 5, the third by 6 and then a bias of 9 is added on top.
Each edge has a unique weight, and each node has a unique bias.
This means that the combination used for each activation is also unique,
which explains why the nodes fire differently.
You may have guessed that the prediction accuracy of a neural net depends on its weights and biases.
We want that accuracy to be high,
meaning we want the neural net to predict a value that is as close to the actual output as possible,
every single time.
The process of improving a neural net’s accuracy is called training,
just like with other machine learning methods.
Here's that forward prop again -
to train the net, the output from forward prop is compared to the output that is known to be correct,
and the cost is the difference of the two.
The point of training is to make that cost as small as possible, across millions of training examples.
To do this, the net tweaks the weights and biases step by step
until the prediction closely matches the correct output.
Once trained well, a neural net has the potential to make accurate predictions each time.
This is a neural net in a nutshell.
At this point you might be wondering;
why create and train a web of classifiers for a task like classification,
when an individual classifier can do the job quite well?
The answer involves the problem of pattern complexity, which we will see in the next video.

# What are are convolutional neural networks?

# Why is deep learning so powerful and what can it be used for?
Be part of a rapidly growing field in data science; there's no better time than now to get started with neural networks.

gradient and vanishing gradient a

Deep Belief Nets
Convolutional Nets
Backpropagation
non-linearity
Image recognition

Big deep learning researchers
* Andrew Ng
* Geoff Hinton
* Yann LeCUn
* Yoshua Bengio
* Andrej Karpathy


# 应用：
* 计算机视觉：
    * 图像分类
    * 计算机视觉的历史
* 自然语言处理
* 语音识别