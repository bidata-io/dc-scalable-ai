import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

def test_step_1_evaluate_model(model, test_loader):
    try:
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for data, target in test_loader:
                output = model(data)
                _, predicted = torch.max(output.data, 1)
                total += target.size(0)
                correct += (predicted == target).sum().item()
        accuracy = 100 * correct / total
        print(f'Step 1: Test Accuracy: {accuracy}%')
    except Exception as e:
        print(f'Step 1: error in model evaluation: {e}')

def test_step_2_save_model(model, file_path='model.pth'):
    try:
        torch.save(model.state_dict(), file_path)
        print('Step 2: Model saved successfully to model.pth')

    except Exception as e:
        print(f'Step 2: Error in saving model: {e}')

def test_step_3_load_model(file_path='model.pth'):
    try:
        loaded_model = SimpleNN()
        loaded_model.load_state_dict(torch.load(file_path))
        loaded_model.eval()
        print('Step 3: Model loaded successfully from model.pth')
        return loaded_model
    except Exception as e:
        print(f'Step 3: Error in loading model: {e}')
        return None

def test_step_4_inference(model):
    try:
        sample_input = torch.randn(1, 1, 28, 28)
        output = model(sample_input)
        print(f'Step 4: Inference output: {output}')
    except Exception as e:
        print(f'Step 4: Error in performing inference: {e}')

if __name__ == "__main__":
    class SimpleNN(nn.Module):
        def __init__(self):
            super(SimpleNN, self).__init__()
            self.fc = nn.Linear(784, 10)

        def forward(self, x):
            x = x.view(-1, 784)
            return self.fc(x)

model = SimpleNN()
# model.load_state_dict(torch.load('trained_model.pth'))

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
test_dataset = datasets.MNIST('.', train=False, transform=transform)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)

print("Testing Step 1: Evaluate Model")
test_step_1_evaluate_model(model, test_loader)

print("Testing Step 2: Save Model")
test_step_2_save_model(model)

print("Testing Step 3: Load Model")
loaded_model = test_step_3_load_model()

if loaded_model:
    print("Testing Step 4: Perform Inference")
    test_step_4_inference(loaded_model)
