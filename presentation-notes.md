# Presentation Notes

Use this as a starting point, then change the wording so it sounds like you.
Be ready to explain each part in your own words.

## Short presentation

Good morning. My mini-project is a student performance prediction website. I
made it to understand how a small machine-learning model can work together with
a web application.

The program takes three inputs: study hours, previous marks, and attendance.
The model is linear regression, trained on the 15 rows in the included CSV
file. The website sends the numeric inputs to a Flask API, which checks them,
gets a prediction, and returns a performance label.

I also evaluated the model using leave-one-out cross-validation and compared
it with a simple baseline that predicts the average mark. On this dataset, the
model's mean absolute error was about 0.64 marks, compared with about 16.65
for the baseline. These results apply only to the small dataset in my project.
Its source is not documented, so I cannot claim that the model is reliable for
real students.

The main thing I learned is that a working prediction is not automatically a
trustworthy one. A larger, properly sourced dataset and an independent test
would be needed before making stronger claims. Thank you.

## Questions you may be asked

**Why did you use linear regression?**  
It is a straightforward model for predicting a numeric value and is suitable
for demonstrating the basic training and prediction workflow.

**What does MAE mean?**  
Mean absolute error is the average size of the difference between a predicted
mark and the actual mark, without considering whether the prediction was too
high or too low.

**Does this prove that study hours cause higher marks?**  
No. The project finds patterns in a small dataset. It does not establish
cause and effect.

**Can a teacher use this to decide a student's grade?**  
No. It is a learning prototype, not a validated grading tool, and it should
not be used for high-stakes decisions.

**What would you improve next?**  
I would first confirm the dataset's source and permission for use, gather more
appropriate data, and evaluate on a separate set of records.
