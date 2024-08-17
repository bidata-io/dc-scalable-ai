# Chapter 3 Capstone

You’ve trained a model, but before deploying it, you must ensure it’s ready for production. This exercise will guide you through the steps of evaluating your model, saving/loading it, and exploring deployment options.

<details>

<summary><h2>Step 1</h2></summary>

### Instructions

- Evaluate your trained model using a testing dataset to ensure it meets production standards. Use the `torchmetrics` library to calculate accuracy and other relevant metrics.

<details>
  
<summary><h3>Hint</h3></summary>

- Combine predictions and labels across batches to calculate overall accuracy.

</details>

### Solution

[solution.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_3/capstone/1/solution.py)

### Sample Code

### Submission Correctness Tests (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_3/capstone/1/sct.py)

</details>

<details>
  
<summary><h2>Step 2</h2></summary>

### Instructions
- After confirming that your model meets the accuracy requirements, save it to a file. Then, reload the model to verify that it can be restored correctly for inference.

<details>

<summary><h3>Hint</h3></summary>

- Ensure you reinstantiate the model class before loading the saved state dictionary.

</details>

### Solution

[solution.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_3/capstone/2/solution.py)

### Submission Correctness Tests (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_3/capstone/2/sct.py)

</details>

<details>
  
<summary><h2>Step 3</h2></summary>

### Instructions

- Explore a deployment option for your model using `torch.jit` to trace the model and convert it to a TorchScript for optimized production deployment.

<details>

<summary><h3>Hint</h3></summary>

- Use `torch.jit.trace` to convert the model to TorchScript, making it suitable for production deployment.

</details>

### Solution

[solution.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_3/capstone/3/solution.py)

### Sample Code

```python
traced_model = torch.jit.trace(loaded_model, sample_input)
```

### Submission Correctness Test (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_3/capstone/3/sct.py)

</details>

<details>

<summary><h2>Step 4</h2></summary>

### Question
- Which library would you use for serving PyTorch models in a scalable production environment?

<details>
<summary><h3>Hint</h3></summary>
- Consider the library’s strength—scalability, management, or creating APIs—when choosing a deployment tool.
  
</details>
### Possible Answers

- TensorFlow Serving
- MLflow
- FastAPI

### Submission Correctness Tests (SCT)

[sct.py](https://github.com/bidata-io/dc-scalable-ai/blob/main/ch_3/capstone/4/sct.py)

</details>
