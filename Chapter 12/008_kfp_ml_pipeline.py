# Script: 008_kfp_ml_pipeline.py

import kfp
from kfp import dsl

# Define the preprocessing operation
def preprocess_op():
    """
    Define the preprocessing step using a container operation.
    Replace <your-docker-username> with your actual Docker Hub username.
    """
    return dsl.ContainerOp(
        name='Preprocess Data',
        image='<your-docker-username>/ml-pipeline-example:latest',  # Update with your Docker image
        command=['python', 'preprocess.py']  # Command to execute preprocessing script
    )

# Define the training operation
def train_op():
    """
    Define the training step using a container operation.
    Replace <your-docker-username> with your actual Docker Hub username.
    """
    return dsl.ContainerOp(
        name='Train Model',
        image='<your-docker-username>/ml-pipeline-example:latest',  # Update with your Docker image
        command=['python', 'train.py']  # Command to execute training script
    )

# Define the pipeline
@dsl.pipeline(
    name='Example Pipeline',
    description='An example pipeline that preprocesses data and trains a model.'
)
def example_pipeline():
    """
    Define the pipeline by specifying the tasks and their dependencies.
    """
    preprocess_task = preprocess_op()  # Preprocessing step
    train_task = train_op()  # Training step
    train_task.after(preprocess_task)  # Ensure training happens after preprocessing

# To compile this pipeline, use:
# kfp.compiler.Compiler().compile(example_pipeline, 'example_pipeline.zip')
