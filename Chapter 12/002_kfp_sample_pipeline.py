# Script: 002_kfp_sample_pipeline.py

# Import Kubeflow Pipelines SDK
import kfp
from kfp import dsl

# Define the preprocessing step
def preprocess_op():
    return dsl.ContainerOp(
        name='Preprocess Data',
        image='your-preprocessing-image',  # Replace with your container image for preprocessing
        arguments=[  # Add arguments specific to your preprocessing logic
            '--input', 'data/input/path',
            '--output', 'data/output/path'
        ]
    )

# Define the training step
def train_op():
    return dsl.ContainerOp(
        name='Train Model',
        image='your-training-image',  # Replace with your container image for training
        arguments=[  # Add arguments specific to your training logic
            '--train-data', 'data/output/path',
            '--model-dir', 'model/output/path'
        ]
    )

# Define the pipeline
@dsl.pipeline(
    name='Sample Pipeline',
    description='A sample pipeline that processes data and trains a model.'
)
def sample_pipeline():
    # Step 1: Preprocess data
    preprocess_task = preprocess_op()
    
    # Step 2: Train model
    train_task = train_op()
    train_task.after(preprocess_task)  # Ensure training happens after preprocessing

# This code can be compiled and run in a Kubeflow Pipelines environment
# Compile the pipeline to a .zip file
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(sample_pipeline, 'sample_pipeline.zip')
    print("Pipeline has been compiled to 'sample_pipeline.zip'")
