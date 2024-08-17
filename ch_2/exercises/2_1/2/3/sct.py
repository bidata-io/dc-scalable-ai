# SCT 2: Check if training_step correctly computes and returns the loss
def test_training_step_loss():
    model = LitModel()
    sample_batch = next(iter(train_loader))
    loss = model.training_step(sample_batch, 0)
    assert isinstance(loss, torch.Tensor), "training_step should return a tensor representing the loss."
    assert loss.item() > 0, "The computed loss should be greater than zero."
    
Ex().success_msg("All checks passed successfully.")
