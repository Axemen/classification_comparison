from typing import List
from sklearn.metrics import *

""" 
Expected code to run 

models = [
    LinearRegression(),
    RandomForest(),
    ...
]

compare_models(models)

This will spin up the local server and open the web browser. 
"""

def compare_models(models:List, X, y):
    results = {}
    pass

if __name__ == "__main__":
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.dummy import DummyClassifier
    from sklearn.model_selection import train_test_split
    import numpy as np

    models = [
        LogisticRegression(),
        RandomForestClassifier(),
        DummyClassifier()
    ]
    
    X = np.random.random_sample((100, 5))
    y = np.random.randint(5, size=(100,))

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    m = LogisticRegression()
    m.fit(X_train, y_train)
    