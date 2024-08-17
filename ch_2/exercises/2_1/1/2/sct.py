# SCT 2: Check if the linear layer is correctly defined in the LitModel's __init__ method
def test_linear_layer():
    model = LitModel()
    assert hasattr(model, 'layer'), "Linear layer is not defined in the model."
    assert isinstance(model.layer, torch.nn.Linear), "layer is not a Linear layer."

# SCT 3: Check if forward method correctly flattens input and passes it through the linear layer
def test_forward():
    model = LitModel()
    sample_input = torch.randn(32, 3, 32, 32)
    output = model(sample_input)
    assert output.shape == torch.Size([32, 10]), "Forward method did not produce the expected output shape."
    
# Ex().success_msg("All checks have passed.")
