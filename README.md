# Student Performance Prediction

A simple college mini-project that predicts a student's final marks from study
hours, previous marks, and attendance using a trained scikit-learn linear
regression model.

## Requirements

- Python 3.10 or newer

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000> in a browser.

## Retrain the model

The training script reads `students.csv` and writes `student_model.pkl`:

```powershell
python train_model.py
```

The included CSV is the example training dataset. The prediction API accepts
study hours from 0 to 24 and previous marks and attendance from 0 to 100.

## Project report

See [research-paper.md](research-paper.md) for a course-project paper draft.
It includes a reproducible cross-validation comparison; run
`python evaluate_model.py` to verify the reported metrics.
For an IEEE conference-style LaTeX draft, see [research-paper-ieee.tex](research-paper-ieee.tex).
Replace all author placeholders and check the target conference's current
template, page limit, and submission rules before submitting.
For an oral presentation, see [presentation-notes.md](presentation-notes.md).
