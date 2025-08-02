# AI Engineering Roadmap: Phase 2 - ML & Data Science Fundamentals 

This roadmap builds on Phase 1, focusing on machine learning (ML) and data science fundamentals, covering supervised, unsupervised, and reinforcement learning, model evaluation, ensemble methods, and practical projects. 

## Phase 2: ML & Data Science Fundamentals

### Objective
Master core machine learning concepts, build and evaluate ML models using scikit-learn, XGBoost, and LightGBM, and complete real-world ML projects. Achieve a certification in machine learning.

### Topics

#### Machine Learning Core Concepts
1. **Learning Paradigms**
   - Supervised Learning: Classification, Regression
   - Unsupervised Learning: Clustering, Dimensionality Reduction
   - Semi-Supervised Learning
   - Reinforcement Learning: Agents, Rewards, Q-Learning, Policy Gradients
2. **Key Concepts**
   - Overfitting and Underfitting
   - Bias-Variance Tradeoff
   - Feature Engineering
   - Train-Test Split
   - K-Fold Cross-Validation (including Stratified K-Fold)
   - Regularization (L1, L2)
   - Variance Inflation Factor (VIF)
   - Hyperparameter Tuning (GridSearchCV, Optuna)
   - Handling Class Imbalance
3. **Model Evaluation Metrics**
   - Accuracy, Precision, Recall, F1 Score
   - Confusion Matrix
   - ROC Curve & AUC
   - Cost-Benefit Analysis Using ROC
   - Log Loss (for classification)
4. **AI Project Lifecycle (10 Stages)**
   - Requirements and Scope of Work (SOW)
   - Data Collection
   - Data Cleaning & Exploratory Data Analysis (EDA)
   - Feature Engineering
   - Model Selection & Training
   - Model Fine-Tuning
   - Model Deployment
   - Monitoring and Feedback (ML Ops)

#### Models to Master
1. **Supervised Learning**
   - **Regression**
     - Simple Linear Regression
     - Multiple Linear Regression
     - Polynomial Regression
     - Cost Function: Mean Squared Error (MSE)
   - **Classification**
     - Logistic Regression (Binary and Multiclass)
     - Support Vector Machines (SVM)
     - K-Nearest Neighbors (KNN)
     - Naive Bayes
     - Decision Trees
     - Random Forests
2. **Unsupervised Learning**
   - Clustering: K-Means, DBSCAN
   - Dimensionality Reduction: PCA, t-SNE
3. **Ensemble Methods**
   - Bagging: Random Forests
   - Boosting: AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost
   - Majority Voting, Average, Weighted Average
4. **Optimization**
   - Gradient Descent
   - Cost Functions (MSE, Log Loss)
   - Derivatives and Partial Derivatives
   - Chain Rule

#### Data Preprocessing
- One-Hot Encoding
- Scaling (Standardization, Normalization)
- Handling Class Imbalance
- Sklearn Pipeline for streamlined preprocessing

#### Tools & Libraries
- scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Optuna (for hyperparameter tuning)
- mlxtend
- Seaborn (for visualization)

### Mini-Projects
1. **Titanic Survival Predictor (Classification)**
   - Use the Titanic dataset to predict survival using logistic regression, SVM, and random forests.
   - Apply feature engineering, handle missing values, and evaluate using accuracy, precision, recall, and F1 score.
2. **MNIST Digit Classifier (Classification)**
   - Build an SVM-based classifier for the MNIST dataset.
   - Perform data preprocessing (scaling) and evaluate using confusion matrix and ROC AUC.
3. **Iris Dataset Visualizer (Clustering)**
   - Apply K-Means and PCA to the Iris dataset.
   - Visualize clusters using Seaborn scatter plots.

### Main Projects
1. **Loan Default Classifier (Classification)**
   - Build a classifier to predict loan defaults using XGBoost or LightGBM.
   - Perform feature engineering, handle class imbalance, and tune hyperparameters with Optuna.
   - Evaluate using ROC AUC and confusion matrix.
2. **House Price Predictor (Regression)**
   - Develop a regression model (e.g., linear regression, random forests) to predict house prices.
   - Use feature engineering (e.g., one-hot encoding) and evaluate with MSE and R².
3. **Customer Segmentation (Unsupervised K-Means)**
   - Apply K-Means clustering to segment customers based on purchasing behavior.
   - Visualize results using PCA and Seaborn.

### Certification
- **Option 1**: Supervised Machine Learning: Regression and Classification (DeepLearning.AI on Coursera)
- **Option 2**: Machine Learning Specialization by Andrew Ng (Coursera)
  - Estimated completion: 2–3 months (10–15 hours/week).

### Outputs
- **GitHub Repository**:
  - Python scripts for all mini-projects and main projects.
  - LeetCode solutions (25–30 DSA patterns: Trees, Arrays, Hashing, Sliding Window).
  - Documentation for ML models and project workflows.
- **Jupyter Notebooks**:
  - EDA, model training, and evaluation for each project.
  - Visualizations using Seaborn and Matplotlib.
- **Certification**:
  - Completion of either DeepLearning.AI or Andrew Ng’s Machine Learning Specialization.

### Timeline
- **Week 6**:
  - Core ML concepts: Supervised, unsupervised, reinforcement learning
  - Models: Linear regression, logistic regression, KNN, Naive Bayes
  - Mini-project: Titanic survival predictor
  - Start certification (DeepLearning.AI or Andrew Ng)
- **Week 7**:
  - Models: Decision trees, random forests, SVM
  - Preprocessing: Scaling, one-hot encoding, Sklearn Pipeline
  - Mini-project: MNIST digit classifier
- **Week 8**:
  - Unsupervised learning: K-Means, DBSCAN, PCA
  - Mini-project: Iris dataset visualizer
  - Continue certification
- **Week 9**:
  - Ensemble methods: XGBoost, LightGBM, AdaBoost
  - Hyperparameter tuning with Optuna
  - Project: Loan default classifier
- **Week 10**:
  - Project: House price predictor
  - Advanced evaluation: ROC, cost-benefit analysis
  - Complete certification
- **Week 11**:
  - Project: Customer segmentation
  - Finalize GitHub repository with all projects and LeetCode solutions
  - Review ML Ops and deployment basics

### Learning Resources
- **Machine Learning**:
  - “Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow” by Aurélien Géron
  - StatQuest YouTube channel (Joshua Starmer) for ML concepts
  - Coursera: DeepLearning.AI or Andrew Ng’s Machine Learning Specialization
- **Programming**:
  - LeetCode for DSA practice
  - scikit-learn, XGBoost, and LightGBM documentation
- **Tools**:
  - Jupyter Notebook for model development and EDA
  - Git/GitHub for version control
  - PyCharm for coding and debugging

### Notes
- Continue practicing DSA (25–30 patterns) alongside ML to strengthen problem-solving skills.
- Use Kanban (e.g., Trello) to manage project tasks and track progress.
- Ensure all projects include proper EDA, feature engineering, and model evaluation.