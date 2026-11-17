# A Small Flask-Based Student Performance Prediction Prototype Using Linear Regression

**Student:** [Your name]  
**Department and college:** [Department, college]  
**Course and year:** [Course, second year]  
**Instructor:** [Instructor name]  
**Date:** [Submission date]

> **Draft note:** This is a course-project paper draft. Fill in the details above and confirm the source and permitted use of the dataset with your instructor before submitting or publishing it.

## Abstract

This project is a small web application that estimates a student's final mark from three inputs: study hours, previous marks, and attendance. It uses a linear regression model trained on the 15 rows in the project's included CSV file. A Flask server provides the prediction, while a simple web page collects the inputs and displays the result.

To make the evaluation repeatable with a small dataset, the model was assessed using leave-one-out cross-validation and compared with a baseline that predicts the training-set average. On these 15 records, the linear regression model had a mean absolute error of 0.640 marks and a root mean squared error of 0.857 marks. These numbers look strong, but they should not be read as evidence that the system will work equally well for other students: the dataset is very small, and its source is not documented. The project is best understood as a learning prototype and a starting point for a more careful study.

**Keywords:** student performance, linear regression, Flask, prediction, educational project

## 1. Introduction

A mark can be affected by many things, and a simple program cannot capture all of them. Still, building a small prediction tool can help a student learn how data, a machine-learning model, and a web application fit together. This project explores that process by using study hours, previous marks, and attendance to estimate final marks.

The goal is not to judge students or replace a teacher's understanding of a learner. It is to demonstrate a basic regression workflow: prepare a dataset, train a model, accept inputs through a web page, and return a prediction through an API.

## 2. Objectives

The project has four practical objectives:

1. Train a linear regression model from a CSV file.
2. Build a small web interface for entering three numeric values.
3. Validate input and return an understandable prediction.
4. Evaluate the model with a repeatable method and discuss its limitations.

## 3. Materials and methods

### 3.1 Dataset

The repository includes `students.csv`, containing 15 records and four numeric columns: `study_hours`, `previous_marks`, `attendance`, and `final_marks`. The first three columns are the model inputs; `final_marks` is the value the model learns to estimate. The dataset does not include names.

The source and collection method for these records are not documented in the project. For that reason, this paper treats them as demonstration data and does not claim that they represent a real student population.

### 3.2 Model

The training script uses scikit-learn's `LinearRegression`. In general, a linear regression model estimates an output as a weighted sum of its inputs [1]. Fitted on all 15 included rows, this project produces the following approximate equation:

```text
predicted marks = 9.223
                + 2.981 * study hours
                + 0.718 * previous marks
                + 0.017 * attendance
```

These coefficients describe the fitted model for this dataset; they do not show that changing any one factor will cause a particular change in a student's marks. The web application limits the displayed prediction to the range 0 to 100 and assigns a simple performance label after prediction.

### 3.3 Web application

The application is written in Python with Flask. The browser sends the three numeric inputs to the `/predict` endpoint. The server checks that each value is present, finite, and within its expected range before passing it to the model. The student's name is used only for display in the browser and is not included in the prediction request.

### 3.4 Evaluation

Because there are only 15 rows, this project uses leave-one-out cross-validation (LOOCV): each row is held out once, while the model is trained on the remaining rows. Cross-validation is a useful way to make more use of a small dataset, but it does not replace evaluation on a larger, independent dataset [2].

The main model is compared with a simple baseline. For each held-out row, the baseline predicts the average final mark in the other rows. The reported metrics are mean absolute error (MAE), root mean squared error (RMSE), and R-squared (R2), calculated across all held-out predictions. Results can be reproduced by running:

```powershell
python evaluate_model.py
```

## 4. Results

| Model | LOOCV MAE (marks) | LOOCV RMSE (marks) | LOOCV R2 |
|---|---:|---:|---:|
| Linear regression | 0.640 | 0.857 | 0.998 |
| Mean baseline | 16.648 | 19.563 | -0.148 |

On the included records, linear regression has lower prediction errors than the mean baseline. This is a result for this particular, very small dataset; it should not be presented as a verified accuracy estimate for students outside it.

## 5. Discussion

Building the application showed how a trained model can be connected to an interface that a person can use. Input checks are important because an empty, non-numeric, or out-of-range value should not be treated as a meaningful prediction. The baseline comparison also gives the model results context: a prediction should be compared with a simple alternative, not judged by a score in isolation.

The very low cross-validation errors need careful interpretation. With just 15 records and no documented data source, the dataset may not capture the variation found in real classrooms. The scores may reflect the pattern in these rows rather than reliable performance on new students. The model also uses only three factors; health, learning environment, teaching quality, access to resources, and many other circumstances are not represented. A coefficient is not proof of cause and effect.

## 6. Limitations and responsible use

- The dataset has only 15 records, and its provenance is unknown.
- There is no independent, larger test dataset.
- The features cannot represent the full circumstances of a student.
- The model is a simple linear model and may not fit other data.
- The prediction and performance label are demonstrations, not official grades.
- A prediction should not be used to make high-stakes decisions about a student.

A more responsible follow-up would use a larger dataset collected with permission, remove direct identifiers, document how the data was obtained, and test the model on data that was not used for training or model selection. Students and instructors should be told what the prediction can and cannot say.

## 7. Conclusion

This mini-project connects a CSV dataset, a linear regression model, a Flask API, and a browser interface in one small application. On the included 15 records, leave-one-out cross-validation produced lower errors than a mean-prediction baseline. The result is useful as a programming and machine-learning exercise, but the dataset is too small and undocumented to support claims about real-world student performance. The main next step is not a more complicated model; it is obtaining appropriate, well-documented data and testing the idea responsibly.

## References

1. Scikit-learn developers. “Linear Models.” *Scikit-learn User Guide*. https://scikit-learn.org/stable/modules/linear_model.html
2. Scikit-learn developers. “Cross-validation: evaluating estimator performance.” *Scikit-learn User Guide*. https://scikit-learn.org/stable/modules/cross_validation.html
