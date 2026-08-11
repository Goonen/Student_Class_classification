# Student_Class_classification
Taken 1000 data of students. I have classified them based on grades to recommend them open class, regular class of their grade preference based on if they do part time job or not and participate in extracurricular activities or not.

## Project Overview
This project focuses on analyzing student academic and extracurricular information to develop a simple Student Class Recommendation System.
We created Jupyter Notebook code to extract three actual files and Python code to develop ML model using 20% of given data and analyze the output on 80% of the 
remaining data and extract three file too. Then compared both to find accuracy of our model. So, basically combining both ML and data analysis in a project.

Using student-related data, I performed data cleaning, data filtering, feature selection, categorization, and rule-based classification to identify suitable class recommendations for different types of students.

The main objective of the project is to use students' academic performance, part-time job status, and extracurricular activities to recommend an appropriate class or learning level.

The project addresses the following key questions:

Which student information is most useful for class recommendation?
How can students be categorized based on their final grades?
How does having a part-time job affect class recommendations?
How can extracurricular activities be considered when recommending classes?
Can student performance and activities be used to recommend easier or more suitable subjects?
How can the recommendation process be separated into different categories for easier communication?
Technical Stack

Dataset: Student Dataset (CSV)

Programming Language: Python

Data Manipulation: Pandas

Data Analysis: Jupyter Notebook

Development Environment: Jupyter Notebook

## Data Analysis & Preparation

The raw student dataset initially contained a large number of fields. I first explored and sorted the data to determine which variables were relevant for the class recommendation process.

After examining the available information, the following variables were selected as the primary features:

student_id
gender
part_time_job
final_grade
extracurricular_activities
previous_grade

These variables were selected because they provide useful information about a student's academic performance, background, and activities outside regular classes.

The data preparation process included:

Examining the structure and data types of the dataset.
Identifying relevant columns.
Removing unnecessary information.
Checking and organizing student records.
Selecting the variables required for recommendation.
Creating a new student-performance category.
Grouping students according to academic performance and activities.
Preparing separate datasets for different class recommendations.
Student Performance Categorization

To make the recommendation process easier, a new variable called student_category was created based on the student's final_grade.

The grading categories were defined as follows:

Final Grade	Student Category
A	Good
B	Average
C	Average
D	Poor
F	Poor

This categorization converts individual letter grades into broader performance groups that can be used by the recommendation system.

# Machine Learning – Student Class Classification

As an extension of the rule-based classification performed in Jupyter Notebook, a Machine Learning model was developed using Python and Scikit-Learn.

The objective was to determine whether a Machine Learning model could classify students into different classes based on selected student characteristics.

The Machine Learning implementation provides a second approach to student classification and allows the results to be evaluated using standard classification metrics.

## Objective

The main objective of the Machine Learning component was to answer:

Can student information be used to automatically classify students into appropriate classes?

The model uses selected student characteristics as input features and predicts the student's recommended class.

The classification focuses specifically on students who have a part-time job.

## Student Class Definition

For the Machine Learning model, the original final grades were converted into three class categories.

Final Grade	Student Class
A, B	Class 1
C, D	Class 2
F	Class 3


Unexpected grades were removed before training the model.

This creates the target variable:

df["student_class"]
Feature Selection

After creating the target variable, three features were selected for Machine Learning:

features = [
    "gender",
    "previous_grade",
    "extracurricular_activities"
]

The target variable was:

target = "student_class"

Therefore, the model attempts to learn the relationship between:

Gender + Previous Grade + Extracurricular Activities → Student Class

Only students with a part-time job were included in this Machine Learning analysis.

## Train-Test Split

The dataset was divided into training and testing sets using an 80/20 split.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

This means:

80% of the data was used to train the model.
20% of the data was held out for testing.
random_state=42 was used to make the experiment reproducible.
stratify=y was used to maintain a similar class distribution in the training and testing datasets.

The test data was not used during model training. It was used to evaluate how well the trained model classified previously unseen records.


## Comparison Between Jupyter Analysis and Python Machine Learning

An important part of the project was comparing the results obtained from the original Jupyter Notebook analysis with the results produced by the Python Machine Learning implementation.

The Jupyter Notebook was primarily used for:

Data exploration
Data cleaning
Feature selection
Student categorization
Rule-based classification
Creating separate student groups

The Python Machine Learning implementation was used for:

Preparing the classification target
Splitting the data into training and testing sets
Preprocessing numerical and categorical features
Training a Random Forest classifier
Predicting student classes
Measuring classification accuracy
Generating a classification report
Exporting class-specific datasets

The outputs from both approaches were analyzed to determine whether the Machine Learning model produced classifications that were consistent with the original data-based classification.

This comparison helped verify the behavior of the classification process and provided an additional evaluation of the student-class recommendation approach.

## Conclusion

This project demonstrates a complete data-analysis and Machine Learning workflow for a Student Class Recommendation System.

The project began with data exploration and cleaning in Jupyter Notebook. Relevant student information was selected, including gender, part-time job status, final grade, extracurricular activities, and previous grade.

Students were then categorized based on their academic performance and additional conditions such as part-time employment and extracurricular activities.

As an extension, a Random Forest classification model was developed using Python and Scikit-Learn. The data was divided into 80% training data and 20% testing data, with appropriate preprocessing applied to numerical and categorical features.

The model's predictions were evaluated using accuracy and a classification report. The Machine Learning results were then compared with the original Jupyter Notebook analysis.

Finally, students were separated into individual class datasets that could be used for further class recommendation and communication.

The overall project workflow is:

Data Cleaning → Feature Selection → Categorization → Rule-Based Classification → Machine Learning → Prediction → Evaluation → Class Recommendation

## Future Improvements

The project can be further improved by:

Using additional student features.
Including attendance and study hours.
Including subject-specific performance.
Considering student interests and preferred subjects.
Using previous academic records more extensively.
Applying cross-validation.
Performing hyperparameter tuning for Random Forest.
Comparing Random Forest with Decision Tree, Logistic Regression, SVM, and other classifiers.
Using confusion matrices to analyze classification errors.
Handling class imbalance if present.
Evaluating the model using MAE, RMSE, precision, recall, and F1-score where appropriate.
Building an interactive Power BI or Tableau dashboard.
Developing a web application for real-time class recommendations.
Allowing students to receive personalized class recommendations.
Evaluating whether recommended classes actually improve subsequent student performance.
