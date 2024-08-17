# Chapter 1 Capstone

> CONTEXT

In this final exercise, you’ll apply the foundational concepts of scalability in AI systems using PyTorch. You'll start by implementing basic element-wise addition using traditional Python lists. Then, you’ll translate this operation into PyTorch, leveraging its efficiency and scalability. Finally, you'll compare the performance of both methods by measuring their execution times. This exercise will solidify your understanding of why PyTorch is crucial for scalable AI solutions.

> PRE-EXERCISE CODE

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
```

<details>

<summary><h2>Step 1</h2></summary>

> INSTRUCTIONS

Add [1, 2, 3] and [4, 5, 6] using a for loop.


<details>

<summary><h3>HINT</h3></summary>

Use a loop or list comprehension to iterate over both lists simultaneously and add corresponding elements.

</details>

> SOLUTION

[solution.py](https://github.com/bidata-io/dc-scalable-ai/main/ch_1/capstone/1/solution.py)

> SAMPLE CODE

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [ ]
```

> SUBMISSION CORRECTNESS TESTS (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/main/ch_1/capstone/1/sct.py)

</details>

<details>
  
<summary><h2>Step 2</h2></summary>

> INSTRUCTIONS

- Repeat the above operation using PyTorch tensors.

<details>

<summary><h2>HINT</h2></summary>

- PyTorch tensors can be added directly using the + operator, similar to how you would add regular numbers in Python.

</details>

> SOLUTION

[solution.py](https://github.com/bidata-io/dc-scalable-ai/new/main/ch_1/capstone/2/solution.py)

> SAMPLE CODE

```python
import torch
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])
result = 
```

> SUBMISSION CORRECTNESS TESTS (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/new/main/ch_1/capstone/2/sct.py)

</details>

<details>
  
<summary><h2>Step 3</h2></summary>

> INSTRUCTIONS

- Compare the results and execution time of both approaches. Measure and compare the execution time of both methods.

<details>

<summary><h3>HINT</h3></summary>

- Use the `time.time()` function before and after the operation to calculate the time taken. Remember to convert the result to seconds if needed.

</details>

> SOLUTION

[solution.py](https://github.com/bidata-io/dc-scalable-ai/new/main/ch_1/capstone/3/solution.py)

> SAMPLE CODE

```python
import time
start_time = time.time()
result = 
python_time = time.time() - start_time

start_time = time.time()
result = 
pytorch_time = time.time() - start_time
```

> SUBMISSION CORRECTNESS TESTS (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/new/main/ch_1/capstone/3/sct.py)

</details>
