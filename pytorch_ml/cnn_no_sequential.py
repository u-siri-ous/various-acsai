from typing import Any
import torch
import torchmetrics
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

training_data = datasets.FashionMNIST(root='data', train=True, download=True, transform=ToTensor()) 
test_data = datasets.FashionMNIST(root='data', train=False, download=True, transform=ToTensor()) 

device = ('cuda' if torch.cuda.is_available() else 'cpu')

class OurCNN(nn.Module):
    def __init__(self):
        # store everything we're gonna use
        super().__init__()

        self.input_layer = nn.Conv2d(1, 5, kernel_size=3)
        self.relu = nn.ReLU()
        self.conv1 = nn.Conv2d(5, 10, kernel_size=3) 
        self.max_pool = nn.MaxPool2d(kernel_size=2)
        self.input_linear = nn.Linear(12*12*10, 10)   
        self.output_linear = nn.Linear(10, 10)

    # create the same model as cnn.py without using Sequential()
    def forward(self, x):
        x = self.input_layer(x)
        x = self.relu(x)
        x = self.conv1(x)
        x = self.relu(x)
        x = self.max_pool(x)

        x = torch.flatten(x, 1)     

        x = self.input_linear(x)
        x = self.relu(x)
        x = self.output_linear(x)
        return x
    
model = OurCNN().to(device)

epochs = 3                                             # how many times should our model analyze the dataset
batch_size = 64                                        # number of samples that we get from the dataset each time (lower if crash)
learning_rate = 0.001                                  # amount of change allowed on weights in backpropagation (changeable in various epochs in certain techniques)

# create the dataloader
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)


# define the loss function - computes the differences between our prediction and the correct labels and is used to update weights on backpropagation
loss_fn = nn.CrossEntropyLoss()     # uses negative log likelihood

# define the optimizer - the mathematical approach used to compute the gradient
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)   # stochastic gradient descent, model.parameters() are the weights

# create accuracy metric
metric = torchmetrics.Accuracy(task='multiclass', num_classes=10)   # multiclassification for 10 classes

# train the model....? define the training loop
def train_loop(dataloader, model, loss_fn, optimizer):    #get samples from dataset, model, loss fn, optimizer
    # get batch from dataset (X=data, y=label)
    for batch, (X,y), in enumerate(dataloader):
        # compute prediction and loss
        pred = model(X)
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