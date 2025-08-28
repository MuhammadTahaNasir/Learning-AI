# Complete Machine Learning Roadmap

A comprehensive, structured learning path for mastering classical Machine Learning from scratch, covering Python, Math, NumPy, Pandas, Data Visualization, Data Preprocessing, Regression, Classification, Model Evaluation, Dimensionality Reduction, Ensemble Methods, and Unsupervised Clustering.

## 🎯 Overview

This repository contains a complete Machine Learning roadmap divided into **12 structured phases**, designed to take you from basic programming concepts to industry-ready ML algorithms and system design. 

- **⏱️ Target Timeline:** June 2025 to January 2026
- **🏆 Outcome:** Solid mathematical understanding and hands-on coding expertise in classical ML algorithms.

---

## 📚 Learning Phases & Progress

### 🐍 [Phase 1: Python Fundamentals](PHASE_01_Python_Fundamentals/)
**Status**: ✅ Completed (Skip if already strong, skim if rusty)
- **Topics**: Variables, data structures, conditional execution, loops, functions, file/exception handling, OOP (Inheritance, MRO, Polymorphism, Abstract methods).
- **Notebooks**: [13 Notebooks](PHASE_01_Python_Fundamentals/)

### 📊 [Phase 2: Math, Statistics & Probability](PHASE_02_Math_Stats_Probability/)
**Status**: 🚧 In Progress (Math foundation)
- **Topics**: ML introduction & life cycle, **Linear Algebra** (Vectors, Matrices, Eigenvalues/Eigenvectors), **Calculus** (Derivatives, Gradients, Optimization), Statistics (Mean/Median/Mode, Variance, Skewness, Kurtosis, Correlation/Covariance), Probability (Bayes Theorem, Distributions, Hypothesis Testing).
- **Projects**:
  - [Linear Algebra Operations](PHASE_02_Math_Stats_Probability/Projects/Linear_Algebra_Operations/): Custom vector and matrix operations.
- **Notebooks**: [37 Notebooks](PHASE_02_Math_Stats_Probability/)

### 🔢 [Phase 3: NumPy](PHASE_03_NumPy/)
**Status**: ✅ Completed
- **Topics**: Array creation, attributes, reshape, indexing/slicing, concatenating/splitting, broadcasting, universal array functions.
- **Notebooks**: [10 Notebooks](PHASE_03_NumPy/)

### 🐼 [Phase 4: Pandas & Data Loading](PHASE_04_Pandas_Data_Loading/)
**Status**: ✅ Completed
- **Topics**: Series & DataFrames, selection/indexing, missing data handling, merge/join/concat, GroupBy, discretization/binning, APIs & Web Scraping, EDA.
- **Notebooks**: [12 Notebooks](PHASE_04_Pandas_Data_Loading/)

### 📈 [Phase 5: Data Visualization](PHASE_05_Data_Visualization/)
**Status**: 🚧 In Progress (Visualization & EDA)
- **Topics**: Matplotlib, Seaborn (Distribution, Categorical, and Matrix plots), Pandas Profiling, Univariate/Bivariate/Multivariate EDA.
- **Projects**:
  - [ThinkBoard Analytics Dashboard](PHASE_05_Data_Visualization/Projects/ThinkBoard/): Full data analytics dashboard deployed on Railway.
- **Notebooks**: [8 Notebooks](PHASE_05_Data_Visualization/)

### 🧹 [Phase 6: Data Preprocessing & Feature Engineering](PHASE_06_Data_Preprocessing_Feature_Engineering/)
**Status**: 📋 Planned
- **Topics**: Missing data (CCA, MICE), outlier detection, feature scaling (Standardization, MinMax), encoding (Label, Ordinal, OHE), Pipelines & Column Transformers, Power transforms, Feature Selection/Extraction, Curse of Dimensionality.
- **Notebooks**: [27 Notebooks](PHASE_06_Data_Preprocessing_Feature_Engineering/)

### 📉 [Phase 7: Regression Algorithms](PHASE_07_Regression_Algorithms/)
**Status**: 🚧 In Progress
- **Topics**: Simple & Multiple Linear Regression math, Least Squares, regression metrics (MSE, MAE, R²), Gradient Descent (Batch, SGD, Mini-Batch) implementation, Polynomial Regression, Bias-Variance Tradeoff, Ridge/Lasso/ElasticNet, Locally Weighted Regression, KNN Regression, Decision Trees.
- **Projects**:
  - [Gradient Descent Simulation](PHASE_07_Regression_Algorithms/Projects/Gradient_Descent_Simulation/): Interactive visualization of optimization.
