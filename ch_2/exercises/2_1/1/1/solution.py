import pytorch_lightning as pl
import torch.nn as nn
import torch

class LitModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        # Define a linear layer
        self.layer = nn.Linear(32 * 32 * 3, 10)
