import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score

def load_pred(path):
    df = pd.read_csv(path)
    return df['Pred'], df['ID']

def load_gt(path):
    df = pd.read_csv(path)
    return df['label'], df['ID']


def evaluate(path_to_gt, path_to_pred):
    y_gt, y_id = load_gt(path_to_gt)
    y_pred, y_pred_id = load_pred(path_to_pred)
    
    print("Accuracy:", accuracy_score(y_gt, y_pred), end='\n\n')
    print("F1 Score:", f1_score(y_gt, y_pred), end='\n\n')
    print("Classification Report:\n", classification_report(y_gt, y_pred))
    