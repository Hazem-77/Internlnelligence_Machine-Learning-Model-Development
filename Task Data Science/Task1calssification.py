# -*- coding: utf-8 -*-
"""Diabetes calssification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17fMVQ436UVK0E4QpXoQgVeRCaqNAhWUG

Import Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix, classification_report, roc_curve, auc, precision_recall_curve

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
import joblib
plt.style.use('fivethirtyeight')

import warnings
warnings.filterwarnings('ignore')

"""# Business Problem Definition:
# The goal of this model is to predict patients' risk of developing diabetes based on their medical data,
# which helps doctors diagnose diabetes early and make appropriate treatment decisions.
"""



"""# Import & Explore The **DATA**"""

df = pd.read_csv("C:/Users/HP/Task Data Science/diabetes.csv")


df.head()

df.info()

df.describe()

missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

"""# *Analysis*"""

# Statistical distribution plot
plt.figure(figsize=(12, 6))
df.hist(bins=20, figsize=(12, 8), color='skyblue', edgecolor='black')
plt.suptitle("Distribution of Features", fontsize=14)
plt.show()

#Boxplot to detect outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Boxplot of Features")
plt.show()

#  Feature correlation map
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

sns.countplot(x='Outcome',data=df,palette=['g','r'])

"""Create Model"""

x= df.drop('Outcome',axis=1)
y= df['Outcome']

# Improved features by Scaling
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

#  Improved feature selection
selector = SelectKBest(score_func=f_classif, k=5)  # Choose the top 5 features
x_selected = selector.fit_transform(x_scaled, y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)

# Try several models
models = {
"Logistic Regression": LogisticRegression(),
"Random Forest": RandomForestClassifier(n_estimators=100),
"XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    }
results = {}
plt.figure(figsize=(10, 5))

for name, model in models.items():
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        y_prob = model.predict_proba(x_test)[:, 1]

results[name] = {
            "Accuracy": accuracy_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "F1 Score": f1_score(y_test, y_pred),
            "Confusion Matrix": confusion_matrix(y_test, y_pred),
            "Classification Report": classification_report(y_test, y_pred)
        }

# 📌  Draw ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_pred)
plt.plot(fpr, tpr, label=f"{name} (AUC = {auc(fpr, tpr):.2f}")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve for Models")
plt.legend()
plt.show()

# Print the results
for model_name, metrics in results.items():
    print(f"\n{name}:")
    print(f"Accuarcy: {metrics['Accuracy']:.4f}")
    print(f" Recall: {metrics['Recall']:.4f}")
    print(f" F1 Score: {metrics['F1 Score']:.4f}")
    print(metrics["Confusion Matrix"])
    print(metrics["Classification Report"])

# Choose the best model
best_model_name = max(results, key=lambda x: results[x]['F1 Score'])
best_model = models[best_model_name]
print(f" Best Model: {best_model_name} With performance{results[best_model_name]}")

# Save the best model
joblib.dump(best_model, "best_model.pkl")
print(" The form has been saved in'best_model.pkl'")

print(" Data analysis, feature optimization, and selection of the best model were completed successfully!")

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("best_model.pkl")

app = FastAPI()

class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.get("/")
def home():
    return {"message": " Diabetes Prediction API is Running!"}

@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    input_data = np.array([[
        data.Pregnancies, data.Glucose, data.BloodPressure, data.SkinThickness,
        data.Insulin, data.BMI, data.DiabetesPedigreeFunction, data.Age
    ]])

    prediction = model.predict(input_data)[0]

    return {"prediction": "Diabetic" if prediction == 1 else "Not Diabetic"}





