![DataCamp](https://miro.medium.com/v2/resize:fit:1400/1*ypaDdrohdvItEcGEKcf7rg.png)

# **Designing Scalable AI Systems**<br/> by **Christine Amuzie**

- Teach: T + R 4P EST
- Campus: Virtual
- Docs: https://instructor-support.datacamp.com

[README](https://github.com/bidata-io/dc-scalable-ai/blob/main/README.md) and sample lesson deadline: 2024-12-31 

As part of the 'Course Spec' process, you will need to complete the following tasks:

- [X] Edit this README by filling in the information for steps 1 - 7 according to our README rubric.
- [X] Update the requirements.sh file in your course repository on GitHub.
- [X] Add the datasets for your course in the Teach Editor.
- [X] Complete one sample lesson according to the sample lesson rubric in the Teach Editor.

## Step 1: Brainstorming 

This part of the 'Course Spec' process is designed to help guide you through course design by having you think through several key questions. Please make sure to delete the examples provided here for you.

### A. What problem(s) will students learn how to solve? (minimum of 5 problems)

*Consider technical problems and 'use case' or business problems.*

- [X] Write a list of ideas for problems that the students will encounter in the course.
> Students will encounter the following within the course:
>- Learn how to build AI systems that can efficiently scale with data and computational resources.
>- Understand and implement techniques to enhance the performance and efficiency of AI models.
>- Use PyTorch and PyTorch Lightning to perform distributed training across multiple GPUs.
>- Conduct experiments and manage hyperparameter tuning to improve model performance.
>- Learn how to evaluate, save, and load models for inference and explore deployment options.


### B. What are the learning objectives of the course?

- [X] Write a list of learning objectives for the course. These are not shown to the students, but they will be used to ensure your vision for the course aligns with the vision of your Curriculum Manager.

>The following are learning objectives for **Designing Scalable AI Systems**:
>- Understand the principles of scalability in AI systems.
>- Learn the basics and advanced features of PyTorch and PyTorch Lightning.
>- Develop and train AI models using PyTorch.
>- Evaluate, save, and load AI models for inference.
>- Explore deployment options and introduce other libraries for productionizing AI models.


### C. What technologies, packages, or functions will students use? Please be exhaustive.

- [X] Write a list of the libraries, packages, functions, methods, or commands that you want to use in the course. Include things like R/Python packages, SQL modules, or Google Sheets add-ons. 

>Technologies, packages, and functions used are below:
>
>- Element-wise mathematical tensor operations (`tensor.add`, `tensor.sub`, `tensor.mul`, `tensor.div`, `tensor.pow`, `tensor.dot`)
>- PyTorch
	>- `torch`, `torch.nn`, `torchvision`, `torch.save`, `torch.load`
>- PyTorch Lightning
	>- `pytorch_lightning`, `pl.LightningModule`, `pl.Trainer`
>- TorchMetrics
>- `numpy`
>- `onnx`
>- Basic Python libraries (e.g., `os`, `sys`)


### D. What terms or jargon will you define?

- [X] Write a list of technical terms, jargon, and acronyms (along with their definitions) that will be used in the course.

>Terms and definitions
>
> - **Tensor:** a multi-dimensional array used for data storage and computation in PyTorch, compatible with GPU operations
> - **Scalability:** the ability of a system to efficiently handle increasing workloads, such as larger datasets or more complex models
> - **Distributed computing:** using multiple computing nodes to perform tasks faster and manage larger datasets effectively
> - **Element-wise operations:** computations applied independently to each element in a tensor, such as addition or multiplication
> - **Neural networks:** models composed of interconnected nodes (neurons) in layers, capable of learning patterns from data
> - **LightningModule:** a PyTorch Lightning component that encapsulates the model architecture and training, validation, and testing logic
> - **Trainer:** manages the training loop, validation, and testing processes, abstracting away boilerplate code in PyTorch Lightning
> - **DataLoader:** a PyTorch class that efficiently handles data batching, shuffling, and parallel loading for model training and evaluation

### E. What analogies or heuristics will you use?

- [X] Write a list of analogies for concepts, heuristics for best practices, and any other non-technical explanations of things that may be helpful to students _(minimum of two)_.

> Think About Coding Like You're Building a House
>
> - **Traditional Coding Methods:** Like building a house from raw materials. You need to source every brick, mix the cement, and follow detailed blueprints for every wall, window, and door. This process is labor-intensive, requires extensive knowledge and skill, and is time-consuming.
> - **PyTorch:** When building a prefab house, you get pre-made walls, windows, and doors that you can easily assemble according to your design. This approach is faster, more efficient, and allows you to focus on the unique features and customizations of the house rather than the basic construction. This is the benefit of PyTorch over traditional coding methods.
> - **PyTorch Lightning:** Now that your house is built, PyTorch Lightning is like using a modular furniture assembly kit with clear instructions. Each piece (module) is designed to fit together seamlessly, and the kit includes all the tools and instructions needed. This makes it easy to build complex, custom furniture without worrying about the individual components or the assembly process, as the kit handles much of the underlying complexity for you.
> - **LightningModule:** the `LightningModule` serves as a blueprint for your model, training steps, and evaluation, organizing everything neatly.
>
> You Have All the Tools You Need
>
> - When using a toolbox where each tool is designed for a specific task, it makes the job easier and more efficient. PyTorch and PyTorch Lightning provide many built-in functions and modules that simplify common tasks, such as layers, loss functions, and optimizers.
>
> Start Simple, Then Scale
>
> - Once you have your blueprint, start by building a scaled down model house before executing a life-size build. Begin with a simple model and dataset to understand the basics before scaling up to more complex models and larger datasets. 
>
> Test, Test, and Test Again
>
> - Back to our house. As you're building, you want to test load-bearing walls, inspect electrical wiring, and seal plumbing during construction to ensure the house is structurally sound and meets safety standards. Similarly, you should frequently evaluate model performance using validation and test datasets to ensure it is learning correctly and to avoid overfitting.

### F. What mistakes or misconceptions do you expect? 

- [X] Write a list of common mistakes _(minimum of two)_ that you think students will make. These can be programming mistakes, conceptual misunderstandings, or simply examples of things that are unintuitive. 

>Expected mistakes and misconceptions:
>
> - Confusing scalability with simple performance optimization.
> - Misunderstanding the differences between PyTorch and PyTorch Lightning.
> - Incorrectly implementing the training loop or misusing DataLoader.
> - Assuming saving and loading models is as simple as saving regular Python objects.


### G. What datasets will you use? 

- [X] Write a list of datasets that you will use in the course, a short description of each dataset (if it's not clear from the title), how you intend to use it and include a link to its source(s).

>CIFAR-10
>
> - The Canadian Institute For Advanced Research (CIFAR-10) is a dataset consisting of 60,000 32x32 color images in 10 classes, with 6,000 images per class. There are 50,000 training images and 10,000 test images. The CIFAR-10 dataset is available through `torchvision` using the code below:
> ```python
> from torchvision.datasets import CIFAR10
> from torchvision.transforms import ToTensor
>
> dataset = CIFAR10(root='data', train=True, download=True, transform=ToTensor())
> ```
> - Source: [CIFAR-10 and CIFAR-100 datasets](https://www.cs.toronto.edu/~kriz/cifar.html)

- [X] Upload these datasets to your course on the Teach Editor. 

[teach_editor_CIFAR-10_dataset_upload](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz)


## Step 2: Who is this course for?

Terms like "beginner" and "expert" mean different things to different people, so we use personas to help instructors clarify a course's audience. When designing a specific course, instructors should explain how it will or won't help these people, and what extra skills or prerequisite knowledge they are assuming their students have above and beyond what's included in the persona.

- [X] Please select the roles and industries that align with your course. 
- [X] Include an explanation describing your reasoning and any other relevant information. 

### What roles would this course be suitable for?

*Check all that apply.*

- [ ] Data Consumer
- [ ] Leader 
- [ ] Data Analyst
- [ ] Citizen Data Scientist
- [X] Data Scientist
- [X] Data Engineer
- [ ] Database Administrator
- [ ] Statistician
- [X] Machine Learning Scientist
- [X] Programmer
- [ ] Other (please describe)

>Data Scientist
>
> - Data Scientists will benefit from this course as it covers essential skills for designing and implementing scalable AI systems using PyTorch and PyTorch Lightning. The course addresses both the theoretical aspects of scalability and practical implementation, which are critical for Data Scientists working with large datasets and complex models.
>
>Data Engineer
> - Data Engineers will find the course valuable as it includes building scalable AI systems and managing data pipelines. While the course focuses more on AI model development, the principles of scalability and efficient data handling are directly applicable to the responsibilities of Data Engineers.
>
>Machine Learning Scientist
>
> - Machine Learning Scientists are focused on developing and refining machine learning models. This course provides in-depth knowledge of PyTorch and PyTorch Lightning, essential tools for building, training, and optimizing models. The advanced topics and production preparation aspects of the course are highly relevant to their work.
>
>Programmer
>
> - Programmers with an interest in AI and machine learning can benefit from this course by learning how to implement and optimize AI models using PyTorch and PyTorch Lightning. The course provides a solid foundation in AI model development and scalability, which can enhance their skill set and open up new career opportunities in AI.

### What industries would this apply to?

>Industries
> - Technology
>	- Companies developing AI-driven products and services
> - Healthcare
> 	- Organizations leveraging AI for diagnostics, patient care, and research
> - Finance
> 	- Firms using AI for predictive modeling, fraud detection, and algorithmic trading
> - Retail
> 	- Businesses applying AI for personalized recommendations, inventory management, and customer analytics
> - Manufacturing
> 	- Industries implementing AI for predictive maintenance, quality control, and automation


### What level of expertise should learners have before beginning the course?

*List three or more examples of skills that you expect learners to have before beginning the course*

>Proficiency in Python Programming
> - Writing clean and efficient Python code.
> - Understanding of core Python libraries such as NumPy and pandas.
> - Experience with object-oriented programming and writing custom classes and functions.
>
>Basic Knowledge of Machine Learning Concepts
> - Understanding of fundamental machine learning algorithms (e.g., linear regression, logistic regression, decision trees).
> - Experience with training and evaluating machine learning models using libraries such as scikit-learn.
> - Familiarity with concepts such as overfitting, underfitting, cross-validation, and model evaluation metrics (e.g., accuracy, precision, recall).
>
>Experience with Deep Learning Frameworks
> - Basic knowledge of neural networks and deep learning concepts (e.g., convolutional neural networks, recurrent neural networks).
> - Experience with deep learning frameworks like TensorFlow or Keras.
> - Ability to build, train, and evaluate simple neural network models.
>
>Understanding of Data Handling and Preprocessing
> - Experience with data preprocessing techniques such as normalization, standardization, and data augmentation.
> - Ability to load and manipulate datasets using libraries like pandas and NumPy.
> - Familiarity with data splitting techniques (e.g., train-test split, cross-validation).
>
>Basic Knowledge of PyTorch
> - Understanding of PyTorch tensors and basic tensor operations.
> - Experience with building and training simple models using PyTorch.
> - Familiarity with PyTorch's autograd mechanism for automatic differentiation.

## Step 3: Course outline

A typical course is structured as follows:

- Chapter 1 has three lessons. This chapter is shorter than the rest since it serves as an introduction to the topic.
- Chapter 2 has 3-4 lessons.
- Chapter 3 has 3-4 lessons.
- Chapter 4 has 3-4 lessons.

A typical lesson is comprised of:

- A video exercise with slides and script, e.g. [sample video exercise](https://campus.datacamp.com/courses/introduction-to-the-tidyverse/data-wrangling-1?ex=4).
- 2-4 exercises that review what is covered in the video exercise.

*Remind yourself about [course terminology](https://authoring.datacamp.com/courses/design#terminology-and-structure), then describe the flow of the course.*

> **Designing Scalable AI Systems**

> Chapter 1 - Introduction to Scalable AI Systems with PyTorch
>	* Lesson 1.1 - Overview of Scalability in AI Systems
>		* Learning Objective: Understand the concept of scalability and its importance in AI systems
>		* Functions: element-wise mathematical `tensor` operations (`.add`, `.sub`, `.mul`, `.div`, `.pow`, `.dot`)
>	* Lesson 1.2 - Introduction to PyTorch
>		* Learning Objective: Understand the basics of PyTorch and its role in scalable AI
>		* Functions: `torch.tensor`, basic tensor operations
> 	* Lesson 1.3 - Coding with and Without PyTorch
> 		* Learning Objective: Compare and contrast traditional Python code with PyTorch code, implementing similar operations using PyTorch for efficiency and scalability
>		* Functions: `torch` operations, matrix multiplications, and element-wise operations

> Chapter 2 - Advanced Topics in PyTorch and PyTorch Lightning
>	* Lesson 2.1 - Introduction to PyTorch Lightning
> 		* Learning Objective: Understand the benefits and basic usage of PyTorch Lightning
> 		* Functions: `pytorch_lightning.LightningModule`, `pytorch_lightning.Trainer`
>	* Lesson 2.2 - Building Models with PyTorch Lightning
>		* Learning Objective: Reconstruct a PyTorch model using PyTorch Lightning for better scalability and readability
>		* Functions: `pytorch_lightning.LightningModule` methods
>	* Lesson 2.3 - Training with PyTorch Lightning
>		* Learning Objective: Train models more efficiently using PyTorch Lightning
>		* Functions: `pytorch_lightning.Trainer.fit`, checkpointing, logging
>	* Lesson 2.4 - Advanced Model Architectures
>		* Learning Objective: Explore and implement advanced model architectures such as CNNs and RNNs
>		* Functions: `torch.nn.Conv2d`, `torch.nn.LSTM`, custom model layers
>	* Lesson 2.5 - Experiment Management with PyTorch Lightning
>		* Learning Objective: Manage and track experiments using built-in features of PyTorch Lightning
>		* Functions: `pytorch_lightning.loggers`, experiment tracking tools

> Chapter 3 - Preparing Models for Production
>	* Lesson 3.1 - Model Evaluation and Testing
>		* Learning Objective: Evaluate and test your model to ensure it meets production standards
>		* Functions: `torchmetrics`, validation steps, testing datasets  
>	* Lesson 3.2 - Saving and Loading Models
>		* Learning Objective: Save trained models and load them for inference
>		* Functions: `torch.save`, `torch.load`, `model.eval`
>	* Lesson 3.3 - Deployment Options
		* Learning Objective: Explore different deployment options for PyTorch models
        * Functions: `torch.jit`, `onnx`, brief mention of cloud deployment options
>	* Lesson 3.4 - Introduction to Other Libraries
>		* Learning Objective: Get an overview of other useful libraries for productionizing AI models
>		* Functions: brief introduction to TensorFlow Serving, MLflow, FastAPI for serving models

  
  - [X] Does each lesson have a clear learning objective?
  - [X] Does each lesson include a brief list of functions or packages that the student will use?
  - [X] Does the outline have at least 12 lessons and no more than 15?

## Step 4: Capstone exercises

Create a capstone exercise for **each chapter** of your course in the Teach Editor. **(Note: This is different from what you did when you submitted your course outline application, which was just one exercise for the entire course)** Let your Curriculum Manager know when you have completed this step so that they can review your exercises and provide you with feedback.

A capstone exercise should showcase how far learners are likely to get at the end of each chapter. Please check out more details on this and further tips [here](http://instructor-support.datacamp.com/courses/course-design/building-capstone-exercises).

In addition to using the `Coding` exercise type, we expect you to use the `Iterative` and `Sequential` exercise types. Be sure to check out our documentation on [Iterative](https://instructor-support.datacamp.com/articles/2375528-course-iterative-exercises) and [Sequential](https://instructor-support.datacamp.com/articles/2375525-course-sequential-exercises) exercises before you start.

Please ensure that your capstone exercises meet our [content guidelines](https://instructor-support.datacamp.com/en/articles/2360978-content-guidelines).

## Step 5: Build ONE complete lesson on the Teach Editor

This should include:
1. A video exercise with slides (this can be the same as or similar to slides/video that you already created for your audition).
2. Between 2 and 4 exercises that allow students to practice what you taught in the video exercise.  This **does not** include Solution Correctness Tests (SCTs), but **does include** the success message for each exercise.

Why create a lesson as part of your course spec?

It will:

- Allow you to become familiar with the Teach Editor along with our different exercise and slide types earlier.
- Give you a better understanding of course scope (e.g., what can be covered in a reasonable amount of time, and what must be saved for a future course - compared to creating just a course outline.)

In combination, this will result in faster course development time, a more frictionless course development experience, and prevent roadblocks that arise out of miscalibrated course scope.

Our experience working with over a hundred expert instructors over the past 4 years has taught us that the most challenging part of creating a DataCamp course is in understanding the scope of what can be covered in a lesson (and, by extension, a course). 

We believe that students learn best when their hands are on the keyboard, writing code, working with data, and solving problems. Consequently, our courses consist of short  3 to 4-minute videos separated by interactive coding exercises, with occasional multiple choice exercises interspersed. The videos are intended to teach students the concepts necessary to solve the exercises that follow. 

You can read through all of our content guidelines [here](https://authoring.datacamp.com/courses/guidelines/content.html).

Four-minute videos correspond to between **400 and 600 words total** in the script. 

**Teaching data science concepts in this amount of time is not easy:** 
- It forces you to drill down to the essence of the concept and eliminate everything extraneous. 
- It requires a different approach compared to giving 50-minute college lectures.
- Writing such a script as part of your sample lesson will help you in creating a course outline that covers the right amount of content.

All lessons MUST follow our [content guidelines](https://authoring.datacamp.com/courses/guidelines/content.html).

## Lesson Rubric and Process

### Process

**Timeline**

Please work with your Curriculum Manager to ensure that all of the following boxes are checked. Once that happens, the Content Development team will review the lesson within **3 working days**, and you must incorporate the feedback (if any!) within the next **3 working days.** 

**Feedback Delivery**

There will be no more than **2 rounds of feedback** by a Content Developer, and in each round of feedback, the Content Developer will be specific and unambiguous in explaining exactly what revisions are necessary before the course can be considered ready for handoff. If, after two rounds of feedback, the lesson is still not deemed acceptable by the Content Development team, DataCamp will not move forward with course development.

### Lesson Rubric

#### General

- [ ] Does the lesson consist of 1 video followed by 2-4 exercises?
- [ ] Are there at least 2 coding exercises?
- [ ] Is there no more than 1 multiple choice exercise?
- [ ] Is the script for the video between 400 and 600 words?
- [ ] Are the titles of the exercises and slides written in sentence case?
- [ ] Do all of the exercises run on DataCamp in less than 3 seconds?
- [ ] Does the build pass?

#### Video

- [ ] Are the slides dynamic? That is, is there movement on the slides, such as in the form of transitions between bullets and lines of code, or progression through a visual/schema?
- [ ] Are full sentences in slides avoided?
- [ ] Is there a clear learning objective and/or narrative that motivates why the concept is important?
- [ ] Is there code in the slides? Learning by Doing requires Teaching by Doing!
- [ ] Does the code incorporate a relevant dataset that is [not overused](https://authoring.datacamp.com/courses/design/brainstorming-datasets.html)?
- [ ] Is the code properly formatted and placed inside backticks? It is your responsibility to ensure that your slides are properly formatted.
- [ ] Is the (trans)script written in complete sentences, without any bullet points or markdown? The script should correspond to exactly what you will say in the final recording and will be used to generate the subtitles for your course.

#### Exercises

- [ ] Are the [Content Guidelines](https://authoring.datacamp.com/courses/guidelines/content.html) met?
- [ ] Context: 180-780 characters
- [ ] Instructions: 1-4 bulleted instructions
- [ ] Hints: 1-4 bulleted hints
- [ ] Sample/Solution code: Less than or equal to 15 lines of code
- [ ] Success Message: Is there an informative success message?
- [ ] Do the comments in the sample and solution code match?
- [ ] Are the comments abbreviated instructions?
- [ ] Are the comments free of backticks?
- [ ] Is each comment less than 60 characters of length?
- [ ] Does each comment start with a space?
- [ ] Are different sections of code properly spaced?
- [ ] Are the instructions bulleted?
- [ ] Are the hints bulleted?
- [ ] Is the sample code appropriately scaffolded? Python courses use 4 underscores.

#### FAQs

##### Which lesson should I create for my sample lesson?

This is your choice. We recommend the final lesson of your course, as it has the following advantages:

- The concepts will likely be more advanced, and confirming that you can adequately teach the material in less than 600 words will verify that the course scope is appropriate.
- Similarly, the code will tend to be more advanced and computationally intensive. Confirming that the code runs on DataCamp and that the exercises meet our content guidelines will provide another check to verify that the course scope is indeed appropriate. 
- It provides clarity on where students will be at the end of the course and a clear stopping point that you can then work towards during the rest of course development.

**Whichever lesson you create, it is important to keep in mind the spirit of the sample lesson:** 
- it is an important check on course scope, 
- an opportunity to acquaint yourself with the tools you will be using to build your course, 
- and a chance to receive early feedback on teaching style to ensure you and DataCamp are aligned on course vision.

## Step 6: Revisit course outline

Having created your sample lesson, you should now have a much better understanding of course scope. This is an ideal time to revisit your outline and update it if necessary.

## Step 7: Write course description and list course prerequisites

**Course Description**

Add a description of the course in the Settings tab of the Course Editor. How to get to editing this is shown below as an image.

![](https://user-images.githubusercontent.com/9215614/52296764-04f95c80-2934-11e9-9ff7-4ae5155ef189.png)

Please review these guidelines when creating it: https://instructor-support.datacamp.com/courses/course-design/datacamp-course-descriptions. 

**Prerequisites**

- [Introduction to Data Science in Python](https://www.datacamp.com/courses/introduction-to-data-science-in-python)
- [Intermediate Python](https://www.datacamp.com/courses/intermediate-python)
- Other prerequisite courses
