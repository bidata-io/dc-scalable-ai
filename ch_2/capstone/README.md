# Chapter 2 Capstone Exercise

## Context

In this capstone exercise, you will apply the concepts learned throughout Chapter 2 to build, train, and manage a Convolutional Neural Network (CNN) using PyTorch Lightning. This exercise will test your ability to structure a model, integrate advanced layers, and leverage PyTorch Lightning’s training and experiment management capabilities.

## Instructions
- Define a `LightningModule` for a CNN that includes convolutional layers, activation functions, and fully connected layers.
- Implement the training step within your `LightningModule`.
- Use `pytorch_lightning.Trainer` to train your model on a sample dataset.
- Integrate logging and checkpointing features to manage your experiment.

<details>

<summary><h2>Hint</h2></summary>

- Focus on correctly configuring the convolutional layers, fully connected layers, and using appropriate hyperparameters in the `Trainer` for training the model.

</details>

## Pre-Exercise Code

```python
import pytorch_lightning as pl
import torch
from torch import nn
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import CIFAR10
from torchvision import transforms

# Define the CNN LightningModule
class CNNModel(pl.LightningModule):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3)
        self.fc1 = nn.Linear(32 * 6 * 6, 128)
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = nn.ReLU()(self.conv1(x))
        x = nn.MaxPool2d(2)(x)
        x = nn.ReLU()(self.conv2(x))
        x = nn.MaxPool2d(2)(x)
        x = torch.flatten(x, 1)
        x = nn.ReLU()(self.fc1(x))
        x = self.fc2(x)
        return x
    
    def training_step(self, batch, batch_idx):
        # Complete the training step
        data, target = batch
        output = self(data)
        loss = nn.CrossEntropyLoss()(output, target)
        return loss
    
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.001)
```

## Solution

[solution.py](https://github.com/bidata-io/dc-scalable-ai/main/ch_2/capstone/1/solution.py)

## Sample Code
```python
# Initialize DataLoader
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_data = CIFAR10(root='data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_data, batch_size=____, shuffle=True)

# Initialize the model and trainer
model = CNNModel()
trainer = pl.Trainer(max_epochs=____, logger=____, checkpoint_callback=____)

# Train the model
trainer.fit(model, train_loader)
```

## Submission Correctness Tests (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/main/ch_2/capstone/1/sct.py)
