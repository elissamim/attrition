# Prediction of Attrition

This repo contains a Jupyter Notebook for a task of balanced binary classification. The aim of this task is to identify if a given employee will leave (1) or stay (0) in a given company, from attrition data, i.e historical data of employees who left or stayed in the company. The dataset gives for each employee additional features regarding age, number of years at the company, office location, number of average monthly hours worked, department and job title, gender, satisfaction level in the job, ...

This classification model is evaluated using a recall, as the cost of False Negatives is higher here than the cost of False Positives, i.e. flagging someone leaving the company as staying in the company is more costly for the company than flagging someone as leaving in the case where this person stays.

The final model is then saved [here](model).
