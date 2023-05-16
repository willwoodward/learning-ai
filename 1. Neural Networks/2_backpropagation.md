# Backpropagation

### What is Backpropagation?
This is the process that is used to 'train' a neural network. It does this by first running a *cost* function to calculate the error of the outputs, then adjusts the weights through the backpropagation process.

It might be helpful to think of the parameters in a simple neural network first. Lets consider a network with 1 input neuron, 2 hidden neurons and 1 output neuron. The cost $C_0$ is calculated by $(y-a_{(L)})^2$, where $y$ is the desired output and $a_{(L)}$ is the output neuron. This calculates the error, and our goal is to reduce the cost as much as possible.

To reduce the cost as much as possible, we want to find the direction of steepest descent: 
$$-\nabla C = -\begin{pmatrix}\frac{\partial C}{\partial w_0} \\\frac{\partial C}{\partial b_0} \\...\\\frac{\partial C}{\partial w_n} \\\frac{\partial C}{\partial b_n} \end{pmatrix}$$