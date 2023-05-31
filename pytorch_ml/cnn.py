from typing import Any
import torch
import torchmetrics
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

# FCN - fully convolutional network 
# lacks the multilayer perceptron layer, used for segmentation tasks 
# classification is made pixelwise by using 1x1 convolutions 

# import train and testing data
training_data = datasets.FashionMNIST(root='data', train=True, download=True, transform=ToTensor()) 
test_data = datasets.FashionMNIST(root='data', train=False, download=True, transform=ToTensor()) 

""" # labels of the dataset (also found online)
labels_map = {
    0: 'tshirt',
    1: 'trousers',
    2: 'pullover',
    3: 'dress',
    4: 'coat',
    5: 'sandal',
    6: 'shirt',
    7: 'sneaker',
    8: 'bag',
    9: 'ankle boot'
} """

# create the model / neural network
device = ('cuda' if torch.cuda.is_available() else 'cpu')

# define our CNN
# the number of channels is important

# shape of tensor: (batch, channels, width, height)
class OurCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.cnn = nn.Sequential(
            # convolutional layer
            nn.Conv2d(1, 5, kernel_size=3),  # input channels == number of channels of input image, we do not care about the size of the image
            # (64, 1, 28, 28)
            nn.ReLU(),
            nn.Conv2d(5, 10, kernel_size=3), # MLP technique: input == output
            # (64, 5, 26, 26)
            # w = h = 26 because if we do not use padding and stride, output for each dimension is dimension - kernel_size + 1
            nn.ReLU(),
            # adding pooling to redure dimensionality, from 24*24*10 to 12*12*10
            nn.MaxPool2d(kernel_size=2)
        )
        self.mlp = nn.Sequential(
            # multilayer perceptron layer for classification
            # nn.Flatten(),    # can be done here on in forward(self, x)
            nn.Linear(12*12*10, 10),   # used torch.size (x.shape) to get correct value after flatten in forward
            nn.ReLU(),
            nn.Linear(10, 10)
        )

    def forward(self, x):
        x = self.cnn(x)
        # x.shape
        x = torch.flatten(x, 1)     # with dimension 1 (array)
        # x.shape
        x = self.mlp(x)
        return x
    
model = OurCNN().to(device)

# define hyperparameters (the model cannot learn them) - the holy three - play with these
epochs = 3                                             # how many times should our model analyze the dataset
batch_size = 64                                        # number of samples that we get from the dataset each time (lower if crash)
learning_rate = 0.001                                  # amount of change allowed on weights in backpropagation (changeable in various epochs in certain techniques)

# create the dataloader
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

# we have to define the training loop (automatically done in sklearn)
# we aim for variability in each epoch, so choosing to increment epochs vs batch_size depends on the dataset

# define the loss function - computes the differences between our prediction and the correct labels and is used to update weights on backpropagation
loss_fn = nn.CrossEntropyLoss()     # uses negative log likelihood

# define the optimizer - the mathematical approach used to compute the gradient
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)   # stochastic gradient descent, model.parameters() are the weights
# adamw is faster and better than sgd, play with hyperparameters as well

# create accuracy metric
metric = torchmetrics.Accuracy(task='multiclass', num_classes=10)   # multiclassification for 10 classes

# train the model....? define the training loop
def train_loop(dataloader, model, loss_fn, optimizer):    #get samples from dataset, model, loss fn, optimizer
    # get batch from dataset (X=data, y=label)
    for batch, (X,y), in enumerate(dataloader):
        # size = len(dataloader)      # sample in datasets, not needed with metric

        # compute prediction and loss
        pred = model(X)
        #y_tensor = torch.tensor([y])       # AS LIST SENNO SCOPPIA
        loss = loss_fn(pred, y)     # difference between true and predicted (tensors)

        # backward pass (backpropagation)
        loss.backward()             # backpropagate error
        optimizer.step()            # compute derivation
        optimizer.zero_grad()       # clean gradient

        # print loss during training (verbose)
        if batch % 100 == 0:        # every 100 iterations
            acc = metric(pred, y)
            print(f'current batch accuracy: {acc}')
            
    # final training accuracy
    acc = metric.compute()
    print(f'epoch accuracy: {acc}')
    metric.reset()  # for next epoch

# test the model
def test_loop(dataloader, model, loss_fn):      # no optimizer cuz we don't need gradient to compute weights
    # disable weight update - assuming optimal weights for testing (freezing)
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            #y_tensor = torch.tensor([y])
            test_loss += loss_fn(pred, y).item()    # compute loss and add it to total loss
            correct += (pred.argmax(1)).type(torch.float).sum().item()  # get all maximum values for the whole batch, then sum them and get the number
            
            # print accuracy and avg. loss, as we have accuracy only for the current batch
            acc = metric(pred, y)
            print(f'current batch accuracy: {acc}')

    # final training accuracy
    acc = metric.compute()
    print(f'epoch accuracy: {acc}')
    metric.reset()  # for next epoch

# daje forte co sto training e sto testing
for t in range(epochs):
    print(f'epoch: {t}')
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)

print('daje lupetti')