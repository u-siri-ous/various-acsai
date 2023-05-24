## Convolutional Neural Networks (CNN)

With MLP we lose spatial indormation, together with the increeasing size of input layer, it makes MLP not suitable for images

We use Convolutional Neural Networks (CNN)!!!

They are Deep Neural Networks that use Convolutions instead of layers:
- Given an input image we apply convolution to each layer
- We use Pooling for dimensionality reduction

[add image]()

At the end of the convolutional layer to extract features, there is a fully connected NN (aka a MLP) to perform **classification**, as convolutions alone do not allow classification

### Types of layers

* Convolutional layer
    * Number of convolutions is specified and arbitrary
    * The image gets transformed into a **feature map** after processing in this layer &rarr; it's not a "proper" image anymore
* Pooling layer
    * Provides spatial invariance and dimensionality reduction through max and/or average pooling
    [add image]()
* Fully connected layer
    * A neural network in which only the pooled image is flattened and passed through it

We will train the kernels of the convolution and the weights of the neural network

### Types of operations

* Convolutions
* Stride
    * For both convolutional and pooling operations, S denotes the number of pixels
* Padding