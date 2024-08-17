# SCT 1: Check if configure_optimizers method is defined in LitModel
def test_configure_optimizers():
    model = LitModel()
    assert hasattr(model, 'configure_optimizers'), "configure_optimizers method is not defined in LitModel."

# SCT 2: Check if configure_optimizers correctly returns an Adam optimizer with the correct learning rate
def test_optimizer():
    model = LitModel()
    optimizer = model.configure_optimizers()
    assert isinstance(optimizer, torch.optim.Adam), "configure_optimizers should return an Adam optimizer."
    assert optimizer.defaults['lr'] == 1e-3, "Learning rate for Adam optimizer should be 1e-3."
    
Ex().success_msg("All checks passed successfully.")
