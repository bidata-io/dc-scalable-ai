def training_step(self, batch, batch_idx):
  x, y = batch
  y_hat = self(x)
