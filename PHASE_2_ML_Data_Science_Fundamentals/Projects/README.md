# 🚀 Phase 2: Machine Learning Projects

A comprehensive collection of machine learning projects covering supervised learning, unsupervised learning, and ensemble methods. Each project demonstrates real-world applications with proper evaluation metrics and deployment strategies.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Table of Contents

- [Overview](#overview)
- [Mini Projects](#mini-projects)
- [Main Projects](#main-projects)
- [Installation](#installation)
- [Usage](#usage)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)

## 🎯 Overview

Phase 2 projects focus on mastering core machine learning concepts through hands-on implementation. Projects range from basic classification to advanced ensemble methods, each with comprehensive evaluation and real-world applications.

### Key Learning Objectives

- **📊 Data Preprocessing**: Handle missing values, feature engineering
- **🤖 Model Training**: Train and evaluate multiple ML algorithms
- **📈 Performance Metrics**: Use appropriate evaluation metrics
- **🔧 Hyperparameter Tuning**: Optimize model performance
- **🚀 Deployment**: Deploy models for real-world use

## 🎯 Mini Projects

### 1. Titanic Survival Predictor (Classification)

**📁 Location**: `Mini_Projects/Titanic_Survival_Predictor/`

**🎯 Objective**: Predict passenger survival on the Titanic using multiple classification algorithms.

**🔧 Technologies**: Logistic Regression, SVM, Random Forest, Scikit-learn

**📊 Key Features**:
- Feature engineering and data preprocessing
- Multiple classification algorithms
- Cross-validation and hyperparameter tuning
- Performance comparison with confusion matrices
- ROC curve analysis

**📈 Performance Metrics**:
- Accuracy: 85-90%
- Precision, Recall, F1-Score
- ROC AUC: 0.85+

**🚀 Quick Start**:
```bash
cd Mini_Projects/Titanic_Survival_Predictor/
python titanic_survival_predictor_fixed.ipynb
```

### 2. MNIST Digit Classifier (Classification)

**📁 Location**: `Mini_Projects/MNIST_Digit_Classifier/`

**🎯 Objective**: Build a high-accuracy digit classifier using the MNIST dataset.

**🔧 Technologies**: SVM, Neural Networks, Scikit-learn

**📊 Key Features**:
- Image preprocessing and normalization
- Support Vector Machine implementation
- Neural network with backpropagation
- Model comparison and evaluation
- Real-time digit prediction

**📈 Performance Metrics**:
- Accuracy: 95%+
- Training time optimization
- Memory-efficient implementation

**🚀 Quick Start**:
```bash
cd Mini_Projects/MNIST_Digit_Classifier/
python mnist_digit_classifier.ipynb
```

### 3. Iris Dataset Visualizer (Clustering)

**📁 Location**: `Mini_Projects/Iris_Dataset_Visualizer/`

**🎯 Objective**: Apply clustering algorithms to the Iris dataset and visualize results.

**🔧 Technologies**: K-Means, PCA, Seaborn, Matplotlib

**📊 Key Features**:
- Unsupervised learning with K-Means
- Dimensionality reduction with PCA
- Interactive visualizations
- Cluster analysis and evaluation
- Silhouette score analysis

**📈 Performance Metrics**:
- Silhouette Score: 0.7+
- Cluster visualization quality
- PCA explained variance ratio

**🚀 Quick Start**:
```bash
cd Mini_Projects/Iris_Dataset_Visualizer/
python iris_visualizer.ipynb
```

## 🏆 Main Projects

### 1. Loan Default Classifier (Classification)

**📁 Location**: `Main_Projects/Loan_Default_Classifier/`

**🎯 Objective**: Build a robust classifier to predict loan defaults using advanced ensemble methods.

**🔧 Technologies**: XGBoost, LightGBM, Optuna, Scikit-learn

**📊 Key Features**:
- Advanced feature engineering
- Ensemble methods (XGBoost, LightGBM)
- Hyperparameter optimization with Optuna
- Class imbalance handling
- Model interpretability with SHAP
- Production-ready deployment

**📈 Performance Metrics**:
- ROC AUC: 0.90+
- Precision: 85%+
- Recall: 80%+
- Business metrics (profit/loss analysis)

**🚀 Quick Start**:
```bash
cd Main_Projects/Loan_Default_Classifier/
python loan_default_classifier.ipynb
```

### 2. House Price Predictor (Regression)

**📁 Location**: `Main_Projects/House_Price_Predictor/`

**🎯 Objective**: Develop a regression model to predict house prices with high accuracy.

**🔧 Technologies**: Linear Regression, Random Forest, XGBoost, Feature Engineering

**📊 Key Features**:
- Comprehensive feature engineering
- Multiple regression algorithms
- Cross-validation and model selection
- Feature importance analysis
- Price prediction API
- Web interface with Streamlit

**📈 Performance Metrics**:
- R² Score: 0.85+
- RMSE: < $50,000
- MAE: < $30,000
- Cross-validation stability

**🚀 Quick Start**:
```bash
cd Main_Projects/House_Price_Predictor/
python house_price_predictor.ipynb
```

### 3. Customer Segmentation (Unsupervised)

**📁 Location**: `Main_Projects/Customer_Segmentation/`

**🎯 Objective**: Segment customers based on purchasing behavior using clustering algorithms.

**🔧 Technologies**: K-Means, DBSCAN, PCA, Visualization

**📊 Key Features**:
- Customer behavior analysis
- Multiple clustering algorithms
- Dimensionality reduction
- Segment profiling and analysis
- Interactive dashboard
- Business insights generation

**📈 Performance Metrics**:
- Silhouette Score: 0.6+
- Cluster stability
- Business value metrics
- Segment interpretability

**🚀 Quick Start**:
```bash
cd Main_Projects/Customer_Segmentation/
python customer_segmentation.ipynb
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd PHASE_2_ML_Data_Science_Fundamentals/Projects
```

### Step 2: Install Dependencies

```bash
# Install core ML libraries
pip install scikit-learn xgboost lightgbm optuna

# Install visualization libraries
pip install matplotlib seaborn plotly

# Install web frameworks
pip install streamlit fastapi uvicorn

# Install utilities
pip install pandas numpy jupyter
```

### Step 3: Verify Installation

```python
python -c "import sklearn, xgboost, lightgbm; print('✅ ML libraries ready!')"
```

## 📖 Usage

### Running Mini Projects

```bash
# Titanic Survival Predictor
cd Mini_Projects/Titanic_Survival_Predictor/
jupyter notebook titanic_survival_predictor_fixed.ipynb

# MNIST Digit Classifier
cd Mini_Projects/MNIST_Digit_Classifier/
jupyter notebook mnist_digit_classifier.ipynb

# Iris Dataset Visualizer
cd Mini_Projects/Iris_Dataset_Visualizer/
jupyter notebook iris_visualizer.ipynb
```

### Running Main Projects

```bash
# Loan Default Classifier
cd Main_Projects/Loan_Default_Classifier/
jupyter notebook loan_default_classifier.ipynb

# House Price Predictor
cd Main_Projects/House_Price_Predictor/
jupyter notebook house_price_predictor.ipynb

# Customer Segmentation
cd Main_Projects/Customer_Segmentation/
jupyter notebook customer_segmentation.ipynb
```

### Project Structure

```
Projects/
├── Mini_Projects/
│   ├── Titanic_Survival_Predictor/
│   │   ├── titanic_survival_predictor_fixed.ipynb
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── MNIST_Digit_Classifier/
│   │   ├── mnist_digit_classifier.ipynb
│   │   ├── README.md
│   │   └── requirements.txt
│   └── Iris_Dataset_Visualizer/
│       ├── iris_visualizer.ipynb
│       ├── README.md
│       └── requirements.txt
├── Main_Projects/
│   ├── Loan_Default_Classifier/
│   │   ├── loan_default_classifier.ipynb
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── House_Price_Predictor/
│   │   ├── house_price_predictor.ipynb
│   │   ├── README.md
│   │   └── requirements.txt
│   └── Customer_Segmentation/
│       ├── customer_segmentation.ipynb
│       ├── README.md
│       └── requirements.txt
└── README.md
```

## 📊 Project Evaluation

### Mini Projects Evaluation

| Project | Accuracy | Key Learning | Difficulty |
|---------|----------|--------------|------------|
| Titanic Predictor | 85-90% | Classification, Feature Engineering | ⭐⭐ |
| MNIST Classifier | 95%+ | Image Classification, SVM | ⭐⭐⭐ |
| Iris Visualizer | 0.7+ Silhouette | Clustering, Visualization | ⭐ |

### Main Projects Evaluation

| Project | Performance | Key Learning | Difficulty |
|---------|-------------|--------------|------------|
| Loan Default | 90%+ AUC | Ensemble Methods, Business ML | ⭐⭐⭐⭐ |
| House Price | 85%+ R² | Regression, Feature Engineering | ⭐⭐⭐ |
| Customer Segmentation | 0.6+ Silhouette | Clustering, Business Analytics | ⭐⭐⭐ |

## 🎓 Learning Outcomes

### Technical Skills

**Machine Learning Fundamentals**:
- Supervised vs Unsupervised Learning
- Classification and Regression
- Model Evaluation Metrics
- Cross-validation Techniques

**Data Preprocessing**:
- Feature Engineering
- Handling Missing Values
- Data Normalization
- Feature Selection

**Advanced Techniques**:
- Ensemble Methods (XGBoost, LightGBM)
- Hyperparameter Tuning (Optuna)
- Model Interpretability (SHAP)
- Deployment Strategies

### Tools & Technologies

**Core Libraries**:
- **Scikit-learn**: Machine learning algorithms
- **XGBoost**: Gradient boosting
- **LightGBM**: Light gradient boosting
- **Optuna**: Hyperparameter optimization

**Visualization**:
- **Matplotlib**: Basic plotting
- **Seaborn**: Statistical visualization
- **Plotly**: Interactive plots

**Deployment**:
- **Jupyter**: Interactive notebooks
- **Streamlit**: Web applications
- **FastAPI**: REST APIs

## 🚀 Advanced Features

### Model Deployment

```python
# Example: Deploy model as API
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load('model.pkl')

@app.post("/predict")
async def predict(data: dict):
    prediction = model.predict([data['features']])
    return {"prediction": prediction[0]}
```

### Hyperparameter Optimization

```python
# Example: Optuna optimization
import optuna

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 100, 1000),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3)
    }
    model = XGBClassifier(**params)
    return cross_val_score(model, X, y, cv=5).mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)
```

### Model Interpretability

```python
# Example: SHAP analysis
import shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

## 🌍 Real-world Applications

### Mini Projects Applications

- **Titanic Predictor**: Risk assessment, survival prediction
- **MNIST Classifier**: OCR, digit recognition systems
- **Iris Visualizer**: Customer segmentation, pattern recognition

### Main Projects Applications

- **Loan Default**: Banking, credit risk assessment
- **House Price**: Real estate, property valuation
- **Customer Segmentation**: Marketing, personalized campaigns

## 🤝 Contributing

We welcome contributions to improve the projects!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 coding standards
- Add comprehensive documentation
- Include unit tests for new features
- Update README files accordingly

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Scikit-learn**: For the machine learning framework
- **XGBoost**: For gradient boosting implementation
- **Optuna**: For hyperparameter optimization
- **Jupyter**: For interactive development environment

---

**🎯 Goal**: Master machine learning fundamentals through hands-on projects

**⏱️ Timeline**: 5 weeks for complete implementation

**🏆 Outcome**: Production-ready ML models with deployment strategies 