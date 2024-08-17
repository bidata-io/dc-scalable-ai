import torch

# Save the model
model_path = 'model.pth'
torch.save(model.state_dict(), model_path)

# Load the model for inference
loaded_model = YourModelClass()  # Replace with your model class
loaded_model.load_state_dict(torch.load(model_path))
loaded_model.eval()

# Verify loading by running inference on a sample input
sample_input, _ = next(iter(test_loader))
sample_output = loaded_model(sample_input)
print(sample_output)
