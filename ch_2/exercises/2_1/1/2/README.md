# Setting Up PyTorch Lightning

***Step 2***

## Instructions

- Implement the `forward` method to flatten the input and pass it through the linear layer.

<details>
  
<summary><h2>Hint</h2></summary>
  
</details>

N/A

## Solution

[solution.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_2/exercises/2_1/1/2/solution.py)

## Sample Code

```python
import pytorch_lightning as pl
import torch.nn as nn
import torch
from torchvision.datasets import CIFAR10
from torchvision.transforms import ToTensor, Normalize, Compose
from torch.utils.data import DataLoader

class LitModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        # Define a linear layer
        self.layer = nn.Linear(32 * 32 * 3, 10)

    def forward(self, x):
        # Flatten the input tensor and pass through the linear layer
        return self.layer(x.view(x.size(0), -1))

transform = Compose([ToTensor(), Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
train_loader = DataLoader(CIFAR10('data', train=True, download=True, transform=transform), batch_size=32, shuffle=True)
```

## Submission Correctness Tests (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_2/exercises/2_1/1/2/sct.py)
