# Trace the model with TorchScript
traced_model = torch.jit.trace(loaded_model, sample_input)

# Save the TorchScript model
traced_model_path = 'traced_model.pt'
traced_model.save(traced_model_path)

# Load the TorchScript model and verify by running inference
loaded_traced_model = torch.jit.load(traced_model_path)
traced_output = loaded_traced_model(sample_input)
print(traced_output)
