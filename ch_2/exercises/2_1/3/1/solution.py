def configure_optimizers(self):
  return torch.optim.Adam(self.parameters(), lr=1e-3)
