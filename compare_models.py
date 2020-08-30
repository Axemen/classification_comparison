import webbrowser
from typing import List

import sklearn.metrics as skmetrics


""" 
Expected code to run 

models = [
    ("Linear Regression", LinearRegression()),
    ("Random Forest", RandomForest()),
    ...
]

create_report(models)

This will spin up the local server and open the web browser. 
"""
def create_report(models, X, y, random_state=42):
    # TODO
    pass

def compare_models(models, X, y,
                   random_state=42,
                   custom_metrics=None):
    """ 
    Takes in a list of models and calculates the metrics for said models

    models = [
        ("Logistic Regression", LogisticRegression()),
        (<name>, <model>)
    ]

    X = Data 
    y = Target

    custom_metrics = [
        ("recall", sklearn.metrics.recall),
        (<name>, metric)
    ]
    """
    # TODO
    results = []
    (X_train, X_test,
        y_train, y_test) = train_test_split(X, y, random_state=random_state)

    for name, model in models:
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        results.append({
            "name": name,
            "metrics": calc_metrics(y_test, preds, metrics)
        })
    return results


def calc_custom_metrics(y_true, y_pred, metrics):
    """
    Takes in the true and predicted value and returns the 
    metrics passed inside of the metrics parameter.

    Metrics can be passed through in the form of 
    (<name>, func_ref)

    The function reference given must accept the arguments y_true, and y_pred
    """
    return {name: metric(y_true, y_pred) for name, metric in metrics}


if __name__ == "__main__":
    # ! This is nothing but a test case

    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.dummy import DummyClassifier
    from sklearn.model_selection import train_test_split
    import numpy as np

    models = [
        ("LR", LogisticRegression()),
        ("RF", RandomForestClassifier()),
        ("DC", DummyClassifier())
    ]

    X = np.random.random_sample((100, 5))
    y = np.random.randint(5, size=(100,))

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    m = LogisticRegression()
    m.fit(X_train, y_train)

    preds = m.predict(X_test)

    results = calc_metrics(y_test, preds, metrics)
    print(results)

    # webbrowser.open_new('https://localhost:5000')
