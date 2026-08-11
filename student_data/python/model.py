# pip install pandas scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# ---------------------------------------------------------
# 1. Load student data
# ---------------------------------------------------------

df = pd.read_csv("student_performance_dataset.csv")

print(df.head())
print(df.columns)

# ---------------------------------------------------------
# 2. Keep only students with a part-time job
# ---------------------------------------------------------

df = df[df["part_time_job"] == "Yes"].copy()

# ---------------------------------------------------------
# 3. Create the new classification target
# ---------------------------------------------------------

def classify_grade(row):

    grade = row["final_grade"]

    if grade in ["A", "B"]:
        return "Class 1"

    elif grade in ["C", "D"]:
        return "Class 2"

    elif grade == "F":
        return "Class 3"

    else:
        return "Unknown"


df["student_class"] = df.apply(classify_grade, axis=1)

# Remove any unexpected grades
df = df[df["student_class"] != "Unknown"]

print("\nNew class distribution:")
print(df["student_class"].value_counts())

# ---------------------------------------------------------
# 4. Define features and target
# ---------------------------------------------------------

features = [
    "gender",
    "previous_grade",
    "extracurricular_activities"
]

target = "student_class"

X = df[features]
y = df[target]

# ---------------------------------------------------------
# 5. Split data
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ---------------------------------------------------------
# 6. Define numeric and categorical features
# ---------------------------------------------------------

numeric_features = [
    "previous_grade"
]

categorical_features = [
    "gender",
    "extracurricular_activities"
]

# ---------------------------------------------------------
# 7. Preprocessing
# ---------------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", StandardScaler(), numeric_features),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)

# ---------------------------------------------------------
# 8. Random Forest classifier
# ---------------------------------------------------------

classifier = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", classifier)
])

# ---------------------------------------------------------
# 9. Train model
# ---------------------------------------------------------

model.fit(X_train, y_train)

# ---------------------------------------------------------
# 10. Make predictions
# ---------------------------------------------------------

predictions = model.predict(X_test)

# ---------------------------------------------------------
# 11. Evaluate model
# ---------------------------------------------------------

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("Accuracy:", accuracy_score(y_test, predictions))

# Create separate dataframes
class_1 = df[df["student_class"] == "Class 1"]
class_2 = df[df["student_class"] == "Class 2"]
class_3 = df[df["student_class"] == "Class 3"]

# Export as separate CSV files
class_1.to_csv("class_1.csv", index=False)
class_2.to_csv("class_2.csv", index=False)
class_3.to_csv("class_3.csv", index=False)

print("Files exported successfully!")
print("Class 1:", len(class_1), "students")
print("Class 2:", len(class_2), "students")
print("Class 3:", len(class_3), "students")