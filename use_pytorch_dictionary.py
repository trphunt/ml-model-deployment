# -*- coding: utf-8 -*-
"""use_pytorch_dictionary.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1an9E72n2kIQeSw9GvaqTrEtQdLUez-Tx
"""

!ls

!wget https://github.com/trphunt/ml-model-deployment/raw/main/customer_buy_state_dict_v1.zip

!ls

!unzip customer_buy_state_dict_v1.zip

!ls

!wget https://github.com/trphunt/ml-model-deployment/raw/main/sc.pickle

import pickle

local_scaler = pickle.load(open('sc.pickle', 'rb'))

import torch
import torch.nn as nn
from torch.nn import functional as F

input_size=2
output_size=2
hidden_size=10

class Net(nn.Module):
  def __init__(self):
    super(Net, self).__init__()
    self.fc1 = torch.nn.Linear(input_size, hidden_size)
    self.fc2 = torch.nn.Linear(hidden_size, hidden_size)
    self.fc3 = torch.nn.Linear(hidden_size, output_size)

  def forward(self, X):
    X = torch.relu((self.fc1(X)))
    X = torch.relu((self.fc2(X)))
    X = self.fc3(X)

    return F.log_softmax(X,dim=1)

new_predictor2 = Net()

new_predictor2.load_state_dict(torch.load('customer_buy_state_dict'))

import numpy as np

y_cust_42_50000 = new_predictor2(torch.from_numpy(local_scaler.transform(np.array([[40,20000]]))).float())
y_cust_42_50000

