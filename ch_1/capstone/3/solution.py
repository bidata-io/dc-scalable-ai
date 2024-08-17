import time
start_time = time.time()
result = [a + b for a, b in zip(list1, list2)]
python_time = time.time() - start_time

start_time = time.time()
result = tensor1 + tensor2
pytorch_time = time.time() - start_time
