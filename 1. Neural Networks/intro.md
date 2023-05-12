# Neural Networks
This is an introductory guide on neural networks from my current understanding. A lot of this will be based on 3Blue1Brown's series on deep learning, I'd highly recommend that!

### What are Neural Networks?
They are basically a set of activation neurons (nodes) that carry a particular value, typically between 0 and 1. There are then a couple of layers of neurons, followed by a layer of output neurons.

Each layer is calculated by the sum of the activation neurons and their associated weights to that neuron:
$$b_i = a_1w_{i1} + a_2w_{i2} + ... + a_nw_{in} = \Sum_{k=1}^{n}a_kw_{ik} = \textbf{a} \cdot \textbf{w}_i$$