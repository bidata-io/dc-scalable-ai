import torch
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])
result = tensor1 + tensor2
assert torch.equal(result, torch.tensor([5, 7, 9])), "Step 2 failed: Incorrect result for PyTorch element-wise addition."

# Ex().success_msg("All checks have passed.")
