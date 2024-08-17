![DataCamp](https://miro.medium.com/v2/resize:fit:1400/1*ypaDdrohdvItEcGEKcf7rg.png)

# Designing Scalable AI Systems

Christine Amuzie, _Course Instructor_

christine@bidata.io

[bidata.io](https://bidata.io)

[//]: # ( ## Step 1: Brainstorming)
[//]: 
<-- (### What problem(s) will students learn how to solve?) -->

[//]: # ( - Design and implement scalable AI systems using PyTorch and PyTorch Lightning.)
[//]: # ( - Optimize AI models for performance and efficiency.)
[//]: # ( - Prepare AI models for production environments.)

[//]: # (### What are the learning objectives of the course?)
[//]: # ( - Understand the principles of scalability in AI systems.)
[//]: # ( - Learn the basics and advanced features of PyTorch and PyTorch Lightning.)
[//]: # ( - Develop and train AI models using PyTorch.)
[//]: # ( - Evaluate, save, and load AI models for inference.)
[//]: # ( - Explore deployment options and introduce other libraries for productionizing AI models.)

[//]: # (### What technologies, packages, or functions will students use?)
[//]: # ( - PyTorch)
[//]: # ( - PyTorch Lightning)
[//]: # ( - TorchMetrics)
[//]: # ( - Numpy)
[//]: # ( - ONNX)
[//]: # ( - torch.save, torch.load)
[//]: # ( - Basic Python libraries e.g., os, sys)

[//]: # (### What terms or jargon will you define?)
[//]: # ( - Scalability)
[//]: # ( - Distributed computing)
[//]: # ( - Element-wise operations)
[//]: # ( - Neural networks)
[//]: # ( - LightningModule)
[//]: # ( - Trainer)
[//]: # ( - DataLoader)

[//]: # (### What analogies or heuristics will you use?)
[//]: # ( - Comparing traditional coding methods with PyTorch to highlight the benefits.)
[//]: # ( - Using the analogy of building blocks to explain the modular approach of PyTorch Lightning.)


[//]: # (### What mistakes or misconceptions do you expect?)
[//]: # ( - Confusing scalability with simple performance optimization.)
[//]: # ( - Misunderstanding the differences between PyTorch and PyTorch Lightning.)
[//]: # ( - Incorrectly implementing the training loop or misusing DataLoader.)
[//]: # ( - Assuming saving and loading models is as simple as saving regular Python objects.)

[//]: # (### What datasets will you use?)
[//]: # ( - CIFAR-10 dataset for image classification tasks.)
[//]: # ( - Custom synthetic datasets for specific exercises.)

[//]: # (## Step 2: Who Is This Course for?)
[//]: # ( - Intermediate to advanced learners with some experience in AI and machine learning.)
[//]: # ( - Data scientists and engineers looking to scale their AI solutions.)
[//]: # ( - Professionals with a background in programming and basic knowledge of machine learning frameworks.)

[//]: # (## Step 3: Course Outline)

## Overview

### Course Description
Dive into the world of scalable AI systems with this course crafted to equip AI practitioners with the knowledge and tools for architecting and deploying AI solutions efficiently. This course focuses on establishing a strong foundation in scalable AI development and deployment with an emphasis on PyTorch and PyTorch Lightning. Learners will gain the expertise to enhance AI system performance and ensure fast deployment across diverse environments. This course is tailored for professionals looking to scale AI projects.

### Prerequisites
- Intermediate knowledge of AI and machine learning.
- Proficiency in Python programming.
- Basic understanding of cloud services.


## Outline

### Chapter 1: Introduction to Scalable AI Systems with PyTorch
- **Lesson 1.1: Overview of Scalability in AI Systems**
  - Learning Objective: Understand the concept of scalability and its importance in AI systems.
  - Functions: element-wise mathematical `tensor` operations (`.add`, `.sub`, `.mul`, `.div`, `.pow`, `.dot`)

- **Lesson 1.2: Introduction to PyTorch**
  - Learning Objective: Understand the basics of PyTorch and its role in scalable AI.
  - Functions: `torch.tensor`, basic tensor operations
    
- **Lesson 1.3: Coding with and Without PyTorch**
  - Learning Objective: Compare and contrast traditional Python code with PyTorch code, implementing similar operations using PyTorch for efficiency and scalability.
  - Functions: `torch` operations, matrix multiplications, and element-wise operations

### Chapter 2: Advanced Topics in PyTorch and PyTorch Lightning
- **Lesson 2.1: Introduction to PyTorch Lightning**
  - Learning Objective: Understand the benefits and basic usage of PyTorch Lightning 
  - Functions: `pytorch_lightning.LightningModule`, `pytorch_lightning.Trainer`
    
- **Lesson 2.2: Building Models with PyTorch Lightning**
  - Learning Objective: Reconstruct a PyTorch model using PyTorch Lightning for better scalability and readability
  - Functions: `pytorch_lightning.LightningModule` methods
    
- **Lesson 2.3: Training with PyTorch Lightning**
  - Learning Objective: Train models more efficiently using PyTorch Lightning
  - Functions: `pytorch_lightning.Trainer.fit`, checkpointing, logging
    
- **Lesson 2.4: Advanced Model Architectures**
  - Learning Objective: Explore and implement advanced model architectures such as CNNs and RNNs.
  - Functions: `torch.nn.Conv2d`, `torch.nn.LSTM`, custom model layers
    
- **Lesson 2.5: Experiment Management with PyTorch Lightning**
  - Learning Objective: Manage and track experiments using built-in features of PyTorch Lightning.
  - Functions: `pytorch_lightning.loggers`, experiment tracking tools

### Chapter 3: Preparing Models for Production
- **Lesson 3.1: Model Evaluation and Testing**
  - Learning Objective: Evaluate and test your model to ensure it meets production standards
  - Functions: `torchmetrics`, validation steps, testing datasets
    
- **Lesson 3.2: Saving and Loading Models**
  - Learning Objective: Save trained models and load them for inference.
  - Functions: `torch.save`, `torch.load`, `model.eval`
    
- **Lesson 3.3: Deployment Options**
  - Learning Objective: Explore different deployment options for PyTorch models
  - Functions: `torch.jit`, `onnx`, brief mention of cloud deployment options
   
- **Lesson 3.4: Introduction to Other Libraries**
  - Learning Objective: Get an overview of other useful libraries for productionizing AI models
  - Functions: brief introduction to TensorFlow Serving, MLflow, FastAPI for serving models

### [**Capstone:** Design A Scalable AI System](https://github.com/bidata-io/dc-scalable-ai/tree/main/ch_4/capstone)




[//]: # (## Step 4: Capstone Exercises)

[//]: # (## Step 5: Build ONE complete lesson in the Teach editor)
[//]: # (## Sneak Peek: Example Lesson)
[//]: # (- **Lesson 2.1: Parallelizing Workloads with Apache Spark**)
[//]: # (- Video Exercise: Introduction to Apache Spark and its use cases.)
[//]: # (- Interactive Exercise 1: Loading data with Spark.)
[//]: # (- Interactive Exercise 2: Transforming data with Spark.)
[//]: # (- Interactive Exercise 3: Performing actions on Spark DataFrames.)

[//]: # (## Step 6: Revisit Course Outline)
[//]: # (- Revisit and refine the outline after building the first complete lesson to ensure alignment with the overall course objectives and structure.)

[//]: # (## Step 7: Write Course Description and List Course Prerequisites)
