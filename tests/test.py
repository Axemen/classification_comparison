# TODO move to proper testing format

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
