# 🚀 Diabetes Prediction Model

## 📌 Project Overview
This project is a **Machine Learning model** developed to predict the risk of diabetes in patients based on their medical data. The model aims to assist doctors in early diagnosis and decision-making for appropriate treatments.

## 🔍 Business Problem Definition
Diabetes is a chronic disease affecting millions of people worldwide. Early detection can help in better management and treatment. The goal of this model is to predict whether a patient has diabetes based on input features such as glucose level, blood pressure, BMI, and other medical parameters.

## 📊 Dataset Information
- **Dataset Name**: PIMA Indians Diabetes Dataset
- **Source**: [Kaggle](https://www.kaggle.com/datasets)
- **Number of Samples**: 768
- **Features**:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
  - **Outcome (Target Variable - 0: No Diabetes, 1: Diabetes)**

## 🛠️ Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Scikit-learn** (Machine Learning models and evaluation)
- **XGBoost** (Boosting Algorithm)
- **Joblib** (Model Saving & Deployment)

## 📌 Model Training & Evaluation
The dataset was preprocessed, and multiple classification models were trained:
1. **Logistic Regression**
2. **Random Forest**
3. **XGBoost**

The models were evaluated using:
- **Accuracy**
- **Precision & Recall**
- **F1-Score**
- **ROC Curve**

### 🎯 Best Model: **XGBoost** (Highest F1-Score)
The best-performing model was selected and saved as `best_model.pkl`.

## 🚀 Deployment Plan (Next Steps)
The model can be deployed using:
- **Flask / FastAPI** for API development
- **Render / Hugging Face Spaces** for cloud deployment
- **AWS SageMaker** for enterprise-level deployment

## 📂 Project Structure
