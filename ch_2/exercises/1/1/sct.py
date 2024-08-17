# SCT 1: Check if LitModel is defined and inherits from LightningModule
def test_litmodel():
    assert 'LitModel' in globals(), "LitModel class is not defined."
    assert issubclass(LitModel, pl.LightningModule), "LitModel does not inherit from LightningModule."
    
# Ex().success_msg("All checks have passed.")
