# SCT 1: Check if training_step method is defined in LitModel
def test_training_step():
    model = LitModel()
    assert hasattr(model, 'training_step'), "training_step method is not defined in LitModel."
    
Ex().success_msg("All checks passed successfully.")
