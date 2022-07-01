### Requirements for before the workshop
1. Install Python (ideally version 3.8)
1. have your favorite IDE set up (VS Code, PyCharm, Atom, etc.)
2. clone this repository: https://github.com/MuradKhalil/ing_it_class_visit:
```
$ git clone git@github.com:MuradKhalil/ing_it_class_visit.git
```
3. create a virtial environment (ideally with python 3.8) and activate it.
   - If using conda then use instructions from here: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
   - Otherwise: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

4. navigate to the cloned repository and run following commands. If no error, then you are set up:
```
$ pip install -r src/requirements.txt
$ kedro run
$ kedro viz
$ kedro jupyter lab
```

### Tasks to be done during the workshop
1. register the input csv files in the **conf/base/catalog.yml** file

2. create a pipeline that
   - combines 3 input csv files into 1 dataframe
   - splits data into train and test sets
   - does feature engineering

3. register the pipeline in **pipeline_registry**

4. create a 2nd pipelline that
   - fits a model to the training set
   - evaluates model's performance on the test set

5. register the 2nd pipeline
6. visualize the pipelines
