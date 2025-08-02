# Titanic Survival Predictor

## Overview
This mini-project implements classification models to predict survival on the Titanic dataset. It demonstrates fundamental machine learning concepts including data preprocessing, feature engineering, model training, and evaluation.

## Features
- **Multiple ML Algorithms**: Logistic Regression, SVM, Random Forest
- **Comprehensive EDA**: Data exploration with visualizations
- **Feature Engineering**: Advanced feature creation and preprocessing
- **Model Evaluation**: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
- **Cross-validation**: Robust model validation
- **Feature Importance**: Analysis using Random Forest

## Project Structure
```
Titanic_Survival_Predictor/
├── titanic_survival_predictor.ipynb  # Interactive Jupyter notebook
├── requirements.txt                   # Dependencies
└── README.md                         # This file
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
jupyter notebook titanic_survival_predictor.ipynb
```

## Learning Objectives
- **Data Preprocessing**: Handle missing values, encode categorical variables
- **Feature Engineering**: Create new features from existing data
- **Model Training**: Train multiple classification algorithms
- **Model Evaluation**: Use various metrics to assess performance
- **Cross-validation**: Ensure model robustness

## Expected Output
- Exploratory Data Analysis with visualizations
- Model training results with metrics
- Feature importance analysis
- Confusion matrices and classification reports

## Technologies Used
- **pandas**: Data manipulation
- **numpy**: Numerical operations
- **matplotlib/seaborn**: Data visualization
- **scikit-learn**: Machine learning algorithms
- **Jupyter Notebook**: Interactive development and analysis

## Notebook Sections
1. **Setup and Imports**: Library imports and configuration
2. **Data Loading**: Loading Titanic dataset from URL
3. **Exploratory Data Analysis**: Comprehensive data exploration and visualizations
4. **Data Preprocessing**: Missing value handling and data cleaning
5. **Feature Engineering**: Creating meaningful features (FamilySize, IsAlone, Title, HasCabin)
6. **Model Training**: Training multiple classification algorithms
7. **Model Evaluation**: Performance metrics and confusion matrices
8. **Feature Importance Analysis**: Understanding key factors affecting survival
9. **Summary**: Key insights and learning points

## Benefits of Notebook Approach
- **Interactive Analysis**: Step-by-step execution with immediate results
- **Rich Visualizations**: Inline plots and charts for better understanding
- **Documentation**: Code and explanations in one place
- **Reproducibility**: Easy to share and reproduce results
- **Learning**: Better for educational purposes with clear sections

## Dataset Information
The Titanic dataset contains:
- **891 passengers** with survival information
- **12 features** including passenger class, age, gender, fare, etc.
- **Binary target**: Survived (1) or Not Survived (0)
- **Historical data**: Real passenger data from the 1912 Titanic disaster
- **Missing values**: Some features have missing data requiring preprocessing 