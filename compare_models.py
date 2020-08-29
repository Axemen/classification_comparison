import webbrowser
from typing import List

import sklearn

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

def compare_models(models, X, y, 
                    random_state=42, 
                    metrics=['recall_score', 'precision_score']):
    # TODO 
    results = []
    (X_train, X_test, 
        y_train, y_test) = train_test_split(X, y, random_state=random_state)

    for model in models:
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        results.append(calc_metrics(y_test, preds, metrics))
    return results

def calc_metrics(y_true, y_pred, metrics):
    """
    Takes in the true and predicted value and returns the 
    metrics passed inside of the metrics parameter.

    Metrics must be in the form of the SK-Learn function name. 
    """
    results = {}

    for metric, kw in metrics:
        func = getattr(sklearn.metrics, metric)
        results[metric] = func(y_true, y_pred, **kw)

    return results

if __name__ == "__main__":
    # ! This is nothing but a test case

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

    preds = m.predict(X_test)

    metrics = [
        ('recall_score', {"average":None}),
        ('precision_score', {"average":None})
    ]

    results = calc_metrics(y_test, preds, metrics)
    print(results)

    # webbrowser.open_new('https://localhost:5000')
