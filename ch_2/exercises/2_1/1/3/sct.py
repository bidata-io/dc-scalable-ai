# SCT 4: Check if the DataLoader is correctly instantiated
def test_dataloader():
    assert 'train_loader' in globals(), "train_loader is not defined."
    assert isinstance(train_loader, DataLoader), "train_loader is not a DataLoader instance."
    
# Ex().success_msg("All checks have passed.")
