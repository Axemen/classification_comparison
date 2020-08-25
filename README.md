# Classification Comparison 

### This is a simple tool to compare multiple classification machine learning models to one another in a local web server format. 


## Setup
Create local environment

```
python -m venv .venv
source .venv/Scripts/activate #Windows 
# IDK what it is on mac
```

install requirements based on requirements.txt
```
pip install -r requirements.txt
```


## Milestones

* Create function to run all models and calculate metrics for them. 
* Capture model outputs and pass to flask
* Display model results in webpage format. 
* Develop website layout for the comparison of models
    * Section containing Confusion Matrix
    * Section containing model metrics 
    * Section containing data desriptions
    * Section containing graphs of model components? This would need to be dynamic and allow for selection of multiple columns. 

