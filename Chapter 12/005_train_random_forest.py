# Script: 005_train_random_forest.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

# Example training steps
def train(input_path, model_path):
    """
    Train a RandomForestClassifier using the input data and save the trained model.
    
    Args:
        input_path (str): Path to the preprocessed CSV file containing features and labels.
        model_path (str): Path to save the trained model as a .pkl file.
    """
    # Load the data
    data = pd.read_csv(input_path)
    
    # Separate features and labels
    X = data.drop('label', axis=1)  # Features
    y = data['label']  # Labels
    
    # Initialize and train the Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)  # Added parameters for consistency
    clf.fit(X, y)
    
    # Save the trained model to a file
    joblib.dump(clf, model_path)
    print(f"Model saved to: {model_path}")

if __name__ == "__main__":
    train('preprocessed_data.csv', 'model.pkl')
