import torch
import torch.nn as nn
class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.conv1 = nn.Conv2d(1,10,10)
        self.pool = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(10,20,10)
        self.fc1 = nn.Linear(10*5*5,200)
        self.fc2 = nn.Linear(200,100)
        self.fc3 = nn.Linear(100,10)
    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1,20*5*5)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
model = LeNet()