- **Notebooks**: [28 Notebooks](PHASE_07_Regression_Algorithms/)

### 🎯 [Phase 8: Classification Algorithms](PHASE_08_Classification_Algorithms/)
**Status**: 🚧 In Progress
- **Topics**: Logistic Regression math & Perceptron, Softmax Regression, evaluation metrics (Confusion Matrix, Precision/Recall, F1, ROC-AUC), Imbalanced data, Naive Bayes variants, SVM math & Kernels, Decision Trees (ID3, CART), KNN.
- **Projects**:
  - [Titanic Survival Predictor](PHASE_08_Classification_Algorithms/Projects/Titanic_Survival_Predictor/): Classic binary classification pipeline.
- **Notebooks**: [41 Notebooks](PHASE_08_Classification_Algorithms/)

### ✅ [Phase 9: Model Evaluation & Validation](PHASE_09_Model_Evaluation_Validation/)
**Status**: 📋 Planned
- **Topics**: Cross-validation (K-Fold, LOOCV), learning theory, hyperparameter tuning (Optuna), SMOTE, error analysis, debugging ML models.
- **Notebooks**: [17 Notebooks](PHASE_09_Model_Evaluation_Validation/)

### 📐 [Phase 10: Dimensionality Reduction](PHASE_10_Dimensionality_Reduction/)
**Status**: 📋 Planned
- **Topics**: PCA (Geometric intuition, mathematical derivation, code), Stanford CS229 PCA + ICA, LDA, Feature Importance.
- **Notebooks**: [7 Notebooks](PHASE_10_Dimensionality_Reduction/)

### 🌲 [Phase 11: Ensemble Methods](PHASE_11_Ensemble_Methods/)
**Status**: 📋 Planned
- **Topics**: Voting Classifiers/Regressors, Bagging & Random Forests (OOB Score, Feature Importance), Boosting (AdaBoost, Gradient Boosting, XGBoost), Stacking & Blending.
- **Notebooks**: [18 Notebooks](PHASE_11_Ensemble_Methods/)

### 🔵 [Phase 12: Unsupervised Learning (Clustering)](PHASE_12_Unsupervised_Learning_Clustering/)
**Status**: 📋 Planned
- **Topics**: K-Means & K-Means++, Elbow Method, Hierarchical Clustering (Agglomerative, Divisive, Linkage methods), DBSCAN, K-Medoids, EM Algorithm, Recommendation Systems.
- **Notebooks**: [13 Notebooks](PHASE_12_Unsupervised_Learning_Clustering/)

---

## 🛠️ Technologies Used

- **Programming:** Python
- **Math Foundations:** Linear Algebra, Calculus, Statistics, Probability
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn, Optuna
- **Web App / Deploys:** Streamlit, Flask, Docker
- **Environment:** Jupyter Notebooks (`.ipynb`)

---

## 📁 Repository Structure

```
Learning-AI/
├── PHASE_01_Python_Fundamentals/
│   ├── 01_values_expressions_statements.ipynb
│   └── ...
├── PHASE_02_Math_Stats_Probability/
│   ├── Projects/Linear_Algebra_Operations/
│   ├── 01_intro_to_ml_history.ipynb
│   └── ...
├── PHASE_03_NumPy/
├── PHASE_04_Pandas_Data_Loading/
├── PHASE_05_Data_Visualization/
│   ├── Projects/ThinkBoard/
│   └── ...
├── PHASE_06_Data_Preprocessing_Feature_Engineering/
├── PHASE_07_Regression_Algorithms/
│   ├── Projects/Gradient_Descent_Simulation/
│   └── ...
├── PHASE_08_Classification_Algorithms/
│   ├── Projects/Titanic_Survival_Predictor/
│   └── ...
├── PHASE_09_Model_Evaluation_Validation/
├── PHASE_10_Dimensionality_Reduction/
├── PHASE_11_Ensemble_Methods/
├── PHASE_12_Unsupervised_Learning_Clustering/
├── scripts/
│   └── generate_roadmap.py
└── README.md
```

---

## 🚀 Getting Started

1. **Clone the Repo:** Clone this to your local environment.
2. **Review Python Basics (Phase 1):** Skim if you are rusty, skip if you are confident.
3. **Work through Jupyter Notebooks:** Open the relevant `.ipynb` file in each phase, study the resources linked inside, write notes, and complete the exercise cells.
4. **Build Projects:** Ensure you complete the key projects marked in each phase to consolidate your learning.

---

## 📄 License

This project is licensed under the MIT License, see the [LICENSE](LICENSE) file for details.
