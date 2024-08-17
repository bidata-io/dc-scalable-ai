def forward(self, x):
  # Flatten the input tensor and pass through the linear layer
  return self.layer(x.view(x.size(0), -1))
