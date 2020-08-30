import json
import webbrowser
from typing import List

import sklearn.metrics as skmetrics
from bs4 import BeautifulSoup
from tqdm import tqdm


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


def write_data_to_html(data, html_path, output_path='report/report.html'):
    with open(html_path, 'r') as html_file:
        soup = BeautifulSoup(html_file.read(), 'html.parser')
        soup.find("script", id='data').string = "let data = " + \
            json.dumps(data)
        open(output_path, 'w').write(str(soup))


def compare_models(models, X, y,
                   random_state=42,
                   custom_metrics=None
                   ):
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

    for name, model in tqdm(models):
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        result = {
            "name": name,
            "clf report": skmetrics.classification_report(y_test, preds,
                                                          zero_division=0,
                                                          output_dict=True),
            "confusion matrix": skmetrics.confusion_matrix(y_test, preds, normalize='true').tolist()
        }

        # TODO Figure out how exactly to easily accept custom metrics and their params
        if custom_metrics:
            raise NotImplementedError
            # results['custom metrics'] = calc_custom_metrics(y_test, preds, custom_metrics)
        # else:
        #     results['custom metrics'] = {}

        results.append(result)
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
        ("DC", DummyClassifier(strategy='stratified'))
    ]

    X = np.random.random_sample((1000, 5))
    y = np.random.randint(5, size=(1000,))

    results = compare_models(models, X, y)
    write_data_to_html(results, 'template.html')
    # print(results)

    # webbrowser.open_new('https://localhost:5000')
