import torch
import torch.nn as nn
import torch.optim as optim
from tochvision import datasets, transforms

class SimpleNN(nn.Module):
  def __init__(self):
    super(SimpleNN, self).__init__()
    self.fc = nn.Linear(784, 10)

  def forward(self, x):
    x = x.view(-1, 784)
    return self.fc(x)

model = SimpleNN()

# Step 1: Evaluate the trained model on the test dataset
transform = _____
test_dataset = datasets.MNIST('.', train=False, transform=transform)
test_loader = torch.utils.data.DataLoader(test_dataset, ____, ____)

model.eval()
correct = ____
total = ____
with torch.no_grad():
  for data, target in test_loader:
    output = model(data)
    _, predicted = torch.max(output.data, 1)
    total += ____
    correct += ____

print(f'Test Accuracy: {100 * correct / total}%')

# Step 2: Save the trained model to a file
torch.save(____)
print('Model saved to model.pth')

# Step 3: Load the saved model from the file
loaded_model = SimpleNN()
loaded_model.load_state_dict(____)
loaded_model.eval()
print('Model loaded from model.pth')

# Step 4: Perform inference using the loaded model on a sample input
sample input = torch.randn(1, 1, 28, 28)
output = ____
print(f'Inference output: {output}')
