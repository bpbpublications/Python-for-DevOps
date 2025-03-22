# Script: 009_mlflow_logging_example.py

import mlflow

# Set or create an experiment in MLflow
mlflow.set_experiment('my_experiment')

def train_model(data, num_trees, max_depth):
    """
    Dummy function to represent training a model.
    Replace this with actual training logic.
    """
    class Model:
        def __init__(self, accuracy, loss):
            self.accuracy = accuracy
            self.loss = loss

    # Example: Return a dummy model with accuracy and loss
    return Model(accuracy=0.92, loss=0.08)

# Example data (replace with your actual dataset)
data = "example_dataset"

# Start an MLflow run
with mlflow.start_run():
    # Log parameters (key-value pairs)
    mlflow.log_param('num_trees', 100)
    mlflow.log_param('max_depth', 5)

    # Train your model (example)
    model = train_model(data, num_trees=100, max_depth=5)

    # Log metrics (key-value pairs)
    mlflow.log_metric('accuracy', model.accuracy)
    mlflow.log_metric('loss', model.loss)

    # Log artifacts (output files)
    # Replace 'output_model.pkl' with your actual model file
    with open('output_model.pkl', 'w') as f:
        f.write('This is a placeholder for the model file.')
    mlflow.log_artifact('output_model.pkl')

mlflow.sklearn.log_model(model, "my_model")