# RNN - recurrent neural network
# rnns do not work well with long sequences because of recursivity

# vanishing gradient problem

# exploding gradient problem 

# LSTM - Long-Short Term Memory
# ability to learn from temporal data
# use this or GRU - Gated Recurrent Unit to work with text

# inside a single lstm node there are three smaller nodes:
# input gate
# forget gate
# output gate

import torch
from torch import nn

'''
input formatting for lstm:

input, h_0, c_0 

input = data
h_0 = initial hidden state of elements in input data
c_0 = initial cell state(s)

#########

input = (L, N, H_in)
L = len(sequence)
N = batch size
H_in = size of input data

h_0 = (D, N, H_out)
D = shape, number of directions (as we can have cycles in lstm
                                ; if set to 1, it works like a normal nn)
N = optional, as before
H_out = features we want as output
                                
c_0 = (D, N, num_cells)
D = same as before
N = optional, as before
num_cells = number of wanted cells (usually equal to H_out)
'''

# create a single lstm node
lstm_node = nn.LSTM(10, 20, 1)       
# LSTM(input size, outputs, number of lstm cells that we wanna start together)

# create the input
input_data = torch.randn(5, 3, 10)
h_0 = torch.randn(1, 3, 20)
c_0 = torch.randn(1, 3, 20)

output, (h_n, c_n) = lstm_node(input_data, (h_0, c_0))

print(output.shape)

# to train it, it works the same as before
