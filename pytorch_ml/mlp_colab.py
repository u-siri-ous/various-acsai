import torch
from torch import nn
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

# print(torch.cuda.is_available()) # cannot use GPU acceleration, daje

# create a tensor from a list
data = [
    [1,2],
    [3,4]
]

pyt_data = torch.tensor(data) #or
#pyt_data = torch.from_numpy(data)

# import train and testing data
training_data = datasets.FashionMNIST(root='data', train=True, download=True, transform=ToTensor()) 
test_data = datasets.FashionMNIST(root='data', train=False, download=True, transform=ToTensor()) 

# labels of the dataset (also found online)
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
}

""" # visualize the model
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols*rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)   # filling cells of the matrix
    plt.title(labels_map[label])    # putting its label as title
    plt.axis('off')
    plt.imshow(img.squeeze(), cmap='gray')      # squeeze() deletes cardinality 1 dimensions 

plt.show()
 """

# create the model / neural network
device = ('cuda' if torch.cuda.is_available() else 'cpu')

# create a model class, which inherits from nn
class OurMLP(nn.Module):
    def __init__(self):
        super().__init__()
        # method 1 - using Sequential
        self.mlp = nn.Sequential(
            nn.Linear(28*28, 50),  # input layer, we can specify input and output size
            nn.Sigmoid(),          # we can specify different activation function in between different hidden layers
            nn.Linear(50, 50),     # pay attention, as output of previous hidden layers should match the input of the next one
            nn.Sigmoid(),
            nn.Linear(50, 10)      # the last output should match the number of classes of the model
        )
        self.flatten = nn.Flatten()     # convert to single array data
    # specify how data passes through model, and how data are connected from input to output
    def forward(self, x):
        x = self.flatten(x)           # flatten the tensor
        logits = self.mlp(x)          # pass the tensor through the neural network
        return logits

# model initialization
model = OurMLP().to(device)   # instance the model and move it to the device

""" # maronn - ci proviamo
X = torch.rand(1,28,28)     # creating a single 28x28 grayscale image
predictions = model(X)
probability = nn.Softmax(dim=1)(predictions)    # normalize to 0-1 probability
y = probability.argmax(1)       # take most likely label

print(f'predicted class: {y}') """

####### train the model yayyyyyy #######

# define hyperparameters (the model cannot learn them) - the holy three - play with these
epochs = 6                                             # how many times should our model analyze the dataset
batch_size = 64                                        # number of samples that we get from the dataset each time (lower if crash)
learning_rate = 0.0001                                 # amount of change allowed on weights in backpropagation (changeable in various epochs in certain techniques)

# we have to define the training loop (automatically done in sklearn)
# we aim for variability in each epoch, so choosing to increment epochs vs batch_size depends on the dataset

# define the loss function - computes the differences between our prediction and the correct labels and is used to update weights on backpropagation
loss_fn = nn.CrossEntropyLoss()     # uses negative log likelihood

# define the optimizer - the mathematical approach used to compute the gradient
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)   # stochastic gradient descent, model.parameters() are the weights

# train the model....? define the training loop
def train_loop(dataloader, model, loss_fn, optimizer):    #get samples from dataset, model, loss fn, optimizer
    # get batch from dataset (X=data, y=label)
    for batch, (X,y), in enumerate(dataloader):
        # move data on GPU (tensor device inconsistency)
        X_gpu = X.to(device)
        size = len(dataloader)      # sample in datasets
        # compute prediction and loss
        pred = model(X_gpu)
        y_tensor = torch.tensor([y])       # AS LIST SENNO SCOPPIA
        y_tensor_gpu = y_tensor.to(device)
        loss = loss_fn(pred, y_tensor_gpu)     # difference between true and predicted

        # backward pass (backpropagation)
        loss.backward()             # backpropagate error
        optimizer.step()            # compute derivation
        optimizer.zero_grad()       # clean gradient

        # print loss during training (verbose)
        if batch % 500 == 0:        # every 500 iterations
            loss, current = loss.item(), (batch+1)*len(X)       # loss number
            print(f'loss: {loss} [{current}/{size}]')

# daje forte co sto training
for t in range(epochs):
    print(f'epoch: {t}')
    train_loop(training_data, model, loss_fn, optimizer)

print('daje lupetti')