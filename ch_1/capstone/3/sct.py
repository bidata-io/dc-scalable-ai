import time

# Timing for Python list addition
start_time = time.time()
result = [a + b for a, b in zip(list1, list2)]
python_time = time.time() - start_time

# Timing for PyTorch tensor addition
start_time = time.time()
result = tensor1 + tensor2
pytorch_time = time.time() - start_time

assert python_time > pytorch_time, "Step 3 failed: PyTorch is not faster as expected."

# Ex().success_msg("All checks have passed.")
