import os
import shutil
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the roadmap data with clean names, no dashes, and no course resources
ROADMAP_DATA = [
    {
        "dir_name": "PHASE_01_Python_Fundamentals",
        "title": "Phase 1: Python Fundamentals",
        "description": "Essential Python coding foundation for Machine Learning. Skip if already strong, skim if rusty.",
        "topics": [
            ("Values, expressions, statements, numbers, booleans, strings", "Core Data Types & Operators"),
            ("String operations, input, type casting, comments", "User Inputs & Types"),
            ("Data structures: Lists, Tuples", "Sequential Containers"),
            ("Dictionaries, Sets", "Key-Value Pairs & Unique Sets"),
            ("Conditional execution: if, elif, else, break, continue, pass", "Control Flow"),
            ("While, for loops, nested loops, list comprehension, iterators", "Iteration & Loops"),
            ("Functions, variable scope, lambda, map, filter", "Functional Programming"),
            ("File handling, exception handling", "File IO & Robust Handling"),
            ("Classes & Objects, instance, class variables, constructors", "Object-Oriented Programming"),
            ("Inheritance: multilevel, hierarchical, multiple, MRO", "Inheritance Models & MRO"),
            ("Access specifiers, name mangling, inner classes", "Encapsulation & Nested Classes"),
            ("Polymorphism, operator overloading, magic, dunder functions", "Polymorphism & Magic Methods"),
            ("Abstract methods, data classes, keyword arguments", "Advanced OOP & Dataclasses")
        ]
    },
    {
        "dir_name": "PHASE_02_Math_Stats_Probability",
        "title": "Phase 2: Math, Statistics & Probability",
        "description": "The foundation everything else builds on, including essential Linear Algebra and Calculus.",
        "topics": [
            ("Intro to ML and History", "ML Overview"),
            ("What is ML and Real life examples", "ML Overview"),
            ("AI vs ML vs DL", "ML Overview"),
            ("Types of ML: Supervised, Unsupervised, RL", "ML Overview"),
            ("Batch vs Online Learning", "ML Design"),
            ("Instance vs Model Based Learning", "ML Design"),
            ("Challenges in ML", "ML Design"),
            ("Applications of ML", "ML Applications"),
            ("ML Development Life Cycle", "ML Lifecycle"),
            ("Stanford CS229 Lec 1: Full ML intro, framing problems", "Stanford CS229"),
            ("Linear Algebra: Vectors, Dot Product, Vector Norms, Matrix Operations", "Linear Algebra"),
            ("Linear Algebra: Systems of Linear Equations, Matrix Inverse, Transpose", "Linear Algebra"),
            ("Linear Algebra: Determinants, Orthogonality, Eigenvalues and Eigenvectors", "Linear Algebra"),
            ("Calculus: Limits, Derivatives, and Differentiation Rules", "Calculus"),
            ("Calculus: Partial Derivatives, Gradients, and Chain Rule", "Calculus"),
            ("Calculus: Optimization Basics (Maxima, Minima, Convexity)", "Calculus"),
            ("Data types: structured or unstructured, quantitative or qualitative", "Data Types"),
            ("Statistics and its types", "Descriptive Stats"),
            ("Mean, Median, Mode", "Descriptive Stats"),
            ("Variance and Standard Deviation", "Descriptive Stats"),
            ("Coefficient of variation, Z score, Percentile, Quartile", "Descriptive Stats"),
            ("Skewness and Kurtosis", "Descriptive Stats"),
            ("Correlation Coefficient: Pearson's", "Descriptive Stats"),
            ("Covariance", "Descriptive Stats"),
            ("Probability basics", "Probability"),
            ("Joint, Marginal and Conditional Probability", "Probability"),
            ("Bayes Theorem", "Probability"),
            ("Probability distributions: Discrete and Continuous", "Probability"),
            ("Bayesian Probability deep dive", "Probability"),
            ("Univariate, Bivariate, Multivariate Analysis", "EDA Theory"),
            ("Sampling techniques", "Inferential Stats"),
            ("Point and Interval Estimate", "Inferential Stats"),
            ("Margin of Error", "Inferential Stats"),
            ("Confidence Interval", "Inferential Stats"),
            ("Hypothesis Testing full series", "Inferential Stats"),
            ("Chi Square Test", "Inferential Stats"),
            ("IQR and Outliers (stats perspective)", "Descriptive Stats")
        ]
    },
    {
        "dir_name": "PHASE_03_NumPy",
        "title": "Phase 3: NumPy",
        "description": "Essential before any ML coding.",
        "topics": [
            ("Intro to NumPy", "NumPy Basics"),
            ("Creating arrays: from list, built in methods, random", "Array Creation"),
            ("Array attributes: shape, dtype, size, ndim", "Array Attributes"),
            ("Array methods: reshape, max, min, argmax, argmin", "Array Methods"),
            ("Array operations: copy, append, insert, sort, delete", "Array Manipulation"),
            ("Concatenating, splitting, searching", "Array Manipulation"),
            ("NumPy indexing, slicing, logical selection", "Indexing & Slicing"),
            ("Broadcasting", "Broadcasting Operations"),
            ("Type casting, arithmetic operations", "Array Math"),
            ("Universal array functions: sqrt, exp, sin, etc.", "Mathematical Functions")
        ]
    },
    {
        "dir_name": "PHASE_04_Pandas_Data_Loading",
        "title": "Phase 4: Pandas & Data Loading",
        "description": "Real data handling starts here.",
        "topics": [
            ("Intro to Pandas: Series and DataFrame", "Pandas Basics"),
            ("Data input, selection, indexing", "Data Access"),
            ("DataFrame operations: head, unique, value_counts, sort, null check", "DataFrame Operations"),
            ("Missing data and handling", "Data Cleaning"),
            ("Merging, joining, concatenation: inner, outer, left, right", "Data Merging"),
            ("GroupBy, discretization, binning", "Data Aggregation"),
            ("Data output/saving, working with CSV, JSON, SQL", "Data Storage"),
            ("Pandas for plotting", "Pandas Plotting"),
            ("Fetching from API and Web Scraping", "Data Ingestion"),
            ("Correlation in Pandas", "Correlation Analysis"),
            ("Loading data with Pandas deep dive", "Data Loading"),
            ("Understanding your data and EDA", "EDA Basics")
        ]
    },
    {
        "dir_name": "PHASE_05_Data_Visualization",
        "title": "Phase 5: Data Visualization",
        "description": "See your data before modeling it.",
        "topics": [
            ("Matplotlib Part 1", "Matplotlib"),
            ("Matplotlib Part 2", "Matplotlib"),
            ("Pandas Profiling", "Automated EDA"),
            ("Seaborn: Distribution plots (distplot, jointplot, kdeplot)", "Seaborn"),
            ("Seaborn: Categorical plots (boxplot, violinplot, barplot, countplot)", "Seaborn"),
            ("Seaborn: Matrix plots, Heatmap", "Seaborn"),
            ("EDA using Univariate Analysis", "EDA Visualization"),
            ("EDA using Bivariate and Multivariate Analysis", "EDA Visualization")
        ]
    },
    {
        "dir_name": "PHASE_06_Data_Preprocessing_Feature_Engineering",
        "title": "Phase 6: Data Preprocessing & Feature Engineering",
        "description": "The most time-consuming phase in real projects.",
        "topics": [
            ("Data Science Life Cycle", "DS Lifecycle"),
            ("Data in ML and How much data needed", "Data Volume"),
            ("Handling Missing Data: CCA, Imputers, MICE", "Data Cleaning"),
            ("Managing Missing Features", "Data Cleaning"),
            ("Outlier detection: Z score, IQR, Percentile, Winsorization", "Outlier Management"),
            ("Feature Scaling: Standardization", "Feature Scaling"),
            ("Feature Scaling: Normalization, MinMax, MaxAbs, Robust", "Feature Scaling"),
            ("Feature Scaling deep dive", "Feature Scaling"),
            ("Managing Categorical Data", "Categorical Encoding"),
            ("Encoding: Label, Ordinal", "Categorical Encoding"),
            ("One Hot Encoding", "Categorical Encoding"),
            ("Fit and Transform method", "Scikit-Learn API"),
            ("Column Transformer and Pipelines", "ML Pipelines"),
            ("Function Transforms: Log, Reciprocal, Square Root", "Feature Transformation"),
            ("Power Transformer: Box Cox, Yeo Johnson", "Feature Transformation"),
            ("Binning and Binarization: Quantile, KMeans", "Discretization"),
            ("Handling Mixed and Date/Time Variables", "Feature Extraction"),
            ("Feature Construction and Splitting", "Feature Construction"),
            ("What is Feature Engineering", "Feature Engineering"),
            ("Feature Selection Techniques", "Feature Selection"),
            ("Feature Extraction", "Feature Selection"),
            ("Curse of Dimensionality", "Dimensionality Basics"),
            ("Data Preprocessing and Cleaning overview", "Data Cleaning"),
            ("Normalization with Python", "Feature Scaling"),
            ("Standardization with Python", "Feature Scaling"),
            ("Binarization with Python", "Discretization"),
            ("Training and Testing data split with Python", "Data Splitting")
        ]
    },
    {
        "dir_name": "PHASE_07_Regression_Algorithms",
        "title": "Phase 7: Regression Algorithms",
        "description": "Pure regression, from simplest to most regularized.",
        "topics": [
            ("Regression intro and dependent/independent variables", "Regression Basics"),
            ("Stanford CS229 Lec 2: Linear Regression and GD full math", "Stanford CS229"),
            ("Simple Linear Regression: intuition and code", "Linear Regression"),
            ("Linear Regression solved numericals", "Linear Regression"),
            ("Linear Regression using Least Squares", "Linear Regression"),
            ("Linear Regression single variable Python", "Linear Regression"),
            ("Regression Metrics: MSE, MAE, RMSE, R2, Adjusted R2", "Model Evaluation"),
            ("SST, SSR, SSE", "Model Evaluation"),
            ("Multiple Linear Regression: intuition and math", "Linear Regression"),
            ("Linear Regression multiple variables Python", "Linear Regression"),
            ("Assumptions of Linear Regression", "Linear Regression"),
            ("Multiple Dependent Variables", "Regression Variations"),
            ("Multiple Linear Regression solved numerical", "Linear Regression"),
            ("Gradient Descent end to end", "Gradient Descent"),
            ("Batch GD, SGD, Mini Batch GD", "Gradient Descent"),
            ("Learning Rate", "Gradient Descent"),
            ("Univariate Linear Regression with GD (without vectorization)", "Gradient Descent"),
            ("Univariate Linear Regression with GD (with vectorization)", "Gradient Descent"),
            ("Multivariate Linear Regression implementation", "Linear Regression"),
            ("Polynomial Regression", "Non-linear Regression"),
            ("Bias Variance Tradeoff and Overfitting/Underfitting", "Model Validation"),
            ("Ridge Regression full series", "Regularization"),
            ("Lasso Regression", "Regularization"),
            ("ElasticNet Regression", "Regularization"),
            ("Stanford CS229 Lec 3: Locally Weighted Regression", "Stanford CS229"),
            ("Locally Weighted Regression", "Locally Weighted"),
            ("KNN Regression", "KNN"),
            ("Regression Trees", "Decision Trees")
        ]
    },
    {
        "dir_name": "PHASE_08_Classification_Algorithms",
        "title": "Phase 8: Classification Algorithms",
        "description": "The most used ML algorithms in industry.",
        "topics": [
            ("Linear vs Logistic Regression", "Classification Intro"),
            ("Stanford CS229 Lec 3: Logistic Regression math", "Stanford CS229"),
            ("Logistic Regression full series: Perceptron, Sigmoid, Loss, GD", "Logistic Regression"),
            ("Logistic Regression with Python", "Logistic Regression"),
            ("Logistic Regression solved numerical", "Logistic Regression"),
            ("Logistic Regression hyperparameters", "Logistic Regression"),
            ("Binary Classification: full implementation", "Classification Implementation"),
            ("Stanford CS229 Lec 4: Perceptron and GLM", "Stanford CS229"),
            ("Softmax / Multinomial Logistic Regression", "Multiclass Classification"),
            ("Multiclass Classification: One vs All, One vs One", "Multiclass Classification"),
            ("Confusion Matrix, Accuracy, Type 1 & 2 errors", "Classification Metrics"),
            ("Precision, Recall, F1 Score", "Classification Metrics"),
            ("ROC AUC full", "Classification Metrics"),
            ("Specificity and Sensitivity", "Classification Metrics"),
            ("Multiclass Confusion Matrix", "Classification Metrics"),
            ("Accuracy vs F1 Score", "Classification Metrics"),
            ("Dataset imbalance and remedies: Augmentation", "Imbalanced Data"),
            ("Conditional Probability", "Probability Basics"),
            ("Bayes Theorem", "Probability Basics"),
            ("Stanford CS229 Lec 5: GDA and Naive Bayes", "Stanford CS229"),
            ("Naive Bayes full series", "Naive Bayes"),
            ("Naive Bayes variants: Bernoulli, Multinomial, Gaussian", "Naive Bayes"),
            ("Naive Bayes solved numerical", "Naive Bayes"),
            ("Bayesian Belief Network", "Bayesian Networks"),
            ("Bayes Optimal Classifier", "Bayesian Learning"),
            ("Concept Learning", "Machine Learning Theory"),
            ("Stanford CS229 Lec 6: SVM", "Stanford CS229"),
            ("SVM geometric intuition", "SVM"),
            ("SVM hard margin and soft margin math", "SVM"),
            ("Stanford CS229 Lec 7: Kernels", "Stanford CS229"),
            ("Kernel trick and Non linear SVM", "SVM"),
            ("SVM implementation", "SVM"),
            ("Decision Tree intuition and Entropy and Info Gain", "Decision Trees"),
            ("ID3, C4.5, CART algorithms", "Decision Trees"),
            ("Decision Tree hyperparameters and overfitting", "Decision Trees"),
            ("Decision Tree visualization", "Decision Trees"),
            ("Decision Tree implementation", "Decision Trees"),
            ("KNN Classification and finding K", "KNN"),
            ("KNN full overview", "KNN"),
            ("Linear Discriminant Analysis (LDA)", "Linear Discriminant"),
            ("Inductive Bias", "Machine Learning Theory")
        ]
    },
    {
        "dir_name": "PHASE_09_Model_Evaluation_Validation",
        "title": "Phase 9: Model Evaluation & Validation",
        "description": "Know if your model is actually good.",
        "topics": [
            ("Training & Testing phase", "Model Validation"),
            ("Classic vs Adaptive Machine", "Model Validation"),
            ("Basics of Training and Testing", "Model Validation"),
            ("Stanford CS229 Lec 8: Data splits and Cross Validation theory", "Stanford CS229"),
            ("Stanford CS229 Discussion: Learning Theory", "Stanford CS229"),
            ("Cross Validation", "Cross Validation"),
            ("K Fold Cross Validation", "Cross Validation"),
            ("LOOCV and Leave P Out", "Cross Validation"),
            ("Overfitting and Underfitting deep dive", "Bias-Variance"),
            ("Model Complexity vs Error", "Bias-Variance"),
            ("Bias Variance Tradeoff", "Bias-Variance"),
            ("Imbalanced Data and SMOTE and Oversampling", "Data Imbalance"),
            ("Hyperparameter Tuning with Optuna", "Hyperparameter Tuning"),
            ("Random State", "General"),
            ("Accuracy Score explained", "Classification Metrics"),
            ("Steps to build any ML model", "ML Pipeline"),
            ("Stanford CS229 Lec 12: Debugging ML and Error Analysis", "Stanford CS229")
        ]
    },
    {
        "dir_name": "PHASE_10_Dimensionality_Reduction",
        "title": "Phase 10: Dimensionality Reduction",
        "description": "Reduce noise, keep signal.",
        "topics": [
            ("PCA Part 1: Geometric intuition", "PCA"),
            ("PCA Part 2: Math and step by step", "PCA"),
            ("PCA Part 3: Code and visualization", "PCA"),
            ("Stanford CS229 Lec 15: PCA and ICA", "Stanford CS229"),
            ("PCA explained", "PCA"),
            ("LDA", "LDA"),
            ("Feature Importance", "Feature Selection")
        ]
    },
    {
        "dir_name": "PHASE_11_Ensemble_Methods",
        "title": "Phase 11: Ensemble Methods",
        "description": "The most powerful classical ML phase, heaviest and most industry-relevant.",
        "topics": [
            ("Intro to Ensemble Learning", "Ensemble Basics"),
            ("Stanford CS229 Lec 9: Decision Trees and Ensemble theory", "Stanford CS229"),
            ("Voting Classifier: Hard and Soft", "Voting Classifiers"),
            ("Voting Regressor", "Voting Classifiers"),
            ("Bagging full series", "Bagging"),
            ("Random Forest intuition and bias variance", "Random Forests"),
            ("Bagging vs Random Forest", "Ensemble Differences"),
            ("Random Forest hyperparameters and tuning", "Random Forests"),
            ("OOB Score", "Random Forests"),
            ("Feature Importance using RF and DT", "Feature Importance"),
            ("AdaBoost intuition and math and code", "Boosting"),
            ("Bagging vs Boosting", "Ensemble Differences"),
            ("Boosting implementation", "Boosting"),
            ("Gradient Boosting full series", "Boosting"),
            ("XGBoost full series", "Boosting"),
            ("Stacking and Blending", "Stacking"),
            ("Bagging vs Boosting vs Stacking", "Ensemble Summary"),
            ("Random Forest: Step wise explanation", "Random Forests")
        ]
    },
    {
        "dir_name": "PHASE_12_Unsupervised_Learning_Clustering",
        "title": "Phase 12: Unsupervised Learning (Clustering)",
        "description": "Find hidden patterns without labels.",
        "topics": [
            ("K Means intuition and code and from scratch", "K-Means"),
            ("K Means++", "K-Means"),
            ("Elbow Method", "K-Means"),
            ("K Means Python implementation", "K-Means"),
            ("Hierarchical Clustering: Agglomerative and Divisive", "Hierarchical Clustering"),
            ("Single Linkage full", "Hierarchical Clustering"),
            ("Complete Linkage full", "Hierarchical Clustering"),
            ("Agglomerative full code", "Hierarchical Clustering"),
            ("K Medoids", "K Medoids"),
            ("DBSCAN", "DBSCAN"),
            ("Recommendation Systems", "Recommendation"),
            ("Stanford CS229 Lec 13: EM Algorithm", "Stanford CS229"),
            ("Stanford CS229 Lec 14: EM and Factor Analysis", "Stanford CS229")
        ]
    }
]

# Write detailed, complete notebook cells for the 13 Python Fundamentals notebooks
PHASE_1_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Values, Expressions, Statements, Numbers, Booleans, Strings",
        "summary": "Introduction to Python basic types (integers, floats, booleans, and strings), mathematical operations, statements, expressions, and dynamic typing.",
        "theory": [
            "### 1. Values & Types\n",
            "A **value** is one of the basic things a program works with, like a letter or a number. Values belong to different **types**:\n",
            "- `int`: Integers (e.g., `10`, `-5`)\n",
            "- `float`: Floating-point numbers (e.g., `3.14`, `-0.001`)\n",
            "- `bool`: Boolean values (`True` and `False`)\n",
            "- `str`: Strings of characters (e.g., `\"Hello, ML!\"`)\n",
            "\n",
            "### 2. Operators & Expressions\n",
            "An **expression** is a combination of values, variables, and operators that evaluates to a single value. Python supports standard arithmetic operators:\n",
            "- Addition (`+`), Subtraction (`-`), Multiplication (`*`)\n",
            "- Floating-Point Division (`/`): Evaluates to a float (e.g., `5 / 2 = 2.5`)\n",
            "- Floor Division (`//`): Truncates the fractional part, returning an int (e.g., `5 // 2 = 2`)\n",
            "- Modulo (`%`): Returns the remainder of division (e.g., `5 % 2 = 1`)\n",
            "- Exponentiation (`**`): Raises a base to a power (e.g., `2 ** 3 = 8`)\n",
            "\n",
            "### 3. Variable Assignment & Statements\n",
            "A **statement** is an instruction that the Python interpreter can execute. An assignment statement (`x = 5`) binds a name (variable) to a value in memory. Python is **dynamically typed**, meaning you do not need to declare a variable's type before using it; its type is determined at runtime based on the value bound to it."
        ],
        "code": [
            "# 1. Explore data types\n",
            "a = 15\n",
            "b = 3.14\n",
            "c = True\n",
            "d = \"Antigravity AI\"\n",
            "\n",
            "print(\"Type of a:\", type(a))\n",
            "print(\"Type of b:\", type(b))\n",
            "print(\"Type of c:\", type(c))\n",
            "print(\"Type of d:\", type(d))\n",
            "\n",
            "# 2. Expressions and Operator Precedence\n",
            "val1 = 10 + 3 * 2 ** 3  # Precedence: **, *, +\n",
            "val2 = (10 + 3) * 2 ** 3\n",
            "print(\"val1:\", val1)  # 10 + 3 * 8 = 34\n",
            "print(\"val2:\", val2)  # 13 * 8 = 104\n",
            "\n",
            "# 3. Division types\n",
            "print(\"Float Division 7/3:\", 7 / 3)\n",
            "print(\"Floor Division 7//3:\", 7 // 3)\n",
            "print(\"Modulo 7%3:\", 7 % 3)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Swap two variables `x` and `y` without using a third temporary variable.\n",
            "2. Calculate the volume of a sphere with radius $r = 5$ using the formula: $V = \\frac{4}{3} \\pi r^3$ (Use `3.14159` for $\\pi$)."
        ],
        "exercise_code": [
            "# Exercise 1: Swap variables\n",
            "x = 10\n",
            "y = 20\n",
            "x, y = y, x\n",
            "print(f\"x: {x}, y: {y}\")\n",
            "\n",
            "# Exercise 2: Sphere Volume\n",
            "r = 5\n",
            "pi = 3.14159\n",
            "volume = (4/3) * pi * (r ** 3)\n",
            "print(f\"Volume: {volume}\")\n"
        ]
    },
    2: {
        "title": "String Operations, Input, Type Casting, Comments",
        "summary": "String indexing, slicing, concatenation, multiplication, comments, keyboard inputs, and conversions between data types.",
        "theory": [
            "### 1. String Slicing & Operations\n",
            "Strings are sequences of characters. You can access individual characters using **indexing** (0-based) or a range of characters using **slicing**:\n",
            "`string[start:stop:step]`\n",
            "- Slicing is *inclusive* of the `start` index and *exclusive* of the `stop` index.\n",
            "- Negative indexes count backward from the end of the string (e.g., `-1` is the last character).\n",
            "- Strings are **immutable**; they cannot be altered in-place.\n",
            "\n",
            "### 2. User Input & Casting\n",
            "- `input(prompt)` always returns user input as a **string** (`str`).\n",
            "- To perform math on inputs, you must explicitly cast them using type conversion functions: `int()`, `float()`, or `str()`.\n",
            "\n",
            "### 3. Comments\n",
            "- `#` for single-line comments.\n",
            "- Triple quotes `\"\"\"` or `'''` for docstrings and multi-line explanations."
        ],
        "code": [
            "# 1. Slicing and Concatenation\n",
            "text = \"Machine Learning\"\n",
            "print(\"First character:\", text[0])\n",
            "print(\"Last character:\", text[-1])\n",
            "print(\"Slice [0:7]:\", text[0:7])\n",
            "print(\"Reverse string:\", text[::-1])\n",
            "\n",
            "# 2. String repetition and checks\n",
            "print(\"ML \" * 3)\n",
            "print(\"Machine\" in text)\n",
            "\n",
            "# 3. Type Casting example\n",
            "num_str = \"123\"\n",
            "num_int = int(num_str)\n",
            "print(\"Cast to int:\", num_int + 7)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Write a script that prompts a user to enter their birth year, converts it to an integer, calculates their age, and prints it in an f-string.\n",
            "2. Given a string `filename = \"data_source.csv\"`, extract the extension (e.g., `csv`) using slicing."
        ],
        "exercise_code": [
            "# Exercise 1: Age Calculator\n",
            "birth_year = 2004\n",
            "current_year = 2026\n",
            "age = current_year - int(birth_year)\n",
            "print(f\"Age: {age}\")\n",
            "\n",
            "# Exercise 2: File Extension Extraction\n",
            "filename = \"data_source.csv\"\n",
            "extension = filename.split(\"_\")[-1].split(\".\")[-1]\n",
            "print(f\"Extension: {extension}\")\n"
        ]
    },
    3: {
        "title": "Data structures: Lists, Tuples",
        "summary": "Comprehensive guide to Python lists and tuples, covering indexing, slicing, common methods, packing/unpacking, and mutability vs immutability.",
        "theory": [
            "### 1. Lists (Mutable Sequences)\n",
            "A **list** is an ordered, mutable sequence of values. Lists are defined using square brackets `[]`:\n",
            "- **Mutable**: Elements can be added, changed, or removed in-place.\n",
            "- **Common Methods**:\n",
            "  - `.append(x)`: Adds item `x` to the end.\n",
            "  - `.extend(iterable)`: Appends elements from another iterable.\n",
            "  - `.insert(i, x)`: Inserts item `x` at index `i`.\n",
            "  - `.pop(i)`: Removes and returns the item at index `i`.\n",
            "  - `.remove(x)`: Removes the first occurrence of item `x`.\n",
            "\n",
            "### 2. Tuples (Immutable Sequences)\n",
            "A **tuple** is an ordered, immutable sequence of values. Defined using parentheses `()`:\n",
            "- **Immutable**: Once created, elements cannot be added, changed, or deleted.\n",
            "- Faster and safer than lists for read-only datasets.\n",
            "- **Tuple Unpacking**: Assigning individual elements of a tuple to variables in one line."
        ],
        "code": [
            "# 1. List Mutability and Operations\n",
            "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
            "fruits.append(\"date\")\n",
            "fruits[1] = \"blueberry\"\n",
            "print(\"List after modification:\", fruits)\n",
            "\n",
            "# 2. Tuple Immutability & Unpacking\n",
            "coordinates = (40.7128, -74.0060)\n",
            "try:\n",
            "    coordinates[0] = 34.0522\n",
            "except TypeError as e:\n",
            "    print(\"Error:\", e)  # Tuples cannot be modified\n",
            "\n",
            "# Unpacking coordinates\n",
            "lat, lon = coordinates\n",
            "print(f\"Latitude: {lat}, Longitude: {lon}\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Given a list `numbers = [3, 1, 4, 1, 5, 9, 2]`, sort it in descending order and remove duplicates without using sets.\n",
            "2. Combine two lists `keys = ['name', 'age']` and `values = ['Taha', 21]` into a list of tuples like `[('name', 'Taha'), ('age', 21)]` using `zip()`."
        ],
        "exercise_code": [
            "# Exercise 1: Sort and deduplicate list\n",
            "numbers = [3, 1, 4, 1, 5, 9, 2]\n",
            "unique_numbers = []\n",
            "for n in numbers:\n",
            "    if n not in unique_numbers:\n",
            "        unique_numbers.append(n)\n",
            "unique_numbers.sort(reverse=True)\n",
            "print(unique_numbers)\n",
            "\n",
            "# Exercise 2: Zip lists\n",
            "keys = ['name', 'age']\n",
            "values = ['Taha', 21]\n",
            "combined = list(zip(keys, values))\n",
            "print(combined)\n"
        ]
    },
    4: {
        "title": "Dictionaries, Sets",
        "summary": "Dictionaries for key-value storage and Sets for unique element algebra, covering access, mutations, keys, values, union, intersection, and difference.",
        "theory": [
            "### 1. Dictionaries (Hash Maps)\n",
            "A **dictionary** is an unordered collection of key-value pairs. Keys must be unique and hashable (immutable):\n",
            "- **Common Operations**:\n",
            "  - `dict[key]`: Access value (throws error if key missing).\n",
            "  - `dict.get(key, default)`: Safely access value without raising errors.\n",
            "  - `dict.items()`: Iterates over `(key, value)` pairs.\n",
            "  - `dict.keys()`, `dict.values()`: Retrieve collections of keys or values.\n",
            "\n",
            "### 2. Sets (Unique Elements)\n",
            "A **set** is an unordered collection of unique elements. Defined using curly braces `{}` or `set()`:\n",
            "- Sets are mutable, but their elements must be hashable.\n",
            "- Useful for removing duplicates and calculating mathematical set relationships:\n",
            "  - Union (`|` or `.union()`)\n",
            "  - Intersection (`&` or `.intersection()`)\n",
            "  - Difference (`-` or `.difference()`)\n",
            "  - Symmetric Difference (`^` or `.symmetric_difference()`)"
        ],
        "code": [
            "# 1. Dictionary creation and access\n",
            "model_meta = {\n",
            "    \"algorithm\": \"Random Forest\",\n",
            "    \"n_estimators\": 100,\n",
            "    \"max_depth\": 12\n",
            "}\n",
            "print(\"Algorithm:\", model_meta.get(\"algorithm\"))\n",
            "print(\"Learning Rate:\", model_meta.get(\"learning_rate\", 0.01))  # Default fallback\n",
            "\n",
            "# 2. Set operations\n",
            "group_a = {\"Python\", \"R\", \"SQL\", \"C++\"}\n",
            "group_b = {\"Java\", \"C++\", \"Python\", \"Go\"}\n",
            "\n",
            "print(\"Union:\", group_a | group_b)\n",
            "print(\"Intersection:\", group_a & group_b)\n",
            "print(\"Difference (A - B):\", group_a - group_b)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Given a dictionary representing word counts: `counts = {'the': 4, 'ml': 12, 'data': 8}`. Increment the count of `'ml'` by 1, and add `'python'` with a count of 5.\n",
            "2. Given a list of user IDs `ids = [101, 102, 101, 105, 102, 108]`, convert it to a set to filter duplicates, then check if `105` is in the set."
        ],
        "exercise_code": [
            "# Exercise 1: Dict updates\n",
            "counts = {'the': 4, 'ml': 12, 'data': 8}\n",
            "counts['ml'] += 1\n",
            "counts['python'] = 5\n",
            "print(counts)\n",
            "\n",
            "# Exercise 2: Set filtration\n",
            "ids = [101, 102, 101, 105, 102, 108]\n",
            "unique_ids = set(ids)\n",
            "is_present = 105 in unique_ids\n",
            "print(f\"Set: {unique_ids}, 105 Present: {is_present}\")\n"
        ]
    },
    5: {
        "title": "Conditional execution: if, elif, else, break, continue, pass",
        "summary": "Branching control structures in Python using logical constraints and loop interrupts.",
        "theory": [
            "### 1. Conditional Branching\n",
            "Python executes code block conditional branches using `if`, `elif` (else if), and `else` blocks:\n",
            "- Code blocks are defined via **indentation** (typically 4 spaces).\n",
            "- Uses comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) and boolean operators (`and`, `or`, `not`).\n",
            "\n",
            "### 2. Loop Interrupts\n",
            "- `break`: Terminates the innermost loop immediately.\n",
            "- `continue`: Skips the rest of the current loop iteration and moves to the next.\n",
            "- `pass`: A null statement/placeholder used when statement block syntactically requires code but you want no action."
        ],
        "code": [
            "# 1. Conditional structure example\n",
            "accuracy = 0.88\n",
            "if accuracy >= 0.95:\n",
            "    print(\"Model performance: Excellent\")\n",
            "elif accuracy >= 0.80:\n",
            "    print(\"Model performance: Good\")\n",
            "else:\n",
            "    print(\"Model performance: Needs tuning\")\n",
            "\n",
            "# 2. Loop Control Statement\n",
            "print(\"Checking loop interrupts:\")\n",
            "for i in range(1, 6):\n",
            "    if i == 3:\n",
            "        continue  # Skip 3\n",
            "    if i == 5:\n",
            "        break  # Abort loop at 5\n",
            "    print(i)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Write a program that classifies a triangle based on the lengths of its three sides `a`, `b`, and `c` (Equilateral, Isosceles, Scalene).\n",
            "2. Write a loop iterating from 1 to 10. Use `pass` as a placeholder for odd numbers, and print even numbers."
        ],
        "exercise_code": [
            "# Exercise 1: Triangle classifier\n",
            "a, b, c = 5, 5, 8\n",
            "if a == b == c:\n",
            "    print(\"Equilateral\")\n",
            "elif a == b or b == c or a == c:\n",
            "    print(\"Isosceles\")\n",
            "else:\n",
            "    print(\"Scalene\")\n",
            "\n",
            "# Exercise 2: Loop with pass\n",
            "for i in range(1, 11):\n",
            "    if i % 2 != 0:\n",
            "        pass\n",
            "    else:\n",
            "        print(i)\n"
        ]
    },
    6: {
        "title": "While, for loops, nested loops, list comprehension, iterators",
        "summary": "Loop constructs, iterator internals, and pythonic list comprehension syntax.",
        "theory": [
            "### 1. Loop Structures\n",
            "- `for` loops: Iterate over collections, ranges, or generator expressions.\n",
            "- `while` loops: Execute as long as a boolean constraint remains `True`.\n",
            "- Nested loops: Loops within loops (e.g., iterating through a 2D matrix).\n",
            "\n",
            "### 2. List Comprehension\n",
            "An elegant, faster syntax to build lists from existing iterables:\n",
            "`[expression for item in iterable if condition]`\n",
            "\n",
            "### 3. Iterators & Iterables\n",
            "- An **iterable** is any object capable of returning its members one at a time (e.g., list, tuple, string).\n",
            "- An **iterator** is the stream object returned by calling `iter()` on an iterable. It yields items sequentially via `next()`."
        ],
        "code": [
            "# 1. Nested loops for matrix traversal\n",
            "matrix = [[1, 2], [3, 4]]\n",
            "for row in matrix:\n",
            "    for val in row:\n",
            "        print(val, end=\" \")\n",
            "print(\"\")\n",
            "\n",
            "# 2. List Comprehension vs For-Loop\n",
            "squares = [x**2 for x in range(1, 6)]\n",
            "print(\"Squares list comprehension:\", squares)\n",
            "\n",
            "# 3. Iterators\n",
            "iterable_list = [10, 20]\n",
            "iterator_obj = iter(iterable_list)\n",
            "print(next(iterator_obj))\n",
            "print(next(iterator_obj))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Rewrite the following code using a single line of list comprehension:\n",
            "   `words = ['data', 'science', 'python', 'ai']; long_words = []`\n",
            "   `for w in words: if len(w) > 2: long_words.append(w.upper())`\n",
            "2. Implement a simple while loop that prints the Fibonacci sequence up to 50."
        ],
        "exercise_code": [
            "# Exercise 1: List Comprehension\n",
            "words = ['data', 'science', 'python', 'ai']\n",
            "long_words = [w.upper() for w in words if len(w) > 2]\n",
            "print(long_words)\n",
            "\n",
            "# Exercise 2: Fibonacci sequence\n",
            "a, b = 0, 1\n",
            "while a <= 50:\n",
            "    print(a, end=\" \")\n",
            "    a, b = b, a + b\n"
        ]
    },
    7: {
        "title": "Functions, variable scope, lambda, map, filter",
        "summary": "Function definitions, local/global variable scoping rules (LEGB), anonymous functions, and map/filter operators.",
        "theory": [
            "### 1. Function Scope (LEGB Rule)\n",
            "Variable lookup resolution in Python follows the **LEGB** order:\n",
            "- **Local**: Defined inside current function.\n",
            "- **Enclosing**: Defined in nested/outer functions.\n",
            "- **Global**: Declared at the top level of the module.\n",
            "- **Built-in**: Python's pre-loaded keywords (e.g., `len`, `range`).\n",
            "Use `global x` or `nonlocal x` to modify variables outside local scope.\n",
            "\n",
            "### 2. Lambda Functions\n",
            "Anonymous, single-expression functions: `lambda arg1, arg2: expression`.\n",
            "\n",
            "### 3. Map & Filter\n",
            "- `map(func, iterable)`: Applies a function to all elements in the sequence.\n",
            "- `filter(func, iterable)`: Filters items that evaluate to `True` for the function."
        ],
        "code": [
            "# 1. LEGB Scope demonstration\n",
            "x = \"global\"\n",
            "def outer_func():\n",
            "    x = \"enclosing\"\n",
            "    def inner_func():\n",
            "        x = \"local\"\n",
            "        print(\"Inner level:\", x)\n",
            "    inner_func()\n",
            "    print(\"Outer level:\", x)\n",
            "outer_func()\n",
            "\n",
            "# 2. Lambda, Map, and Filter\n",
            "numbers = [1, 2, 3, 4, 5]\n",
            "squared = list(map(lambda x: x**2, numbers))\n",
            "evens = list(filter(lambda x: x % 2 == 0, numbers))\n",
            "print(\"Squared:\", squared)\n",
            "print(\"Evens:\", evens)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Write a function `compute_stats(data_list)` that calculates and returns both the sum and the mean of a list of numbers as a tuple.\n",
            "2. Using `filter()` and `lambda`, extract all words that start with 's' from the list: `words = ['stats', 'probability', 'statistics', 'math', 'sample']`."
        ],
        "exercise_code": [
            "# Exercise 1: Sum and Mean\n",
            "def compute_stats(data_list):\n",
            "    s = sum(data_list)\n",
            "    m = s / len(data_list) if data_list else 0\n",
            "    return s, m\n",
            "print(compute_stats([10, 20, 30]))\n",
            "\n",
            "# Exercise 2: Words filtering\n",
            "words = ['stats', 'probability', 'statistics', 'math', 'sample']\n",
            "s_words = list(filter(lambda w: w.startswith('s'), words))\n",
            "print(s_words)\n"
        ]
    },
    8: {
        "title": "File handling, exception handling",
        "summary": "File input/output pipelines, context managers, exceptions, handling runtime anomalies, and custom errors.",
        "theory": [
            "### 1. File Handling (Context Managers)\n",
            "Always use the `with` statement when opening files. It acts as a **context manager**, automatically closing the file stream when execution exits the block, preventing memory leaks:\n",
            "`with open(file_path, mode) as f:`\n",
            "Modes: `'r'` (read), `'w'` (write/overwrite), `'a'` (append).\n",
            "\n",
            "### 2. Exception Handling\n",
            "Errors are handled dynamically using `try`, `except`, `else`, and `finally` blocks:\n",
            "- `try`: Block containing code that might throw an error.\n",
            "- `except ExceptionType`: Code to execute if specific error occurs.\n",
            "- `else`: Executes if **no** exception occurred in the try block.\n",
            "- `finally`: Executes unconditionally at the end (useful for closing connections/cleanup).\n",
            "\n",
            "### 3. Custom Exceptions\n",
            "Declare custom error structures by inheriting from the base `Exception` class."
        ],
        "code": [
            "# 1. Writing and Reading Files\n",
            "filepath = \"sample_notes.txt\"\n",
            "with open(filepath, \"w\") as f:\n",
            "    f.write(\"Python for ML Roadmap\\nFirst Topic: Foundational Core\")\n",
            "\n",
            "with open(filepath, \"r\") as f:\n",
            "    print(\"File Contents:\\n\", f.read())\n",
            "\n",
            "# 2. Exception Handling Example\n",
            "try:\n",
            "    result = 10 / 0\n",
            "except ZeroDivisionError as e:\n",
            "    print(\"Caught error:\", e)\n",
            "finally:\n",
            "    print(\"Cleanup actions complete.\")\n",
            "    if os.path.exists(filepath):\n",
            "        os.remove(filepath)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Implement a custom exception class named `NegativeValueError`. Write a function `square_root(val)` that raises this exception if the input is negative.\n",
            "2. Write a script that safely attempts to read a non-existent file, catches the `FileNotFoundError`, and prints a user-friendly error message."
        ],
        "exercise_code": [
            "# Exercise 1: Custom Exception\n",
            "class NegativeValueError(Exception):\n",
            "    pass\n",
            "\n",
            "def square_root(val):\n",
            "    if val < 0:\n",
            "        raise NegativeValueError(\"Negative numbers are not allowed.\")\n",
            "    return val ** 0.5\n",
            "\n",
            "try:\n",
            "    square_root(-4)\n",
            "except NegativeValueError as e:\n",
            "    print(\"Error raised:\", e)\n",
            "\n",
            "# Exercise 2: File Not Found Catch\n",
            "try:\n",
            "    with open(\"ghost.csv\", \"r\") as f:\n",
            "        data = f.read()\n",
            "except FileNotFoundError:\n",
            "    print(\"Notice: File was not found. Initializing empty dataset.\")\n"
        ]
    },
    9: {
        "title": "Classes & Objects, instance, class variables, constructors",
        "summary": "Core Object-Oriented structures, class creation, self references, attributes, instance vs class namespace scopes.",
        "theory": [
            "### 1. Classes, Objects, and Constructors\n",
            "- **Class**: A user-defined template or blueprint for creating objects.\n",
            "- **Object**: An instance of a class.\n",
            "- **Constructor (`__init__`)**: The initialization method called automatically when creating a new object. Initializes instance variables.\n",
            "- **`self`**: Refers to the current instance of the class.\n",
            "\n",
            "### 2. Instance vs Class Variables\n",
            "- **Instance Variables**: Defined inside constructor methods with `self.`. Unique to each instance object.\n",
            "- **Class Variables**: Defined directly inside the class body, outside any methods. Shared across all instance objects of that class."
        ],
        "code": [
            "class MachineLearningModel:\n",
            "    # Class variable: Shared by all instances\n",
            "    framework = \"Scikit-Learn\"\n",
            "    \n",
            "    def __init__(self, name, model_type):\n",
            "        # Instance variables: Unique to each instance\n",
            "        self.name = name\n",
            "        self.model_type = model_type\n",
            "        \n",
            "    def display_details(self):\n",
            "        return f\"{self.name} is a {self.model_type} model using {self.framework}.\"\n",
            "\n",
            "# Instantiate objects\n",
            "model1 = MachineLearningModel(\"Ridge\", \"Regression\")\n",
            "model2 = MachineLearningModel(\"SVC\", \"Classification\")\n",
            "\n",
            "print(model1.display_details())\n",
            "print(model2.display_details())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Implement a `Circle` class with a class variable `PI = 3.14159`, an instance variable `radius`, and methods to calculate area and perimeter.\n",
            "2. Modify a class variable using `ClassName.variable_name = new_value` and observe how it affects existing instances."
        ],
        "exercise_code": [
            "# Exercise 1: Circle class\n",
            "class Circle:\n",
            "    PI = 3.14159\n",
            "    def __init__(self, radius):\n",
            "        self.radius = radius\n",
            "    def area(self): return self.PI * (self.radius ** 2)\n",
            "    def perimeter(self): return 2 * self.PI * self.radius\n",
            "\n",
            "c = Circle(3)\n",
            "print(f\"Area: {c.area()}, Perimeter: {c.perimeter()}\")\n"
        ]
    },
    10: {
        "title": "Inheritance: multilevel, hierarchical, multiple, MRO",
        "summary": "Code reuse using class inheritance models, solving conflicts using Method Resolution Order (MRO) and super().",
        "theory": [
            "### 1. Types of Inheritance\n",
            "- **Single**: Child inherits from a single parent.\n",
            "- **Multilevel**: Parent -> Child -> Grandchild.\n",
            "- **Hierarchical**: Multiple subclasses inherit from a single parent.\n",
            "- **Multiple**: A subclass inherits from more than one parent.\n",
            "\n",
            "### 2. Method Resolution Order (MRO)\n",
            "When using multiple inheritance, class namespaces can conflict (the Diamond Problem). Python solves this using the **C3 Linearization** algorithm to determine Method Resolution Order (MRO):\n",
            "- Call `ClassName.mro()` or print `obj.__class__.__mro__` to view the hierarchy.\n",
            "- Use `super()` to call parent constructors and methods safely according to MRO sequence."
        ],
        "code": [
            "class Base:\n",
            "    def show(self):\n",
            "        print(\"Base execution\")\n",
            "\n",
            "class Left(Base):\n",
            "    def show(self):\n",
            "        print(\"Left start\")\n",
            "        super().show()\n",
            "        print(\"Left end\")\n",
            "\n",
            "class Right(Base):\n",
            "    def show(self):\n",
            "        print(\"Right start\")\n",
            "        super().show()\n",
            "        print(\"Right end\")\n",
            "\n",
            "class SubChild(Left, Right):\n",
            "    def show(self):\n",
            "        print(\"SubChild start\")\n",
            "        super().show()\n",
            "        print(\"SubChild end\")\n",
            "\n",
            "child = SubChild()\n",
            "child.show()\n",
            "print(\"\\nMRO order:\", SubChild.mro())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Implement a class structure: Parent class `Dataset` with attributes `filepath` and constructor. Subclass `TabularDataset` adding `delimiter`, and another subclass `ImageDataset` adding `dimensions` and overriding dataset loading statements.\n",
            "2. Define three classes `A`, `B`, and `C` where `C` inherits from both `A` and `B`. Verify class `C`'s resolution sequence using `.mro()`."
        ],
        "exercise_code": [
            "# Exercise 1: Dataset structures\n",
            "class Dataset:\n",
            "    def __init__(self, filepath):\n",
            "        self.filepath = filepath\n",
            "\n",
            "class TabularDataset(Dataset):\n",
            "    def __init__(self, filepath, delimiter=','):\n",
            "        super().__init__(filepath)\n",
            "        self.delimiter = delimiter\n",
            "\n",
            "t = TabularDataset(\"data.csv\", ';')\n",
            "print(f\"File: {t.filepath}, Delimiter: {t.delimiter}\")\n"
        ]
    },
    11: {
        "title": "Access specifiers, name mangling, inner classes",
        "summary": "Encapsulation, public/protected/private variables, name mangling behavior, and nesting inner classes.",
        "theory": [
            "### 1. Encapsulation & Access Specifiers\n",
            "Python doesn't enforce strict access controls like Java/C++, but relies on conventions:\n",
            "- **Public**: `var`. Accessible from anywhere.\n",
            "- **Protected**: `_var`. Convention indicating it shouldn't be accessed directly outside subclasses.\n",
            "- **Private**: `__var`. Restricts external access using Name Mangling.\n",
            "\n",
            "### 2. Name Mangling\n",
            "Python renames private attributes prefixing double underscores (e.g. `__attr` in `ClassName` becomes `_ClassName__attr`) to prevent accidental overrides in subclasses.\n",
            "\n",
            "### 3. Inner (Nested) Classes\n",
            "Declaring a class inside another class. Useful for logical clustering and nested architectures."
        ],
        "code": [
            "class Outer:\n",
            "    def __init__(self):\n",
            "        self.public_var = \"Public\"\n",
            "        self._protected_var = \"Protected\"\n",
            "        self.__private_var = \"Private\"\n",
            "        self.inner = self.Inner()\n",
            "        \n",
            "    class Inner:\n",
            "        def __init__(self):\n",
            "            self.data = \"Nested Data\"\n",
            "            \n",
            "obj = Outer()\n",
            "print(\"Public variable:\", obj.public_var)\n",
            "print(\"Protected variable:\", obj._protected_var)\n",
            "try:\n",
            "    print(obj.__private_var)\n",
            "except AttributeError as e:\n",
            "    print(\"Private access failed:\", e)\n",
            "\n",
            "# Accessing mangled name\n",
            "print(\"Mangled access:\", obj._Outer__private_var)\n",
            "print(\"Inner Class data:\", obj.inner.data)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Implement a class `SecureConfig` that stores a private API token `__token`. Provide getter and setter methods to access and modify the token with length validation (>10 chars).\n",
            "2. Instantiate an inner class directly from outer scope (i.e. without instantiating it inside Outer's constructor)."
        ],
        "exercise_code": [
            "# Exercise 1: Encapsulated secure config\n",
            "class SecureConfig:\n",
            "    def __init__(self, token):\n",
            "        self.__token = token\n",
            "    def get_token(self): return self.__token\n",
            "    def set_token(self, token):\n",
            "        if len(token) > 10:\n",
            "            self.__token = token\n",
            "        else:\n",
            "            print(\"Invalid Token\")\n",
            "\n",
            "sc = SecureConfig(\"secret_token_123\")\n",
            "print(\"Token:\", sc.get_token())\n"
        ]
    },
    12: {
        "title": "Polymorphism, operator overloading, magic, dunder functions",
        "summary": "Dynamic polymorphism, customizing operator behavior using magic dunder methods.",
        "theory": [
            "### 1. Polymorphism\n",
            "Polymorphism allows different classes to have methods with the same name but different behaviors, allowing a unified interface to process diverse object types.\n",
            "\n",
            "### 2. Operator Overloading & Magic Methods\n",
            "Magic/Dunder (Double Underscore) methods allow you to define how custom objects behave with built-in operations (arithmetic, comparisons, length checks):\n",
            "- `__add__(self, other)`: Overloads addition (`+`)\n",
            "- `__sub__(self, other)`: Overloads subtraction (`-`)\n",
            "- `__mul__(self, other)`: Overloads multiplication (`*`)\n",
            "- `__len__(self)`: Custom return for `len()`\n",
            "- `__str__(self)`: Human-readable string representation (`print(obj)`)\n",
            "- `__repr__(self)`: Official string representation for debugging"
        ],
        "code": [
            "class Vector2D:\n",
            "    def __init__(self, x, y):\n",
            "        self.x = x\n",
            "        self.y = y\n",
            "        \n",
            "    # Overload addition (+)\n",
            "    def __add__(self, other):\n",
            "        return Vector2D(self.x + other.x, self.y + other.y)\n",
            "        \n",
            "    # Overload string representations\n",
            "    def __str__(self):\n",
            "        return f\"Vector({self.x}, {self.y})\"\n",
            "        \n",
            "    def __len__(self):\n",
            "        # Custom length: magnitude (integer part)\n",
            "        return int((self.x**2 + self.y**2)**0.5)\n",
            "\n",
            "v1 = Vector2D(3, 4)\n",
            "v2 = Vector2D(1, 2)\n",
            "v3 = v1 + v2\n",
            "\n",
            "print(\"Resulting Vector:\", v3)\n",
            "print(\"Magnitude of v1:\", len(v1))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Implement a class `HypothesisParameter` that stores a float parameter value. Overload the equality operator `==` (`__eq__`) so that two parameters are considered equal if their values are within a tolerance of `1e-5`.\n",
            "2. Overload the multiplication operator `*` (`__mul__`) for the `Vector2D` class to compute vector dot product: $v_1 \\cdot v_2 = x_1 x_2 + y_1 y_2$."
        ],
        "exercise_code": [
            "# Exercise 1: Parameters comparison\n",
            "class HypothesisParameter:\n",
            "    def __init__(self, val):\n",
            "        self.val = val\n",
            "    def __eq__(self, other):\n",
            "        return abs(self.val - other.val) < 1e-5\n",
            "\n",
            "p1 = HypothesisParameter(0.500001)\n",
            "p2 = HypothesisParameter(0.500002)\n",
            "print(\"p1 == p2:\", p1 == p2)\n"
        ]
    },
    13: {
        "title": "Abstract methods, data classes, keyword arguments",
        "summary": "Interface enforcement using Abstract Base Classes (ABCs), clean storage using dataclasses, and function signature positional/keyword limits.",
        "theory": [
            "### 1. Abstract Base Classes (ABCs)\n",
            "Abstract classes act as blueprints for subclasses. They cannot be instantiated directly and can enforce that derived classes implement specific methods using the `@abstractmethod` decorator from the `abc` module.\n",
            "\n",
            "### 2. Data Classes (`@dataclass`)\n",
            "Introduced in Python 3.7, the `@dataclass` decorator automatically generates common boilerplate methods like `__init__()`, `__repr__()`, and `__eq__()` based on type annotations.\n",
            "\n",
            "### 3. Argument Enforcement (`/`, `*`, `*args`, `**kwargs`)\n",
            "- `/`: Arguments before this symbol are **positional-only**.\n",
            "- `*`: Arguments after this symbol are **keyword-only**.\n",
            "- `*args`: Captures variable positional arguments.\n",
            "- `**kwargs`: Captures variable keyword arguments."
        ],
        "code": [
            "from abc import ABC, abstractmethod\n",
            "from dataclasses import dataclass\n",
            "\n",
            "# 1. Abstract Base Class\n",
            "class Estimator(ABC):\n",
            "    @abstractmethod\n",
            "    def fit(self, X, y):\n",
            "        pass\n",
            "\n",
            "class LinearEstimator(Estimator):\n",
            "    def fit(self, X, y):\n",
            "        print(\"Fitting linear weights...\")\n",
            "\n",
            "# 2. Dataclass Example\n",
            "@dataclass\n",
            "class Hyperparameters:\n",
            "    learning_rate: float\n",
            "    epochs: int\n",
            "    optimizer: str = \"SGD\"\n",
            "\n",
            "# 3. Argument Restriction function\n",
            "def train_model(X, y, /, *, verbose=False):\n",
            "    # X and y are positional-only, verbose is keyword-only\n",
            "    print(f\"Training. Verbose={verbose}\")\n",
            "\n",
            "est = LinearEstimator()\n",
            "est.fit(None, None)\n",
            "\n",
            "params = Hyperparameters(0.01, 100)\n",
            "print(\"Hyperparameters:\", params)\n",
            "\n",
            "train_model([1, 2], [3, 4], verbose=True)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Implement an abstract class `Metric` with an abstract method `compute(y_true, y_pred)`. Subclass `Accuracy` implementing the metric calculation.\n",
            "2. Modify `train_model` to accept variable positional parameters (`*args`) and variable keyword parameters (`**kwargs`), printing out whatever gets captured."
        ],
        "exercise_code": [
            "# Exercise 1: Metric ABC\n",
            "from abc import ABC, abstractmethod\n",
            "class Metric(ABC):\n",
            "    @abstractmethod\n",
            "    def compute(self, y_true, y_pred):\n",
            "        pass\n",
            "\n",
            "class Accuracy(Metric):\n",
            "    def compute(self, y_true, y_pred):\n",
            "        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)\n",
            "        return correct / len(y_true)\n",
            "\n",
            "acc = Accuracy()\n",
            "print(\"Accuracy:\", acc.compute([1, 0, 1], [1, 0, 0]))\n"
        ]
    }
}

# Pre-defined complete notebook cells for the 37 Math/Stats/Probability notebooks
PHASE_2_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Intro to ML and History",
        "summary": "Overview of Machine Learning, its historical roots, major milestones, and evolution from standard statistics to modern AI systems.",
        "theory": [
            "### 1. What is Machine Learning?\n",
            "Machine Learning (ML) is a branch of Artificial Intelligence (AI) that focuses on building systems that learn from data, identify patterns, and make decisions with minimal human intervention.\n",
            "\n",
            "### 2. Historical Milestones\n",
            "- **1950**: Alan Turing proposes the *Turing Test* to check machine intelligence.\n",
            "- **1952**: Arthur Samuel builds the first checkers-playing program that learns from games, coining the term **\"Machine Learning\"**.\n",
            "- **1957**: Frank Rosenblatt invents the *Perceptron*, the ancestor of modern neural networks.\n",
            "- **1986**: Geoffrey Hinton publishes the backpropagation algorithm for training multi-layer neural networks.\n",
            "- **1997**: IBM's *Deep Blue* defeats world chess champion Garry Kasparov.\n",
            "- **2012**: AlexNet wins the ImageNet competition, initiating the deep learning boom."
        ],
        "code": [
            "# Print historical milestones\n",
            "milestones = {\n",
            "    1952: \"Arthur Samuel coins 'Machine Learning'\",\n",
            "    1957: \"Rosenblatt Perceptron\",\n",
            "    1986: \"Backpropagation popularized by Hinton\",\n",
            "    2012: \"AlexNet wins ImageNet (Deep Learning revolution)\"\n",
            "}\n",
            "for year, event in milestones.items():\n",
            "    print(f\"{year}: {event}\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. List three differences between traditional rule-based programming and Machine Learning."
        ],
        "exercise_code": [
            "# Answer list\n",
            "print(\"1. Rules vs Data-Driven: Traditional uses rules+data->answers; ML uses data+answers->rules.\")\n",
            "print(\"2. Adaptability: ML models adapt automatically to new data.\")\n",
            "print(\"3. Scalability: ML solves complex problems where human rules are impossible to write.\")\n"
        ]
    },
    2: {
        "title": "What is ML and Real Life Examples",
        "summary": "Real-world applications of machine learning, framing tasks into inputs and targets.",
        "theory": [
            "### Real Life Examples of ML\n",
            "ML is embedded in many modern services:\n",
            "- **Spam Filtering**: Classifying emails as Spam or Ham based on words.\n",
            "- **Recommendation Systems**: Netflix/YouTube recommending videos using your watch history.\n",
            "- **Predictive Maintenance**: Predicting when a factory machine will fail based on sensor data.\n",
            "- **Financial Fraud Detection**: Flagging suspicious transactions based on spending behavior patterns."
        ],
        "code": [
            "# Map inputs and outputs for real-world tasks\n",
            "tasks = [\n",
            "    {\"task\": \"Spam Filtering\", \"input (X)\": \"Email text\", \"target (y)\": \"Spam/Not Spam\"},\n",
            "    {\"task\": \"House Pricing\", \"input (X)\": \"Size, Rooms, Location\", \"target (y)\": \"Price in USD\"}\n",
            "]\n",
            "import pandas as pd\n",
            "print(pd.DataFrame(tasks))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Frame an ML task of your own choice by listing the inputs (features) and target (labels)."
        ],
        "exercise_code": [
            "# Frame your own task\n",
            "print(\"Task: Customer Churn Prediction\")\n",
            "print(\"Inputs (X): Usage frequency, support calls, contract length\")\n",
            "print(\"Target (y): Churn (Yes/No)\")\n"
        ]
    },
    3: {
        "title": "AI vs ML vs DL",
        "summary": "Understanding boundaries between Artificial Intelligence, Machine Learning, and Deep Learning.",
        "theory": [
            "### 1. Venn Diagram Hierarchy\n",
            "```\n",
            "+--------------------------------------------------+\n",
            "| Artificial Intelligence (AI)                     |\n",
            "|   (Programs that mimic human intelligence)        |\n",
            "|                                                  |\n",
            "|   +------------------------------------------+   |\n",
            "|   | Machine Learning (ML)                    |   |\n",
            "|   |   (Algorithms that learn from data)      |   |\n",
            "|   |                                          |   |\n",
            "|   |   +----------------------------------+   |   |\n",
            "|   |   | Deep Learning (DL)               |   |   |\n",
            "|   |   |   (Multi-layer Neural Networks)  |   |   |\n",
            "|   |   +----------------------------------+   |   |\n",
            "|   +------------------------------------------+   |\n",
            "+--------------------------------------------------+\n",
            "```\n",
            "\n",
            "### 2. Definitions\n",
            "- **AI**: Broadest term. Covers anything simulating human intelligence (e.g. expert systems, pathfinding).\n",
            "- **ML**: Subset of AI. Systems that learn parameters from data instead of hardcoded rules.\n",
            "- **DL**: Subset of ML. Uses Deep Neural Networks with many hidden layers to automatically extract features from raw data (e.g. pixels, audio)."
        ],
        "code": [
            "# Simple check\n",
            "categories = [\"AI\", \"ML\", \"DL\"]\n",
            "for c in categories:\n",
            "    print(f\"{c} is a subset of the previous category (if any).\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Classify the following as AI-only, ML, or DL: (A) Chess engine using Alpha-Beta pruning, (B) Logistic Regression model, (C) Convolutional Neural Network (CNN) for face recognition."
        ],
        "exercise_code": [
            "print(\"A: AI-only (uses search heuristics)\")\n",
            "print(\"B: ML (classical machine learning)\")\n",
            "print(\"C: DL (uses deep neural networks)\")\n"
        ]
    },
    4: {
        "title": "Types of ML: Supervised, Unsupervised, RL",
        "summary": "Core paradigms of machine learning: learning from labeled data, finding patterns, or taking action in environments.",
        "theory": [
            "### 1. Supervised Learning\n",
            "Learning with a teacher. The dataset consists of input-output pairs $(X, y)$. Goal: learn a mapping function $f: X \\rightarrow y$.\n",
            "- **Regression**: Continuous output (e.g. predicting price).\n",
            "- **Classification**: Discrete labels (e.g. predicting spam/ham).\n",
            "\n",
            "### 2. Unsupervised Learning\n",
            "Learning without labels. Dataset consists only of inputs $X$. Goal: discover underlying structures or distributions.\n",
            "- **Clustering**: Grouping similar items (e.g. customer segmentation).\n",
            "- **Dimensionality Reduction**: Projecting data to fewer dimensions (e.g. PCA).\n",
            "\n",
            "### 3. Reinforcement Learning (RL)\n",
            "Learning by trial and error. An **agent** interacts with an **environment** by performing **actions** to maximize cumulative **rewards**."
        ],
        "code": [
            "paradigms = {\n",
            "    \"Supervised\": \"Labeled data (X, y)\",\n",
            "    \"Unsupervised\": \"Unlabeled data (X)\",\n",
            "    \"Reinforcement\": \"Agent, Environment, Actions, Rewards\"\n",
            "}\n",
            "for p, desc in paradigms.items():\n",
            "    print(f\"{p} Learning: {desc}\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Classify the task: Grouping news articles into topics. (Supervised or Unsupervised?)\n",
            "2. Classify the task: Predicting future stock price based on historical price patterns. (Regression or Classification?)"
        ],
        "exercise_code": [
            "print(\"1. Unsupervised (Clustering)\")\n",
            "print(\"2. Supervised (Regression)\")\n"
        ]
    },
    5: {
        "title": "Batch vs Online Learning",
        "summary": "Model updating strategies: offline batch training vs incremental updates from streaming data.",
        "theory": [
            "### 1. Batch (Offline) Learning\n",
            "The model is trained on the entire dataset at once. \n",
            "- If new data arrives, you must retrain a completely new model from scratch using old and new data.\n",
            "- Computationally heavy; updates happen infrequently.\n",
            "\n",
            "### 2. Online (Incremental) Learning\n",
            "The model is trained incrementally by feeding it data instances sequentially, either individually or in small groups (mini-batches).\n",
            "- Rapid adaptation to new data streams.\n",
            "- Low memory footprint.\n",
            "- **Out-of-Core Learning**: Training on datasets that do not fit into RAM."
        ],
        "code": [
            "print(\"Batch learning is standard for static datasets.\")\n",
            "print(\"Online learning is used for streaming stock data, traffic patterns, etc.\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What is the risk associated with Online Learning when feeding it corrupted or noisy data? (Hint: Catastrophic forgetting / model drift)."
        ],
        "exercise_code": [
            "print(\"Risk: If noisy/bad data is streamed in, model performance will degrade rapidly. Requires close monitoring.\")\n"
        ]
    },
    6: {
        "title": "Instance vs Model Based Learning",
        "summary": "How ML systems generalize from training data to predict unseen data.",
        "theory": [
            "### 1. Instance-Based Learning\n",
            "The system learns the training examples by heart, then generalizes to new cases by comparing them using a similarity metric (e.g. Euclidean distance).\n",
            "- **Example**: k-Nearest Neighbors (k-NN).\n",
            "- No training time (lazy learner), but high inference time.\n",
            "\n",
            "### 2. Model-Based Learning\n",
            "The system builds a model (parameterized mathematical equation) from the training data, then uses that model to make predictions.\n",
            "- **Example**: Linear Regression ($y = w_1 x + w_0$).\n",
            "- Long training time (eager learner) to optimize weights, but instant inference time."
        ],
        "code": [
            "# Simulate instance-based lookup\n",
            "training_instances = {\"x\": [1, 2, 3], \"y\": [2, 4, 6]}\n",
            "def predict_instance(new_x):\n",
            "    # Simple nearest neighbor lookup\n",
            "    dists = [abs(x - new_x) for x in training_instances[\"x\"]]\n",
            "    min_idx = dists.index(min(dists))\n",
            "    return training_instances[\"y\"][min_idx]\n",
            "\n",
            "print(\"Instance-based prediction for 2.2:\", predict_instance(2.2))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain why model-based learning is typically preferred over instance-based learning for low-latency web applications."
        ],
        "exercise_code": [
            "print(\"Model-based requires only a single mathematical operation at inference, making it extremely fast compared to searching through millions of stored training records.\")\n"
        ]
    },
    7: {
        "title": "Challenges in ML",
        "summary": "Common pitfalls in machine learning pipelines, including bad data, overfitting, and underfitting.",
        "theory": [
            "### Common Challenges\n",
            "1. **Insufficient Quantity of Data**: Models need thousands of examples to learn patterns.\n",
            "2. **Nonrepresentative Training Data**: Leads to sampling bias.\n",
            "3. **Poor Quality Data**: Noisy data, outliers, or missing features degrade model capacity.\n",
            "4. **Irrelevant Features**: 'Garbage in, garbage out'. Requires Feature Selection.\n",
            "5. **Overfitting**: Model performs well on training data but poorly on test data. Fixed by regularization, simple models, or more data.\n",
            "6. **Underfitting**: Model is too simple to learn the underlying structure. Fixed by complex models or better features."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "\n",
            "# Visualizing underfitting vs overfitting conceptually\n",
            "x = np.linspace(-3, 3, 20)\n",
            "y = 0.5 * x**3 - x + np.random.normal(0, 0.5, 20)\n",
            "\n",
            "plt.scatter(x, y, color='red', label='Data points')\n",
            "plt.plot(x, 0.5*x, label='Underfit (Linear)', color='blue')\n",
            "plt.plot(x, 0.5*x**3 - x, label='Perfect Fit (Cubic)', color='green')\n",
            "plt.legend()\n",
            "plt.title(\"Concept: Underfitting vs Perfect Fit\")\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Mention two ways to combat overfitting in machine learning models."
        ],
        "exercise_code": [
            "print(\"1. Regularization (L1/L2 penalty)\")\n",
            "print(\"2. Gather more training data, or simplify the model architecture.\")\n"
        ]
    },
    8: {
        "title": "Applications of ML",
        "summary": "Case studies of machine learning across healthcare, finance, transport, and language processing.",
        "theory": [
            "### Industry Applications\n",
            "- **Healthcare**: Tumor detection from MRI scans, drug discovery.\n",
            "- **Finance**: Algorithmic trading, credit scoring.\n",
            "- **Autonomous Vehicles**: Pedestrian detection, lane tracking.\n",
            "- **Natural Language Processing (NLP)**: Translation, sentiment analysis."
        ],
        "code": [
            "print(\"Industrial ML requires high reliability and model monitoring metrics.\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Name one ethical concern associated with deploying ML in credit scoring or resume screening."
        ],
        "exercise_code": [
            "print(\"Bias and Discrimination: If historical training data contains biases, the model will learn and perpetuate them.\")\n"
        ]
    },
    9: {
        "title": "ML Development Life Cycle",
        "summary": "Step-by-step pipeline of building an ML product from problem definition to monitoring.",
        "theory": [
            "### The Lifecycle Pipeline\n",
            "```\n",
            "[1. Define Problem] -> [2. Collect Data] -> [3. Prepare/Clean Data] \n",
            "                                                  |\n",
            "                                                  v\n",
            "[6. Monitor] <- [5. Deploy] <- [4. Train & Evaluate Model]\n",
            "```\n",
            "- **Problem Definition**: What are we trying to predict? How will we measure success?\n",
            "- **Data Prep**: Handling missing values, scaling, encoding.\n",
            "- **Model Training**: Hyperparameter tuning, validating models.\n",
            "- **Deployment & Monitoring**: Serving model endpoints, tracking model drift over time."
        ],
        "code": [
            "steps = [\n",
            "    \"1. Define Problem\", \"2. Collect Data\", \"3. Prepare Data\",\n",
            "    \"4. Train & Evaluate\", \"5. Deploy\", \"6. Monitor & Retrain\"\n",
            "]\n",
            "for idx, step in enumerate(steps, 1):\n",
            "    print(f\"Step {idx}: {step}\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is monitoring crucial after deployment? (Hint: Data drift / Concept drift)."
        ],
        "exercise_code": [
            "print(\"Data drift occurs when real-world data distribution changes over time, causing accuracy to degrade. Monitoring alerts us when to retrain the model.\")\n"
        ]
    },
    10: {
        "title": "Stanford CS229 Lec 1: Full ML intro, framing problems",
        "summary": "Notes on Andrew Ng's CS229 Lecture 1 covering syllabus, problem framing, and linear classification vs regression.",
        "theory": [
            "### CS229 Lecture 1 Takeaways\n",
            "- **Supervised Learning**: Learn mapping function from $X$ to $y$. Example: housing prediction.\n",
            "- **Unsupervised Learning**: Learn structures, like grouping. Example: microarray gene grouping, social network analysis.\n",
            "- **Reinforcement Learning**: Uses rewards. Example: helicopter autopilot.\n",
            "- **Problem Formulation**: Choose features $x^{(i)}$ and target labels $y^{(i)}$ carefully. Ensure the data is clean and matches the task objective."
        ],
        "code": [
            "print(\"CS229 is the gold standard course for ML mathematical foundations.\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. If we have a dataset of tumors labeled benign or malignant, which learning paradigm is this?"
        ],
        "exercise_code": [
            "print(\"Supervised learning (specifically Classification)\")\n"
        ]
    },
    11: {
        "title": "Linear Algebra: Vectors, Dot Product, Vector Norms, Matrix Operations",
        "summary": "Mathematical basics of vectors, matrices, dot products, matrix multiplication, and Vector Norms.",
        "theory": [
            "### 1. Vectors & Dot Product\n",
            "A vector $\\mathbf{x} \\in \\mathbb{R}^n$ is an ordered sequence of numbers. \n",
            "The **dot product** of two vectors $\\mathbf{u}, \\mathbf{v} \\in \\mathbb{R}^n$ is:\n",
            "$$\\mathbf{u} \\cdot \\mathbf{v} = \\sum_{i=1}^n u_i v_i = \\mathbf{u}^T \\mathbf{v}$$\n",
            "\n",
            "### 2. Vector Norms\n",
            "Norms measure vector magnitude (size):\n",
            "- **$L_1$ Norm (Manhattan)**: $\\|\\mathbf{x}\\|_1 = \\sum |x_i|$\n",
            "- **$L_2$ Norm (Euclidean)**: $\\|\\mathbf{x}\\|_2 = \\sqrt{\\sum x_i^2}$\n",
            "\n",
            "### 3. Matrix Multiplication\n",
            "If $A$ is $m \\times n$ and $B$ is $n \\times p$, then $C = AB$ is $m \\times p$:\n",
            "$$C_{ij} = \\sum_{k=1}^n A_{ik} B_{kj}$$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "u = np.array([1, 2, 3])\n",
            "v = np.array([4, 5, 6])\n",
            "\n",
            "print(\"Dot Product:\", np.dot(u, v))\n",
            "print(\"L1 Norm of u:\", np.linalg.norm(u, 1))\n",
            "print(\"L2 Norm of u:\", np.linalg.norm(u, 2))\n",
            "\n",
            "A = np.array([[1, 2], [3, 4]])\n",
            "B = np.array([[5, 6], [7, 8]])\n",
            "print(\"Matrix Multiplication AB:\\n\", np.dot(A, B))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "\n",
            "1. Calculate by hand and write a NumPy block to compute the Euclidean distance between $\\mathbf{p} = [1, 1]$ and $\\mathbf{q} = [4, 5]$."
        ],
        "exercise_code": [
            "p = np.array([1, 1])\n",
            "q = np.array([4, 5])\n",
            "dist = np.linalg.norm(p - q)\n",
            "print(\"Distance:\", dist)  # Should be 5.0 (sqrt(3^2 + 4^2))\n"
        ]
    },
    12: {
        "title": "Linear Algebra: Systems of Linear Equations, Matrix Inverse, Transpose",
        "summary": "Representing systems of linear equations in matrix form, matrix transposition, identity matrices, and matrix inverses.",
        "theory": [
            "### 1. Matrix Transpose\n",
            "The transpose $A^T$ of matrix $A$ swaps rows with columns: $(A^T)_{ij} = A_{ji}$.\n",
            "Properties: $(AB)^T = B^T A^T$.\n",
            "\n",
            "### 2. Systems of Linear Equations\n",
            "A system of equations can be written as:\n",
            "$$A\\mathbf{x} = \\mathbf{b}$$\n",
            "\n",
            "### 3. Matrix Inverse\n",
            "If $A$ is square, its inverse $A^{-1}$ satisfies:\n",
            "$$A A^{-1} = A^{-1} A = I$$\n",
            "where $I$ is the Identity matrix. If $\\det(A) \\neq 0$, the inverse exists, and:\n",
            "$$\\mathbf{x} = A^{-1}\\mathbf{b}$$\n",
            "In ML, inverses are crucial for solving Normal Equations in Linear Regression."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "A = np.array([[2, 1], [1, 3]])\n",
            "b = np.array([5, 5])\n",
            "\n",
            "# Solve Ax = b\n",
            "x = np.linalg.solve(A, b)\n",
            "print(\"Solution x:\", x)\n",
            "\n",
            "# Transpose and Inverse\n",
            "print(\"A Transpose:\\n\", A.T)\n",
            "print(\"A Inverse:\\n\", np.linalg.inv(A))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Solve the system $2x + y = 8$, $x - y = 1$ using matrix inverse."
        ],
        "exercise_code": [
            "A = np.array([[2, 1], [1, -1]])\n",
            "b = np.array([8, 1])\n",
            "x = np.dot(np.linalg.inv(A), b)\n",
            "print(\"x, y:\", x)  # x=3, y=2\n"
        ]
    },
    13: {
        "title": "Linear Algebra: Determinants, Orthogonality, Eigenvalues and Eigenvectors",
        "summary": "Determinants, orthogonal vectors, matrix decomposition, eigenvalues, and eigenvectors.",
        "theory": [
            "### 1. Determinants\n",
            "The determinant $\\det(A)$ of a square matrix describes its scaling factor. If $\\det(A) = 0$, the matrix is singular (no inverse).\n",
            "\n",
            "### 2. Orthogonality\n",
            "Two vectors are orthogonal if their dot product is zero: $\\mathbf{u} \\cdot \\mathbf{v} = 0$.\n",
            "\n",
            "### 3. Eigenvalues & Eigenvectors\n",
            "For a square matrix $A$, a non-zero vector $\\mathbf{v}$ is an **eigenvector** if:\n",
            "$$A\\mathbf{v} = \\lambda\\mathbf{v}$$\n",
            "where $\\lambda$ is a scalar called the **eigenvalue**.\n",
            "- Critical for Dimensionality Reduction (PCA) and Spectral Clustering."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "A = np.array([[4, 2], [1, 3]])\n",
            "eigenvalues, eigenvectors = np.linalg.eig(A)\n",
            "\n",
            "print(\"Eigenvalues:\", eigenvalues)\n",
            "print(\"Eigenvectors:\\n\", eigenvectors)\n",
            "print(\"Determinant of A:\", np.linalg.det(A))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Define a symmetric matrix $S = \\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \\end{bmatrix}$ and compute its eigenvalues. Verify that eigenvectors of symmetric matrices are orthogonal."
        ],
        "exercise_code": [
            "S = np.array([[2, 1], [1, 2]])\n",
            "vals, vecs = np.linalg.eig(S)\n",
            "# vecs[:, 0] is first eigenvector, vecs[:, 1] is second\n",
            "dot_prod = np.dot(vecs[:, 0], vecs[:, 1])\n",
            "print(\"Dot product of eigenvectors (orthogonal):\", np.round(dot_prod, 5))\n"
        ]
    },
    14: {
        "title": "Calculus: Limits, Derivatives, and Differentiation Rules",
        "summary": "Fundamentals of single-variable calculus, derivatives, power rule, product rule, and quotient rule.",
        "theory": [
            "### 1. Limits and Derivatives\n",
            "The derivative of $f(x)$ measures the instantaneous rate of change of $f$ with respect to $x$:\n",
            "$$f'(x) = \\lim_{h \\to 0} \\frac{f(x+h) - f(x)}{h}$$\n",
            "\n",
            "### 2. Standard Rules of Differentiation\n",
            "- **Power Rule**: $\\frac{d}{dx}[x^n] = n x^{n-1}$\n",
            "- **Constant Factor**: $\\frac{d}{dx}[c \\cdot f(x)] = c \\cdot f'(x)$\n",
            "- **Sum/Difference Rule**: $\\frac{d}{dx}[f(x) \\pm g(x)] = f'(x) \\pm g'(x)$\n",
            "- **Product Rule**: $\\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$\n",
            "- **Quotient Rule**: $\\frac{d}{dx}[\\frac{f(x)}{g(x)}] = \\frac{f'(x)g(x) - f(x)g'(x)}{(g(x))^2}$"
        ],
        "code": [
            "# Numerical differentiation in python\n",
            "def f(x):\n",
            "    return x**2 + 3*x\n",
            "\n",
            "def derivative(func, x, h=1e-5):\n",
            "    return (func(x + h) - func(x)) / h\n",
            "\n",
            "print(\"Numerical derivative at x=2:\", derivative(f, 2))\n",
            "print(\"Analytical derivative at x=2 (2x + 3):\", 2*2 + 3)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Find the derivative of $f(x) = 3x^3 - 5x^2 + 2$ at $x = 1$ analytically and verify numerically."
        ],
        "exercise_code": [
            "func = lambda x: 3*(x**3) - 5*(x**2) + 2\n",
            "print(\"Numerical:\", derivative(func, 1))\n"
        ]
    },
    15: {
        "title": "Calculus: Partial Derivatives, Gradients, and Chain Rule",
        "summary": "Multi-variable derivatives, partial derivatives, the Gradient vector, and Multi-variable Chain Rule.",
        "theory": [
            "### 1. Partial Derivatives\n",
            "For a function of multiple variables $f(x, y)$, the partial derivative $\\frac{\\partial f}{\\partial x}$ is computed by treating all other variables (like $y$) as constants.\n",
            "\n",
            "### 2. The Gradient\n",
            "The **gradient** $\\nabla f(\\mathbf{x})$ is a vector of all partial derivatives:\n",
            "$$\\nabla f(x, y) = \\begin{bmatrix} \\frac{\\partial f}{\\partial x} \\\\ \\frac{\\partial f}{\\partial y} \\end{bmatrix}$$\n",
            "- The gradient points in the direction of steepest ascent.\n",
            "- Used to update weights in Gradient Descent: $\\mathbf{w} \\leftarrow \\mathbf{w} - \\alpha \\nabla L(\\mathbf{w})$.\n",
            "\n",
            "### 3. Chain Rule\n",
            "For nested functions $y = f(g(x))$:\n",
            "$$\\frac{dy}{dx} = f'(g(x)) \\cdot g'(x)$$\n",
            "Critical for backpropagation in neural networks."
        ],
        "code": [
            "# Compute numerical gradient of f(x, y) = x^2 + 3xy + y^2 at (1, 2)\n",
            "def f(x, y):\n",
            "    return x**2 + 3*x*y + y**2\n",
            "\n",
            "h = 1e-5\n",
            "grad_x = (f(1 + h, 2) - f(1, 2)) / h\n",
            "grad_y = (f(1, 2 + h) - f(1, 2)) / h\n",
            "\n",
            "print(\"Numerical Gradient at (1, 2):\", [grad_x, grad_y])\n",
            "print(\"Analytical Gradient at (1, 2) [2x+3y, 3x+2y]:\", [2*1 + 3*2, 3*1 + 2*2])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Given loss function $L(w) = (y - (w x + b))^2$. Calculate partial derivatives $\\frac{\\partial L}{\\partial w}$ and $\\frac{\\partial L}{\\partial b}$ using the chain rule."
        ],
        "exercise_code": [
            "print(\"dL/dw = -2 * x * (y - (w*x + b))\")\n",
            "print(\"dL/db = -2 * (y - (w*x + b))\")\n"
        ]
    },
    16: {
        "title": "Calculus: Optimization Basics (Maxima, Minima, Convexity)",
        "summary": "Finding critical points, second derivative tests, and convexity in optimization problems.",
        "theory": [
            "### 1. Critical Points (Local Maxima/Minima)\n",
            "A critical point of $f(x)$ occurs where $f'(x) = 0$:\n",
            "- **Local Minimum**: $f'(x) = 0$ and $f''(x) > 0$ (concave up).\n",
            "- **Local Maximum**: $f'(x) = 0$ and $f''(x) < 0$ (concave down).\n",
            "\n",
            "### 2. Convexity\n",
            "A function $f(x)$ is **convex** if the line segment between any two points on its graph lies above or on the graph. \n",
            "- In multi-variable calculus, $f$ is convex if its Hessian matrix $H$ (second derivative matrix) is positive semi-definite.\n",
            "- **Convex Optimization**: Crucial in ML because any local minimum is guaranteed to be the global minimum (e.g. Linear Regression, SVM)."
        ],
        "code": [
            "# Plotting a convex function f(x) = x^2\n",
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "\n",
            "x = np.linspace(-10, 10, 100)\n",
            "y = x**2\n",
            "\n",
            "plt.plot(x, y, label='f(x) = x^2 (Convex)')\n",
            "plt.scatter([0], [0], color='red', zorder=5, label='Global Min (0, 0)')\n",
            "plt.title(\"Convex Optimization Space\")\n",
            "plt.legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Find the global minimum of $f(x) = x^2 - 4x + 7$ by setting the first derivative to zero."
        ],
        "exercise_code": [
            "# f'(x) = 2x - 4 = 0 => x = 2\n",
            "print(\"Global minimum x coordinate:\", 2)\n"
        ]
    },
    17: {
        "title": "Data types: structured or unstructured, quantitative or qualitative",
        "summary": "Introduction to data classification types: structured databases vs unstructured media, and numerical vs categorical properties.",
        "theory": [
            "### Data Classification Schema\n",
            "\n",
            "```\n",
            "              DATA TYPES\n",
            "              /        \\\n",
            "     Structured        Unstructured\n",
            "     (Tables, CSV)     (Text, Images, Audio)\n",
            "       /      \\ \n",
            " Quantitative  Qualitative (Categorical)\n",
            " (Numerical)   |-- Nominal (No order: e.g. Red, Blue)\n",
            "   |           |-- Ordinal (Ordered: e.g. Low, High)\n",
            "   |-- Discrete (Counts: e.g. 5 children)\n",
            "   |-- Continuous (Measurements: e.g. 1.75 meters)\n",
            "```\n",
            "- **Structured Data**: Fits in row-column database schemas.\n",
            "- **Unstructured Data**: Raw media. Needs special preprocessing (feature extraction) to be used in ML.\n",
            "- **Quantitative**: Numerical data (Discrete vs Continuous).\n",
            "- **Qualitative**: Categorical data (Nominal vs Ordinal)."
        ],
        "code": [
            "import pandas as pd\n",
            "df = pd.DataFrame({\n",
            "    \"Height (Continuous)\": [1.75, 1.82, 1.68],\n",
            "    \"Children (Discrete)\": [2, 0, 3],\n",
            "    \"Education (Ordinal)\": [\"BSc\", \"PhD\", \"MSc\"],\n",
            "    \"City (Nominal)\": [\"Karachi\", \"Lahore\", \"Islamabad\"]\n",
            "})\n",
            "print(df)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Classify the variable: Movie Rating (1 star, 2 stars, 3 stars...).\n",
            "2. Classify the variable: Daily temperature in Celsius."
        ],
        "exercise_code": [
            "print(\"1. Qualitative Ordinal\")\n",
            "print(\"2. Quantitative Continuous\")\n"
        ]
    },
    18: {
        "title": "Statistics and its types",
        "summary": "Boundaries and definition of Descriptive Statistics vs Inferential Statistics.",
        "theory": [
            "### Types of Statistics\n",
            "\n",
            "### 1. Descriptive Statistics\n",
            "Methods to summarize and describe the features of a specific dataset:\n",
            "- Measures of Central Tendency: Mean, Median, Mode.\n",
            "- Measures of Dispersion: Variance, Standard Deviation, Range.\n",
            "- Distribution shapes: Skewness, Kurtosis.\n",
            "\n",
            "### 2. Inferential Statistics\n",
            "Methods to make predictions or draw conclusions about a larger population based on a sample of data:\n",
            "- Hypothesis Testing (z-test, t-test, Chi square).\n",
            "- Confidence Intervals.\n",
            "- Point Estimations."
        ],
        "code": [
            "import numpy as np\n",
            "data = [2, 4, 4, 4, 5, 5, 7, 9]\n",
            "print(\"Descriptive Mean:\", np.mean(data))\n",
            "print(\"Descriptive StdDev:\", np.std(data))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Classify: A survey of 100 voters shows 52% support candidate A, and we conclude candidate A has a 95% chance of winning the city-wide election. (Descriptive or Inferential?)"
        ],
        "exercise_code": [
            "print(\"Inferential Statistics (making inferences about population from sample)\")\n"
        ]
    },
    19: {
        "title": "Mean, Median, Mode",
        "summary": "Measures of central tendency: mathematical formulation and application to data.",
        "theory": [
            "### Measures of Central Tendency\n",
            "\n",
            "### 1. Mean (Arithmetic Average)\n",
            "$$\\mu = \\frac{1}{N} \\sum_{i=1}^N x_i$$\n",
            "- Sensitive to extreme outliers.\n",
            "\n",
            "### 2. Median (Middle Value)\n",
            "The middle value when data is sorted in ascending order. If $N$ is even, it is the average of the two middle values.\n",
            "- **Robust to outliers**.\n",
            "\n",
            "### 3. Mode (Most Frequent)\n",
            "The value that occurs most frequently in the dataset.\n",
            "- Useful for categorical data."
        ],
        "code": [
            "import numpy as np\n",
            "from scipy import stats\n",
            "\n",
            "dataset = [1, 2, 2, 3, 4, 100]  # 100 is an outlier\n",
            "\n",
            "print(\"Mean:\", np.mean(dataset))\n",
            "print(\"Median:\", np.median(dataset))  # Much more representative middle\n",
            "print(\"Mode:\", stats.mode(dataset, keepdims=True).mode[0])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the mean and median of the list: `[10, 20, 30, 40, 50, 1000]`. Discuss which metric is better here."
        ],
        "exercise_code": [
            "vals = [10, 20, 30, 40, 50, 1000]\n",
            "print(\"Mean:\", np.mean(vals))\n",
            "print(\"Median:\", np.median(vals))\n"
        ]
    },
    20: {
        "title": "Variance and Standard Deviation",
        "summary": "Measures of data dispersion: Variance and Standard Deviation formulations for populations and samples.",
        "theory": [
            "### 1. Population Variance ($\\sigma^2$)\n",
            "Average of squared differences from the Mean:\n",
            "$$\\sigma^2 = \\frac{1}{N} \\sum_{i=1}^N (x_i - \\mu)^2$$\n",
            "\n",
            "### 2. Sample Variance ($s^2$)\n",
            "Uses Bessel's correction ($N-1$ in denominator) to provide an unbiased estimate:\n",
            "$$s^2 = \\frac{1}{N-1} \\sum_{i=1}^n (x_i - \\bar{x})^2$$\n",
            "\n",
            "### 3. Standard Deviation ($\\sigma$ or $s$)\n",
            "The square root of the variance, returning dispersion to the original measurement units:\n",
            "$$\\sigma = \\sqrt{\\sigma^2}$$"
        ],
        "code": [
            "import numpy as np\n",
            "data = [2, 4, 4, 6, 8]\n",
            "\n",
            "print(\"Population Variance:\", np.var(data))\n",
            "print(\"Sample Variance (ddof=1):\", np.var(data, ddof=1))\n",
            "print(\"Standard Deviation:\", np.std(data))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Given a dataset: `[5, 10, 15]`. Compute the sample variance and sample standard deviation by hand, then check with NumPy."
        ],
        "exercise_code": [
            "data = [5, 10, 15]\n",
            "print(\"Sample Variance:\", np.var(data, ddof=1))  # (5^2 + 0^2 + 5^2)/(3-1) = 50/2 = 25\n",
            "print(\"Sample StdDev:\", np.std(data, ddof=1))    # sqrt(25) = 5\n"
        ]
    },
    21: {
        "title": "Coefficient of variation, Z score, Percentile, Quartile",
        "summary": "Descriptive statistics measurements: relative variance, standardizing data, and positional splits.",
        "theory": [
            "### 1. Coefficient of Variation (CV)\n",
            "Relative standard deviation (dimensionless): $CV = \\frac{\\sigma}{\\mu}$. Used to compare variance across different scales.\n",
            "\n",
            "### 2. Z Score\n",
            "Measures how many standard deviations a data point $x$ is from the mean:\n",
            "$$z = \\frac{x - \\mu}{\\sigma}$$\n",
            "- Used to detect outliers (typically $|z| > 3$).\n",
            "\n",
            "### 3. Percentiles and Quartiles\n",
            "- **Percentile**: The value below which a percentage of data falls (e.g. 90th percentile).\n",
            "- **Quartiles**: Splits sorted data into four equal groups:\n",
            "  - $Q_1$: 25th percentile (lower quartile).\n",
            "  - $Q_2$: 50th percentile (Median).\n",
            "  - $Q_3$: 75th percentile (upper quartile)."
        ],
        "code": [
            "import numpy as np\n",
            "data = [10, 12, 14, 15, 18, 20, 22, 100]  # 100 is outlier\n",
            "\n",
            "# Calculate Z scores\n",
            "mean = np.mean(data)\n",
            "std = np.std(data)\n",
            "z_scores = [(x - mean) / std for x in data]\n",
            "print(\"Z scores:\", np.round(z_scores, 2))\n",
            "\n",
            "# Percentiles\n",
            "print(\"25th percentile (Q1):\", np.percentile(data, 25))\n",
            "print(\"75th percentile (Q3):\", np.percentile(data, 75))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Using z-score threshold $>2$, find the outliers in `data = [10, 12, 14, 15, 18, 20, 22, 100]`."
        ],
        "exercise_code": [
            "outliers = [x for x in data if abs((x - mean)/std) > 2]\n",
            "print(\"Outliers:\", outliers)\n"
        ]
    },
    22: {
        "title": "Skewness and Kurtosis",
        "summary": "Measures of distribution shape: asymmetry (skewness) and tail weight (kurtosis).",
        "theory": [
            "### 1. Skewness (Measure of Asymmetry)\n",
            "- **Positive (Right) Skew**: Tail extends to the right. $\\text{Mean} > \\text{Median} > \\text{Mode}$.\n",
            "- **Negative (Left) Skew**: Tail extends to the left. $\\text{Mean} < \\text{Median} < \\text{Mode}$.\n",
            "- **Symmetric**: Skewness $\\approx 0$.\n",
            "\n",
            "### 2. Kurtosis (Measure of Tailedness)\n",
            "Measures the thickness/weight of the tails of a distribution relative to a Normal distribution:\n",
            "- **Mesokurtic**: Kurtosis $= 3$ (Normal distribution).\n",
            "- **Leptokurtic**: Kurtosis $> 3$ (heavy tails, high peak).\n",
            "- **Platykurtic**: Kurtosis $< 3$ (thin tails, flat peak)."
        ],
        "code": [
            "from scipy.stats import skew, kurtosis\n",
            "import numpy as np\n",
            "\n",
            "# Generate asymmetric right-skewed data\n",
            "data = np.random.exponential(scale=2, size=1000)\n",
            "print(\"Skewness:\", skew(data))\n",
            "print(\"Kurtosis:\", kurtosis(data))  # excess kurtosis (kurtosis - 3)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. If a stock's returns have high positive Kurtosis, what does that mean for an investor? (Hint: extreme market movements / outliers)."
        ],
        "exercise_code": [
            "print(\"High kurtosis indicates high probability of extreme values (outliers), indicating higher investment risk.\")\n"
        ]
    },
    23: {
        "title": "Correlation Coefficient: Pearson's",
        "summary": "Quantifying the linear relationship between two variables using Pearson's correlation coefficient.",
        "theory": [
            "### Pearson Correlation Coefficient ($r$)\n",
            "Measures the strength and direction of the linear relationship between two continuous variables:\n",
            "$$r = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum (x_i - \\bar{x})^2 \\sum (y_i - \\bar{y})^2}}$$\n",
            "- Range: $[-1, 1]$.\n",
            "- $r = 1$: Perfect positive linear correlation.\n",
            "- $r = -1$: Perfect negative linear correlation.\n",
            "- $r = 0$: No linear correlation."
        ],
        "code": [
            "import numpy as np\n",
            "x = np.array([1, 2, 3, 4, 5])\n",
            "y = np.array([2.1, 3.9, 6.2, 8.1, 9.9])  # highly correlated\n",
            "\n",
            "r = np.corrcoef(x, y)[0, 1]\n",
            "print(\"Pearson correlation coefficient r:\", r)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. If $y = -2x + 5$, what is the Pearson correlation coefficient between $x$ and $y$?"
        ],
        "exercise_code": [
            "print(\"r = -1.0 (perfect negative linear relationship)\")\n"
        ]
    },
    24: {
        "title": "Covariance",
        "summary": "Measures how two variables move together: direction of linear relationship.",
        "theory": [
            "### Covariance\n",
            "Covariance measures the joint variability of two random variables:\n",
            "$$\\text{Cov}(X, Y) = \\frac{1}{N} \\sum_{i=1}^N (x_i - \\mu_x)(y_i - \\mu_y)$$\n",
            "- **Positive Covariance**: As $X$ increases, $Y$ tends to increase.\n",
            "- **Negative Covariance**: As $X$ increases, $Y$ tends to decrease.\n",
            "- Unlike correlation, covariance is **scale-dependent** (changing data units changes the covariance value)."
        ],
        "code": [
            "import numpy as np\n",
            "x = np.array([1, 2, 3, 4, 5])\n",
            "y = np.array([2, 4, 6, 8, 10])\n",
            "\n",
            "cov_matrix = np.cov(x, y, ddof=0)\n",
            "print(\"Covariance Matrix:\\n\", cov_matrix)\n",
            "print(\"Cov(x, y):\", cov_matrix[0, 1])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Show mathematically that $\\text{Cov}(X, X) = \\text{Var}(X)$."
        ],
        "exercise_code": [
            "print(\"Cov(X, X) = E[(X - ux)(X - ux)] = E[(X - ux)^2] = Var(X)\")\n"
        ]
    },
    25: {
        "title": "Probability basics",
        "summary": "Fundamental rules of probability, sample spaces, and events.",
        "theory": [
            "### Probability Foundations\n",
            "- **Sample Space ($S$)**: Set of all possible outcomes (e.g. for a coin toss: $\\{H, T\\}$).\n",
            "- **Event ($A$)**: A subset of the sample space.\n",
            "- **Probability of Event ($P(A)$)**:\n",
            "  $$0 \\le P(A) \\le 1$$\n",
            "  $$P(S) = 1$$\n",
            "- **Complement Rule**: $P(A^c) = 1 - P(A)$.\n",
            "- **Addition Rule**: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$."
        ],
        "code": [
            "# Simulate roll of a fair die\n",
            "import numpy as np\n",
            "rolls = np.random.randint(1, 7, size=10000)\n",
            "prob_even = np.sum(rolls % 2 == 0) / len(rolls)\n",
            "print(\"Simulated Probability of rolling an even number:\", prob_even)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Two cards are drawn from a standard 52-card deck. What is the probability that both are Aces if the first card is replaced before drawing the second?"
        ],
        "exercise_code": [
            "prob = (4/52) * (4/52)\n",
            "print(\"Probability:\", prob)\n"
        ]
    },
    26: {
        "title": "Joint, Marginal and Conditional Probability",
        "summary": "Multi-event spaces: calculating combined probabilities, slice probabilities, and dependencies.",
        "theory": [
            "### Probabilities in Multi-Event Spaces\n",
            "\n",
            "### 1. Joint Probability\n",
            "The probability of two events occurring simultaneously: $P(A \\cap B)$ or $P(A, B)$.\n",
            "\n",
            "### 2. Marginal Probability\n",
            "The probability of a single event occurring, ignoring other variables:\n",
            "$$P(A) = \\sum_b P(A, B=b)$$\n",
            "\n",
            "### 3. Conditional Probability\n",
            "The probability of event $A$ occurring given that event $B$ has already occurred:\n",
            "$$P(A | B) = \\frac{P(A \\cap B)}{P(B)}$$\n",
            "- **Independent Events**: If $A$ and $B$ are independent, $P(A | B) = P(A)$, and $P(A \\cap B) = P(A)P(B)$."
        ],
        "code": [
            "# Simple contingency table simulation\n",
            "# rows: Gender (0=Male, 1=Female), cols: Prefers Python (0=No, 1=Yes)\n",
            "table = np.array([[30, 20], [10, 40]])  # sum = 100\n",
            "\n",
            "joint_prob_female_python = table[1, 1] / 100  # P(F, Yes)\n",
            "marginal_prob_python = np.sum(table[:, 1]) / 100  # P(Yes)\n",
            "conditional_female_given_python = table[1, 1] / np.sum(table[:, 1])  # P(F | Yes)\n",
            "\n",
            "print(\"Joint Probability P(Female, Yes):\", joint_prob_female_python)\n",
            "print(\"Marginal Probability P(Yes):\", marginal_prob_python)\n",
            "print(\"Conditional Probability P(Female | Yes):\", conditional_female_given_python)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Given $P(A) = 0.6$, $P(B) = 0.4$, and $P(A \\cap B) = 0.2$. Find $P(A | B)$."
        ],
        "exercise_code": [
            "p_a_given_b = 0.2 / 0.4\n",
            "print(\"P(A|B):\", p_a_given_b)  # 0.5\n"
        ]
    },
    27: {
        "title": "Bayes Theorem",
        "summary": "Inverting conditional probabilities using prior belief and likelihood inputs.",
        "theory": [
            "### Bayes' Theorem\n",
            "Allows us to update our probability beliefs for a hypothesis $H$ given new evidence $E$:\n",
            "$$P(H | E) = \\frac{P(E | H) P(H)}{P(E)}$$\n",
            "\n",
            "- $P(H | E)$: **Posterior probability** (probability of hypothesis given evidence).\n",
            "- $P(E | H)$: **Likelihood** (probability of evidence given hypothesis).\n",
            "- $P(H)$: **Prior probability** (initial probability of hypothesis before evidence).\n",
            "- $P(E)$: **Marginal likelihood** (normalizing constant): $P(E) = P(E|H)P(H) + P(E|H^c)P(H^c)$.\n",
            "\n",
            "Crucial for Bayesian Classifiers (Naive Bayes) in classification pipelines."
        ],
        "code": [
            "# Cancer screening problem\n",
            "# H: has cancer, E: positive test\n",
            "# P(H) = 0.01 (prior)\n",
            "# P(E | H) = 0.95 (sensitivity / likelihood)\n",
            "# P(E | not H) = 0.05 (false positive rate)\n",
            "\n",
            "p_h = 0.01\n",
            "p_e_given_h = 0.95\n",
            "p_e_given_not_h = 0.05\n",
            "\n",
            "# P(E) = P(E|H)P(H) + P(E|not H)P(not H)\n",
            "p_e = (p_e_given_h * p_h) + (p_e_given_not_h * (1 - p_h))\n",
            "\n",
            "p_h_given_e = (p_e_given_h * p_h) / p_e\n",
            "print(\"Posterior Probability P(Cancer | Positive Test):\", round(p_h_given_e, 4))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. A spam filter detects 99% of spam emails. 1% of normal emails are falsely marked as spam. If 10% of all incoming emails are spam, what is the probability that an email marked as spam is actually spam?"
        ],
        "exercise_code": [
            "p_spam = 0.10\n",
            "p_s_given_spam = 0.99\n",
            "p_s_given_ham = 0.01\n",
            "p_s = (p_s_given_spam * p_spam) + (p_s_given_ham * (1 - p_spam))\n",
            "p_spam_given_s = (p_s_given_spam * p_spam) / p_s\n",
            "print(\"P(Spam | Marked Spam):\", round(p_spam_given_s, 4))  # ~91.6%\n"
        ]
    },
    28: {
        "title": "Probability distributions: Discrete and Continuous",
        "summary": "Probability mass functions vs probability density functions, and common distributions.",
        "theory": [
            "### Probability Distributions\n",
            "\n",
            "### 1. Discrete Distributions\n",
            "Variables take countable values. Described by a **Probability Mass Function (PMF)** where $\\sum P(X=x) = 1$.\n",
            "- **Bernoulli**: Single trial with binary outcome (success $p$, failure $1-p$).\n",
            "- **Binomial**: Number of successes in $n$ independent Bernoulli trials.\n",
            "\n",
            "### 2. Continuous Distributions\n",
            "Variables take uncountable values in an interval. Described by a **Probability Density Function (PDF)** where $\\int_{-\\infty}^{\\infty} f(x) dx = 1$.\n",
            "- **Normal (Gaussian)**: Bell-shaped curve centered at mean $\\mu$ with standard deviation $\\sigma$.\n",
            "- **Uniform**: Equal probability density over an interval $[a, b]$."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "import scipy.stats as stats\n",
            "\n",
            "# Generate normal distribution PDF\n",
            "x = np.linspace(-4, 4, 100)\n",
            "y = stats.norm.pdf(x, 0, 1)\n",
            "\n",
            "plt.plot(x, y, label='Standard Normal PDF')\n",
            "plt.title(\"Normal Distribution\")\n",
            "plt.legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Generate a binomial distribution PMF for $n=10$ trials and $p=0.5$ using `scipy.stats.binom` and print probabilities of getting exactly 5 heads."
        ],
        "exercise_code": [
            "import scipy.stats as stats\n",
            "prob_5 = stats.binom.pmf(5, n=10, p=0.5)\n",
            "print(\"P(X=5) for Binomial(10, 0.5):\", prob_5)\n"
        ]
    },
    29: {
        "title": "Bayesian Probability deep dive",
        "summary": "Theoretical contrast between Frequentist and Bayesian philosophies, and conjugate priors.",
        "theory": [
            "### Frequentist vs Bayesian Views\n",
            "- **Frequentist**: Probability represents the limit of relative frequency in infinite repeated trials. Parameters are fixed but unknown.\n",
            "- **Bayesian**: Probability measures degrees of belief or certainty. Parameters are treated as random variables with distributions.\n",
            "\n",
            "### Conjugate Priors\n",
            "In Bayesian inference, if the posterior distribution is in the same probability family as the prior distribution, the prior is called a **conjugate prior** for the likelihood.\n",
            "- **Example**: Beta prior is conjugate to Binomial likelihood (Beta-Binomial update: $\\alpha_{post} = \\alpha_{prior} + \\text{successes}$, $\\beta_{post} = \\beta_{prior} + \\text{failures}$)."
        ],
        "code": [
            "# Beta-Binomial Conjugate Update\n",
            "# Prior: Beta(2, 2) (Uniform-ish)\n",
            "# Experiment: 8 successes, 2 failures\n",
            "prior_alpha, prior_beta = 2, 2\n",
            "successes, failures = 8, 2\n",
            "\n",
            "post_alpha = prior_alpha + successes\n",
            "post_beta = prior_beta + failures\n",
            "print(f\"Posterior Distribution parameters: Beta({post_alpha}, {post_beta})\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain why treating parameters as random variables (the Bayesian approach) is useful when training models on small datasets."
        ],
        "exercise_code": [
            "print(\"It allows us to incorporate prior domain knowledge (via the prior) which prevents the model from overfitting to the small dataset.\")\n"
        ]
    },
    30: {
        "title": "Univariate, Bivariate, Multivariate Analysis",
        "summary": "Exploring datasets by analyzing one, two, or multiple variables simultaneously.",
        "theory": [
            "### Exploratory Data Analysis (EDA) Dimensions\n",
            "\n",
            "### 1. Univariate Analysis\n",
            "Analyzing a single variable in isolation. Looks at shape, central tendency, frequency.\n",
            "- **Plots**: Histograms, box plots, count plots.\n",
            "\n",
            "### 2. Bivariate Analysis\n",
            "Analyzing the relationship between two variables.\n",
            "- **Plots**: Scatter plots, line plots, bar plots, cross-tabs.\n",
            "\n",
            "### 3. Multivariate Analysis\n",
            "Analyzing relationships between three or more variables simultaneously.\n",
            "- **Plots**: Pair plots, 3D scatter plots, heatmaps of correlation matrices."
        ],
        "code": [
            "import seaborn as sns\n",
            "import matplotlib.pyplot as plt\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "\n",
            "# Generate dummy dataset\n",
            "np.random.seed(42)\n",
            "df = pd.DataFrame({\n",
            "    \"Size\": np.random.normal(150, 20, 100),\n",
            "    \"Price\": np.random.normal(300, 50, 100),\n",
            "    \"Rooms\": np.random.choice([2, 3, 4], 100)\n",
            "})\n",
            "\n",
            "# Bivariate Scatter Plot\n",
            "sns.scatterplot(data=df, x=\"Size\", y=\"Price\", hue=\"Rooms\", palette=\"viridis\")\n",
            "plt.title(\"Bivariate/Multivariate Plot\")\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Use `sns.heatmap` to plot the correlation matrix of the generated dataframe `df`."
        ],
        "exercise_code": [
            "sns.heatmap(df.corr(), annot=True, cmap=\"coolwarm\")\n",
            "plt.show()\n"
        ]
    },
    31: {
        "title": "Sampling techniques",
        "summary": "Methods of selecting subsets of data to represent populations: probability vs non-probability sampling.",
        "theory": [
            "### Probability Sampling Techniques\n",
            "1. **Simple Random Sampling (SRS)**: Every member of the population has an equal chance of selection.\n",
            "2. **Stratified Sampling**: Population is divided into subgroups (strata), and SRS is applied to each stratum (critical for ML train/test splits to avoid class imbalance biases).\n",
            "3. **Systematic Sampling**: Members are selected at regular intervals (e.g. every $k$-th item).\n",
            "4. **Cluster Sampling**: Population is divided into clusters, and random clusters are chosen entirely."
        ],
        "code": [
            "import pandas as pd\n",
            "df = pd.DataFrame({\n",
            "    \"ID\": range(1, 11),\n",
            "    \"Class\": ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B']\n",
            "})\n",
            "\n",
            "# Stratified Sample using pandas groupby\n",
            "stratified_sample = df.groupby('Class', group_keys=False).apply(lambda x: x.sample(2))\n",
            "print(\"Stratified Sample (2 from each class):\\n\", stratified_sample)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is stratified sampling preferred over simple random sampling when dealing with highly imbalanced classification targets (e.g., fraud detection)?"
        ],
        "exercise_code": [
            "print(\"Stratified sampling ensures the train/test sets preserve the minority class ratio, preventing training/testing sets from having zero fraud cases.\")\n"
        ]
    },
    32: {
        "title": "Point and Interval Estimate",
        "summary": "Estimating population parameters: single value points vs range intervals.",
        "theory": [
            "### Estimation Theory\n",
            "\n",
            "### 1. Point Estimate\n",
            "A single value calculated from sample data that serves as the best guess for an unknown population parameter.\n",
            "- **Example**: The sample mean $\\bar{x}$ is a point estimate of the population mean $\\mu$.\n",
            "\n",
            "### 2. Interval Estimate (Confidence Interval)\n",
            "A range of values, derived from sample statistics, that is likely to contain the population parameter.\n",
            "- Form: $\\text{Point Estimate} \\pm \\text{Margin of Error}$."
        ],
        "code": [
            "import numpy as np\n",
            "sample = [1.2, 1.5, 1.4, 1.8, 1.6]\n",
            "print(\"Point Estimate of Mean:\", np.mean(sample))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. True or False: A larger sample size generally decreases the margin of error of an interval estimate."
        ],
        "exercise_code": [
            "print(\"True (standard error decreases as sample size increases)\")\n"
        ]
    },
    33: {
        "title": "Margin of Error",
        "summary": "Determining sample deviation bounds and precision limits.",
        "theory": [
            "### Margin of Error (MoE)\n",
            "Represents the maximum expected difference between the sample statistic and the true population parameter:\n",
            "$$MoE = z^* \\times \\left(\\frac{\\sigma}{\\sqrt{n}}\\right)$$\n",
            "where:\n",
            "- $z^*$ is the critical value (z-score matching confidence level).\n",
            "- $\\frac{\\sigma}{\\sqrt{n}}$ is the standard error.\n",
            "- $n$ is the sample size."
        ],
        "code": [
            "# Calculate MoE for 95% confidence (z*=1.96), sample size n=100, std=5\n",
            "import math\n",
            "z_critical = 1.96\n",
            "std_dev = 5\n",
            "n = 100\n",
            "moe = z_critical * (std_dev / math.sqrt(n))\n",
            "print(\"Margin of Error:\", moe)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. How does doubling the sample size $n$ affect the Margin of Error?"
        ],
        "exercise_code": [
            "print(\"It reduces the Margin of Error by a factor of sqrt(2) (~1.414)\")\n"
        ]
    },
    34: {
        "title": "Confidence Interval",
        "summary": "Constructing confidence intervals for population parameters.",
        "theory": [
            "### Confidence Interval (CI)\n",
            "A confidence interval specifies the range of values within which a population parameter is expected to fall with a certain probability (confidence level, e.g. 95%):\n",
            "$$CI = \\bar{x} \\pm z^* \\left(\\frac{s}{\\sqrt{n}}\\right)$$\n",
            "- **95% Confidence interpretation**: If we take 100 independent samples and construct a 95% CI for each, approximately 95 of those intervals will contain the true population mean."
        ],
        "code": [
            "import numpy as np\n",
            "import scipy.stats as stats\n",
            "\n",
            "data = [12, 15, 14, 16, 18, 15, 13, 14, 15, 16]\n",
            "mean = np.mean(data)\n",
            "sem = stats.sem(data)  # standard error of the mean\n",
            "ci = stats.t.interval(0.95, df=len(data)-1, loc=mean, scale=sem)\n",
            "print(\"95% Confidence Interval for mean:\", ci)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the 99% confidence interval for the same data using `stats.t.interval`."
        ],
        "exercise_code": [
            "ci_99 = stats.t.interval(0.99, df=len(data)-1, loc=mean, scale=sem)\n",
            "print(\"99% Confidence Interval:\", ci_99)\n"
        ]
    },
    35: {
        "title": "Hypothesis Testing full series",
        "summary": "Formulating hypotheses, significance levels, type 1 and 2 errors, z-tests, and t-tests.",
        "theory": [
            "### Hypothesis Testing Framework\n",
            "\n",
            "### 1. Formulate Hypotheses\n",
            "- **Null Hypothesis ($H_0$)**: Statement of no effect or no difference.\n",
            "- **Alternative Hypothesis ($H_a$)**: What we want to prove.\n",
            "\n",
            "### 2. Error Types\n",
            "- **Type I Error ($\\alpha$)**: Rejecting $H_0$ when it is actually true (false positive).\n",
            "- **Type II Error ($\\beta$)**: Failing to reject $H_0$ when it is actually false (false negative).\n",
            "\n",
            "### 3. Z-test vs T-test\n",
            "- **Z-test**: Used when sample size is large ($n \\ge 30$) or population variance $\\sigma$ is known.\n",
            "- **T-test**: Used when sample size is small ($n < 30$) and population variance is unknown (uses sample standard deviation $s$)."
        ],
        "code": [
            "import numpy as np\n",
            "import scipy.stats as stats\n",
            "\n",
            "# One-sample t-test\n",
            "# H0: mean = 100\n",
            "# Ha: mean != 100\n",
            "scores = [102, 105, 98, 103, 101, 105, 99]\n",
            "t_stat, p_value = stats.ttest_1samp(scores, 100)\n",
            "print(\"T-statistic:\", t_stat)\n",
            "print(\"p-value:\", p_value)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. If significance level $\\alpha = 0.05$, do we reject the null hypothesis $H_0$ based on the p-value computed above?"
        ],
        "exercise_code": [
            "alpha = 0.05\n",
            "print(\"Reject Null?\", p_value < alpha)  # If True, reject\n"
        ]
    },
    36: {
        "title": "Chi Square Test",
        "summary": "Chi square test of independence and goodness-of-fit.",
        "theory": [
            "### Chi Square Test ($\\chi^2$)\n",
            "Used to analyze categorical variables:\n",
            "\n",
            "### 1. Goodness-of-Fit Test\n",
            "Determines if an observed frequency distribution matches an expected distribution.\n",
            "\n",
            "### 2. Test of Independence\n",
            "Determines whether two categorical variables are independent or associated:\n",
            "$$\\chi^2 = \\sum \\frac{(O - E)^2}{E}$$\n",
            "where $O$ is observed frequencies, $E$ is expected frequencies."
        ],
        "code": [
            "import scipy.stats as stats\n",
            "import numpy as np\n",
            "\n",
            "# Contingency table: Columns=Smoking (Yes/No), Rows=Exercise (Low/High)\n",
            "observed = np.array([[10, 30], [20, 40]])\n",
            "chi2, p_val, dof, expected = stats.chi2_contingency(observed)\n",
            "print(\"Chi2 Statistic:\", chi2)\n",
            "print(\"p-value:\", p_val)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. At $\\alpha = 0.05$, are Smoking and Exercise level significantly associated based on the p-value above?"
        ],
        "exercise_code": [
            "print(\"Significant Association?\", p_val < 0.05)\n"
        ]
    },
    37: {
        "title": "IQR and Outliers (stats perspective)",
        "summary": "Detecting outliers using Interquartile Range boundaries.",
        "theory": [
            "### Outlier Detection using IQR\n",
            "The **Interquartile Range (IQR)** measures statistical dispersion:\n",
            "$$IQR = Q_3 - Q_1$$\n",
            "\n",
            "### Outlier Boundaries\n",
            "Data points are classified as outliers if they fall outside the boundaries:\n",
            "- **Lower Bound**: $Q_1 - 1.5 \\times IQR$\n",
            "- **Upper Bound**: $Q_3 + 1.5 \\times IQR$\n",
            "- In Box Plots, the whiskers represent these limits."
        ],
        "code": [
            "import numpy as np\n",
            "data = [3, 5, 6, 7, 7, 8, 9, 25]  # 25 is outlier\n",
            "\n",
            "q1 = np.percentile(data, 25)\n",
            "q3 = np.percentile(data, 75)\n",
            "iqr = q3 - q1\n",
            "lower_bound = q1 - 1.5 * iqr\n",
            "upper_bound = q3 + 1.5 * iqr\n",
            "\n",
            "outliers = [x for x in data if x < lower_bound or x > upper_bound]\n",
            "print(f\"IQR: {iqr}, Outlier Limits: [{lower_bound}, {upper_bound}]\")\n"
            "print(\"Outliers identified:\", outliers)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Write a function `remove_outliers_iqr(dataset)` that takes a list, computes the IQR boundaries, and returns a new list with outliers removed."
        ],
        "exercise_code": [
            "def remove_outliers_iqr(dataset):\n",
            "    arr = np.array(dataset)\n",
            "    q1, q3 = np.percentile(arr, [25, 75])\n",
            "    iqr = q3 - q1\n",
            "    filtered = arr[(arr >= q1 - 1.5*iqr) & (arr <= q3 + 1.5*iqr)]\n",
            "    return list(filtered)\n",
            "\n",
            "print(\"Deduplicated dataset:\", remove_outliers_iqr([3, 5, 6, 7, 7, 8, 9, 25]))\n"
        ]
    }
}


PHASE_3_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Intro to NumPy",
        "summary": "Introduction to NumPy, ndarray concept, and comparing performance with standard Python lists.",
        "theory": [
            "### 1. What is NumPy?\n",
            "NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides a high-performance multidimensional array object, **ndarray**, and tools for working with these arrays.\n",
            "\n",
            "### 2. Why use NumPy over Lists?\n",
            "- **Memory Efficiency**: NumPy arrays use contiguous blocks of memory, whereas Python lists store pointers to objects scattered in memory.\n",
            "- **Performance**: NumPy operations are implemented in compiled C code, allowing element-wise operations (vectorization) without slow Python loops.\n",
            "- **Convenience**: Math operations on arrays can be written concisely, like `a * b` instead of writing a loop."
        ],
        "code": [
            "import numpy as np\n",
            "import time\n",
            "\n",
            "# Performance Comparison: List vs NumPy Array\n",
            "size = 1000000\n",
            "list1 = list(range(size))\n",
            "list2 = list(range(size))\n",
            "arr1 = np.arange(size)\n",
            "arr2 = np.arange(size)\n",
            "\n",
            "# Measure list addition time\n",
            "start = time.time()\n",
            "list_result = [x + y for x, y in zip(list1, list2)]\n",
            "print(\"List time:\", time.time() - start, \"seconds\")\n",
            "\n",
            "# Measure array addition time\n",
            "start = time.time()\n",
            "arr_result = arr1 + arr2\n",
            "print(\"NumPy Array time:\", time.time() - start, \"seconds\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Multiply a Python list of size 100,000 by a scalar 5 using list comprehension, and compare its execution time with a NumPy array multiplied by the same scalar."
        ],
        "exercise_code": [
            "size = 100000\n",
            "l = list(range(size))\n",
            "a = np.arange(size)\n",
            "\n",
            "t0 = time.time()\n",
            "res_l = [x * 5 for x in l]\n",
            "print(\"List multiplication time:\", time.time() - t0)\n",
            "\n",
            "t1 = time.time()\n",
            "res_a = a * 5\n",
            "print(\"NumPy multiplication time:\", time.time() - t1)\n"
        ]
    },
    2: {
        "title": "Creating arrays: from list, built in methods, random",
        "summary": "Creating arrays from python iterables and using built-in functions like np.zeros, np.ones, np.arange, np.linspace, and random generators.",
        "theory": [
            "### Array Creation Methods\n",
            "NumPy provides several convenient built-in functions to initialize arrays:\n",
            "\n",
            "### 1. From Python Iterables\n",
            "- `np.array(iterable)`: Converts lists, tuples, etc. into an ndarray.\n",
            "\n",
            "### 2. Built-in Constant/Range Initializers\n",
            "- `np.zeros(shape)`: Creates an array filled with 0.\n",
            "- `np.ones(shape)`: Creates an array filled with 1.\n",
            "- `np.arange(start, stop, step)`: Creates sequence of numbers with a constant step.\n",
            "- `np.linspace(start, stop, num)`: Creates a sequence of `num` equally spaced numbers in a closed interval.\n",
            "\n",
            "### 3. Random Number Generators\n",
            "- `np.random.rand(d0, d1)`: Uniformly distributed floats in [0, 1).\n",
            "- `np.random.randn(d0, d1)`: Normal (Gaussian) distributed floats (mean=0, variance=1).\n",
            "- `np.random.randint(low, high, size)`: Random integers in [low, high)."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "print(\"Zeros Matrix:\\n\", np.zeros((2, 3)))\n",
            "print(\"Ones Matrix:\\n\", np.ones((2, 2)))\n",
            "print(\"arange(0, 10, 2):\", np.arange(0, 10, 2))\n",
            "print(\"linspace(0, 1, 5):\", np.linspace(0, 1, 5))\n",
            "print(\"randint(1, 10, 5):\", np.random.randint(1, 10, 5))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create a 3x3 matrix filled with random values from a standard normal distribution.\n",
            "2. Generate an array of 20 equally spaced values between 0 and 10."
        ],
        "exercise_code": [
            "norm_matrix = np.random.randn(3, 3)\n",
            "spaced_vals = np.linspace(0, 10, 20)\n",
            "print(\"Normal Matrix:\\n\", norm_matrix)\n",
            "print(\"Spaced Values:\\n\", spaced_vals)\n"
        ]
    },
    3: {
        "title": "Array attributes: shape, dtype, size, ndim",
        "summary": "Querying metadata of NumPy arrays: dimensions, shape, element count, and data type.",
        "theory": [
            "### Metadata Attributes of ndarray\n",
            "Every NumPy array has standard attributes to describe its structure and layout in memory:\n",
            "\n",
            "- `ndim`: The number of axes (dimensions) of the array.\n",
            "- `shape`: A tuple of integers showing the size of the array along each dimension.\n",
            "- `size`: The total number of elements in the array (equal to the product of shape elements).\n",
            "- `dtype`: An object describing the type of elements in the array (e.g., int32, float64)."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)\n",
            "print(\"Array dimensions (ndim):\", arr.ndim)\n",
            "print(\"Array shape:\", arr.shape)\n",
            "print(\"Total elements (size):\", arr.size)\n",
            "print(\"Data type (dtype):\", arr.dtype)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create a 3D array of shape (2, 3, 4) and display its ndim, shape, size, and dtype attributes."
        ],
        "exercise_code": [
            "arr_3d = np.ones((2, 3, 4))\n",
            "print(f\"ndim: {arr_3d.ndim}, shape: {arr_3d.shape}, size: {arr_3d.size}, dtype: {arr_3d.dtype}\")\n"
        ]
    },
    4: {
        "title": "Array methods: reshape, max, min, argmax, argmin",
        "summary": "Reshaping arrays and finding maximum/minimum values along with their indices.",
        "theory": [
            "### Array Manipulation & Statistics\n",
            "\n",
            "### 1. Reshaping\n",
            "- `reshape(new_shape)`: Returns an array containing the same data with a new shape. The new shape must have the same total size as the original.\n",
            "\n",
            "### 2. Statistical Aggregations\n",
            "- `max()` and `min()`: Find the maximum and minimum values in the array (optionally along a specific axis).\n",
            "- `argmax()` and `argmin()`: Find the flat indices of the maximum and minimum values."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "arr = np.array([3, 10, 1, 15, 2, 8])\n",
            "reshaped = arr.reshape((2, 3))\n",
            "print(\"Reshaped 2x3 Matrix:\\n\", reshaped)\n",
            "print(\"Max Value:\", reshaped.max())\n",
            "print(\"Min Value:\", reshaped.min())\n",
            "print(\"Index of Max:\", reshaped.argmax())\n",
            "print(\"Index of Max along column (axis=0):\", reshaped.argmax(axis=0))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create an array of 12 numbers and reshape it into a 3x4 matrix.\n",
            "2. Find the index of the minimum value in each row (axis=1) of the matrix."
        ],
        "exercise_code": [
            "a = np.arange(12).reshape((3, 4))\n",
            "np.random.shuffle(a) # Shuffle rows to make it interesting\n",
            "print(\"Matrix:\\n\", a)\n",
            "print(\"Argmin along rows:\", a.argmin(axis=1))\n"
        ]
    },
    5: {
        "title": "Array operations: copy, append, insert, sort, delete",
        "summary": "Array manipulations: shallow vs deep copies, appending, inserting, sorting, and deleting elements.",
        "theory": [
            "### Manipulating Array Elements\n",
            "Unlike lists, NumPy arrays have a fixed size. Operations like append or delete create a new array copy underneath:\n",
            "\n",
            "- **Copy (`np.copy`)**: Standard slicing returns a *view* (shallow reference). Modifying a view changes the original array. Use `copy()` to create an independent array.\n",
            "- **Append (`np.append(arr, values)`)**: Appends values to the end of an array.\n",
            "- **Insert (`np.insert(arr, obj, values)`)**: Inserts values at a specific index.\n",
            "- **Delete (`np.delete(arr, obj)`)**: Deletes items at the specified index/indices.\n",
            "- **Sort (`np.sort(arr)`)**: Returns a sorted copy of the array."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "arr = np.array([40, 10, 30, 20])\n",
            "view = arr[1:3]\n",
            "view[0] = 99\n",
            "print(\"Original modified by view change:\", arr)\n",
            "\n",
            "copied = np.copy(arr)\n",
            "copied[0] = 500\n",
            "print(\"Original untouched by copy change:\", arr)\n",
            "\n",
            "print(\"Sorted array:\", np.sort(arr))\n",
            "print(\"Appended:\", np.append(arr, [100, 200]))\n",
            "print(\"Deleted index 1:\", np.delete(arr, 1))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create an array `[10, 5, 8, 3]`. Sort it in descending order, then insert the value `99` at index 2."
        ],
        "exercise_code": [
            "a = np.array([10, 5, 8, 3])\n",
            "sorted_desc = np.sort(a)[::-1]\n",
            "result = np.insert(sorted_desc, 2, 99)\n",
            "print(\"Resulting Array:\", result)\n"
        ]
    },
    6: {
        "title": "Concatenating, splitting, searching",
        "summary": "Joining multiple arrays, splitting an array into sub-arrays, and searching for element locations.",
        "theory": [
            "### Structural Merging, Splitting, and Conditional Search\n",
            "\n",
            "### 1. Concatenation\n",
            "- `np.concatenate((a1, a2), axis)`: Joins a sequence of arrays along an existing axis.\n",
            "\n",
            "### 2. Splitting\n",
            "- `np.split(arr, indices_or_sections)`: Splits an array into multiple sub-arrays.\n",
            "\n",
            "### 3. Searching\n",
            "- `np.where(condition)`: Returns indices of elements that satisfy the given condition. Can also be used to conditionally replace values: `np.where(cond, x, y)`."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "a = np.array([[1, 2], [3, 4]])\n",
            "b = np.array([[5, 6], [7, 8]])\n",
            "print(\"Concatenate Vertically:\\n\", np.concatenate((a, b), axis=0))\n",
            "print(\"Concatenate Horizontally:\\n\", np.concatenate((a, b), axis=1))\n",
            "\n",
            "arr = np.arange(9)\n",
            "split_arr = np.split(arr, 3)\n",
            "print(\"Split array:\", split_arr)\n",
            "\n",
            "# Search even numbers\n",
            "even_indices = np.where(arr % 2 == 0)\n",
            "print(\"Indices of evens:\", even_indices)\n",
            "print(\"Even values:\", arr[even_indices])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Given an array `arr = np.array([15, 22, 9, 34, 50, 4, 18])`, use `np.where` to replace all values greater than 20 with `999` and all other values with `-1`."
        ],
        "exercise_code": [
            "arr = np.array([15, 22, 9, 34, 50, 4, 18])\n",
            "replaced = np.where(arr > 20, 999, -1)\n",
            "print(\"Replaced Array:\", replaced)\n"
        ]
    },
    7: {
        "title": "NumPy indexing, slicing, logical selection",
        "summary": "Selecting elements from 1D and 2D arrays, indexing slices, and boolean/logical filtering.",
        "theory": [
            "### Slicing and Filtering Techniques\n",
            "\n",
            "### 1. Slice Notation\n",
            "- `arr[start:stop:step]`\n",
            "- For 2D matrices: `matrix[row_start:row_stop, col_start:col_stop]`\n",
            "\n",
            "### 2. Logical (Boolean) Selection\n",
            "- Creating a boolean condition like `mask = arr > 5` returns an array of booleans.\n",
            "- Passing this mask back into the array, `arr[mask]`, filters out only `True` values."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "matrix = np.array([\n",
            "    [10, 20, 30],\n",
            "    [40, 50, 60],\n",
            "    [70, 80, 90]\n",
            "])\n",
            "\n",
            "print(\"Slice row 0 and columns 1-2:\", matrix[0, 1:3])\n",
            "print(\"Extract 2x2 submatrix:\\n\", matrix[:2, :2])\n",
            "\n",
            "# Filter values greater than 50\n",
            "mask = matrix > 50\n",
            "print(\"Boolean Mask:\\n\", mask)\n",
            "print(\"Filtered Values:\", matrix[mask])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. From a 3x3 matrix of integers from 1 to 9, extract the middle column.\n",
            "2. Filter out all odd numbers from this matrix using boolean indexing."
        ],
        "exercise_code": [
            "m = np.arange(1, 10).reshape((3, 3))\n",
            "print(\"Middle column:\", m[:, 1])\n",
            "print(\"Even numbers:\", m[m % 2 == 0])\n"
        ]
    },
    8: {
        "title": "Broadcasting",
        "summary": "Mathematical operations on arrays of different shapes.",
        "theory": [
            "### Broadcasting Rules\n",
            "Broadcasting allows arithmetic operations on arrays of different shapes. NumPy expands the smaller array to match the size of the larger one without copy overhead.\n",
            "\n",
            "### Broadcasting Rules Compatibility:\n",
            "Two dimensions are compatible if:\n",
            "1. They are equal, OR\n",
            "2. One of them is 1.\n",
            "\n",
            "If these conditions are not met, NumPy raises a `ValueError: operands could not be broadcast together`."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "matrix = np.array([[1, 2, 3], [4, 5, 6]]) # shape (2, 3)\n",
            "row_vector = np.array([10, 20, 30])      # shape (3,)\n",
            "\n",
            "# Add shape (2,3) to shape (3,) -> Row vector broadcasted across rows\n",
            "print(\"Broadcast Addition Result:\\n\", matrix + row_vector)\n",
            "\n",
            "col_vector = np.array([[100], [200]])    # shape (2, 1)\n",
            "print(\"Col Vector Broadcast:\\n\", matrix + col_vector)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Multiply a 3x3 matrix of ones by a 1x3 column vector `[[10], [20], [30]]` using broadcasting."
        ],
        "exercise_code": [
            "m = np.ones((3, 3))\n",
            "col = np.array([[10], [20], [30]])\n",
            "print(\"Broadcast Multiplication:\\n\", m * col)\n"
        ]
    },
    9: {
        "title": "Type casting, arithmetic operations",
        "summary": "Changing data types of arrays and element-wise arithmetic operations.",
        "theory": [
            "### Arithmetic & Data Type Conversion\n",
            "\n",
            "### 1. Data Type Casting\n",
            "- Use `astype(new_dtype)` to cast elements (e.g. converting `float64` to `int32` to save memory).\n",
            "\n",
            "### 2. Element-Wise Arithmetic\n",
            "- Basic arithmetic operators `+`, `-`, `*`, `/`, `**` execute element-wise operations on arrays."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "floats = np.array([1.2, 2.5, 3.8])\n",
            "ints = floats.astype(np.int32)\n",
            "print(\"Casted to integers:\", ints)\n",
            "\n",
            "a = np.array([2, 4, 6])\n",
            "b = np.array([1, 2, 3])\n",
            "print(\"Addition:\", a + b)\n",
            "print(\"Power:\", a ** b)\n",
            "print(\"Division:\", a / b)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create a float array `[1.9, 2.9, 3.9]`. Cast it to `int32` and explain if values were rounded or truncated.\n",
            "2. Generate an array `a = np.array([10, 20, 30])` and find its reciprocal element-wise."
        ],
        "exercise_code": [
            "f = np.array([1.9, 2.9, 3.9])\n",
            "i = f.astype(np.int32)\n",
            "print(\"Casted (truncated):\", i)\n",
            "reciprocal = 1.0 / np.array([10, 20, 30])\n",
            "print(\"Reciprocals:\", reciprocal)\n"
        ]
    },
    10: {
        "title": "Universal array functions: sqrt, exp, sin, etc.",
        "summary": "Fast mathematical element-wise functions (ufuncs) in NumPy.",
        "theory": [
            "### Universal Functions (ufunc)\n",
            "A universal function (or **ufunc**) is a function that operates on ndarrays in an element-by-element fashion, supporting vectorization.\n",
            "Common ufuncs include:\n",
            "- `np.sqrt(arr)`: Computes square root.\n",
            "- `np.exp(arr)`: Computes natural exponential ($e^x$).\n",
            "- `np.log(arr)`: Computes natural logarithm ($ln$).\n",
            "- `np.sin(arr)`, `np.cos(arr)`: Trigonometric operations."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "arr = np.array([1, 4, 9])\n",
            "print(\"Square root:\", np.sqrt(arr))\n",
            "print(\"Exponential:\", np.exp(arr))\n",
            "print(\"Logarithm (base e):\", np.log(arr))\n",
            "print(\"Sine (in radians):\", np.sin(np.array([0, np.pi/2, np.pi])))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Given an array `[10, 20, 30]`, calculate the element-wise exponential and natural log values."
        ],
        "exercise_code": [
            "a = np.array([10, 20, 30])\n",
            "print(\"Exponential:\", np.exp(a))\n",
            "print(\"Log:\", np.log(a))\n"
        ]
    }
}


PHASE_4_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Intro to Pandas: Series and DataFrame",
        "summary": "Series (1D) and DataFrame (2D), basic construction from lists/dicts, and basic metadata inspections.",
        "theory": [
            "### 1. What is Pandas?\n",
            "Pandas is the primary library for data manipulation and analysis in Python. It provides high-performance data structures: **Series** (1-dimensional) and **DataFrame** (2-dimensional).\n",
            "\n",
            "### 2. Core Data Structures\n",
            "- **Series**: A 1D labeled array capable of holding any data type (integers, strings, floats, Python objects). It has an axis label called the index.\n",
            "- **DataFrame**: A 2D labeled data structure with columns of potentially different types, resembling a spreadsheet or SQL table."
        ],
        "code": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "\n",
            "# 1. Creating a Series\n",
            "s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])\n",
            "print(\"Series:\\n\", s)\n",
            "\n",
            "# 2. Creating a DataFrame from a dictionary\n",
            "data = {\n",
            "    'Name': ['Alice', 'Bob', 'Charlie'],\n",
            "    'Age': [25, 30, 35],\n",
            "    'City': ['New York', 'Paris', 'London']\n",
            "}\n",
            "df = pd.DataFrame(data)\n",
            "print(\"\\nDataFrame:\\n\", df)\n",
            "print(\"\\nColumns:\", df.columns)\n",
            "print(\"Shape:\", df.shape)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create a Series of 5 elements representing employee salaries, with employee names as the index.\n",
            "2. Create a DataFrame from a list of dictionaries representing products (columns: ProductID, Price, Stock)."
        ],
        "exercise_code": [
            "salaries = pd.Series([50000, 60000, 75000, 80000, 45000], index=['Alex', 'Sarah', 'Ryan', 'John', 'Emma'])\n",
            "products = pd.DataFrame([\n",
            "    {'ProductID': 101, 'Price': 15.5, 'Stock': 120},\n",
            "    {'ProductID': 102, 'Price': 20.0, 'Stock': 80},\n",
            "    {'ProductID': 103, 'Price': 9.9, 'Stock': 200}\n",
            "])\n",
            "print(\"Salaries Series:\\n\", salaries)\n",
            "print(\"\\nProducts DataFrame:\\n\", products)\n"
        ]
    },
    2: {
        "title": "Data input, selection, indexing",
        "summary": "Loading datasets and selecting rows/columns using loc and iloc.",
        "theory": [
            "### Data Selection & Indexing in Pandas\n",
            "We can select subsets of data in a DataFrame using standard indexing or optimized attributes:\n",
            "\n",
            "- **`df['col_name']`**: Selects a single column as a Series.\n",
            "- **`df[['col1', 'col2']]`**: Selects multiple columns as a DataFrame.\n",
            "- **`loc`**: Label-based indexing. Selects rows and columns by their labels: `df.loc[row_label, col_label]`.\n",
            "- **`iloc`**: Integer position-based indexing. Selects rows and columns by their numerical indices: `df.iloc[row_pos, col_pos]`."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "# Load sample dataset from URL\n",
            "url = \"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv\"\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "print(\"First 3 rows of Iris:\\n\", df.head(3))\n",
            "\n",
            "# loc selection (label-based)\n",
            "print(\"\\nloc selection (row index 0, col 'sepal_length'):\", df.loc[0, 'sepal_length'])\n",
            "\n",
            "# iloc selection (integer position-based)\n",
            "print(\"iloc selection (first 2 rows, first 3 columns):\\n\", df.iloc[:2, :3])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Using the Iris dataset, filter and select all rows where `species` is equal to `'setosa'` and display the first 5 records.\n",
            "2. Select only the `sepal_width` and `petal_width` columns for rows with index positions 10 to 15 (inclusive) using `.loc` or `.iloc`."
        ],
        "exercise_code": [
            "setosa_subset = df[df['species'] == 'setosa'].head(5)\n",
            "slice_subset = df.iloc[10:16, [1, 3]]\n",
            "print(\"Setosa subset:\\n\", setosa_subset)\n",
            "print(\"\\nSlice position-based subset:\\n\", slice_subset)\n"
        ]
    },
    3: {
        "title": "DataFrame operations: head, unique, value_counts, sort, null check",
        "summary": "Basic explorations on DataFrames (head, tail, unique values, value counts, sorting, and null value inspections).",
        "theory": [
            "### Core DataFrame Inspection Methods\n",
            "To understand a dataset's structure and contents, we use these common operations:\n",
            "\n",
            "- `df.head(n)` / `df.tail(n)`: View the first or last $n$ rows.\n",
            "- `df.info()`: Summarizes index, columns, null statuses, and memory usage.\n",
            "- `df.describe()`: Computes summary statistics (mean, std, percentiles) for numerical columns.\n",
            "- `col.unique()` / `col.nunique()`: Get unique elements or count of unique elements in a column.\n",
            "- `col.value_counts()`: Frequency counts of each unique category.\n",
            "- `df.sort_values(by, ascending)`: Sorts the DataFrame by specific column(s).\n",
            "- `df.isnull().sum()`: Counts missing values in each column."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = \"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv\"\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "print(\"Shape of Titanic:\", df.shape)\n",
            "print(\"\\nUnique values in Survived:\", df['Survived'].unique())\n",
            "print(\"\\nGender value counts:\\n\", df['Sex'].value_counts())\n",
            "print(\"\\nMissing values per column:\\n\", df.isnull().sum())\n",
            "print(\"\\nFirst 3 rows sorted by Fare descending:\\n\", df.sort_values(by='Fare', ascending=False).head(3))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Find the count of survivors (value counts of `Survived`) in the Titanic dataset.\n",
            "2. Identify the column with the highest number of null values and compute the percentage of null values in it."
        ],
        "exercise_code": [
            "survival_counts = df['Survived'].value_counts()\n",
            "null_percentages = (df.isnull().sum() / len(df)) * 100\n",
            "print(\"Survival Counts:\\n\", survival_counts)\n",
            "print(\"\\nNull percentages per column:\\n\", null_percentages)\n"
        ]
    },
    4: {
        "title": "Missing data and handling",
        "summary": "Techniques for identifying and resolving missing values (dropping, filling).",
        "theory": [
            "### Handling Missing Data\n",
            "Real-world data often has missing values (NaN or None). Pandas provides several methods to manage them:\n",
            "\n",
            "- **Detecting Nulls**: `df.isnull()` returns a boolean mask. `df.isnull().sum()` totals nulls per column.\n",
            "- **Dropping Nulls (`dropna`)**: Removes rows or columns containing missing values. Useful if missingness is small or column is mostly empty.\n",
            "- **Imputing Nulls (`fillna`)**: Fills missing values with a placeholder, like a constant value, mean, median, or mode."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = \"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv\"\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "# Check null status\n",
            "print(\"Null counts in Age:\", df['Age'].isnull().sum())\n",
            "\n",
            "# Fill Age missing values with its median\n",
            "median_age = df['Age'].median()\n",
            "df_filled = df.copy()\n",
            "df_filled['Age'] = df_filled['Age'].fillna(median_age)\n",
            "print(\"Null counts in Age after fillna:\", df_filled['Age'].isnull().sum())\n",
            "\n",
            "# Drop rows where Cabin is missing\n",
            "df_dropped = df.dropna(subset=['Cabin'])\n",
            "print(\"Shape after dropping Cabin null rows:\", df_dropped.shape)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Locate missing values in the `Embarked` column of the Titanic dataset and fill them with the most frequent value (mode) of that column."
        ],
        "exercise_code": [
            "mode_embarked = df['Embarked'].mode()[0]\n",
            "df['Embarked'] = df['Embarked'].fillna(mode_embarked)\n",
            "print(\"Null count in Embarked after filling:\", df['Embarked'].isnull().sum())\n"
        ]
    },
    5: {
        "title": "Merging, joining, concatenation: inner, outer, left, right",
        "summary": "Combining multiple datasets vertically and horizontally using merge, join, and concat.",
        "theory": [
            "### Combining Datasets\n",
            "\n",
            "### 1. Concatenation (`pd.concat`)\n",
            "Stacks multiple DataFrames vertically (axis=0) or horizontally (axis=1).\n",
            "\n",
            "### 2. Merging (`pd.merge`)\n",
            "Database-style joins based on matching keys (columns):\n",
            "- **Inner Join**: Keeps rows with matching keys in both DataFrames.\n",
            "- **Outer Join**: Keeps all rows from both DataFrames, filling missing matches with NaN.\n",
            "- **Left Join**: Keeps all rows from left DataFrame, along with matching rows from the right.\n",
            "- **Right Join**: Keeps all rows from right DataFrame, along with matching rows from the left."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "df1 = pd.DataFrame({'id': [1, 2, 3], 'Product': ['Apple', 'Banana', 'Orange']})\n",
            "df2 = pd.DataFrame({'id': [2, 3, 4], 'Price': [0.5, 0.8, 1.2]})\n",
            "\n",
            "# 1. Inner Merge\n",
            "print(\"Inner Merge:\\n\", pd.merge(df1, df2, on='id', how='inner'))\n",
            "\n",
            "# 2. Left Merge\n",
            "print(\"\\nLeft Merge:\\n\", pd.merge(df1, df2, on='id', how='left'))\n",
            "\n",
            "# 3. Concatenation (vertical stacking)\n",
            "df3 = pd.DataFrame({'id': [5], 'Product': ['Grape']})\n",
            "print(\"\\nConcatenated DataFrame:\\n\", pd.concat([df1, df3], axis=0, ignore_index=True))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Merge `df1` and `df2` using an **outer join** and explain why some rows contain null values."
        ],
        "exercise_code": [
            "outer_merge = pd.merge(df1, df2, on='id', how='outer')\n",
            "print(\"Outer Merge:\\n\", outer_merge)\n"
        ]
    },
    6: {
        "title": "GroupBy, discretization, binning",
        "summary": "Aggregating data by categories and converting continuous variables to categorical bins.",
        "theory": [
            "### Grouping & Discretization (Binning)\n",
            "\n",
            "### 1. GroupBy\n",
            "The `groupby` method implements the **Split-Apply-Combine** workflow. It splits data by a category, applies an aggregation (like sum, mean, count), and combines results into a summary table.\n",
            "\n",
            "### 2. Discretization / Binning\n",
            "- **`pd.cut`**: Bin values into discrete intervals based on numerical edges (e.g. dividing Age into Child/Adult/Senior).\n",
            "- **`pd.qcut`**: Bin values into equal-sized quantiles (e.g., dividing salary into quartiles)."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = \"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv\"\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "# Average Fare by Passenger Class\n",
            "avg_fare_by_class = df.groupby('Pclass')['Fare'].mean()\n",
            "print(\"Average Fare by Pclass:\\n\", avg_fare_by_class)\n",
            "\n",
            "# Discretize Age into 3 bins\n",
            "df_clean = df.dropna(subset=['Age']).copy()\n",
            "df_clean['AgeGroup'] = pd.cut(df_clean['Age'], bins=[0, 12, 60, 100], labels=['Child', 'Adult', 'Senior'])\n",
            "print(\"\\nAge group counts:\\n\", df_clean['AgeGroup'].value_counts())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Use `groupby` to compute the survival rate (mean of `Survived`) grouped by passenger `Sex` and `Pclass` together."
        ],
        "exercise_code": [
            "survival_rates = df.groupby(['Sex', 'Pclass'])['Survived'].mean()\n",
            "print(\"Survival rates by Sex and Pclass:\\n\", survival_rates)\n"
        ]
    },
    7: {
        "title": "Data output/saving, working with CSV, JSON, SQL",
        "summary": "Saving DataFrames to CSV, JSON, and database tables.",
        "theory": [
            "### Exporting Data in Pandas\n",
            "Once data preprocessing is complete, we serialize it to external file formats using `to_*` methods:\n",
            "\n",
            "- `df.to_csv(filepath, index=False)`: Exports to CSV. Setting `index=False` prevents exporting row indices as a column.\n",
            "- `df.to_json(filepath)`: Exports data structure to JSON format.\n",
            "- `df.to_excel(filepath)`: Exports to Microsoft Excel sheets (requires openpyxl dependency)."
        ],
        "code": [
            "import pandas as pd\n",
            "import os\n",
            "\n",
            "data = {\n",
            "    'Product': ['Laptop', 'Mouse', 'Keyboard'],\n",
            "    'Price': [1200, 25, 45]\n",
            "}\n",
            "df = pd.DataFrame(data)\n",
            "\n",
            "# Save to CSV\n",
            "df.to_csv('products_exported.csv', index=False)\n",
            "print(\"File saved as products_exported.csv! Checking existence:\", os.path.exists('products_exported.csv'))\n",
            "\n",
            "# Clean up file\n",
            "if os.path.exists('products_exported.csv'):\n",
            "    os.remove('products_exported.csv')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create a dictionary representing student scores, load it into a DataFrame, and save it as a JSON file named `student_scores.json`."
        ],
        "exercise_code": [
            "students = pd.DataFrame({\n",
            "    'Student': ['Alice', 'Bob', 'Charlie'],\n",
            "    'Score': [92, 85, 88]\n",
            "})\n",
            "students.to_json('student_scores.json', indent=2)\n",
            "print(\"student_scores.json created!\")\n",
            "if os.path.exists('student_scores.json'):\n",
            "    os.remove('student_scores.json')\n"
        ]
    },
    8: {
        "title": "Pandas for plotting",
        "summary": "Built-in plotting capabilities of Pandas using Matplotlib backend.",
        "theory": [
            "### Built-in Plotting in Pandas\n",
            "Pandas provides wrapper methods around `matplotlib.pyplot` directly on Series and DataFrames via the `plot` accessor:\n",
            "\n",
            "- `df['col'].plot(kind='line')`: Line plots (default).\n",
            "- `df['col'].plot(kind='bar')`: Bar charts for categorical variables.\n",
            "- `df['col'].plot(kind='hist')`: Histograms for distributions.\n",
            "- `df.plot(kind='scatter', x, y)`: Scatter plots for bivariate analysis.\n",
            "- `df['col'].plot(kind='box')`: Box plots for statistical summaries (outliers)."
        ],
        "code": [
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "url = \"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv\"\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "# Generate plot data internally\n",
            "class_counts = df['Pclass'].value_counts().sort_index()\n",
            "\n",
            "# Plotting directly with Pandas\n",
            "class_counts.plot(kind='bar', title='Passenger Counts by Pclass')\n",
            "plt.xlabel('Passenger Class')\n",
            "plt.ylabel('Count')\n",
            "# We close or show depending on notebook context\n",
            "plt.close() # Prevents showing output during script run\n",
            "print(\"Pandas plot setup completed successfully!\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Plot a histogram of the `Age` column in the Titanic dataset with 20 bins."
        ],
        "exercise_code": [
            "df['Age'].plot(kind='hist', bins=20, title='Distribution of Passenger Ages')\n",
            "plt.xlabel('Age')\n",
            "plt.close()\n",
            "print(\"Histogram code executed!\")\n"
        ]
    },
    9: {
        "title": "Fetching from API and Web Scraping",
        "summary": "Loading JSON data from REST APIs and scraping HTML tables directly into DataFrames.",
        "theory": [
            "### Fetching Remote Web Data\n",
            "Pandas handles web scraping and API ingestion very efficiently:\n",
            "\n",
            "### 1. Ingesting APIs\n",
            "API JSON endpoints can be retrieved using standard `requests` and parsed into a DataFrame: `pd.DataFrame(requests.get(url).json())`.\n",
            "\n",
            "### 2. Reading HTML Tables\n",
            "**`pd.read_html(url)`**: Parses all HTML `<table>` elements in the web page into a list of DataFrames. Highly useful for scraping tabular data."
        ],
        "code": [
            "import pandas as pd\n",
            "import requests\n",
            "\n",
            "# Fetching mock JSON API data\n",
            "api_url = \"https://jsonplaceholder.typicode.com/posts\"\n",
            "response = requests.get(api_url)\n",
            "if response.status_code == 200:\n",
            "    posts_df = pd.DataFrame(response.json())\n",
            "    print(\"Data ingested from REST API (posts shape):\", posts_df.shape)\n",
            "    print(posts_df.head(2))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Fetch list of users from `https://jsonplaceholder.typicode.com/users` and display a DataFrame containing columns `id`, `name`, `username`, and `email`."
        ],
        "exercise_code": [
            "resp = requests.get(\"https://jsonplaceholder.typicode.com/users\")\n",
            "if resp.status_code == 200:\n",
            "    users = pd.DataFrame(resp.json())\n",
            "    print(\"Users subset:\\n\", users[['id', 'name', 'username', 'email']].head(3))\n"
        ]
    },
    10: {
        "title": "Correlation in Pandas",
        "summary": "Calculating correlation matrices for numerical columns using Pandas correlation methods.",
        "theory": [
            "### Linear Correlation in Pandas\n",
            "The correlation coefficient ($r$) measures the strength and direction of the linear relationship between two quantitative variables ($[-1, 1]$):\n",
            "- $r = 1$: Perfect positive relationship.\n",
            "- $r = -1$: Perfect negative relationship.\n",
            "- $r = 0$: No linear relationship.\n",
            "\n",
            "**`df.corr()`** computes the element-wise correlation matrix for all numerical columns in the DataFrame."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = \"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv\"\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "# Select numeric columns\n",
            "numeric_df = df.select_dtypes(include=['float64', 'int64'])\n",
            "print(\"Correlation Matrix on Iris:\\n\", numeric_df.corr())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Using the Titanic dataset, compute the correlation matrix for `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, and `Fare` columns, and find which variable correlates most with `Survived`."
        ],
        "exercise_code": [
            "titanic_url = \"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv\"\n",
            "t_df = pd.read_csv(titanic_url)\n",
            "cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']\n",
            "print(\"Titanic Correlation:\\n\", t_df[cols].corr())\n"
        ]
    },
    11: {
        "title": "Loading data with Pandas deep dive",
        "summary": "Advanced parameters for reading files: parsing columns, chunks loading, and memory optimization.",
        "theory": [
            "### Advanced File Ingestion\n",
            "When dealing with large datasets, loading options must be tuned to conserve system memory:\n",
            "\n",
            "- **`usecols`**: Reads only specific columns, avoiding loading unwanted data.\n",
            "- **`nrows`**: Loads only the first $N$ rows (great for schema inspection).\n",
            "- **`chunksize`**: Loads data iteratively in blocks of size $N$ as a generator, preventing Out-Of-Memory errors.\n",
            "- **`parse_dates`**: Automatically parses date strings into datetime objects during loading."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = \"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv\"\n",
            "\n",
            "# 1. Read only Name and Survived\n",
            "df_small = pd.read_csv(url, usecols=['Name', 'Survived'])\n",
            "print(\"Cols read with usecols:\", df_small.columns.tolist())\n",
            "\n",
            "# 2. Chunk loading\n",
            "chunk_iterator = pd.read_csv(url, chunksize=200)\n",
            "for i, chunk in enumerate(chunk_iterator, 1):\n",
            "    print(f\"Chunk {i} shape: {chunk.shape}\")\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Read the first 50 rows of Titanic selecting only Pclass, Sex, and Survived columns."
        ],
        "exercise_code": [
            "df_50 = pd.read_csv(url, usecols=['Pclass', 'Sex', 'Survived'], nrows=50)\n",
            "print(\"Shape of loaded slice:\", df_50.shape)\n"
        ]
    },
    12: {
        "title": "Understanding your data and EDA",
        "summary": "A full exploratory data analysis (EDA) pipeline using descriptive statistics.",
        "theory": [
            "### Exploratory Data Analysis (EDA)\n",
            "EDA is the practice of investigating datasets to summarize main patterns, identify anomalies, check assumptions, and visualize distributions. A standard EDA checklist includes:\n",
            "1. **Dimensions**: Checking shape ($N \\times M$).\n",
            "2. **Datatypes**: Inspecting column data types.\n",
            "3. **Null values**: Quantifying missing values.\n",
            "4. **Descriptive Stats**: Summarizing numerical ranges and categorical categories.\n",
            "5. **Groupings**: Splitting target variable across key categories."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = \"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv\"\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "print(\"--- 1. Shape of Data ---\")\n",
            "print(df.shape)\n",
            "\n",
            "print(\"\\n--- 2. Column Types ---\")\n",
            "print(df.dtypes)\n",
            "\n",
            "print(\"\\n--- 3. Missing Values ---\")\n",
            "print(df.isnull().sum())\n",
            "\n",
            "print(\"\\n--- 4. Summary Stats ---\")\n",
            "print(df.describe())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Write an EDA summary report on the Titanic dataset, detailing dimensions, data types, null counts, and mean survival rates grouped by Sex."
        ],
        "exercise_code": [
            "titanic_url = \"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv\"\n",
            "t_df = pd.read_csv(titanic_url)\n",
            "print(\"Shape:\", t_df.shape)\n",
            "print(\"Nulls:\\n\", t_df.isnull().sum())\n",
            "print(\"Survival rate by Sex:\\n\", t_df.groupby('Sex')['Survived'].mean())\n"
        ]
    }
}

PHASE_5_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Matplotlib Part 1",
        "summary": "Matplotlib fundamentals, figures, axes, line plots, scatter plots, basic styling, and customization.",
        "theory": [
            "### Matplotlib Fundamentals\n",
            "Matplotlib is the foundation of data visualization in Python. It uses a hierarchy of objects:\n",
            "- **Figure**: The overall window or page that holds the drawings.\n",
            "- **Axes**: The actual plotting area where data is drawn (each figure can have multiple axes).\n",
            "\n",
            "We can use the state-based interface (`plt.plot`) or the Object-Oriented (OO) interface (`fig, ax = plt.subplots()`). The OO interface is preferred for complex layouts."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "\n",
            "# 1. Generate synthetic data\n",
            "x = np.linspace(0, 10, 100)\n",
            "y1 = np.sin(x)\n",
            "y2 = np.cos(x)\n",
            "\n",
            "# 2. Plot using Object-Oriented interface\n",
            "fig, ax = plt.subplots(figsize=(8, 4))\n",
            "ax.plot(x, y1, label='Sin Wave', color='teal', linestyle='-', linewidth=2)\n",
            "ax.scatter(x[::5], y2[::5], label='Cos Points', color='coral', marker='o')\n",
            "\n",
            "ax.set_title('Sine Wave & Cosine Points')\n",
            "ax.set_xlabel('X Axis')\n",
            "ax.set_ylabel('Y Axis')\n",
            "ax.legend()\n",
            "ax.grid(True, linestyle='--', alpha=0.5)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Plot a custom mathematical function $y = x^2 - 4x + 4$ for $x \\in [-5, 5]$ as a dashed line. Add labels and a grid."
        ],
        "exercise_code": [
            "x_custom = np.linspace(-5, 5, 100)\n",
            "y_custom = x_custom**2 - 4*x_custom + 4\n",
            "fig, ax = plt.subplots()\n",
            "ax.plot(x_custom, y_custom, 'r--', label='quadratic')\n",
            "ax.set_title('Quadratic Plot')\n",
            "ax.set_xlabel('x')\n",
            "ax.set_ylabel('y')\n",
            "ax.legend()\n",
            "ax.grid(True)\n",
            "plt.show()\n"
        ]
    },
    2: {
        "title": "Matplotlib Part 2",
        "summary": "Subplots, advanced styling, bar plots, histograms, pie charts, and saving figures.",
        "theory": [
            "### Advanced Matplotlib Layouts\n",
            "Matplotlib allows grid layouts using `plt.subplots(nrows, ncols)`. We can customize multiple axes independently and save the resulting figures to disk using `fig.savefig('filename.png', dpi=300)`."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "import os\n",
            "\n",
            "categories = ['A', 'B', 'C', 'D']\n",
            "values = [20, 35, 40, 15]\n",
            "distribution = np.random.normal(0, 1, 1000)\n",
            "\n",
            "fig, axes = plt.subplots(1, 2, figsize=(12, 5))\n",
            "\n",
            "# Bar Plot\n",
            "axes[0].bar(categories, values, color='skyblue', edgecolor='black')\n",
            "axes[0].set_title('Categorical Bar Plot')\n",
            "\n",
            "# Histogram\n",
            "axes[1].hist(distribution, bins=30, color='violet', edgecolor='black', alpha=0.7)\n",
            "axes[1].set_title('Normal Distribution Histogram')\n",
            "\n",
            "plt.tight_layout()\n",
            "fig.savefig('matplotlib_subplot.png')\n",
            "plt.show()\n",
            "\n",
            "# Clean up saved file\n",
            "if os.path.exists('matplotlib_subplot.png'):\n",
            "    os.remove('matplotlib_subplot.png')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create a figure with a 2x1 grid of subplots. The first subplot should show a bar chart, and the second should show a histogram."
        ],
        "exercise_code": [
            "fig, axes = plt.subplots(2, 1, figsize=(6, 8))\n",
            "axes[0].bar(['Group 1', 'Group 2'], [10, 20], color='lightgreen')\n",
            "axes[0].set_title('Group Sizes')\n",
            "axes[1].hist(np.random.rand(100), bins=10, color='coral')\n",
            "axes[1].set_title('Uniform Distribution')\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ]
    },
    3: {
        "title": "Pandas Profiling",
        "summary": "Overview of automated EDA libraries, generating summaries, and reading reports.",
        "theory": [
            "### Automated Exploratory Data Analysis\n",
            "Automated profiling tools generate comprehensive statistics and summaries from DataFrames. We can inspect missing rates, correlations, histograms, and basic metadata programmatically."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = \"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv\"\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "print(\"=== Dataset Shape ===\")\n",
            "print(df.shape)\n",
            "print(\"\\n=== Column Data Types ===\")\n",
            "print(df.dtypes)\n",
            "print(\"\\n=== Missing Values Count ===\")\n",
            "print(df.isnull().sum())\n",
            "print(\"\\n=== Statistical Summary ===\")\n",
            "print(df.describe())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Load the Titanic dataset from the URL `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv` and print its missing values count and summary statistics."
        ],
        "exercise_code": [
            "titanic_url = \"https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv\"\n",
            "t_df = pd.read_csv(titanic_url)\n",
            "print(\"Missing values:\\n\", t_df.isnull().sum())\n",
            "print(\"\\nSummary statistics:\\n\", t_df.describe())\n"
        ]
    },
    4: {
        "title": "Seaborn: Distribution plots (distplot, jointplot, kdeplot)",
        "summary": "Visualizing continuous variables using Seaborn.",
        "theory": [
            "### Visualizing Distributions with Seaborn\n",
            "Seaborn makes statistical visualization easy. We can analyze the shapes of continuous variables using:\n",
            "- `histplot`: Displays the distribution of a single numerical variable.\n",
            "- `kdeplot`: Fits and plots a smooth kernel density estimate.\n",
            "- `jointplot`: Creates a multi-panel plot showing the relationship between two variables along with marginal distributions."
        ],
        "code": [
            "import seaborn as sns\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "tips = sns.load_dataset('tips')\n",
            "\n",
            "# KDE Plot\n",
            "plt.figure(figsize=(8, 4))\n",
            "sns.kdeplot(data=tips, x='total_bill', hue='time', fill=True, common_norm=False, palette='viridis')\n",
            "plt.title('Total Bill KDE by Time of Day')\n",
            "plt.show()\n",
            "\n",
            "# Joint Plot\n",
            "sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex', color='purple')\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Load the Iris dataset. Plot a `kdeplot` of `sepal_length` partitioned by `species` using the `hue` parameter."
        ],
        "exercise_code": [
            "iris = sns.load_dataset('iris')\n",
            "plt.figure(figsize=(8, 4))\n",
            "sns.kdeplot(data=iris, x='sepal_length', hue='species', fill=True)\n",
            "plt.title('Sepal Length KDE by Species')\n",
            "plt.show()\n"
        ]
    },
    5: {
        "title": "Seaborn: Categorical plots (boxplot, violinplot, barplot, countplot)",
        "summary": "Visualizing categorical relationships using Seaborn.",
        "theory": [
            "### Categorical Explorations\n",
            "When analyzing data, we often need to examine distributions of numerical values across different categorical groups:\n",
            "- `boxplot`: Displays five-number summaries and outlines outliers.\n",
            "- `violinplot`: Combines a boxplot with a kernel density plot to reveal distribution density shape.\n",
            "- `countplot`: Shows counts of observations in each categorical bin."
        ],
        "code": [
            "import seaborn as sns\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "tips = sns.load_dataset('tips')\n",
            "\n",
            "fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n",
            "\n",
            "# Boxplot\n",
            "sns.boxplot(ax=axes[0], data=tips, x='day', y='total_bill', hue='smoker', palette='Set2')\n",
            "axes[0].set_title('Boxplot of Total Bill by Day')\n",
            "\n",
            "# Violinplot\n",
            "sns.violinplot(ax=axes[1], data=tips, x='day', y='total_bill', hue='smoker', split=True, palette='muted')\n",
            "axes[1].set_title('Violinplot of Total Bill by Day')\n",
            "\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Load the Titanic dataset. Create a countplot displaying passenger class (`class`) frequencies grouped by survival status (`alive`) as the `hue` variable."
        ],
        "exercise_code": [
            "titanic = sns.load_dataset('titanic')\n",
            "plt.figure(figsize=(8, 4))\n",
            "sns.countplot(data=titanic, x='class', hue='alive', palette='coolwarm')\n",
            "plt.title('Survival count per Passenger Class')\n",
            "plt.show()\n"
        ]
    },
    6: {
        "title": "Seaborn: Matrix plots, Heatmap",
        "summary": "Multi-dimensional visual inspection, generating correlation matrices, and plotting styled Heatmaps.",
        "theory": [
            "### Correlation & Matrix Plotting\n",
            "Matrix plots represent correlation grids. We compute a pairwise Pearson correlation matrix first, then render it visually using `sns.heatmap` with annotations to quickly spot patterns."
        ],
        "code": [
            "import seaborn as sns\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "iris = sns.load_dataset('iris')\n",
            "corr_matrix = iris.drop(columns='species').corr()\n",
            "\n",
            "plt.figure(figsize=(8, 6))\n",
            "sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)\n",
            "plt.title('Iris Correlation Matrix Heatmap')\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Load the Titanic dataset, compute the correlation matrix of numerical features (`survived`, `pclass`, `age`, `sibsp`, `parch`, `fare`), and display it as a Heatmap."
        ],
        "exercise_code": [
            "titanic = sns.load_dataset('titanic')\n",
            "numeric_cols = titanic.select_dtypes(include=['float64', 'int64']).corr()\n",
            "plt.figure(figsize=(8, 6))\n",
            "sns.heatmap(numeric_cols, annot=True, cmap='mako')\n",
            "plt.title('Titanic Correlation Matrix')\n",
            "plt.show()\n"
        ]
    },
    7: {
        "title": "EDA using Univariate Analysis",
        "summary": "Single-variable EDA checklist, checking distributions, counts, and detecting anomalies.",
        "theory": [
            "### Univariate Analysis Checklist\n",
            "Univariate analysis examines one feature at a time. It covers:\n",
            "- **For Numeric Variables**: Statistics (mean, variance, quartiles) and plotting distributions via KDE or boxplot.\n",
            "- **For Categorical Variables**: Frequency tables and count plots."
        ],
        "code": [
            "import pandas as pd\n",
            "import seaborn as sns\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "tips = sns.load_dataset('tips')\n",
            "\n",
            "# 1. Statistical Summary\n",
            "print(\"=== Tip Column Statistics ===\")\n",
            "print(tips['tip'].describe())\n",
            "\n",
            "# 2. Plotting distribution\n",
            "fig, axes = plt.subplots(1, 2, figsize=(12, 4))\n",
            "sns.histplot(ax=axes[0], data=tips, x='tip', kde=True, color='purple')\n",
            "axes[0].set_title('Tip Distribution Histogram')\n",
            "\n",
            "sns.boxplot(ax=axes[1], data=tips, x='tip', color='lightgreen')\n",
            "axes[1].set_title('Tip Boxplot (Outlier Detection)')\n",
            "\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Conduct a univariate analysis on the `fare` column in the Titanic dataset. Print descriptive statistics and plot the distribution."
        ],
        "exercise_code": [
            "titanic = sns.load_dataset('titanic')\n",
            "print(titanic['fare'].describe())\n",
            "plt.figure(figsize=(8, 4))\n",
            "sns.histplot(data=titanic, x='fare', kde=True, bins=50)\n",
            "plt.title('Titanic Fare Distribution')\n",
            "plt.show()\n"
        ]
    },
    8: {
        "title": "EDA using Bivariate and Multivariate Analysis",
        "summary": "Multi-variable EDA checklist, exploring relationships, correlations, and interactions.",
        "theory": [
            "### Multi-variable Visual Inspections\n",
            "Bivariate analysis explores correlations between pairs of columns, while multivariate analysis uses color hue, markers, and sizing to examine multiple variables simultaneously."
        ],
        "code": [
            "import seaborn as sns\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "tips = sns.load_dataset('tips')\n",
            "\n",
            "# Bivariate Scatter plot with multi-dimensional dimensions\n",
            "plt.figure(figsize=(8, 5))\n",
            "sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', style='time', size='size', palette='deep')\n",
            "plt.title('Bivariate Scatter Plot with Multi-variables')\n",
            "plt.show()\n",
            "\n",
            "# Bivariate Boxplot\n",
            "plt.figure(figsize=(8, 4))\n",
            "sns.boxplot(data=tips, x='time', y='total_bill', hue='sex', palette='coolwarm')\n",
            "plt.title('Bivariate Comparison: Bill by Time & Sex')\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Create a `pairplot` of the Iris dataset, setting the `hue` column to `species` to analyze multivariate relationships."
        ],
        "exercise_code": [
            "iris = sns.load_dataset('iris')\n",
            "sns.pairplot(iris, hue='species')\n",
            "plt.show()\n"
        ]
    }
}


PHASE_6_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Data Science Life Cycle",
        "summary": "Overview of CRISP-DM and OSEMN frameworks and where data preprocessing fits.",
        "theory": [
            "### Data Science Lifecycle & Preprocessing\n",
            "The data science lifecycle is typically modeled using frameworks like **CRISP-DM** (Cross-Industry Standard Process for Data Mining) or **OSEMN**:\n",
            "1. **O**btain, 2. **S**crub, 3. **E**xplore, 4. **M**odel, 5. i**N**terpret.\n",
            "Data Preprocessing sits firmly in the **Scrub** phase and is estimated to take up to **70-80%** of a data scientist's time."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "# Load Titanic dataset to represent real-world data\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)\n",
            "print('=== Basic Scrubbing Checklist ===')\n",
            "print('Dataset Shape:', df.shape)\n",
            "print('\\nMissing values:\\n', df.isnull().sum())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the percentage of missing values for each column in the Titanic dataset."
        ],
        "exercise_code": [
            "missing_pct = (df.isnull().sum() / len(df)) * 100\n",
            "print('Missing value percentages:\\n', missing_pct)\n"
        ]
    },
    2: {
        "title": "Data in ML and How much data needed",
        "summary": "Sample size rules-of-thumb and dataset volume considerations.",
        "theory": [
            "### How Much Data is Needed?\n",
            "Common guidelines include:\n",
            "- **Rule of 10**: At least 10 times as many training examples as there are features.\n",
            "- **Complexity Scaling**: High-bias models (e.g., Naive Bayes) need less data; high-variance models (e.g., Deep Learning) need orders of magnitude more."
        ],
        "code": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "\n",
            "# Calculate feature-to-sample ratio\n",
            "features_count = 10\n",
            "recommended_samples = features_count * 10\n",
            "print(f'For {features_count} features, we need at least {recommended_samples} samples.')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the feature-to-sample ratio for the Titanic dataset (using all available raw columns)."
        ],
        "exercise_code": [
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)\n",
            "raw_cols = df.shape[1]\n",
            "samples = df.shape[0]\n",
            "ratio = samples / raw_cols\n",
            "print(f'Raw columns: {raw_cols}, Samples: {samples}, Ratio: {ratio:.2f}x')\n"
        ]
    },
    3: {
        "title": "Handling Missing Data: CCA, Imputers, MICE",
        "summary": "Complete Case Analysis (CCA), Simple Imputation, and MICE.",
        "theory": [
            "### Missing Data Mechanisms & Treatments\n",
            "- **MCAR** (Missing Completely at Random), **MAR** (Missing at Random), **MNAR** (Missing Not at Random).\n",
            "- **CCA** (Trimming missing rows): Only safe if MCAR and missingness is <5%.\n",
            "- **Simple Imputation**: Mean/Median/Mode substitution.\n",
            "- **MICE** (Multivariate Imputation by Chained Equations): Fills missing values using regression models on other variables iteratively."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.impute import SimpleImputer\n",
            "from sklearn.experimental import enable_iterative_imputer\n",
            "from sklearn.impute import IterativeImputer\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df_missing = pd.read_csv(url)[['Age', 'Fare']]\n",
            "\n",
            "# Simple Imputer\n",
            "si = SimpleImputer(strategy='median')\n",
            "df_si = pd.DataFrame(si.fit_transform(df_missing), columns=df_missing.columns)\n",
            "\n",
            "# MICE (Iterative Imputer)\n",
            "mice = IterativeImputer(max_iter=10, random_state=42)\n",
            "df_mice = pd.DataFrame(mice.fit_transform(df_missing), columns=df_missing.columns)\n",
            "print('Original Nulls:', df_missing['Age'].isnull().sum())\n",
            "print('Simple Imputed Nulls:', df_si['Age'].isnull().sum())\n",
            "print('MICE Imputed Nulls:', df_mice['Age'].isnull().sum())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Perform mode imputation on the 'Embarked' column of the Titanic dataset."
        ],
        "exercise_code": [
            "embarked_missing = pd.read_csv(url)[['Embarked']]\n",
            "mode_imputer = SimpleImputer(strategy='most_frequent')\n",
            "embarked_imputed = mode_imputer.fit_transform(embarked_missing)\n",
            "print('Nulls remaining:', pd.Series(embarked_imputed.flatten()).isnull().sum())\n"
        ]
    },
    4: {
        "title": "Managing Missing Features",
        "summary": "Using Missing Indicators to preserve information about missing values.",
        "theory": [
            "### Missing Indicators\n",
            "Sometimes the *absence* of data is itself a strong predictor. We create binary columns where $1$ denotes missing and $0$ denotes present before imputing."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.impute import MissingIndicator\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Age']]\n",
            "\n",
            "indicator = MissingIndicator()\n",
            "missing_mask = indicator.fit_transform(df)\n",
            "df['Age_Was_Missing'] = missing_mask.astype(int)\n",
            "print(df.head(10))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Apply the Scikit-Learn `SimpleImputer` to the 'Age' column while setting the `add_indicator=True` parameter, and print the output shape."
        ],
        "exercise_code": [
            "from sklearn.impute import SimpleImputer\n",
            "imputer_with_indicator = SimpleImputer(strategy='mean', add_indicator=True)\n",
            "res = imputer_with_indicator.fit_transform(df[['Age']])\n",
            "print('Output shape after imputation + indicator:', res.shape)\n"
        ]
    },
    5: {
        "title": "Outlier detection: Z score, IQR, Percentile, Winsorization",
        "summary": "Outlier detection strategies: mathematical capping vs trimming.",
        "theory": [
            "### Outlier Methods\n",
            "- **Z-Score Method**: Points beyond $\\pm 3$ standard deviations from the mean (safe for Gaussian data).\n",
            "- **IQR Method**: Bounds are $Q_1 - 1.5 \\times IQR$ and $Q_3 + 1.5 \\times IQR$.\n",
            "- **Winsorization**: Capping outlier values at specific percentiles (e.g., 1st and 99th)."
        ],
        "code": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Fare']].dropna()\n",
            "\n",
            "# IQR Calculation\n",
            "q1 = df['Fare'].quantile(0.25)\n",
            "q3 = df['Fare'].quantile(0.75)\n",
            "iqr = q3 - q1\n",
            "lower_bound = q1 - 1.5 * iqr\n",
            "upper_bound = q3 + 1.5 * iqr\n",
            "\n",
            "outliers = df[(df['Fare'] < lower_bound) | (df['Fare'] > upper_bound)]\n",
            "print(f'Found {len(outliers)} outliers using IQR method.')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Implement Winsorization (capping values at the 95th percentile) for the 'Fare' column."
        ],
        "exercise_code": [
            "p95 = df['Fare'].quantile(0.95)\n",
            "df['Fare_Capped'] = np.where(df['Fare'] > p95, p95, df['Fare'])\n",
            "print('Max fare before capping:', df['Fare'].max())\n",
            "print('Max fare after capping:', df['Fare_Capped'].max())\n"
        ]
    },
    6: {
        "title": "Feature Scaling: Standardization",
        "summary": "Mathematical details and application of Standardization (Z-score scaling).",
        "theory": [
            "### Standardization\n",
            "Standardization transforms features to have a mean of 0 and a standard deviation of 1:\n",
            "$$z = \\frac{x - \\mu}{\\sigma}$$"
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Age', 'Fare']].dropna()\n",
            "\n",
            "scaler = StandardScaler()\n",
            "scaled_features = scaler.fit_transform(df)\n",
            "df_scaled = pd.DataFrame(scaled_features, columns=df.columns)\n",
            "print('Scaled Means:\\n', df_scaled.mean().round(4))\n",
            "print('\\nScaled Std Devs:\\n', df_scaled.std().round(4))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Verify manually that the standard deviation of the scaled 'Age' column is 1.0."
        ],
        "exercise_code": [
            "import numpy as np\n",
            "print('Manual calculation of scaled standard deviation:', np.std(df_scaled['Age'], ddof=1))\n"
        ]
    },
    7: {
        "title": "Feature Scaling: Normalization, MinMax, MaxAbs, Robust",
        "summary": "Range-bound scaling (MinMax, MaxAbs, and Robust Scalers).",
        "theory": [
            "### Range Scalers\n",
            "- **MinMaxScaler**: Scales to a range (usually $[0, 1]$): $x_{scaled} = \\frac{x - x_{min}}{x_{max} - x_{min}}$.\n",
            "- **MaxAbsScaler**: Scales to $[-1, 1]$ by dividing by max absolute value: $x_{scaled} = \\frac{x}{|x|_{max}}$.\n",
            "- **RobustScaler**: Scales using median and IQR, making it robust to outliers: $x_{scaled} = \\frac{x - Median}{IQR}$."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import MinMaxScaler, RobustScaler\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Age', 'Fare']].dropna()\n",
            "\n",
            "minmax = MinMaxScaler()\n",
            "robust = RobustScaler()\n",
            "\n",
            "df_minmax = pd.DataFrame(minmax.fit_transform(df), columns=df.columns)\n",
            "df_robust = pd.DataFrame(robust.fit_transform(df), columns=df.columns)\n",
            "print('MinMax range of Fare:', df_minmax['Fare'].min(), 'to', df_minmax['Fare'].max())\n",
            "print('Robust range of Fare:', df_robust['Fare'].min(), 'to', df_robust['Fare'].max())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Apply MaxAbsScaler to the 'Fare' column and print the maximum value of the scaled variable."
        ],
        "exercise_code": [
            "from sklearn.preprocessing import MaxAbsScaler\n",
            "maxabs = MaxAbsScaler()\n",
            "res = maxabs.fit_transform(df[['Fare']])\n",
            "print('MaxAbs scaled maximum fare:', res.max())\n"
        ]
    },
    8: {
        "title": "Feature Scaling deep dive",
        "summary": "Comparing distribution outputs of different scaling algorithms.",
        "theory": [
            "### Scaler Comparison\n",
            "StandardScaler changes scale but keeps the relative variance structure. MinMaxScaler bounds the domain strictly to $[0, 1]$. RobustScaler does not compress the outliers, keeping the IQR core structured."
        ],
        "code": [
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Age']].dropna()\n",
            "\n",
            "# Run scalers\n",
            "df['Standard'] = StandardScaler().fit_transform(df[['Age']])\n",
            "df['MinMax'] = MinMaxScaler().fit_transform(df[['Age']])\n",
            "df['Robust'] = RobustScaler().fit_transform(df[['Age']])\n",
            "\n",
            "print(df.describe().round(3))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Plot the density of the three scaled columns to compare their distributions."
        ],
        "exercise_code": [
            "df[['Standard', 'MinMax', 'Robust']].plot(kind='kde', figsize=(8, 4))\n",
            "plt.title('Density Comparison of Scalers')\n",
            "plt.show()\n"
        ]
    },
    9: {
        "title": "Managing Categorical Data",
        "summary": "Handling categories, cardinalities, and sorting categories.",
        "theory": [
            "### Categorical Variables\n",
            "- **Nominal**: Variables with no implicit ordering (e.g., City, Gender).\n",
            "- **Ordinal**: Variables with a defined, sequential order (e.g., Education: High School < Bachelor's < Ph.D.).\n",
            "- High cardinality refers to categorical features with many unique levels, which can expand dimensions significantly if OHE is applied."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)\n",
            "\n",
            "print('=== Unique Value Counts (Cardinality) ===')\n",
            "print(df.select_dtypes(include=['object']).nunique())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Categorize raw columns in the Titanic dataset into nominal and ordinal feature groups."
        ],
        "exercise_code": [
            "print('Nominal: Sex, Embarked, Ticket, Cabin, Name')\n",
            "print('Ordinal/Discrete: Pclass, SibSp, Parch')\n"
        ]
    },
    10: {
        "title": "Encoding: Label, Ordinal",
        "summary": "Encoding ordinal variables cleanly.",
        "theory": [
            "### Label vs Ordinal Encoding\n",
            "- `LabelEncoder`: Encodes values to 0..n-1 integers. Typically used for target variables.\n",
            "- `OrdinalEncoder`: Encodes features. Allows custom ordering mapping for categories."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import OrdinalEncoder\n",
            "\n",
            "df = pd.DataFrame({'Size': ['Small', 'Medium', 'Large', 'Medium']})\n",
            "\n",
            "# Explicitly mapping order\n",
            "encoder = OrdinalEncoder(categories=[['Small', 'Medium', 'Large']])\n",
            "df['Size_Encoded'] = encoder.fit_transform(df[['Size']])\n",
            "print(df)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Map the 'Pclass' category from Titanic dataset using OrdinalEncoder and output its mapping array."
        ],
        "exercise_code": [
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "titanic_df = pd.read_csv(url)[['Pclass']]\n",
            "oe = OrdinalEncoder()\n",
            "titanic_df['Pclass_Encoded'] = oe.fit_transform(titanic_df)\n",
            "print(oe.categories_)\n"
        ]
    },
    11: {
        "title": "One Hot Encoding",
        "summary": "One-Hot Encoding and avoiding the Dummy Variable Trap.",
        "theory": [
            "### One-Hot Encoding\n",
            "For nominal variables, we split the feature into $N$ binary dummy columns. To prevent multicollinearity (where one column can be perfectly predicted from the others), we set `drop='first'` to exclude the reference category."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import OneHotEncoder\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Sex']].dropna()\n",
            "\n",
            "ohe = OneHotEncoder(drop='first', sparse_output=False)\n",
            "encoded_sex = ohe.fit_transform(df[['Sex']])\n",
            "df_encoded = pd.DataFrame(encoded_sex, columns=ohe.get_feature_names_out())\n",
            "print(df_encoded.head())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. One-hot encode the 'Embarked' column dropping the first value."
        ],
        "exercise_code": [
            "embarked_df = pd.read_csv(url)[['Embarked']].dropna()\n",
            "ohe_emb = OneHotEncoder(drop='first', sparse_output=False)\n",
            "encoded_emb = ohe_emb.fit_transform(embarked_df)\n",
            "print(pd.DataFrame(encoded_emb, columns=ohe_emb.get_feature_names_out()).head())\n"
        ]
    },
    12: {
        "title": "Fit and Transform method",
        "summary": "Avoiding Data Leakage with fit and transform methods.",
        "theory": [
            "### Avoiding Data Leakage\n",
            "Data leakage occurs when target or test information leaks into model preparation. We must:\n",
            "1. Call `fit_transform` on the **Training Set** only (which stores parameters like mean and std).\n",
            "2. Call `transform` on the **Testing Set** (applying the same stored parameter values without calculating new ones)."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Age', 'Fare']].dropna()\n",
            "\n",
            "X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)\n",
            "\n",
            "scaler = StandardScaler()\n",
            "X_train_scaled = scaler.fit_transform(X_train)\n",
            "# Transform only!\n",
            "X_test_scaled = scaler.transform(X_test)\n",
            "print('Scaler Mean parameter stored:', scaler.mean_)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain what would happen if you ran `fit_transform` separately on both train and test partitions."
        ],
        "exercise_code": [
            "print('It would compute separate means/standard deviations for the test set, creating data leakage and inconsistent feature scaling.')\n"
        ]
    },
    13: {
        "title": "Column Transformer and Pipelines",
        "summary": "Building automated preprocessing Pipelines with ColumnTransformer.",
        "theory": [
            "### ColumnTransformer & Pipelines\n",
            "We construct pipelines to chain imputations, encodings, and scaling steps dynamically across heterogeneous column groupings, ensuring a clean and reproducible pipeline."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.pipeline import Pipeline\n",
            "from sklearn.compose import ColumnTransformer\n",
            "from sklearn.impute import SimpleImputer\n",
            "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Age', 'Fare', 'Sex', 'Embarked', 'Pclass']].dropna()\n",
            "# Drop Pclass from columns so we can use same num/cat features\n",
            "\n",
            "num_pipeline = Pipeline([\n",
            "    ('impute', SimpleImputer(strategy='median')),\n",
            "    ('scale', StandardScaler())\n",
            "])\n",
            "\n",
            "cat_pipeline = Pipeline([\n",
            "    ('encode', OneHotEncoder(drop='first', sparse_output=False))\n",
            "])\n",
            "\n",
            "preprocessor = ColumnTransformer([\n",
            "    ('num', num_pipeline, ['Age', 'Fare']),\n",
            "    ('cat', cat_pipeline, ['Sex', 'Embarked'])\n",
            "])\n",
            "\n",
            "processed_data = preprocessor.fit_transform(df)\n",
            "print('Processed output shape:', processed_data.shape)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Add 'Pclass' to the categorical pipeline of features inside the preprocessor."
        ],
        "exercise_code": [
            "preprocessor_new = ColumnTransformer([\n",
            "    ('num', num_pipeline, ['Age', 'Fare']),\n",
            "    ('cat', cat_pipeline, ['Sex', 'Embarked', 'Pclass'])\n",
            "])\n",
            "res = preprocessor_new.fit_transform(df)\n",
            "print('New Processed output shape:', res.shape)\n"
        ]
    },
    14: {
        "title": "Function Transforms: Log, Reciprocal, Square Root",
        "summary": "Transforming right-skewed feature ranges to normal shapes.",
        "theory": [
            "### Function Transformations\n",
            "Right-skewed data can be normalized using mathematical transformations:\n",
            "- **Log Transform**: $y = \\log(x + 1)$. Essential for variables with exponential distribution.\n",
            "- **Reciprocal Transform**: $y = 1 / x$.\n",
            "- **Square Root**: $y = \\sqrt{x}$."
        ],
        "code": [
            "import pandas as pd\n",
            "import numpy as np\n",
            "from sklearn.preprocessing import FunctionTransformer\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Fare']].dropna()\n",
            "\n",
            "log_transformer = FunctionTransformer(np.log1p)\n",
            "df['Log_Fare'] = log_transformer.transform(df[['Fare']])\n",
            "print('Original skewness:', df['Fare'].skew())\n",
            "print('Log Transformed skewness:', df['Log_Fare'].skew())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Plot the distribution of the original and log-transformed Fare using seaborn."
        ],
        "exercise_code": [
            "import seaborn as sns\n",
            "import matplotlib.pyplot as plt\n",
            "fig, axes = plt.subplots(1, 2, figsize=(10, 4))\n",
            "sns.histplot(df['Fare'], ax=axes[0], kde=True)\n",
            "sns.histplot(df['Log_Fare'], ax=axes[1], kde=True)\n",
            "plt.show()\n"
        ]
    },
    15: {
        "title": "Power Transformer: Box Cox, Yeo Johnson",
        "summary": "Advanced Box-Cox and Yeo-Johnson transformations.",
        "theory": [
            "### Power Transforms\n",
            "- **Box-Cox**: Requires strictly positive data ($x > 0$). Uses parameter estimation to select the optimal power transform.\n",
            "- **Yeo-Johnson**: Generalization that supports zero and negative values."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import PowerTransformer\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Fare']].dropna()\n",
            "\n",
            "pt = PowerTransformer(method='yeo-johnson')\n",
            "df['Yeo_Fare'] = pt.fit_transform(df[['Fare']])\n",
            "print('Yeo-Johnson Transformed Skewness:', df['Yeo_Fare'].skew())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Fit the Box-Cox transformer to the 'Fare' column (filter out values $\\leq 0$ first) and print its optimal lambda parameter."
        ],
        "exercise_code": [
            "positive_fares = df[df['Fare'] > 0][['Fare']]\n",
            "bc = PowerTransformer(method='box-cox')\n",
            "bc.fit(positive_fares)\n",
            "print('Optimal Box-Cox lambda:', bc.lambdas_)\n"
        ]
    },
    16: {
        "title": "Binning and Binarization: Quantile, KMeans",
        "summary": "Discretization and thresholding.",
        "theory": [
            "### Discretization & Binarization\n",
            "- **Binning**: Converting a continuous feature into discrete bins (e.g. groups of ages). Types: Equal-width, Quantile (equal-frequency), or K-Means.\n",
            "- **Binarization**: Thresholding features to binary $[0, 1]$ flags."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import KBinsDiscretizer, Binarizer\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Age', 'Fare']].dropna()\n",
            "\n",
            "# Binning Age into 5 bins\n",
            "kbd = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='quantile')\n",
            "df['Age_Binned'] = kbd.fit_transform(df[['Age']])\n",
            "\n",
            "# Binarizing Fare at 20.0\n",
            "binarizer = Binarizer(threshold=20.0)\n",
            "df['Fare_Over_20'] = binarizer.transform(df[['Fare']])\n",
            "print(df.head())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Binarize the 'Age' column of the Titanic dataset at threshold 18.0 to mark minor status."
        ],
        "exercise_code": [
            "bin_age = Binarizer(threshold=18.0)\n",
            "is_adult = bin_age.transform(df[['Age']])\n",
            "print('\\nAdult status counts:\\n', pd.Series(is_adult.flatten()).value_counts())\n"
        ]
    },
    17: {
        "title": "Handling Mixed and Date/Time Variables",
        "summary": "Deconstructing mixed alphanumeric and datetime features.",
        "theory": [
            "### Mixed Data Processing\n",
            "- **Mixed variables**: Features containing both numbers and text (e.g., ticket codes). We split these into separate numeric and categorical columns.\n",
            "- **DateTime variables**: Features representing timestamps. We extract year, month, day, day of week, or hour."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "# Alphanumeric splitting\n",
            "df = pd.DataFrame({'Ticket': ['A/5 21171', 'PC 17599', '3101298']})\n",
            "df['Ticket_Num'] = df['Ticket'].str.extract(r'(\\d+)')\n",
            "df['Ticket_Cat'] = df['Ticket'].str.extract(r'([a-zA-Z/\\.]+)')\n",
            "df['Ticket_Cat'] = df['Ticket_Cat'].fillna('Numeric')\n",
            "print(df)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Parse the string date series `['2025-08-30 14:30:00', '2025-08-31 15:45:00']` and extract the Hour and Day of Week features."
        ],
        "exercise_code": [
            "dates = pd.Series(pd.to_datetime(['2025-08-30 14:30:00', '2025-08-31 15:45:00']))\n",
            "print('Hours:', dates.dt.hour.values)\n",
            "print('Days of week:', dates.dt.dayofweek.values)\n"
        ]
    },
    18: {
        "title": "Feature Construction and Splitting",
        "summary": "Building new compound variables and splitting existing string fields.",
        "theory": [
            "### Feature Construction\n",
            "Creating new variables by combining existing features (e.g. creating `FamilySize = SibSp + Parch + 1` or calculating ratios like `FarePerPerson = Fare / FamilySize`)."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['SibSp', 'Parch', 'Fare']]\n",
            "\n",
            "df['Family_Size'] = df['SibSp'] + df['Parch'] + 1\n",
            "df['Fare_Per_Person'] = df['Fare'] / df['Family_Size']\n",
            "print(df.head())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Construct a binary feature 'Is_Alone' which evaluates to 1 if Family Size is 1, and 0 otherwise."
        ],
        "exercise_code": [
            "df['Is_Alone'] = (df['Family_Size'] == 1).astype(int)\n",
            "print(df['Is_Alone'].value_counts())\n"
        ]
    },
    19: {
        "title": "What is Feature Engineering",
        "summary": "Generating Polynomial and Interaction features.",
        "theory": [
            "### Feature Engineering Overview\n",
            "Feature Engineering is the process of using domain knowledge to extract features from raw data. We can automate this using methods like `PolynomialFeatures` to capture non-linear relationships."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import PolynomialFeatures\n",
            "\n",
            "df = pd.DataFrame({'X1': [2, 3, 4], 'X2': [5, 6, 7]})\n",
            "\n",
            "poly = PolynomialFeatures(degree=2, include_bias=False)\n",
            "poly_feats = poly.fit_transform(df)\n",
            "df_poly = pd.DataFrame(poly_feats, columns=poly.get_feature_names_out())\n",
            "print(df_poly)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Apply PolynomialFeatures of degree 2 to the features 'Age' and 'Fare' in the Titanic dataset."
        ],
        "exercise_code": [
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "titanic_feats = pd.read_csv(url)[['Age', 'Fare']].dropna()\n",
            "poly_res = poly.fit_transform(titanic_feats)\n",
            "print('Output dimension after polynomial expansion:', poly_res.shape)\n"
        ]
    },
    20: {
        "title": "Feature Selection Techniques",
        "summary": "VarianceThreshold, SelectKBest, and basic feature selection algorithms.",
        "theory": [
            "### Feature Selection\n",
            "- **Filter Methods**: Select features based on statistical scores (e.g. ANOVA F-value, Chi-Square, Mutual Information).\n",
            "- **Wrapper Methods**: Search through subsets of features recursively (e.g. Recursive Feature Elimination).\n",
            "- **Embedded Methods**: Features selected during model training (e.g. Lasso regularization)."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.feature_selection import SelectKBest, f_classif\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Survived', 'Pclass', 'SibSp', 'Parch', 'Fare']].dropna()\n",
            "X = df.drop(columns='Survived')\n",
            "y = df['Survived']\n",
            "\n",
            "# Select the 2 best features\n",
            "selector = SelectKBest(score_func=f_classif, k=2)\n",
            "X_selected = selector.fit_transform(X, y)\n",
            "print('Selected Features:', selector.get_feature_names_out())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Fit a `VarianceThreshold` selector to drop columns with near-zero variance on a mock binary matrix."
        ],
        "exercise_code": [
            "from sklearn.feature_selection import VarianceThreshold\n",
            "import numpy as np\n",
            "X_bin = np.array([[1, 0, 1], [1, 0, 0], [1, 0, 1]])\n",
            "vt = VarianceThreshold(threshold=0.1)\n",
            "print('\\nSelected columns:\\n', vt.fit_transform(X_bin))\n"
        ]
    },
    21: {
        "title": "Feature Extraction",
        "summary": "Dimensionality reduction using Principal Component Analysis (PCA).",
        "theory": [
            "### Feature Extraction & PCA\n",
            "PCA projects data from its original high-dimensional space to a lower-dimensional subspace of orthogonal components called principal components, which maximize the explained variance."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "from sklearn.decomposition import PCA\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'\n",
            "df = pd.read_csv(url)\n",
            "X = df.drop(columns='species')\n",
            "y = df['species']\n",
            "\n",
            "X_scaled = StandardScaler().fit_transform(X)\n",
            "\n",
            "pca = PCA(n_components=2)\n",
            "X_pca = pca.fit_transform(X_scaled)\n",
            "print('PCA component shapes:', X_pca.shape)\n",
            "print('Explained variance ratio:', pca.explained_variance_ratio_)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the cumulative sum of explained variance from PCA for all 4 components of the Iris features."
        ],
        "exercise_code": [
            "pca_full = PCA(n_components=4)\n",
            "pca_full.fit(X_scaled)\n",
            "import numpy as np\n",
            "print('Cumulative explained variance:', np.cumsum(pca_full.explained_variance_ratio_))\n"
        ]
    },
    22: {
        "title": "Curse of Dimensionality",
        "summary": "Analyzing feature expansion problems mathematically.",
        "theory": [
            "### The Curse of Dimensionality\n",
            "As the number of features (dimensions) increases, the volume of the space grows exponentially. This causes:\n",
            "1. Sparsity of training samples.\n",
            "2. Distances between points to converge (making clustering and distance-based models less effective)."
        ],
        "code": [
            "import numpy as np\n",
            "from scipy.spatial.distance import pdist\n",
            "\n",
            "# Generate random points in 2D vs 100D\n",
            "pts_2d = np.random.rand(100, 2)\n",
            "pts_100d = np.random.rand(100, 100)\n",
            "\n",
            "dist_2d = pdist(pts_2d)\n",
            "dist_100d = pdist(pts_100d)\n",
            "\n",
            "print('Ratio of (Max - Min) / Min distance:')\n",
            "print('2D:', (dist_2d.max() - dist_2d.min()) / dist_2d.min())\n",
            "print('100D:', (dist_100d.max() - dist_100d.min()) / dist_100d.min())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Discuss how the difference between maximum and minimum distance changes as dimensions increase."
        ],
        "exercise_code": [
            "print('As dimensions increase, the distance between any two points converges, reducing discriminative distance indicators.')\n"
        ]
    },
    23: {
        "title": "Data Preprocessing and Cleaning overview",
        "summary": "A summary checklist for standard data preprocessing pipelines.",
        "theory": [
            "### Preprocessing Summary Checklist\n",
            "1. Resolve Nulls (Imputation or Indicators).\n",
            "2. Encode Categories (One-Hot or Ordinal).\n",
            "3. Scale numeric parameters (Standardization or MinMaxScaler).\n",
            "4. Correct skewed variables (Power Transformations).\n",
            "5. Apply pipeline to train and test splits to prevent leakage."
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "print('=== Typical Pipeline Order ===')\n",
            "print('Raw Data -> Train/Test Split -> Missing Treatment -> Encode Categories -> Scale Features -> Model')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Formulate a step-by-step preprocessing pipeline plan for predicting house prices."
        ],
        "exercise_code": [
            "print('1. Impute missing square footage (median), 2. Target encode Neighborhoods, 3. Log-transform sale price target, 4. Scale inputs using StandardScaler.')\n"
        ]
    },
    24: {
        "title": "Normalization with Python",
        "summary": "Code-only exercises for MinMaxScaler.",
        "theory": [
            "### MinMaxScaler Code Verification\n",
            "Normalizing values to a strict $[0, 1]$ range."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import MinMaxScaler\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Fare']].dropna()\n",
            "\n",
            "scaler = MinMaxScaler()\n",
            "df['Normalized_Fare'] = scaler.fit_transform(df[['Fare']])\n",
            "print(df.describe())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Normalize the 'Age' column of the Titanic dataset and print the minimum and maximum scaled values."
        ],
        "exercise_code": [
            "age_col = pd.read_csv(url)[['Age']].dropna()\n",
            "scaled_age = MinMaxScaler().fit_transform(age_col)\n",
            "print('Min scaled age:', scaled_age.min())\n",
            "print('Max scaled age:', scaled_age.max())\n"
        ]
    },
    25: {
        "title": "Standardization with Python",
        "summary": "Code-only exercises for StandardScaler.",
        "theory": [
            "### StandardScaler Code Verification\n",
            "Scaling values to zero mean and unit variance."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Age']].dropna()\n",
            "\n",
            "scaler = StandardScaler()\n",
            "df['Standardized_Age'] = scaler.fit_transform(df[['Age']])\n",
            "print(df.describe())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Standardize the 'Fare' column and check if the mean is approximately 0."
        ],
        "exercise_code": [
            "fare_col = pd.read_csv(url)[['Fare']].dropna()\n",
            "scaled_fare = StandardScaler().fit_transform(fare_col)\n",
            "print('Scaled mean:', scaled_fare.mean().round(6))\n"
        ]
    },
    26: {
        "title": "Binarization with Python",
        "summary": "Code-only exercises for Binarizer.",
        "theory": [
            "### Binarizer Code Verification\n",
            "Thresholding features to binary variables."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.preprocessing import Binarizer\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Fare']].dropna()\n",
            "\n",
            "binarizer = Binarizer(threshold=50.0)\n",
            "df['High_Fare'] = binarizer.transform(df[['Fare']])\n",
            "print(df['High_Fare'].value_counts())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Binarize the 'Age' column of the Titanic dataset at threshold 60.0 to identify elderly passengers."
        ],
        "exercise_code": [
            "age_col = pd.read_csv(url)[['Age']].dropna()\n",
            "is_elderly = Binarizer(threshold=60.0).transform(age_col)\n",
            "print('\\nElderly counts:\\n', pd.Series(is_elderly.flatten()).value_counts())\n"
        ]
    },
    27: {
        "title": "Training and Testing data split with Python",
        "summary": "Code-only exercises for train_test_split.",
        "theory": [
            "### Train Test Splitting\n",
            "Partitioning datasets into training and validation sets to validate model performance."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'\n",
            "df = pd.read_csv(url)[['Survived', 'Pclass', 'Sex', 'Age']].dropna()\n",
            "\n",
            "X = df.drop(columns='Survived')\n",
            "y = df['Survived']\n",
            "\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)\n",
            "print('Train size:', X_train.shape)\n",
            "print('Test size:', X_test.shape)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Split the Iris dataset into 70% train and 30% test sets, stratified by species."
        ],
        "exercise_code": [
            "from sklearn.datasets import load_iris\n",
            "iris = load_iris()\n",
            "X_iris, y_iris = iris.data, iris.target\n",
            "X_tr, X_te, y_tr, y_te = train_test_split(X_iris, y_iris, test_size=0.3, random_state=42, stratify=y_iris)\n",
            "print('Iris Train split shape:', X_tr.shape)\n",
            "print('Iris Test split shape:', X_te.shape)\n"
        ]
    }
}



PHASE_7_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Regression intro and dependent/independent variables",
        "summary": "Introduction to regression modeling and target vs predictor variables.",
        "theory": [
            "### Regression Analysis\n",
            "Regression is a supervised learning task where the goal is to predict a continuous numerical value $Y$ based on one or more input features $X$.\n",
            "- **Independent Variable ($X$):** The predictor, input, or feature.\n",
            "- **Dependent Variable ($Y$):** The target, output, or response.\n",
            "Examples: House size ($X$) vs price ($Y$), study hours ($X$) vs grade ($Y$)."
        ],
        "code": [
            "import pandas as pd\n",
            "import seaborn as sns\n",
            "\n",
            "tips = sns.load_dataset('tips')\n",
            "print('Tips dataset columns:', tips.columns.tolist())\n",
            "print(tips[['total_bill', 'tip']].head())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Identify the independent and dependent variables in a dataset predicting car fuel efficiency (mpg) from weight and horsepower."
        ],
        "exercise_code": [
            "print('Independent variables: Weight, Horsepower')\n",
            "print('Dependent variable: mpg')\n"
        ]
    },
    2: {
        "title": "Stanford CS229 Lec 2: Linear Regression and GD full math",
        "summary": "Mathematical foundations of Linear Regression, hypothesis representation, and gradient descent.",
        "theory": [
            "### Mathematical Formulation\n",
            "- **Hypothesis:** $h_\\theta(x) = \\sum_{j=0}^n \\theta_j x_j = \\theta^T x$ (where $x_0 = 1$)\n",
            "- **Cost Function (Mean Squared Error):** $J(\\theta) = \\frac{1}{2m} \\sum_{i=1}^m (h_\\theta(x^{(i)}) - y^{(i)})^2$\n",
            "- **Gradient Descent Update Rule:** \\theta_j := \\theta_j - \\alpha \\frac{\\partial J(\\theta)}{\\partial \\theta_j}$"
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Simulate a quadratic cost function curve J(theta)\n",
            "theta = np.linspace(-10, 10, 100)\n",
            "J = 0.5 * (theta - 2)**2 + 3\n",
            "\n",
            "plt.plot(theta, J, label='Cost Function J(theta)')\n",
            "plt.axvline(2, color='red', linestyle='--', label='Optimal theta=2')\n",
            "plt.xlabel('theta')\n",
            "plt.ylabel('J(theta)')\n",
            "plt.legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Plot the gradient tangent line at $\\theta = -5$ for the simulated cost function."
        ],
        "exercise_code": [
            "theta_val = -5\n",
            "J_val = 0.5 * (theta_val - 2)**2 + 3\n",
            "slope = theta_val - 2\n",
            "tangent = slope * (theta - theta_val) + J_val\n",
            "plt.plot(theta, J, label='Cost Function')\n",
            "plt.plot(theta, tangent, '--', label='Tangent at theta=-5')\n",
            "plt.scatter([theta_val], [J_val], color='red')\n",
            "plt.ylim(0, 50)\n",
            "plt.legend()\n",
            "plt.show()\n"
        ]
    },
    3: {
        "title": "Simple Linear Regression: intuition and code",
        "summary": "Simple linear regression intuition, line of best fit y = mx + c, and Scikit-Learn LinearRegression.",
        "theory": [
            "### Simple Linear Regression\n",
            "Fits a straight line to the data: $y = mx + c$, where $m$ is the slope and $c$ is the intercept."
        ],
        "code": [
            "import pandas as pd\n",
            "import seaborn as sns\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.linear_model import LinearRegression\n",
            "\n",
            "tips = sns.load_dataset('tips')\n",
            "X = tips[['total_bill']]\n",
            "y = tips['tip']\n",
            "\n",
            "model = LinearRegression()\n",
            "model.fit(X, y)\n",
            "print('Slope (m):', model.coef_[0])\n",
            "print('Intercept (c):', model.intercept_)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Use the trained model to predict the tip for a total bill of $30.00."
        ],
        "exercise_code": [
            "pred_tip = model.predict(pd.DataFrame([[30.0]], columns=['total_bill']))[0]\n",
            "print(f'Predicted tip for $30 bill: ${pred_tip:.2f}')\n"
        ]
    },
    4: {
        "title": "Linear Regression solved numericals",
        "summary": "Hand-calculated numerical example of finding m and c on small data.",
        "theory": [
            "### Analytical Calculation of Coefficients\n",
            "For $y = mx + c$:\n",
            "- $m = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum (x_i - \\bar{x})^2}$\n",
            "- $c = \\bar{y} - m\\bar{x}$"
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.linear_model import LinearRegression\n",
            "\n",
            "X = np.array([1, 2, 3, 4, 5])\n",
            "y = np.array([2, 3, 5, 4, 6])\n",
            "\n",
            "x_bar, y_bar = np.mean(X), np.mean(y)\n",
            "m = np.sum((X - x_bar) * (y - y_bar)) / np.sum((X - x_bar)**2)\n",
            "c = y_bar - m * x_bar\n",
            "print(f'Manual slope: {m}, intercept: {c}')\n",
            "\n",
            "lr = LinearRegression().fit(X.reshape(-1, 1), y)\n",
            "print(f'Sklearn slope: {lr.coef_[0]}, intercept: {lr.intercept_}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate $m$ and $c$ manually for inputs $X=[1, 2, 3]$ and $Y=[2, 4, 5]$."
        ],
        "exercise_code": [
            "X_ex = np.array([1, 2, 3])\n",
            "y_ex = np.array([2, 4, 5])\n",
            "m_ex = np.sum((X_ex - np.mean(X_ex)) * (y_ex - np.mean(y_ex))) / np.sum((X_ex - np.mean(X_ex))**2)\n",
            "c_ex = np.mean(y_ex) - m_ex * np.mean(X_ex)\n",
            "print(f'Manual slope: {m_ex:.4f}, intercept: {c_ex:.4f}')\n"
        ]
    },
    5: {
        "title": "Linear Regression using Least Squares",
        "summary": "Mathematical derivation of Ordinary Least Squares (OLS) closed-form solution.",
        "theory": [
            "### OLS Normal Equation\n",
            "The analytical closed-form solution to minimize MSE in matrix form is:\n",
            "$$\\theta = (X^T X)^{-1} X^T y$$"
        ],
        "code": [
            "import numpy as np\n",
            "import pandas as pd\n",
            "import seaborn as sns\n",
            "\n",
            "tips = sns.load_dataset('tips')[['total_bill', 'size', 'tip']].dropna()\n",
            "X = tips[['total_bill', 'size']].values\n",
            "# Add intercept column of ones\n",
            "X_b = np.c_[np.ones((len(X), 1)), X]\n",
            "y = tips['tip'].values\n",
            "\n",
            "# Compute normal equation\n",
            "theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)\n",
            "print('OLS Normal Equation Coefficients [Intercept, total_bill, size]:')\n",
            "print(theta)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Predict the tip for total_bill = 25.0 and size = 3 using the computed theta vector."
        ],
        "exercise_code": [
            "sample = np.array([1, 25.0, 3])\n",
            "pred = sample.dot(theta)\n",
            "print(f'Predicted tip: ${pred:.2f}')\n"
        ]
    },
    6: {
        "title": "Linear Regression single variable Python",
        "summary": "Step-by-step single variable linear regression without ML libraries.",
        "theory": [
            "### Single Variable Regression\n",
            "Implementing predictions $\\hat{y} = mx + c$ and MSE calculation directly using basic NumPy operations."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "np.random.seed(42)\n",
            "X = np.random.rand(50) * 10\n",
            "y = 2.5 * X + 1.5 + np.random.randn(50) * 2\n",
            "\n",
            "# Fit parameters analytically\n",
            "m = np.cov(X, y)[0, 1] / np.var(X)\n",
            "c = np.mean(y) - m * np.mean(X)\n",
            "y_pred = m * X + c\n",
            "print(f'Parameters: m = {m:.3f}, c = {c:.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the residuals ($y - \\hat{y}$) and print their mean (which should be close to 0)."
        ],
        "exercise_code": [
            "residuals = y - y_pred\n",
            "print(f'Mean of residuals: {residuals.mean():.6f}')\n"
        ]
    },
    7: {
        "title": "Regression Metrics: MSE, MAE, RMSE, R2, Adjusted R2",
        "summary": "Evaluation metrics for regression and their math.",
        "theory": [
            "### Regression Metrics\n",
            "- **Mean Squared Error (MSE):** $\\frac{1}{n} \\sum (y_i - \\hat{y}_i)^2$\n",
            "- **Mean Absolute Error (MAE):** $\\frac{1}{n} \\sum |y_i - \\hat{y}_i|$\n",
            "- **Root Mean Squared Error (RMSE):** $\\sqrt{MSE}$\n",
            "- **R-Squared ($R^2$):** $1 - \\frac{SS_{res}}{SS_{tot}}$\n",
            "- **Adjusted $R^2$:** $1 - (1-R^2)\\frac{n-1}{n-p-1}$ (penalizes unnecessary features)"
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score\n",
            "\n",
            "y_true = np.array([3.0, -0.5, 2.0, 7.0])\n",
            "y_pred = np.array([2.5, 0.0, 2.0, 8.0])\n",
            "\n",
            "mse = mean_squared_error(y_true, y_pred)\n",
            "mae = mean_absolute_error(y_true, y_pred)\n",
            "rmse = np.sqrt(mse)\n",
            "r2 = r2_score(y_true, y_pred)\n",
            "\n",
            "print(f'MSE: {mse}, MAE: {mae}, RMSE: {rmse}, R2: {r2}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compute Adjusted R2 for a model with $R^2 = 0.85$, $n = 100$ samples, and $p = 5$ features."
        ],
        "exercise_code": [
            "r2_val = 0.85\n",
            "n = 100\n",
            "p = 5\n",
            "adj_r2 = 1 - (1 - r2_val) * (n - 1) / (n - p - 1)\n",
            "print(f'Adjusted R2: {adj_r2:.4f}')\n"
        ]
    },
    8: {
        "title": "SST, SSR, SSE",
        "summary": "Partitioning variance into SST, SSR, and SSE.",
        "theory": [
            "### Variance Decomposition\n",
            "- **SST (Sum of Squares Total):** $\\sum (y_i - \\bar{y})^2$ (Total variation in target)\n",
            "- **SSR (Sum of Squares Regression):** $\\sum (\\hat{y}_i - \\bar{y})^2$ (Explained variation)\n",
            "- **SSE (Sum of Squares Error):** $\\sum (y_i - \\hat{y}_i)^2$ (Unexplained variation)\n",
            "Relationship: $SST = SSR + SSE$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "y_true = np.array([10, 12, 15, 18, 20])\n",
            "y_pred = np.array([10.5, 11.8, 14.2, 18.5, 19.3])\n",
            "y_bar = np.mean(y_true)\n",
            "\n",
            "sst = np.sum((y_true - y_bar)**2)\n",
            "ssr = np.sum((y_pred - y_bar)**2)\n",
            "sse = np.sum((y_true - y_pred)**2)\n",
            "\n",
            "print(f'SST: {sst:.3f}, SSR: {ssr:.3f}, SSE: {sse:.3f}')\n",
            "print(f'SSR + SSE = {ssr+sse:.3f} (SST={sst:.3f})')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Verify that $R^2 = SSR / SST$ matches the standard formula metric."
        ],
        "exercise_code": [
            "r2_calc = ssr / sst\n",
            "print(f'Calculated R2 from SST/SSR: {r2_calc:.4f}')\n"
        ]
    },
    9: {
        "title": "Multiple Linear Regression: intuition and math",
        "summary": "Extending regression to multiple features and matrix formulation.",
        "theory": [
            "### Multiple Linear Regression\n",
            "Fits a hyperplane in $n$-dimensional space:\n",
            "$$y = \\theta_0 + \\theta_1 x_1 + \\theta_2 x_2 + \\dots + \\theta_n x_n = X\\theta$$"
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.datasets import load_diabetes\n",
            "from sklearn.linear_model import LinearRegression\n",
            "\n",
            "diabetes = load_diabetes()\n",
            "X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)\n",
            "y = diabetes.target\n",
            "\n",
            "mlr = LinearRegression().fit(X, y)\n",
            "print('Model Intercept:', mlr.intercept_)\n",
            "print('First 3 Coefficients:', mlr.coef_[:3])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Train a model using only the 'age', 'sex', and 'bmi' features from the diabetes dataset."
        ],
        "exercise_code": [
            "X_sub = X[['age', 'sex', 'bmi']]\n",
            "mlr_sub = LinearRegression().fit(X_sub, y)\n",
            "print('Subset coefficients:', mlr_sub.coef_)\n"
        ]
    },
    10: {
        "title": "Linear Regression multiple variables Python",
        "summary": "Implementing multiple linear regression using LinearRegression.",
        "theory": [
            "### Multi-Feature Regressor\n",
            "Fitting model with all available continuous attributes and evaluating weights."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.datasets import load_diabetes\n",
            "from sklearn.linear_model import LinearRegression\n",
            "\n",
            "diabetes = load_diabetes()\n",
            "df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)\n",
            "df['progression'] = diabetes.target\n",
            "\n",
            "X = df.drop(columns='progression')\n",
            "y = df['progression']\n",
            "\n",
            "lr_model = LinearRegression().fit(X, y)\n",
            "for feat, coef in zip(X.columns, lr_model.coef_):\n",
            "    print(f'{feat:8s} : {coef:10.4f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Sort the features by the absolute value of their coefficient weights to identify the most predictive feature."
        ],
        "exercise_code": [
            "importance = pd.Series(lr_model.coef_, index=X.columns).abs().sort_values(ascending=False)\n",
            "print('Feature Importance Weights:\\n', importance)\n"
        ]
    },
    11: {
        "title": "Assumptions of Linear Regression",
        "summary": "Linear regression assumptions: Linearity, Independence, Homoscedasticity, Normality.",
        "theory": [
            "### Core Assumptions of OLS\n",
            "1. **Linearity:** Relationship between $X$ and $Y$ is linear.\n",
            "2. **Independence:** Residuals are independent.\n",
            "3. **Homoscedasticity:** Constant variance of residuals across predictions.\n",
            "4. **Normality of Residuals:** Error terms are normally distributed."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import scipy.stats as stats\n",
            "\n",
            "# Generate simulated residuals\n",
            "np.random.seed(42)\n",
            "residuals = np.random.normal(0, 1, 100)\n",
            "\n",
            "# Q-Q Plot to check normality assumption\n",
            "stats.probplot(residuals, dist='norm', plot=plt)\n",
            "plt.title('Residual Q-Q Plot')\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the skewness of the residuals."
        ],
        "exercise_code": [
            "skew = stats.skew(residuals)\n",
            "print(f'Residual Skewness: {skew:.4f}')\n"
        ]
    },
    12: {
        "title": "Multiple Dependent Variables",
        "summary": "Multivariate regression where target Y is multi-dimensional.",
        "theory": [
            "### Multi-Output Regression\n",
            "Predicting multiple continuous target values simultaneously: $Y \\in \\mathbb{R}^{m \\times k}$."
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.linear_model import LinearRegression\n",
            "\n",
            "X = np.random.rand(100, 3)\n",
            "# Targets are correlated with features\n",
            "y1 = X[:, 0] * 2 + X[:, 1]\n",
            "y2 = X[:, 2] * 3 - X[:, 1]\n",
            "y = np.column_stack([y1, y2])\n",
            "\n",
            "multi_lr = LinearRegression().fit(X, y)\n",
            "print('Coefficient matrix shape:', multi_lr.coef_.shape)\n",
            "print('Coefficients:\\n', multi_lr.coef_)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Predict targets for a test point $X = [[0.5, 0.5, 0.5]]$."
        ],
        "exercise_code": [
            "pred = multi_lr.predict([[0.5, 0.5, 0.5]])\n",
            "print('Predicted outputs:', pred)\n"
        ]
    },
    13: {
        "title": "Multiple Linear Regression solved numerical",
        "summary": "Multi-variable normal equation solved on a small matrix.",
        "theory": [
            "### Matrix Normal Equation Solver\n",
            "Solving $(X^T X)^{-1} X^T y$ manually on a small $3 \\times 2$ feature dataset."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "# Features: Col 0 is intercept (ones), Col 1 is X1, Col 2 is X2\n",
            "X = np.array([[1, 2, 3],\n",
            "              [1, 3, 5],\n",
            "              [1, 4, 6]])\n",
            "y = np.array([5, 8, 10])\n",
            "\n",
            "# Compute beta = (X^T * X)^(-1) * X^T * y\n",
            "XTX = X.T.dot(X)\n",
            "beta = np.linalg.inv(XTX).dot(X.T).dot(y)\n",
            "print('Calculated weights beta:', beta)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the determinant of $X^T X$ to verify if it is invertible (i.e. det != 0)."
        ],
        "exercise_code": [
            "det = np.linalg.det(XTX)\n",
            "print(f'Determinant of XTX: {det:.4f}')\n"
        ]
    },
    14: {
        "title": "Gradient Descent end to end",
        "summary": "Optimization using Gradient Descent algorithm.",
        "theory": [
            "### Optimization via Gradient Descent\n",
            "Minimizing an objective function by updating values in the opposite direction of the gradient:\n",
            "$$x_{new} := x_{old} - \\alpha f'(x_{old})$$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "# Function: f(x) = x^2 - 4x + 4, Derivative: f'(x) = 2x - 4\n",
            "x = 10.0 # start point\n",
            "lr = 0.1\n",
            "\n",
            "for epoch in range(1, 11):\n",
            "    grad = 2*x - 4\n",
            "    x = x - lr * grad\n",
            "    print(f'Epoch {epoch}: x = {x:.5f}, f(x) = {x**2 - 4*x + 4:.5f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Minimize the same function using a learning rate of 0.8 and observe oscillation behavior."
        ],
        "exercise_code": [
            "x_osc = 10.0\n",
            "for epoch in range(1, 6):\n",
            "    x_osc = x_osc - 0.8 * (2*x_osc - 4)\n",
            "    print(f'Epoch {epoch} (lr=0.8): x = {x_osc:.5f}')\n"
        ]
    },
    15: {
        "title": "Batch GD, SGD, Mini Batch GD",
        "summary": "Variations of gradient descent based on data batching.",
        "theory": [
            "### Gradient Descent Variants\n",
            "- **Batch GD:** Calculates gradient on the *entire* dataset.\n",
            "- **Stochastic GD (SGD):** Calculates gradient on *one* sample at a time (noisy but fast).\n",
            "- **Mini-batch GD:** Calculates gradient on a small batch of size $B$ (compromise)."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "X = np.random.rand(100, 1)\n",
            "y = 3*X + 2 + np.random.randn(100, 1)*0.1\n",
            "X_b = np.c_[np.ones((100, 1)), X] # add bias\n",
            "\n",
            "# SGD Implementation\n",
            "theta = np.random.randn(2, 1)\n",
            "lr = 0.01\n",
            "for i in range(100):\n",
            "    rand_idx = np.random.randint(100)\n",
            "    xi = X_b[rand_idx:rand_idx+1]\n",
            "    yi = y[rand_idx:rand_idx+1]\n",
            "    gradients = 2 * xi.T.dot(xi.dot(theta) - yi)\n",
            "    theta = theta - lr * gradients\n",
            "print('SGD final theta:', theta.flatten())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Implement Batch Gradient Descent on the same data and print the final parameters."
        ],
        "exercise_code": [
            "theta_bgd = np.random.randn(2, 1)\n",
            "for i in range(500):\n",
            "    gradients_bgd = 2/100 * X_b.T.dot(X_b.dot(theta_bgd) - y)\n",
            "    theta_bgd = theta_bgd - 0.1 * gradients_bgd\n",
            "print('Batch GD final theta:', theta_bgd.flatten())\n"
        ]
    },
    16: {
        "title": "Learning Rate",
        "summary": "Influence of learning rate on gradient descent convergence.",
        "theory": [
            "### Hyperparameter: Learning Rate ($\\alpha$)\n",
            "- Too small: very slow convergence.\n",
            "- Too large: divergence, cost increases, oscillation."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "x_start = 10.0\n",
            "\n",
            "def run_gd(lr, epochs=5):\n",
            "    x = x_start\n",
            "    history = []\n",
            "    for _ in range(epochs):\n",
            "        grad = 2*x\n",
            "        x = x - lr * grad\n",
            "        history.append(x)\n",
            "    return history\n",
            "\n",
            "print('Optimal LR (0.1):', run_gd(0.1))\n",
            "print('Diverging LR (1.1):', run_gd(1.1))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Run GD with a very small learning rate (0.001) for 5 epochs and observe progress."
        ],
        "exercise_code": [
            "print('Very small LR (0.001):', run_gd(0.001))\n"
        ]
    },
    17: {
        "title": "Univariate Linear Regression with GD (without vectorization)",
        "summary": "Implementing simple linear regression using loops for gradient updates.",
        "theory": [
            "### Loop-based Gradient Descent\n",
            "Updating weights $m$ and $c$ using explicit iterations over data samples instead of vector operations."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "X = np.array([1, 2, 3, 4, 5])\n",
            "y = np.array([2, 4, 5, 4, 5])\n",
            "\n",
            "m, c = 0.0, 0.0\n",
            "lr = 0.01\n",
            "n = len(X)\n",
            "\n",
            "for epoch in range(100):\n",
            "    grad_m = 0.0\n",
            "    grad_c = 0.0\n",
            "    for i in range(n):\n",
            "        y_pred = m * X[i] + c\n",
            "        grad_m += (y_pred - y[i]) * X[i]\n",
            "        grad_c += (y_pred - y[i])\n",
            "    m = m - lr * (2/n) * grad_m\n",
            "    c = c - lr * (2/n) * grad_c\n",
            "\n",
            "print(f'Fitted parameters: m = {m:.3f}, c = {c:.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the final Mean Squared Error of this model."
        ],
        "exercise_code": [
            "final_preds = m * X + c\n",
            "mse = np.mean((y - final_preds)**2)\n",
            "print(f'Final MSE: {mse:.4f}')\n"
        ]
    },
    18: {
        "title": "Univariate Linear Regression with GD (with vectorization)",
        "summary": "Vectorized univariate linear regression using NumPy.",
        "theory": [
            "### Vectorized GD formulation\n",
            "Avoiding slow python loops by calculating gradients using matrix transpose and vector multiplications."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "X = np.array([1, 2, 3, 4, 5])\n",
            "y = np.array([2, 4, 5, 4, 5])\n",
            "X_b = np.c_[np.ones((len(X), 1)), X]\n",
            "\n",
            "theta = np.zeros(2)\n",
            "lr = 0.01\n",
            "m = len(X)\n",
            "\n",
            "for epoch in range(100):\n",
            "    gradients = (2/m) * X_b.T.dot(X_b.dot(theta) - y)\n",
            "    theta = theta - lr * gradients\n",
            "print('Vectorized fitted parameters [c, m]:', theta)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compare the predictions of vectorized GD against the loop-based GD predictions."
        ],
        "exercise_code": [
            "loop_pred = 0.700 * X + 1.900 # from loop GD\n",
            "vec_pred = X_b.dot(theta)\n",
            "print('Difference:', np.abs(loop_pred - vec_pred).max())\n"
        ]
    },
    19: {
        "title": "Multivariate Linear Regression implementation",
        "summary": "Vectorized multi-feature linear regression with gradient descent.",
        "theory": [
            "### Multivariate Vectorized Formulation\n",
            "Gradient: $\\nabla_\\theta J = \\frac{2}{m} X^T(X\\theta - y)$"
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.datasets import load_diabetes\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "\n",
            "diabetes = load_diabetes()\n",
            "X = diabetes.data[:, :3] # use first 3 features\n",
            "y = diabetes.target\n",
            "\n",
            "# Standardize features to aid GD convergence\n",
            "X_scaled = StandardScaler().fit_transform(X)\n",
            "X_b = np.c_[np.ones((len(X_scaled), 1)), X_scaled]\n",
            "\n",
            "theta = np.zeros(4)\n",
            "lr = 0.1\n",
            "m_samples = len(y)\n",
            "\n",
            "for epoch in range(200):\n",
            "    gradients = (2/m_samples) * X_b.T.dot(X_b.dot(theta) - y)\n",
            "    theta = theta - lr * gradients\n",
            "print('Fitted coefficients [Intercept, Beta1, Beta2, Beta3]:', theta)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the final objective cost $J(\\theta)$ on the training dataset."
        ],
        "exercise_code": [
            "cost = (1 / (2*m_samples)) * np.sum((X_b.dot(theta) - y)**2)\n",
            "print(f'Final cost J: {cost:.4f}')\n"
        ]
    },
    20: {
        "title": "Polynomial Regression",
        "summary": "Non-linear regression using polynomial feature expansions.",
        "theory": [
            "### Polynomial Mapping\n",
            "Mapping features $X \\to [1, X, X^2, X^3]$ to fit non-linear curved bounds using standard OLS solvers."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.preprocessing import PolynomialFeatures\n",
            "from sklearn.linear_model import LinearRegression\n",
            "\n",
            "# Generate curved data\n",
            "np.random.seed(42)\n",
            "X = np.sort(np.random.rand(40, 1) * 6, axis=0)\n",
            "y = 0.5 * X**3 - 3 * X**2 + X + np.random.randn(40, 1) * 2\n",
            "\n",
            "poly = PolynomialFeatures(degree=3, include_bias=False)\n",
            "X_poly = poly.fit_transform(X)\n",
            "\n",
            "model = LinearRegression().fit(X_poly, y)\n",
            "print('Polynomial Coefficients:', model.coef_)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate predictions and print the R2 score of the polynomial model."
        ],
        "exercise_code": [
            "r2 = model.score(X_poly, y)\n",
            "print(f'Polynomial R2 score: {r2:.4f}')\n"
        ]
    },
    21: {
        "title": "Bias Variance Tradeoff and Overfitting/Underfitting",
        "summary": "Concepts of Bias, Variance, Underfitting and Overfitting.",
        "theory": [
            "### Bias vs Variance Tradeoff\n",
            "- **High Bias:** Underfitting (model is too simple to capture patterns, eg. degree 1 on curved data).\n",
            "- **High Variance:** Overfitting (model fits training noise too closely, eg. degree 15 on small dataset)."
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.preprocessing import PolynomialFeatures\n",
            "from sklearn.linear_model import LinearRegression\n",
            "from sklearn.metrics import mean_squared_error\n",
            "\n",
            "np.random.seed(42)\n",
            "X = np.random.rand(30, 1) * 4\n",
            "y = np.sin(X).ravel() + np.random.randn(30) * 0.2\n",
            "\n",
            "def evaluate_deg(deg):\n",
            "    poly = PolynomialFeatures(degree=deg)\n",
            "    X_p = poly.fit_transform(X)\n",
            "    model = LinearRegression().fit(X_p, y)\n",
            "    train_mse = mean_squared_error(y, model.predict(X_p))\n",
            "    return train_mse\n",
            "\n",
            "print('Underfit Degree 1 Train MSE:', evaluate_deg(1))\n",
            "print('Overfit Degree 12 Train MSE:', evaluate_deg(12))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. State which degree will likely generalize better on unseen test points."
        ],
        "exercise_code": [
            "print('Optimal degree is likely 2 or 3; degree 12 will overfit and have very poor generalization (high variance).')\n"
        ]
    },
    22: {
        "title": "Ridge Regression full series",
        "summary": "Ridge regression (L2 regularization) math and code.",
        "theory": [
            "### Ridge Regularization\n",
            "Applies an $L_2$ squared penalty to coefficients to reduce collinearity and prevent overfitting:\n",
            "$$J(\\theta) = MSE + \\alpha \\sum_{j=1}^n \\theta_j^2$$"
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.linear_model import Ridge\n",
            "from sklearn.datasets import load_diabetes\n",
            "\n",
            "diabetes = load_diabetes()\n",
            "X, y = diabetes.data, diabetes.target\n",
            "\n",
            "ridge = Ridge(alpha=1.0)\n",
            "ridge.fit(X, y)\n",
            "print('Ridge Coefficients norm:', np.linalg.norm(ridge.coef_))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compare Ridge coefficients norm with standard OLS Linear Regression norm."
        ],
        "exercise_code": [
            "from sklearn.linear_model import LinearRegression\n",
            "ols = LinearRegression().fit(X, y)\n",
            "print('OLS Coefficients norm:', np.linalg.norm(ols.coef_))\n",
            "print('Notice that Ridge shrinks the coefficient magnitudes.')\n"
        ]
    },
    23: {
        "title": "Lasso Regression",
        "summary": "Lasso regression (L1 regularization) and feature selection.",
        "theory": [
            "### Lasso Regularization\n",
            "Applies an $L_1$ absolute penalty to coefficients, which encourages sparsity (zeroing out weights):\n",
            "$$J(\\theta) = MSE + \\alpha \\sum_{j=1}^n |\\theta_j|$$"
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.linear_model import Lasso\n",
            "from sklearn.datasets import load_diabetes\n",
            "\n",
            "diabetes = load_diabetes()\n",
            "X, y = diabetes.data, diabetes.target\n",
            "\n",
            "lasso = Lasso(alpha=0.1)\n",
            "lasso.fit(X, y)\n",
            "print('Lasso Coefficients:', lasso.coef_)\n",
            "print('Number of features zeroed out:', np.sum(lasso.coef_ == 0))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Train Lasso with a very large alpha (e.g., 5.0) and see how many features remain non-zero."
        ],
        "exercise_code": [
            "lasso_large = Lasso(alpha=5.0).fit(X, y)\n",
            "print('Non-zero coefficients count:', np.sum(lasso_large.coef_ != 0))\n"
        ]
    },
    24: {
        "title": "ElasticNet Regression",
        "summary": "ElasticNet combining L1 and L2 regularization.",
        "theory": [
            "### ElasticNet Regularization\n",
            "Combines L1 and L2 penalties using mixing ratio $r$ (l1_ratio):\n",
            "$$J(\\theta) = MSE + r \\cdot \\alpha \\sum |\\theta_j| + \\frac{1-r}{2} \\cdot \\alpha \\sum \\theta_j^2$$"
        ],
        "code": [
            "from sklearn.linear_model import ElasticNet\n",
            "from sklearn.datasets import load_diabetes\n",
            "\n",
            "diabetes = load_diabetes()\n",
            "X, y = diabetes.data, diabetes.target\n",
            "\n",
            "enet = ElasticNet(alpha=0.1, l1_ratio=0.5)\n",
            "enet.fit(X, y)\n",
            "print('ElasticNet score:', enet.score(X, y))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Run ElasticNet with l1_ratio = 1.0 and confirm if it yields identical coefficients to Lasso."
        ],
        "exercise_code": [
            "from sklearn.linear_model import Lasso\n",
            "import numpy as np\n",
            "enet_lasso = ElasticNet(alpha=0.1, l1_ratio=1.0).fit(X, y)\n",
            "lasso_comp = Lasso(alpha=0.1).fit(X, y)\n",
            "print('Difference:', np.max(np.abs(enet_lasso.coef_ - lasso_comp.coef_)))\n"
        ]
    },
    25: {
        "title": "Stanford CS229 Lec 3: Locally Weighted Regression",
        "summary": "Non-parametric regression using local weight kernels.",
        "theory": [
            "### Locally Weighted Regression (LWR)\n",
            "A non-parametric algorithm: weights $w^{(i)}$ are evaluated centered around query prediction point $x$:\n",
            "$$w^{(i)} = \\exp\\left(-\\frac{(x^{(i)} - x)^2}{2\\tau^2}\\right)$$\n",
            "Cost to minimize: $\\sum w^{(i)} (y^{(i)} - \\theta^T x^{(i)})^2$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "# Generate noisy 1D sine wave\n",
            "np.random.seed(0)\n",
            "X = np.sort(np.random.rand(50) * 6)\n",
            "y = np.sin(X) + np.random.randn(50) * 0.1\n",
            "\n",
            "def lwr_predict(x_query, X, y, tau):\n",
            "    weights = np.exp(-((X - x_query)**2) / (2 * tau**2))\n",
            "    W = np.diag(weights)\n",
            "    # Add bias term\n",
            "    X_b = np.c_[np.ones(len(X)), X]\n",
            "    query_b = np.array([1, x_query])\n",
            "    # Closed-form weighted OLS: theta = (X^T W X)^(-1) X^T W y\n",
            "    theta = np.linalg.inv(X_b.T.dot(W).dot(X_b)).dot(X_b.T).dot(W).dot(y)\n",
            "    return query_b.dot(theta)\n",
            "\n",
            "print('Prediction at query point 3.0 (tau=0.5):', lwr_predict(3.0, X, y, tau=0.5))\n",
            "print('True sine value at 3.0:', np.sin(3.0))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Predict the value at query point 1.5 with a very tight bandwidth $\\tau = 0.05$."
        ],
        "exercise_code": [
            "pred_tight = lwr_predict(1.5, X, y, tau=0.05)\n",
            "print(f'Prediction (tau=0.05): {pred_tight:.4f}, True sine: {np.sin(1.5):.4f}')\n"
        ]
    },
    26: {
        "title": "Locally Weighted Regression",
        "summary": "Practical implementation and evaluation of locally weighted regression.",
        "theory": [
            "### Bandwidth Parameter ($\\tau$)\n",
            "- $\\tau$ too large: High bias (local weights become flat, converges to global linear regression).\n",
            "- $\\tau$ too small: High variance (fits local noise)."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Generate noisy 1D sine wave\n",
            "np.random.seed(0)\n",
            "X = np.sort(np.random.rand(50) * 6)\n",
            "y = np.sin(X) + np.random.randn(50) * 0.1\n",
            "\n",
            "def lwr_predict(x_query, X, y, tau):\n",
            "    weights = np.exp(-((X - x_query)**2) / (2 * tau**2))\n",
            "    W = np.diag(weights)\n",
            "    X_b = np.c_[np.ones(len(X)), X]\n",
            "    query_b = np.array([1, x_query])\n",
            "    theta = np.linalg.inv(X_b.T.dot(W).dot(X_b)).dot(X_b.T).dot(W).dot(y)\n",
            "    return query_b.dot(theta)\n",
            "\n",
            "queries = np.linspace(0.1, 5.9, 30)\n",
            "preds_large_tau = [lwr_predict(q, X, y, tau=2.0) for q in queries]\n",
            "preds_small_tau = [lwr_predict(q, X, y, tau=0.1) for q in queries]\n",
            "\n",
            "plt.scatter(X, y, color='black', label='Data')\n",
            "plt.plot(queries, preds_large_tau, 'r-', label='tau = 2.0')\n",
            "plt.plot(queries, preds_small_tau, 'g-', label='tau = 0.1')\n",
            "plt.legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain the effect of setting $\\tau=0.1$ compared to $\\tau=2.0$ based on the plot."
        ],
        "exercise_code": [
            "print('tau=0.1 captures non-linear curvature cleanly. tau=2.0 underfits because the weights are too flat.')\n"
        ]
    },
    27: {
        "title": "KNN Regression",
        "summary": "K-Nearest Neighbors regression intuition and code.",
        "theory": [
            "### KNN Regression\n",
            "Finds the $K$ closest samples in feature space and averages their target values to make a prediction."
        ],
        "code": [
            "import seaborn as sns\n",
            "from sklearn.neighbors import KNeighborsRegressor\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "tips = sns.load_dataset('tips')\n",
            "X = tips[['total_bill', 'size']]\n",
            "y = tips['tip']\n",
            "\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
            "knn_reg = KNeighborsRegressor(n_neighbors=5)\n",
            "knn_reg.fit(X_train, y_train)\n",
            "print('KNN Test R2 Score:', knn_reg.score(X_test, y_test))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Train KNN models for $K=1$ and $K=15$ and compare test R2 scores."
        ],
        "exercise_code": [
            "r2_k1 = KNeighborsRegressor(n_neighbors=1).fit(X_train, y_train).score(X_test, y_test)\n",
            "r2_k15 = KNeighborsRegressor(n_neighbors=15).fit(X_train, y_train).score(X_test, y_test)\n",
            "print(f'R2 for K=1: {r2_k1:.4f}, R2 for K=15: {r2_k15:.4f}')\n"
        ]
    },
    28: {
        "title": "Regression Trees",
        "summary": "Decision Trees for regression tasks.",
        "theory": [
            "### Regression Tree split criteria\n",
            "Recursively partitions feature space using thresholds that minimize Mean Squared Error (MSE) within resulting regions."
        ],
        "code": [
            "import seaborn as sns\n",
            "from sklearn.tree import DecisionTreeRegressor\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "tips = sns.load_dataset('tips')\n",
            "X = tips[['total_bill', 'size']]\n",
            "y = tips['tip']\n",
            "\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
            "\n",
            "tree_reg = DecisionTreeRegressor(max_depth=3, random_state=42)\n",
            "tree_reg.fit(X_train, y_train)\n",
            "print('Tree Test R2 Score:', tree_reg.score(X_test, y_test))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compute the depth of standard tree regression without depth limit, and print its training R2 score."
        ],
        "exercise_code": [
            "tree_full = DecisionTreeRegressor(random_state=42).fit(X_train, y_train)\n",
            "print('Full Tree depth:', tree_full.get_depth())\n",
            "print('Full Tree Train R2 Score:', tree_full.score(X_train, y_train))\n"
        ]
    }
}



PHASE_8_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Linear vs Logistic Regression",
        "summary": "Comparison between regression and classification boundary limits.",
        "theory": [
            "### Limits of Linear Regression for Classification\n",
            "- **Predicting out of bounds:** Linear regression predicts values in $(-\\infty, \\infty)$, but probabilities must be in $[0, 1]$.\n",
            "- **Sensitivity to outliers:** Adding extreme points shifts the decision boundary significantly, leading to misclassifications.\n",
            "- **Non-constant variance:** Error terms violate homoscedasticity assumption in binary target scenarios."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.linear_model import LinearRegression, LogisticRegression\n",
            "\n",
            "# Generate toy binary dataset\n",
            "X = np.array([1, 2, 3, 4, 10, 11, 12, 13]).reshape(-1, 1)\n",
            "y = np.array([0, 0, 0, 0, 1, 1, 1, 1])\n",
            "\n",
            "lin_reg = LinearRegression().fit(X, y)\n",
            "log_reg = LogisticRegression().fit(X, y)\n",
            "\n",
            "plt.scatter(X, y, color='black', label='Data')\n",
            "plt.plot(X, lin_reg.predict(X), 'r--', label='Linear Regression')\n",
            "plt.plot(X, log_reg.predict_proba(X)[:, 1], 'g-', label='Logistic Regression probability')\n",
            "plt.axhline(0.5, color='gray', linestyle=':')\n",
            "plt.legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain the effect of an outlier at $X=50, y=1$ on the linear regression decision boundary compared to logistic regression."
        ],
        "exercise_code": [
            "print('Linear regression boundary will shift to the right due to the leverage of the outlier, misclassifying intermediate points. Logistic regression boundary remains stable.')\n"
        ]
    },
    2: {
        "title": "Stanford CS229 Lec 3: Logistic Regression math",
        "summary": "Derivation of the log-likelihood function, gradient ascent, and Newton's Method.",
        "theory": [
            "### Logistic Regression Math\n",
            "- **Hypothesis:** $h_\\theta(x) = g(\\theta^T x) = \\frac{1}{1 + e^{-\\theta^T x}}$\n",
            "- **Log-Likelihood:** $\\ell(\\theta) = \\sum_{i=1}^m y^{(i)}\\log h(x^{(i)}) + (1-y^{(i)})\\log(1-h(x^{(i)}))$\n",
            "- **Gradient:** $\\nabla_\\theta \\ell(\\theta) = X^T (y - h(x))$"
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Sigmoid function\n",
            "z = np.linspace(-10, 10, 100)\n",
            "g = 1 / (1 + np.exp(-z))\n",
            "dg = g * (1 - g)\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "plt.plot(z, g, 'b-', label='Sigmoid g(z)')\n",
            "plt.plot(z, dg, 'r--', label=\"Sigmoid Derivative g'(z)\")\n",
            "plt.axhline(0.5, color='gray', linestyle=':')\n",
            "plt.axvline(0.0, color='gray', linestyle=':')\n",
            "plt.title('Sigmoid Activation and its Derivative')\n",
            "plt.xlabel('z')\n",
            "plt.ylabel('Activation')\n",
            "plt.legend()\n",
            "plt.grid(True)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the log-likelihood for predictions $[0.99, 0.01]$ and labels $[1, 0]$."
        ],
        "exercise_code": [
            "p_ex = np.array([0.99, 0.01])\n",
            "y_ex = np.array([1, 0])\n",
            "print('Log-Likelihood:', np.sum(y_ex * np.log(p_ex) + (1-y_ex) * np.log(1-p_ex)))\n"
        ]
    },
    3: {
        "title": "Logistic Regression full series: Perceptron, Sigmoid, Loss, GD",
        "summary": "Detailed perceptron algorithm vs logistic regression, sigmoid activation, BCE loss, and gradient descent.",
        "theory": [
            "### Binary Cross Entropy (BCE) Loss\n",
            "$$L(\\theta) = -\\frac{1}{m} \\sum_{i=1}^m [y^{(i)}\\log(\\hat{y}^{(i)}) + (1-y^{(i)})\\log(1-\\hat{y}^{(i)})]$$"
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "p = np.linspace(0.01, 0.99, 100)\n",
            "loss_y1 = -np.log(p)\n",
            "loss_y0 = -np.log(1 - p)\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "plt.plot(p, loss_y1, 'g-', label='BCE Loss for y=1: -log(p)')\n",
            "plt.plot(p, loss_y0, 'r--', label='BCE Loss for y=0: -log(1-p)')\n",
            "plt.xlabel('Predicted Probability p')\n",
            "plt.ylabel('Loss Value')\n",
            "plt.title('Binary Cross Entropy Loss Curves')\n",
            "plt.legend()\n",
            "plt.grid(True)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compute the binary cross entropy loss for true label 0 and prediction 0.25."
        ],
        "exercise_code": [
            "def bce_loss(y_true, y_pred):\n",
            "    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))\n",
            "print('BCE Loss:', bce_loss(0, 0.25))\n"
        ]
    },
    4: {
        "title": "Logistic Regression with Python",
        "summary": "Using Scikit-Learn's LogisticRegression for binary classification.",
        "theory": [
            "### Scikit-Learn Logistic Regression\n",
            "Optimizes logistic regression parameters using iterative solvers (default: lbfgs)."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.datasets import load_breast_cancer\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "data = load_breast_cancer()\n",
            "X = pd.DataFrame(data.data, columns=data.feature_names)\n",
            "y = data.target\n",
            "\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
            "model = LogisticRegression(max_iter=10000)\n",
            "model.fit(X_train, y_train)\n",
            "print('Train Score:', model.score(X_train, y_train))\n",
            "print('Test Score:', model.score(X_test, y_test))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Print the model intercept and check how many features were used in training."
        ],
        "exercise_code": [
            "print('Intercept:', model.intercept_)\n",
            "print('Number of features:', model.n_features_in_)\n"
        ]
    },
    5: {
        "title": "Logistic Regression solved numerical",
        "summary": "Hand-calculated step of gradient descent update for logistic regression.",
        "theory": [
            "### GD Update Calculation\n",
            "Weight update: $\\theta_j := \\theta_j - \\alpha (h_\\theta(x) - y)x_j$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "X = np.array([1.0, 2.0]) # feature vector (including bias)\n",
            "y = 1.0\n",
            "theta = np.array([0.0, 0.5])\n",
            "alpha = 0.1\n",
            "\n",
            "# Sigmoid prediction\n",
            "z = np.dot(theta, X)\n",
            "h = 1 / (1 + np.exp(-z))\n",
            "\n",
            "# Gradient step\n",
            "theta_new = theta - alpha * (h - y) * X\n",
            "print('New Theta:', theta_new)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Perform the calculation with a learning rate $\\alpha = 0.5$."
        ],
        "exercise_code": [
            "theta_new_5 = theta - 0.5 * (h - y) * X\n",
            "print('New Theta (lr=0.5):', theta_new_5)\n"
        ]
    },
    6: {
        "title": "Logistic Regression hyperparameters",
        "summary": "Tuning C parameter, penalty type (L1, L2, ElasticNet), and optimization solvers.",
        "theory": [
            "### Regularization Strength (C)\n",
            "- $C = \\frac{1}{\\lambda}$: Smaller $C$ leads to stronger regularization."
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.datasets import load_breast_cancer\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "\n",
            "data = load_breast_cancer()\n",
            "X, y = data.data, data.target\n",
            "\n",
            "model_l1 = LogisticRegression(penalty='l1', solver='liblinear', C=0.1, max_iter=10000, random_state=42)\n",
            "model_l1.fit(X, y)\n",
            "print('L1 non-zero coefficients:', np.sum(model_l1.coef_ != 0))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Fit a LogisticRegression model using L2 regularization and C=0.01. Compare training score with L1."
        ],
        "exercise_code": [
            "model_l2 = LogisticRegression(penalty='l2', C=0.01, max_iter=10000, random_state=42).fit(X, y)\n",
            "print('L2 score:', model_l2.score(X, y))\n"
        ]
    },
    7: {
        "title": "Binary Classification: full implementation",
        "summary": "Complete scratch implementation of Logistic Regression class with fit/predict methods.",
        "theory": [
            "### From-Scratch Sigmoid Neurons\n",
            "Calculating sigmoid activations, derivatives, and updating parameters in a single loop."
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.datasets import load_breast_cancer\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "\n",
            "data = load_breast_cancer()\n",
            "X_scaled = StandardScaler().fit_transform(data.data)\n",
            "y = data.target\n",
            "\n",
            "class CustomLogisticRegression:\n",
            "    def fit(self, X, y, lr=0.1, epochs=100):\n",
            "        m, n = X.shape\n",
            "        self.w = np.zeros(n)\n",
            "        self.b = 0.0\n",
            "        for _ in range(epochs):\n",
            "            z = np.dot(X, self.w) + self.b\n",
            "            y_pred = 1 / (1 + np.exp(-z))\n",
            "            dw = (1/m) * np.dot(X.T, (y_pred - y))\n",
            "            db = (1/m) * np.sum(y_pred - y)\n",
            "            self.w -= lr * dw\n",
            "            self.b -= lr * db\n",
            "    def predict(self, X):\n",
            "        z = np.dot(X, self.w) + self.b\n",
            "        return (1 / (1 + np.exp(-z)) >= 0.5).astype(int)\n",
            "\n",
            "custom = CustomLogisticRegression()\n",
            "custom.fit(X_scaled, y, epochs=200)\n",
            "preds = custom.predict(X_scaled)\n",
            "print('Custom Model Train Accuracy:', np.mean(preds == y))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Print final weights and intercept values."
        ],
        "exercise_code": [
            "print('Bias:', custom.b)\n",
            "print('First 3 weights:', custom.w[:3])\n"
        ]
    },
    8: {
        "title": "Stanford CS229 Lec 4: Perceptron and GLM",
        "summary": "Exponential family distributions, Generalized Linear Model (GLM) formulation.",
        "theory": [
            "### GLM Formulation\n",
            "1. $y|x; \\theta \\sim \\text{ExponentialFamily}(\\eta)$\n",
            "2. $h_\\theta(x) = E[y|x]$\n",
            "3. $\\eta = \\theta^T x$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "def log_odds(p):\n",
            "    return np.log(p / (1 - p))\n",
            "\n",
            "print('Log-odds of 0.8 probability:', log_odds(0.8))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compute the probability $p$ when the log-odds (logit) value $\\eta = 0.0$."
        ],
        "exercise_code": [
            "print('Probability:', 1 / (1 + np.exp(-0.0)))\n"
        ]
    },
    9: {
        "title": "Softmax / Multinomial Logistic Regression",
        "summary": "Softmax regression for multiclass classification tasks.",
        "theory": [
            "### Softmax Regression\n",
            "Generalization of Logistic Regression to multiclass targets ($K > 2$):\n",
            "$$P(y=i|x) = \\frac{e^{\\theta_i^T x}}{\\sum_{j=1}^K e^{\\theta_j^T x}}$$"
        ],
        "code": [
            "from sklearn.datasets import load_wine\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "wine = load_wine()\n",
            "X, y = wine.data, wine.target\n",
            "\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
            "softmax_reg = LogisticRegression(solver='lbfgs', max_iter=10000, random_state=42)\n",
            "softmax_reg.fit(X_train, y_train)\n",
            "print('Multiclass Test Accuracy:', softmax_reg.score(X_test, y_test))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Output prediction probability estimates for the first sample in `X_test`."
        ],
        "exercise_code": [
            "print('Probabilities:', softmax_reg.predict_proba(X_test[:1]))\n"
        ]
    },
    10: {
        "title": "Multiclass Classification: One vs All, One vs One",
        "summary": "Extending binary classification models to multiclass targets.",
        "theory": [
            "### OvR and OvO\n",
            "- **One-vs-Rest (OvR):** Fits $K$ classifiers. Fast but may suffer from size imbalances.\n",
            "- **One-vs-One (OvO):** Fits $\\frac{K(K-1)}{2}$ classifiers. Slower but robust."
        ],
        "code": [
            "from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier\n",
            "from sklearn.svm import SVC\n",
            "from sklearn.datasets import load_wine\n",
            "\n",
            "wine = load_wine()\n",
            "X, y = wine.data, wine.target\n",
            "\n",
            "ovr = OneVsRestClassifier(SVC(kernel='linear')).fit(X, y)\n",
            "ovo = OneVsOneClassifier(SVC(kernel='linear')).fit(X, y)\n",
            "print('OvR score:', ovr.score(X, y))\n",
            "print('OvO score:', ovo.score(X, y))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the number of models trained in OvO for a classification task with 6 classes."
        ],
        "exercise_code": [
            "classes = 6\n",
            "print('OvO models:', int(classes * (classes - 1) / 2))\n"
        ]
    },
    11: {
        "title": "Confusion Matrix, Accuracy, Type 1 & 2 errors",
        "summary": "Metrics for classification evaluation and confusion matrices.",
        "theory": [
            "### Confusion Matrix Details\n",
            "- **Type I Error (False Positive):** Rejecting null hypothesis when true.\n",
            "- **Type II Error (False Negative):** Failing to reject null hypothesis when false."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from sklearn.metrics import confusion_matrix, accuracy_score\n",
            "\n",
            "y_true = [0, 1, 0, 1, 0, 1, 1, 0]\n",
            "y_pred = [0, 1, 0, 0, 0, 1, 1, 1]\n",
            "cm = confusion_matrix(y_true, y_pred)\n",
            "\n",
            "plt.figure(figsize=(5, 4))\n",
            "sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=['Negative (0)', 'Positive (1)'], yticklabels=['Negative (0)', 'Positive (1)'])\n",
            "plt.xlabel('Predicted Label')\n",
            "plt.ylabel('True Label')\n",
            "plt.title('Binary Confusion Matrix Heatmap')\n",
            "plt.show()\n",
            "print('Accuracy:', accuracy_score(y_true, y_pred))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the count of Type I and Type II errors from the code predictions above."
        ],
        "exercise_code": [
            "print('Type I (FP):', cm[0, 1])\n",
            "print('Type II (FN):', cm[1, 0])\n"
        ]
    },
    12: {
        "title": "Precision, Recall, F1 Score",
        "summary": "Precision vs Recall tradeoff and the F1 Score.",
        "theory": [
            "### Mathematical Definitions\n",
            "- $\\text{Precision} = \\frac{TP}{TP + FP}$\n",
            "- $\\text{Recall} = \\frac{TP}{TP + FN}$\n",
            "- $\\text{F1} = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}}$"
        ],
        "code": [
            "from sklearn.metrics import precision_score, recall_score, f1_score\n",
            "\n",
            "y_true = [0, 1, 0, 1, 0, 1, 1, 0]\n",
            "y_pred = [0, 1, 0, 0, 0, 1, 1, 1]\n",
            "\n",
            "print('Precision:', precision_score(y_true, y_pred))\n",
            "print('Recall:', recall_score(y_true, y_pred))\n",
            "print('F1 Score:', f1_score(y_true, y_pred))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate F1 Score manually if precision is 0.75 and recall is 0.5."
        ],
        "exercise_code": [
            "p, r = 0.75, 0.5\n",
            "print('Manual F1:', 2 * p * r / (p + r))\n"
        ]
    },
    13: {
        "title": "ROC AUC full",
        "summary": "ROC curve plotting and Area Under the Curve metric.",
        "theory": [
            "### ROC AUC\n",
            "Plots True Positive Rate (Sensitivity) vs False Positive Rate (1 - Specificity) across different thresholds."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.metrics import roc_curve, roc_auc_score\n",
            "\n",
            "y_true = [0, 0, 1, 1]\n",
            "scores = [0.1, 0.4, 0.35, 0.8] # predicted probabilities\n",
            "\n",
            "fpr, tpr, thresholds = roc_curve(y_true, scores)\n",
            "auc = roc_auc_score(y_true, scores)\n",
            "\n",
            "plt.figure(figsize=(6, 5))\n",
            "plt.plot(fpr, tpr, 'b-', label=f'ROC Curve (AUC = {auc:.2f})')\n",
            "plt.plot([0, 1], [0, 1], 'r--', label='Random Guessing (AUC = 0.5)')\n",
            "plt.xlabel('False Positive Rate (FPR)')\n",
            "plt.ylabel('True Positive Rate (TPR)')\n",
            "plt.title('Receiver Operating Characteristic (ROC) Curve')\n",
            "plt.legend()\n",
            "plt.grid(True)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain what an AUC score of 0.5 implies about classification ability."
        ],
        "exercise_code": [
            "print('An AUC of 0.5 represents a model with no discriminatory capability (equivalent to random guessing).')\n"
        ]
    },
    14: {
        "title": "Specificity and Sensitivity",
        "summary": "Definitions of Specificity, Sensitivity, and their applications.",
        "theory": [
            "### Sensitivity and Specificity\n",
            "- **Sensitivity (TPR):** Ability to correctly spot positive samples.\n",
            "- **Specificity (TNR):** Ability to correctly spot negative samples ($TN / (TN + FP)$)."
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.metrics import confusion_matrix\n",
            "\n",
            "y_true = np.array([0, 1, 0, 1, 0, 0, 1])\n",
            "y_pred = np.array([0, 1, 1, 1, 0, 0, 0])\n",
            "\n",
            "cm = confusion_matrix(y_true, y_pred)\n",
            "tn, fp, fn, tp = cm.ravel()\n",
            "print('Sensitivity:', tp / (tp + fn))\n",
            "print('Specificity:', tn / (tn + fp))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain why clinical diagnostic tests prioritize sensitivity over specificity."
        ],
        "exercise_code": [
            "print('Clinical tests prioritize sensitivity because failing to diagnose a sick patient (false negative) is far more critical than causing a false alarm.')\n"
        ]
    },
    15: {
        "title": "Multiclass Confusion Matrix",
        "summary": "Analyzing confusion matrices for multiclass problems.",
        "theory": [
            "### Macro vs Micro Averages\n",
            "- **Macro:** Calculate metric independently for each class and average them.\n",
            "- **Micro:** Aggregate all class contributions before calculating metrics."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from sklearn.metrics import classification_report, confusion_matrix\n",
            "\n",
            "y_true = [0, 1, 2, 0, 1, 2]\n",
            "y_pred = [0, 2, 2, 0, 1, 1]\n",
            "cm = confusion_matrix(y_true, y_pred)\n",
            "\n",
            "plt.figure(figsize=(6, 5))\n",
            "sns.heatmap(cm, annot=True, cmap='Oranges', fmt='d', xticklabels=['Class 0', 'Class 1', 'Class 2'], yticklabels=['Class 0', 'Class 1', 'Class 2'])\n",
            "plt.xlabel('Predicted Label')\n",
            "plt.ylabel('True Label')\n",
            "plt.title('Multiclass Confusion Matrix Heatmap')\n",
            "plt.show()\n",
            "print(classification_report(y_true, y_pred))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the precision of class 2 based on the predictions."
        ],
        "exercise_code": [
            "print('Class 2 Precision: 0.50 (TP=1, FP=1 (class 1 predicted as 2))')\n"
        ]
    },
    16: {
        "title": "Accuracy vs F1 Score",
        "summary": "Why accuracy is misleading on imbalanced datasets.",
        "theory": [
            "### Accuracy Pitfalls\n",
            "If class A represents 99% of sample data, a dummy classifier always guessing A gets 99% accuracy but has 0 F1."
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.metrics import accuracy_score, f1_score\n",
            "\n",
            "# Highly imbalanced targets\n",
            "y_true = np.array([0]*95 + [1]*5)\n",
            "y_pred = np.array([0]*100) # always predicts majority\n",
            "\n",
            "print('Accuracy:', accuracy_score(y_true, y_pred))\n",
            "print('F1 Score:', f1_score(y_true, y_pred, zero_division=0))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Discuss how predicting majority class only affects precision and recall."
        ],
        "exercise_code": [
            "print('Both precision and recall for the positive class will be 0.0 because there are no true positives.')\n"
        ]
    },
    17: {
        "title": "Dataset imbalance and remedies: Augmentation",
        "summary": "Handling imbalanced data using class weights and resampling.",
        "theory": [
            "### Remedying Imbalance\n",
            "- Cost-sensitive learning: increasing misclassification penalty of minority class."
        ],
        "code": [
            "from sklearn.datasets import make_classification\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "\n",
            "X, y = make_classification(n_samples=200, n_features=4, weights=[0.9, 0.1], random_state=42)\n",
            "\n",
            "lr_unbalanced = LogisticRegression().fit(X, y)\n",
            "lr_balanced = LogisticRegression(class_weight='balanced').fit(X, y)\n",
            "\n",
            "print('Unbalanced class predictions:', lr_unbalanced.predict(X).sum())\n",
            "print('Balanced class predictions:', lr_balanced.predict(X).sum())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Describe how setting class_weight='balanced' changes the loss formulation."
        ],
        "exercise_code": [
            "print('It scales the loss contribution of each class inversely proportional to their class frequency in input data.')\n"
        ]
    },
    18: {
        "title": "Conditional Probability",
        "summary": "Mathematical foundations of conditional probability.",
        "theory": [
            "### Formula\n",
            "$$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$$"
        ],
        "code": [
            "import pandas as pd\n",
            "\n",
            "# Toy survey data\n",
            "df = pd.DataFrame({\n",
            "    'Purchased': [1, 0, 1, 1, 0, 1],\n",
            "    'Gender': ['F', 'M', 'F', 'M', 'F', 'F']\n",
            "})\n",
            "\n",
            "# P(Purchased | Female)\n",
            "female_subset = df[df['Gender'] == 'F']\n",
            "p_cond = (female_subset['Purchased'] == 1).mean()\n",
            "print('P(Purchased | Female) =', p_cond)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Find P(Female | Purchased) from the dataframe."
        ],
        "exercise_code": [
            "purchased_subset = df[df['Purchased'] == 1]\n",
            "p_female_cond = (purchased_subset['Gender'] == 'F').mean()\n",
            "print('P(Female | Purchased) =', p_female_cond)\n"
        ]
    },
    19: {
        "title": "Bayes Theorem",
        "summary": "Bayes theorem formula and probability updating.",
        "theory": [
            "### Updating Probabilities\n",
            "$$P(A|B) = \\frac{P(B|A)P(A)}{P(B)}$$"
        ],
        "code": [
            "# Calculate updated probability after positive medical test\n",
            "prev = 0.01      # Prior P(Disease)\n",
            "sens = 0.99      # Likelihood P(Pos | Disease)\n",
            "spec = 0.95      # P(Neg | No Disease)\n",
            "\n",
            "# Marginal P(Pos)\n",
            "p_pos = sens * prev + (1 - spec) * (1 - prev)\n",
            "# Posterior P(Disease | Pos)\n",
            "post = sens * prev / p_pos\n",
            "print(f'Posterior Probability: {post:.4f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Re-calculate the posterior probability if disease prevalence rises to 5%."
        ],
        "exercise_code": [
            "prev_new = 0.05\n",
            "p_pos_new = sens * prev_new + (1 - spec) * (1 - prev_new)\n",
            "post_new = sens * prev_new / p_pos_new\n",
            "print(f'New Posterior Probability: {post_new:.4f}')\n"
        ]
    },
    20: {
        "title": "Stanford CS229 Lec 5: GDA and Naive Bayes",
        "summary": "Generative vs Discriminative algorithms, GDA, and Naive Bayes.",
        "theory": [
            "### GDA and Naive Bayes\n",
            "- **GDA:** Assumes $x|y \\sim N(\\mu, \\Sigma)$. Best for continuous variables.\n",
            "- **Naive Bayes:** Assumes features are conditionally independent given label $y$."
        ],
        "code": [
            "from sklearn.datasets import load_iris\n",
            "from sklearn.naive_bayes import GaussianNB\n",
            "\n",
            "iris = load_iris()\n",
            "model = GaussianNB().fit(iris.data, iris.target)\n",
            "print('Class priors:', model.class_prior_)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. State the key assumption difference between GDA and Naive Bayes."
        ],
        "exercise_code": [
            "print('GDA assumes multivariate normality with shared covariance, while Naive Bayes assumes independent conditional distributions.')\n"
        ]
    },
    21: {
        "title": "Naive Bayes full series",
        "summary": "Math of Naive Bayes, Laplace smoothing, and log-probabilities.",
        "theory": [
            "### Laplace Smoothing\n",
            "$$P(x_j|y) = \\frac{N_{jc} + \\alpha}{N_c + \\alpha D}$$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "# Count matrix for single feature: [counts class 0, counts class 1]\n",
            "counts = np.array([0, 5])\n",
            "n_0 = 10\n",
            "n_1 = 12\n",
            "vocab = 4\n",
            "\n",
            "# Unsmoothed\n",
            "p_raw_0 = counts[0] / n_0\n",
            "# Smoothed (alpha=1)\n",
            "p_smooth_0 = (counts[0] + 1) / (n_0 + vocab)\n",
            "print(f'Raw: {p_raw_0}, Smoothed: {p_smooth_0}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compute Laplace-smoothed probability for feature 1 given class 0."
        ],
        "exercise_code": [
            "p_smooth_1 = (counts[1] + 1) / (n_1 + vocab)\n",
            "print(f'Smoothed Class 1: {p_smooth_1:.4f}')\n"
        ]
    },
    22: {
        "title": "Naive Bayes variants: Bernoulli, Multinomial, Gaussian",
        "summary": "Comparing Naive Bayes variants in Scikit-Learn.",
        "theory": [
            "### NB Scikit-Learn Variants\n",
            "- **GaussianNB:** Inputs are continuous normal values.\n",
            "- **MultinomialNB:** Inputs are discrete word/feature occurrences.\n",
            "- **BernoulliNB:** Inputs are binary indicators."
        ],
        "code": [
            "from sklearn.naive_bayes import GaussianNB, BernoulliNB\n",
            "from sklearn.datasets import load_iris\n",
            "\n",
            "X, y = load_iris(return_X_y=True)\n",
            "gnb = GaussianNB().fit(X, y)\n",
            "bnb = BernoulliNB().fit(X, y)\n",
            "print('Gaussian NB score:', gnb.score(X, y))\n",
            "print('Bernoulli NB score:', bnb.score(X, y))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is BernoulliNB performance low on the Iris dataset?"
        ],
        "exercise_code": [
            "print('Iris features are continuous rather than binary variables, making BernoulliNB assumptions invalid.')\n"
        ]
    },
    23: {
        "title": "Naive Bayes solved numerical",
        "summary": "Solved text classification example with document probabilities.",
        "theory": [
            "### Hand Numerical Example\n",
            "Classify text given word occurrence counts and prior distribution probabilities."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "# Priors\n",
            "prior_spam = 0.4\n",
            "prior_ham = 0.6\n",
            "\n",
            "# Word probabilities: [P(free|Spam), P(free|Ham)]\n",
            "p_free = [0.8, 0.1]\n",
            "\n",
            "# Score for document containing 'free'\n",
            "score_spam = prior_spam * p_free[0]\n",
            "score_ham = prior_ham * p_free[1]\n",
            "print('Spam score:', score_spam)\n",
            "print('Ham score:', score_ham)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Classify the document based on the calculated scores."
        ],
        "exercise_code": [
            "print('Decision: SPAM' if score_spam > score_ham else 'Decision: HAM')\n"
        ]
    },
    24: {
        "title": "Bayesian Belief Network",
        "summary": "Directed acyclic graphs and joint probability factorization.",
        "theory": [
            "### Joint Factorization\n",
            "$$P(X_1, X_2, X_3) = P(X_1)P(X_2|X_1)P(X_3|X_2)$$"
        ],
        "code": [
            "# Calculating joint probability of path in simple network\n",
            "p_rain = 0.2\n",
            "p_sprinkler_given_rain = 0.01\n",
            "p_sprinkler_given_no_rain = 0.4\n",
            "\n",
            "# P(Rain = True, Sprinkler = True)\n",
            "p_joint = p_rain * p_sprinkler_given_rain\n",
            "print('Joint Probability:', p_joint)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compute P(Rain = False, Sprinkler = True)."
        ],
        "exercise_code": [
            "p_joint_no_rain = (1 - p_rain) * p_sprinkler_given_no_rain\n",
            "print('Joint Probability (No Rain):', p_joint_no_rain)\n"
        ]
    },
    25: {
        "title": "Bayes Optimal Classifier",
        "summary": "Bayes Error and Bayes Optimal decision boundary.",
        "theory": [
            "### Optimal Classification Boundary\n",
            "The decision boundary where class conditional probability densities intersect: $P(Y=0|x) = P(Y=1|x)$."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from scipy.stats import norm\n",
            "\n",
            "x = np.linspace(-5, 5, 200)\n",
            "p_x_c0 = norm.pdf(x, loc=-1.0, scale=1.0) # class 0 density\n",
            "p_x_c1 = norm.pdf(x, loc=1.0, scale=1.0)  # class 1 density\n",
            "\n",
            "plt.plot(x, p_x_c0, 'r', label='Class 0')\n",
            "plt.plot(x, p_x_c1, 'g', label='Class 1')\n",
            "plt.axvline(0.0, color='black', linestyle='--', label='Bayes Boundary')\n",
            "plt.legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. State what Bayes Error represents."
        ],
        "exercise_code": [
            "print('Bayes Error is the irreducible error rate corresponding to the optimal classifier decision boundary.')\n"
        ]
    },
    26: {
        "title": "Concept Learning",
        "summary": "Version Spaces and Find-S algorithm.",
        "theory": [
            "### Hypothesis Space\n",
            "- **Find-S:** Finds the most specific hypothesis consistent with positive training examples."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "# Instances [Outlook, Temp], label\n",
            "data = [\n",
            "    (['Sunny', 'Hot'], 1),\n",
            "    (['Sunny', 'Warm'], 1),\n",
            "    (['Rainy', 'Cold'], 0)\n",
            "]\n",
            "\n",
            "hypothesis = ['pi', 'pi'] # most specific\n",
            "\n",
            "for attrs, label in data:\n",
            "    if label == 1:\n",
            "        for j in range(len(attrs)):\n",
            "            if hypothesis[j] == 'pi':\n",
            "                hypothesis[j] = attrs[j]\n",
            "            elif hypothesis[j] != attrs[j]:\n",
            "                hypothesis[j] = '?'\n",
            "print('Final Hypothesis:', hypothesis)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Discuss how negative training instances affect the Find-S algorithm."
        ],
        "exercise_code": [
            "print('Find-S completely ignores negative instances, relying exclusively on positive instances to generalize.')\n"
        ]
    },
    27: {
        "title": "Stanford CS229 Lec 6: SVM",
        "summary": "Support Vector Machines, margins, and optimization dual problem.",
        "theory": [
            "### Support Vector Classifier Optimization\n",
            "Objective: Minimize $\\frac{1}{2}\\|w\\|^2$ subject to $y^{(i)}(w^T x^{(i)} + b) \\ge 1$."
        ],
        "code": [
            "from sklearn.datasets import load_iris\n",
            "from sklearn.svm import SVC\n",
            "\n",
            "X, y = load_iris(return_X_y=True)\n",
            "# Binary classification subset\n",
            "X, y = X[y < 2], y[y < 2]\n",
            "\n",
            "svm_model = SVC(kernel='linear')\n",
            "svm_model.fit(X, y)\n",
            "print('Support Vectors count:', len(svm_model.support_vectors_))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Output the indices of the support vectors."
        ],
        "exercise_code": [
            "print('Indices:', svm_model.support_)\n"
        ]
    },
    28: {
        "title": "SVM geometric intuition",
        "summary": "Hyperplane geometry and support vectors visualization.",
        "theory": [
            "### Decision Hyperplane\n",
            "Maximizing distance (margin) between boundary and support vectors."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import make_blobs\n",
            "from sklearn.svm import SVC\n",
            "\n",
            "X, y = make_blobs(n_samples=40, centers=2, random_state=6)\n",
            "clf = SVC(kernel='linear', C=1000)\n",
            "clf.fit(X, y)\n",
            "\n",
            "plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)\n",
            "# Plot decision function\n",
            "ax = plt.gca()\n",
            "xlim = ax.get_xlim()\n",
            "ylim = ax.get_ylim()\n",
            "xx = np.linspace(xlim[0], xlim[1], 30)\n",
            "yy = np.linspace(ylim[0], ylim[1], 30)\n",
            "YY, XX = np.meshgrid(yy, xx)\n",
            "xy = np.vstack([XX.ravel(), YY.ravel()]).T\n",
            "Z = clf.decision_function(xy).reshape(XX.shape)\n",
            "\n",
            "ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])\n",
            "ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, linewidth=1, facecolors='none', edgecolors='k')\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain what happens if data points outside the support vectors are modified."
        ],
        "exercise_code": [
            "print('Nothing happens to the boundary, as the decision hyperplane depends entirely on support vectors.')\n"
        ]
    },
    29: {
        "title": "SVM hard margin and soft margin math",
        "summary": "Formulations for hard margin vs soft margin with slack variables.",
        "theory": [
            "### Soft Margin Objective\n",
            "Minimize $\\frac{1}{2}\\|w\\|^2 + C \\sum_{i=1}^m \\xi_i$ (where $\\xi_i \\ge 0$ represents margin violation slack)."
        ],
        "code": [
            "from sklearn.datasets import make_classification\n",
            "from sklearn.svm import SVC\n",
            "\n",
            "X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)\n",
            "\n",
            "clf_hard = SVC(kernel='linear', C=100.0) # low slack tolerance\n",
            "clf_soft = SVC(kernel='linear', C=0.1)   # high slack tolerance\n",
            "\n",
            "clf_hard.fit(X, y)\n",
            "clf_soft.fit(X, y)\n",
            "print('Hard C support vectors count:', len(clf_hard.support_vectors_))\n",
            "print('Soft C support vectors count:', len(clf_soft.support_vectors_))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain the regularization role of parameter C."
        ],
        "exercise_code": [
            "print('Large C imposes a high penalty on violations, leading to a narrower margin. Small C allows violations, yielding a wider margin.')\n"
        ]
    },
    30: {
        "title": "Stanford CS229 Lec 7: Kernels",
        "summary": "Kernel trick, Mercer's theorem, and non-linear mappings.",
        "theory": [
            "### Kernel Representation\n",
            "Instead of computing $\\Phi(x)$ explicitly, calculate inner product function $K(x, z) = \\Phi(x)^T \\Phi(z)$."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "def rbf_kernel(x1, x2, gamma=1.0):\n",
            "    return np.exp(-gamma * np.sum((x1 - x2)**2))\n",
            "\n",
            "a = np.array([1, 2])\n",
            "b = np.array([1.5, 2.5])\n",
            "print('RBF Kernel valuation:', rbf_kernel(a, b))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compute the RBF kernel valuation for $a$ and $b$ using gamma = 0.1."
        ],
        "exercise_code": [
            "print('RBF (gamma=0.1):', rbf_kernel(a, b, gamma=0.1))\n"
        ]
    },
    31: {
        "title": "Kernel trick and Non linear SVM",
        "summary": "Solving non-linearly separable problems using SVC kernels.",
        "theory": [
            "### Mappings in SVM\n",
            "Circular XOR classification separation using Radial Basis Function (RBF) mapping."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import make_circles\n",
            "from sklearn.svm import SVC\n",
            "\n",
            "X, y = make_circles(n_samples=100, noise=0.1, factor=0.5, random_state=42)\n",
            "clf_rbf = SVC(kernel='rbf', C=1.0).fit(X, y)\n",
            "\n",
            "xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 100), np.linspace(-1.5, 1.5, 100))\n",
            "Z = clf_rbf.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)\n",
            "\n",
            "plt.figure(figsize=(6, 5))\n",
            "plt.contourf(xx, yy, Z, levels=20, cmap='RdYlBu', alpha=0.8)\n",
            "plt.scatter(X[:, 0], X[:, 1], c=y, cmap='RdYlBu', edgecolors='k')\n",
            "plt.title('RBF Kernel SVM Decision Boundary')\n",
            "plt.colorbar(label='Decision Score')\n",
            "plt.show()\n",
            "\n",
            "clf_linear = SVC(kernel='linear').fit(X, y)\n",
            "print('Linear kernel accuracy:', clf_linear.score(X, y))\n",
            "print('RBF kernel accuracy:', clf_rbf.score(X, y))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Fit a Polynomial kernel SVM model on circular dataset and print score."
        ],
        "exercise_code": [
            "clf_poly = SVC(kernel='poly', degree=2).fit(X, y)\n",
            "print('Polynomial score:', clf_poly.score(X, y))\n"
        ]
    },
    32: {
        "title": "SVM implementation",
        "summary": "Practical SVM classification with Scikit-Learn.",
        "theory": [
            "### Scikit-Learn SVM API\n",
            "Tuning parameters `C`, `kernel`, and `gamma` for standard datasets."
        ],
        "code": [
            "from sklearn.datasets import load_wine\n",
            "from sklearn.svm import SVC\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "wine = load_wine()\n",
            "X_scaled = StandardScaler().fit_transform(wine.data)\n",
            "y = wine.target\n",
            "\n",
            "X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)\n",
            "model = SVC(kernel='rbf', C=1.0, gamma='scale')\n",
            "model.fit(X_train, y_train)\n",
            "print('Test Accuracy:', model.score(X_test, y_test))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Train SVM with a very small gamma (0.001) and print score."
        ],
        "exercise_code": [
            "model_g = SVC(kernel='rbf', gamma=0.001).fit(X_train, y_train)\n",
            "print('Test score (gamma=0.001):', model_g.score(X_test, y_test))\n"
        ]
    },
    33: {
        "title": "Decision Tree intuition and Entropy and Info Gain",
        "summary": "Node splitting math: Entropy, Gini Impurity, and Information Gain.",
        "theory": [
            "### Split Criteria\n",
            "- **Entropy:** $H(S) = -\\sum p_i \\log_2 p_i$\n",
            "- **Gini:** $G(S) = 1 - \\sum p_i^2$\n",
            "- **Information Gain:** $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "def entropy(probs):\n",
            "    return -np.sum([p * np.log2(p) for p in probs if p > 0])\n",
            "\n",
            "def gini(probs):\n",
            "    return 1 - np.sum([p**2 for p in probs])\n",
            "\n",
            "print('Entropy of [0.5, 0.5] uniform split:', entropy([0.5, 0.5]))\n",
            "print('Gini Impurity of [0.5, 0.5] uniform split:', gini([0.5, 0.5]))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the entropy of a distribution with classes ratio $[0.9, 0.1]$."
        ],
        "exercise_code": [
            "print('Entropy:', f'{entropy([0.9, 0.1]):.4f}')\n"
        ]
    },
    34: {
        "title": "ID3, C4.5, CART algorithms",
        "summary": "Comparing decision tree construction algorithms.",
        "theory": [
            "### Tree Generation Algorithms\n",
            "- **ID3:** Relies on Information Gain. Only supports categorical splits.\n",
            "- **C4.5:** Uses Gain Ratio to penalize multi-way branching bias.\n",
            "- **CART:** Uses Gini Impurity. Restricts splits to binary choices."
        ],
        "code": [
            "from sklearn.tree import DecisionTreeClassifier\n",
            "from sklearn.datasets import load_iris\n",
            "\n",
            "iris = load_iris()\n",
            "# CART algorithm is implemented in Scikit-Learn\n",
            "clf = DecisionTreeClassifier(criterion='gini', random_state=42)\n",
            "clf.fit(iris.data, iris.target)\n",
            "print('CART Tree Score:', clf.score(iris.data, iris.target))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Fit the DecisionTreeClassifier using 'entropy' (Information Gain) criterion instead."
        ],
        "exercise_code": [
            "clf_ent = DecisionTreeClassifier(criterion='entropy', random_state=42).fit(iris.data, iris.target)\n",
            "print('Entropy Tree Score:', clf_ent.score(iris.data, iris.target))\n"
        ]
    },
    35: {
        "title": "Decision Tree hyperparameters and overfitting",
        "summary": "Regularizing decision trees to prevent overfitting.",
        "theory": [
            "### Controlling Tree Expansion\n",
            "- `max_depth`: Limits maximum vertical layers.\n",
            "- `min_samples_split`: Samples needed to split a node.\n",
            "- `min_samples_leaf`: Minimum samples allowed in a leaf."
        ],
        "code": [
            "from sklearn.datasets import load_breast_cancer\n",
            "from sklearn.tree import DecisionTreeClassifier\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "data = load_breast_cancer()\n",
            "X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)\n",
            "\n",
            "clf_overfit = DecisionTreeClassifier(random_state=42)\n",
            "clf_overfit.fit(X_train, y_train)\n",
            "\n",
            "clf_reg = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=42)\n",
            "clf_reg.fit(X_train, y_train)\n",
            "\n",
            "print('Overfit test score:', clf_overfit.score(X_test, y_test))\n",
            "print('Regularized test score:', clf_reg.score(X_test, y_test))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. State the depth of the fully grown overfit tree."
        ],
        "exercise_code": [
            "print('Depth:', clf_overfit.get_depth())\n"
        ]
    },
    36: {
        "title": "Decision Tree visualization",
        "summary": "Visualizing fitted decision trees in Python.",
        "theory": [
            "### Visualizing Splits\n",
            "Plotting tree decisions to trace decision nodes and path criteria."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import load_iris\n",
            "from sklearn.tree import DecisionTreeClassifier, plot_tree\n",
            "\n",
            "iris = load_iris()\n",
            "clf = DecisionTreeClassifier(max_depth=2, random_state=42)\n",
            "clf.fit(iris.data, iris.target)\n",
            "\n",
            "plt.figure(figsize=(8, 6))\n",
            "plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Identify the feature used for the root node split in the visualization."
        ],
        "exercise_code": [
            "print('Root node split feature:', iris.feature_names[clf.tree_.feature[0]])\n"
        ]
    },
    37: {
        "title": "Decision Tree implementation",
        "summary": "Practical decision tree classification and feature importance.",
        "theory": [
            "### Feature Importance\n",
            "Impurity reduction importance: total Gini reduction contributed by each feature split."
        ],
        "code": [
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import load_wine\n",
            "from sklearn.tree import DecisionTreeClassifier\n",
            "\n",
            "wine = load_wine()\n",
            "X = pd.DataFrame(wine.data, columns=wine.feature_names)\n",
            "y = wine.target\n",
            "\n",
            "clf = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X, y)\n",
            "imp = pd.Series(clf.feature_importances_, index=X.columns).sort_values(ascending=True)\n",
            "\n",
            "plt.figure(figsize=(8, 5))\n",
            "imp.plot(kind='barh', color='teal')\n",
            "plt.title('Decision Tree Feature Importances (Wine Dataset)')\n",
            "plt.xlabel('Gini Importance')\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Confirm if the sum of all feature importances totals 1.0."
        ],
        "exercise_code": [
            "print('Sum of importances:', imp.sum())\n"
        ]
    },
    38: {
        "title": "KNN Classification and finding K",
        "summary": "KNN classification and choosing the optimal K value.",
        "theory": [
            "### Selecting neighbors count (K)\n",
            "- $K$ too small: Fits noise, high variance.\n",
            "- $K$ too large: Flat boundaries, high bias."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import load_iris\n",
            "from sklearn.neighbors import KNeighborsClassifier\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "iris = load_iris()\n",
            "X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)\n",
            "\n",
            "k_values = range(1, 31)\n",
            "accuracies = []\n",
            "for k in k_values:\n",
            "    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)\n",
            "    accuracies.append(knn.score(X_test, y_test))\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "plt.plot(k_values, accuracies, 'bo-')\n",
            "plt.xlabel('Number of Neighbors K')\n",
            "plt.ylabel('Test Accuracy')\n",
            "plt.title('KNN Parameter Tuning: K vs Accuracy')\n",
            "plt.grid(True)\n",
            "plt.show()\n",
            "\n",
            "print('Test Accuracy (K=5):', accuracies[4])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Evaluate test accuracy for $K = 1$ and $K = 25$."
        ],
        "exercise_code": [
            "print(f'Accuracy K=1: {accuracies[0]:.4f}, K=25: {accuracies[24]:.4f}')\n"
        ]
    },
    39: {
        "title": "KNN full overview",
        "summary": "Lazy learner characteristics, distance metrics, and scaling requirements.",
        "theory": [
            "### Distance calculation sensitivity\n",
            "KNN is a lazy learner (no explicit training phase). It is highly sensitive to features magnitude differences."
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.neighbors import KNeighborsClassifier\n",
            "\n",
            "# Unscaled dataset where feature 1 has large magnitude\n",
            "X = np.array([[1.0, 1000.0], [1.1, 1010.0], [5.0, 10.0], [5.1, 15.0]])\n",
            "y = np.array([0, 0, 1, 1])\n",
            "\n",
            "knn = KNeighborsClassifier(n_neighbors=1).fit(X, y)\n",
            "# Predict query point close to class 1 features, but slightly shifted on feature 2\n",
            "print('Prediction for [5.0, 100.0]:', knn.predict([[5.0, 100.0]])[0])\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Discuss why the model predicted 0 instead of 1."
        ],
        "exercise_code": [
            "print('Distance is dominated by the scale of feature 2, making the query point seem closer to class 0.')\n"
        ]
    },
    40: {
        "title": "Linear Discriminant Analysis (LDA)",
        "summary": "Dimensionality reduction and classification using LDA.",
        "theory": [
            "### LDA projection objective\n",
            "Find projection vector $w$ that maximizes the between-class variance relative to within-class variance."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.discriminant_analysis import LinearDiscriminantAnalysis\n",
            "from sklearn.datasets import load_iris\n",
            "\n",
            "iris = load_iris()\n",
            "lda = LinearDiscriminantAnalysis(n_components=2)\n",
            "X_r2 = lda.fit_transform(iris.data, iris.target)\n",
            "\n",
            "plt.figure(figsize=(6, 5))\n",
            "for color, i, target_name in zip(['navy', 'turquoise', 'darkorange'], [0, 1, 2], iris.target_names):\n",
            "    plt.scatter(X_r2[iris.target == i, 0], X_r2[iris.target == i, 1], alpha=.8, color=color, label=target_name)\n",
            "plt.legend(loc='best', shadow=False, scatterpoints=1)\n",
            "plt.title('LDA Projection of Iris Dataset')\n",
            "plt.xlabel('LD 1')\n",
            "plt.ylabel('LD 2')\n",
            "plt.grid(True)\n",
            "plt.show()\n",
            "\n",
            "print('Explained variance ratio:', lda.explained_variance_ratio_)\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Verify the accuracy of LDA classifier predictions directly on Iris dataset."
        ],
        "exercise_code": [
            "print('LDA Classification Score:', lda.score(iris.data, iris.target))\n"
        ]
    },
    41: {
        "title": "Inductive Bias",
        "summary": "Concept of inductive bias in learning algorithms.",
        "theory": [
            "### Inductive Bias Examples\n",
            "- **Linear Models (Logistic Regression):** Assume the class separation boundary is a linear hyperplane.\n",
            "- **Decision Trees (CART):** Assume boundaries are orthogonal splits parallel to feature axes.\n",
            "- **Nearest Neighbors (KNN):** Assume decision boundaries are determined locally by neighborhood clustering (Voronoi-like cells).\n",
            "- **Support Vector Machines (Kernel SVM):** Assume boundaries can be mapped to high-dimensional spaces to find smooth, maximum-margin non-linear curves."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import make_moons\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "from sklearn.tree import DecisionTreeClassifier\n",
            "from sklearn.neighbors import KNeighborsClassifier\n",
            "from sklearn.svm import SVC\n",
            "\n",
            "X, y = make_moons(n_samples=150, noise=0.25, random_state=42)\n",
            "models = {\n",
            "    'Logistic Regression (Linear Bias)': LogisticRegression(),\n",
            "    'Decision Tree (Axis-Aligned Bias)': DecisionTreeClassifier(max_depth=4, random_state=42),\n",
            "    'KNN (K=3) (Local Instance Bias)': KNeighborsClassifier(n_neighbors=3),\n",
            "    'SVM (RBF) (Radial Distance Bias)': SVC(kernel='rbf', C=1.0, random_state=42)\n",
            "}\n",
            "\n",
            "fig, axes = plt.subplots(2, 2, figsize=(12, 10))\n",
            "axes = axes.ravel()\n",
            "xx, yy = np.meshgrid(np.linspace(-2, 3, 100), np.linspace(-1.5, 2, 100))\n",
            "grid = np.c_[xx.ravel(), yy.ravel()]\n",
            "\n",
            "for ax, (name, model) in zip(axes, models.items()):\n",
            "    model.fit(X, y)\n",
            "    Z = model.predict(grid).reshape(xx.shape)\n",
            "    ax.contourf(xx, yy, Z, cmap='RdYlBu', alpha=0.6)\n",
            "    ax.scatter(X[:, 0], X[:, 1], c=y, cmap='RdYlBu', edgecolors='k')\n",
            "    ax.set_title(name, fontsize=12)\n",
            "    ax.grid(True, linestyle=':', alpha=0.5)\n",
            "\n",
            "plt.suptitle('Classifier Inductive Bias Comparison (4 Classification Maps)', fontsize=16, y=0.98)\n",
            "plt.tight_layout()\n",
            "plt.show()\n",
            "\n",
            "print('Inductive bias represents the set of assumptions a learner uses to predict outputs for unseen inputs.')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Contrast preference bias vs restriction bias."
        ],
        "exercise_code": [
            "print('Restriction bias limits the hypothesis space of functional forms. Preference bias prefers certain hypotheses over others within that space.')\n"
        ]
    }
}



PHASE_9_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Training & Testing Phase",
        "summary": "Overview of model validation splitting, statistical independence, and dataset partitioning.",
        "theory": [
            "### 1. Dataset Partitioning\n",
            "- **Training set:** Used by the model to fit weights and parameters.\n",
            "- **Testing set:** Kept completely isolated during training to evaluate generalized performance.\n",
            "- **Independence assumption:** Data points in train and test sets must be independent and identically distributed (i.i.d.). Data leakage occurs when test set statistical information leaks into training."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.datasets import make_classification\n",
            "\n",
            "X, y = make_classification(n_samples=200, n_features=2, n_informative=2, n_redundant=0, random_state=42)\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
            "\n",
            "plt.figure(figsize=(6, 4))\n",
            "plt.bar(['Train Set', 'Test Set'], [len(X_train), len(X_test)], color=['skyblue', 'salmon'])\n",
            "plt.title('Dataset Split Sizes')\n",
            "plt.ylabel('Number of Samples')\n",
            "plt.show()\n",
            "print(f'Train set size: {len(X_train)}, Test set size: {len(X_test)}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain why a test size of 99% is problematic."
        ],
        "exercise_code": [
            "print('A test size of 99% leaves only 1% of the data for training, which will cause the model to severely underfit and represent the data poorly.')\n"
        ]
    },
    2: {
        "title": "Classic vs Adaptive Machine",
        "summary": "Batch learning vs Adaptive/Online learning systems.",
        "theory": [
            "### Batch vs Online Learning\n",
            "- **Classic (Batch) Learning:** Models are trained offline on a static, complete dataset. Model updates require retraining from scratch.\n",
            "- **Adaptive (Online) Learning:** Models update incrementally by consuming a stream of instances. Fits scenarios with concept drift or hardware constraints."
        ],
        "code": [
            "import numpy as np\n",
            "from sklearn.linear_model import SGDClassifier\n",
            "\n",
            "# Simulate stream of data\n",
            "clf = SGDClassifier(loss='log_loss', random_state=42)\n",
            "X_stream = np.random.randn(10, 5)\n",
            "y_stream = np.random.randint(0, 2, size=10)\n",
            "\n",
            "# Online training using partial_fit\n",
            "for i in range(len(X_stream)):\n",
            "    clf.partial_fit(X_stream[i:i+1], y_stream[i:i+1], classes=[0, 1])\n",
            "\n",
            "print('Successfully completed online incremental training steps!')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Define concept drift."
        ],
        "exercise_code": [
            "print('Concept drift refers to the statistical properties of the target variable changing over time in unforeseen ways, degrading model performance.')\n"
        ]
    },
    3: {
        "title": "Basics of Training and Testing",
        "summary": "Train/test evaluation metrics and standard scikit-learn API usage.",
        "theory": [
            "### Basic Validation Flow\n",
            "Evaluating model predictions against true labels using scikit-learn model fitting API."
        ],
        "code": [
            "from sklearn.datasets import load_iris\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.neighbors import KNeighborsClassifier\n",
            "\n",
            "X, y = load_iris(return_X_y=True)\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
            "clf = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)\n",
            "print('Train Score:', clf.score(X_train, y_train))\n",
            "print('Test Score:', clf.score(X_test, y_test))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What is the risk of tuning hyperparameters directly on the test set?"
        ],
        "exercise_code": [
            "print('Tuning hyperparameters on the test set causes data leakage (optimizing for the test set specifically), leading to optimistic but biased performance estimates.')\n"
        ]
    },
    4: {
        "title": "Stanford CS229 Lec 8: Data splits and Cross Validation theory",
        "summary": "Generalization error bounds, Hoeffding's inequality, Empirical Risk Minimization (ERM), and uniform convergence bounds.",
        "theory": [
            "### Empirical Risk Minimization (ERM)\n",
            "- **Empirical Risk (Train Error):** $\\hat{\\epsilon}(h) = \\frac{1}{m} \\sum_{i=1}^m I(h(x^{(i)}) \\neq y^{(i)})$\n",
            "- **Generalization Error:** $\\epsilon(h) = P_{(x,y) \\sim D}(h(x) \\neq y)$\n",
            "- **Hoeffding's Inequality:** $P(|\\hat{\\epsilon}(h) - \\epsilon(h)| > \\gamma) \\le 2e^{-2\\gamma^2 m}$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "def hoeffding_bound(m, gamma):\n",
            "    return 2 * np.exp(-2 * (gamma ** 2) * m)\n",
            "\n",
            "print('Bound for m=100, gamma=0.1:', hoeffding_bound(100, 0.1))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Calculate the bound for $m=1000$ and $\\gamma=0.05$."
        ],
        "exercise_code": [
            "print('Bound:', hoeffding_bound(1000, 0.05))\n"
        ]
    },
    5: {
        "title": "Stanford CS229 Discussion: Learning Theory",
        "summary": "Stanford CS229 discussion on learning theory, VC dimension, and sample complexity.",
        "theory": [
            "### VC Dimension\n",
            "- **Shattering:** A hypothesis space $H$ shatters a set of points if it can separate all possible label assignments.\n",
            "- **VC Dimension:** Size of largest set shattered by $H$. Sample complexity bound:\n",
            "  $$m = O\\left(\\frac{1}{\\epsilon} \\log \\frac{1}{\\delta} + \\frac{VC(H)}{\\epsilon} \\log \\frac{1}{\\epsilon}\\right)$$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "def sample_complexity(vc_dim, epsilon=0.05, delta=0.05):\n",
            "    return (1.0 / epsilon) * (np.log(1.0 / delta) + vc_dim * np.log(1.0 / epsilon))\n",
            "\n",
            "print('Required samples for VC=3 (Linear Classifier in 2D):', int(sample_complexity(3)))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Compute sample complexity for $VC=10$."
        ],
        "exercise_code": [
            "print('Samples for VC=10:', int(sample_complexity(10)))\n"
        ]
    },
    6: {
        "title": "Cross Validation",
        "summary": "Hold-out validation vs K-Fold cross-validation comparison.",
        "theory": [
            "### Cross-Validation Concept\n",
            "Reduces bias of hold-out split evaluation by rotating training and validation partitions."
        ],
        "code": [
            "from sklearn.model_selection import cross_val_score\n",
            "from sklearn.datasets import load_iris\n",
            "from sklearn.svm import SVC\n",
            "\n",
            "X, y = load_iris(return_X_y=True)\n",
            "scores = cross_val_score(SVC(), X, y, cv=5)\n",
            "print('Cross-Validation Accuracies:', scores)\n",
            "print('Mean Accuracy:', scores.mean())\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. List one limitation of cross-validation."
        ],
        "exercise_code": [
            "print('Cross-validation is computationally expensive because the model must be trained and evaluated k times.')\n"
        ]
    },
    7: {
        "title": "K Fold Cross Validation",
        "summary": "K-Fold CV mechanics.",
        "theory": [
            "### Split Visualization\n",
            "Partitioning dataset into $K$ mutual subsets, using one as validation and $K-1$ as training."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.model_selection import KFold\n",
            "\n",
            "kf = KFold(n_splits=5, shuffle=True, random_state=42)\n",
            "X = np.arange(25)\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "for i, (train_idx, val_idx) in enumerate(kf.split(X)):\n",
            "    plt.scatter(train_idx, [i]*len(train_idx), color='blue', marker='o', label='Train' if i==0 else \"\")\n",
            "    plt.scatter(val_idx, [i]*len(val_idx), color='red', marker='x', label='Validation' if i==0 else \"\")\n",
            "plt.yticks(range(5), [f'Fold {i+1}' for i in range(5)])\n",
            "plt.xlabel('Sample Index')\n",
            "plt.title('K-Fold Cross-Validation Splitting')\n",
            "plt.legend()\n",
            "plt.grid(True, linestyle=':', alpha=0.6)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain why `shuffle=True` is crucial when K-Folding sorted datasets."
        ],
        "exercise_code": [
            "print('If the dataset is sorted by class label, each fold without shuffling will contain highly skewed or single-class distributions, causing model evaluation to fail.')\n"
        ]
    },
    8: {
        "title": "LOOCV and Leave P Out",
        "summary": "Leave-One-Out (LOOCV) and Leave-P-Out CV techniques.",
        "theory": [
            "### LOOCV Properties\n",
            "- **Leave-One-Out (LOOCV):** Fits models using $K=N$. Gives unbiased estimates but high variance.\n",
            "- **Leave-P-Out:** Leaves $P$ samples for validation."
        ],
        "code": [
            "from sklearn.model_selection import LeaveOneOut\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "from sklearn.datasets import load_iris\n",
            "import numpy as np\n",
            "\n",
            "X, y = load_iris(return_X_y=True)\n",
            "X = np.vstack([X[:15], X[50:65]])\n",
            "y = np.hstack([y[:15], y[50:65]])\n",
            "\n",
            "loo = LeaveOneOut()\n",
            "scores = []\n",
            "for train_idx, test_idx in loo.split(X):\n",
            "    X_train, X_test = X[train_idx], X[test_idx]\n",
            "    y_train, y_test = y[train_idx], y[test_idx]\n",
            "    model = LogisticRegression().fit(X_train, y_train)\n",
            "    scores.append(model.score(X_test, y_test))\n",
            "\n",
            "print('LOOCV Mean Accuracy:', np.mean(scores))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What makes LOOCV computationally prohibitive for large datasets?"
        ],
        "exercise_code": [
            "print('LOOCV requires training the model N times. For a dataset of size N = 100,000, training 100,000 models is computationally infeasible.')\n"
        ]
    },
    9: {
        "title": "Overfitting and Underfitting deep dive",
        "summary": "Underfitting/Overfitting definition and polynomials.",
        "theory": [
            "### Visualizing Capacity\n",
            "Varying model parameter complexity (degree of polynomial expansion) changes decision flexibility."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.pipeline import make_pipeline\n",
            "from sklearn.preprocessing import PolynomialFeatures\n",
            "from sklearn.linear_model import LinearRegression\n",
            "\n",
            "np.random.seed(42)\n",
            "X = np.sort(np.random.rand(30) * 5)\n",
            "y = np.sin(X) + np.random.randn(30) * 0.15\n",
            "X = X[:, np.newaxis]\n",
            "\n",
            "degrees = [1, 3, 15]\n",
            "plt.figure(figsize=(12, 4))\n",
            "X_plot = np.linspace(0, 5, 100)[:, np.newaxis]\n",
            "\n",
            "for i, deg in enumerate(degrees):\n",
            "    model = make_pipeline(PolynomialFeatures(deg), LinearRegression())\n",
            "    model.fit(X, y)\n",
            "    plt.subplot(1, 3, i+1)\n",
            "    plt.scatter(X, y, color='black')\n",
            "    plt.plot(X_plot, model.predict(X_plot), label=f'Degree {deg}')\n",
            "    plt.ylim(-1.5, 1.5)\n",
            "    plt.title(f'Degree {deg} (\"Underfit\" if deg==1 else \"Good\" if deg==3 else \"Overfit\")')\n",
            "    plt.legend()\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. How does adding L2 regularization (Ridge) affect a high-degree polynomial regression model?"
        ],
        "exercise_code": [
            "print('L2 regularization penalizes large coefficient weights, flattening the model curves and reducing overfitting by introducing a small bias in exchange for a large variance reduction.')\n"
        ]
    },
    10: {
        "title": "Model Complexity vs Error",
        "summary": "Train error vs validation error relationship.",
        "theory": [
            "### U-Shaped Curves\n",
            "As capacity grows, training set error goes to zero, but validation set error begins to rise as generalization fails."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "from sklearn.tree import DecisionTreeClassifier\n",
            "from sklearn.datasets import load_breast_cancer\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "data = load_breast_cancer()\n",
            "X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)\n",
            "\n",
            "depths = range(1, 15)\n",
            "train_errors = []\n",
            "test_errors = []\n",
            "\n",
            "for d in depths:\n",
            "    clf = DecisionTreeClassifier(max_depth=d, random_state=42).fit(X_train, y_train)\n",
            "    train_errors.append(1 - clf.score(X_train, y_train))\n",
            "    test_errors.append(1 - clf.score(X_test, y_test))\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "plt.plot(depths, train_errors, 'b-o', label='Training Error')\n",
            "plt.plot(depths, test_errors, 'r-o', label='Testing Error')\n",
            "plt.xlabel('Tree Max Depth (Model Complexity)')\n",
            "plt.ylabel('Classification Error Rate')\n",
            "plt.title('Model Complexity vs Train/Test Error')\n",
            "plt.legend()\n",
            "plt.grid(True)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Identify the optimal tree depth range based on the generated plot."
        ],
        "exercise_code": [
            "optimal_depth = depths[np.argmin(test_errors)]\n",
            "print(f'Optimal Depth is at max_depth = {optimal_depth} where validation error is minimized before overfitting begins.')\n"
        ]
    },
    11: {
        "title": "Bias Variance Tradeoff",
        "summary": "Mathematical derivation of the bias-variance decomposition.",
        "theory": [
            "### Mathematical Derivation\n",
            "Decomposing expected prediction error into Squared Bias, Variance, and Irreducible Noise:\n",
            "$$E[(y - \\hat{f}(x))^2] = \\text{Bias}[\\hat{f}(x)]^2 + \\text{Var}[\\hat{f}(x)] + \\sigma^2$$"
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "np.random.seed(42)\n",
            "true_f = lambda x: 2 * x + 1.5\n",
            "\n",
            "x_query = 2.0\n",
            "predictions = []\n",
            "for _ in range(50):\n",
            "    x_train = np.random.uniform(0, 4, 10)\n",
            "    y_train = true_f(x_train) + np.random.normal(0, 0.5, 10)\n",
            "    coef, intercept = np.polyfit(x_train, y_train, 1)\n",
            "    predictions.append(coef * x_query + intercept)\n",
            "\n",
            "pred_mean = np.mean(predictions)\n",
            "bias_sq = (pred_mean - true_f(x_query)) ** 2\n",
            "variance = np.var(predictions)\n",
            "print(f'Query true value: {true_f(x_query)}')\n",
            "print(f'Query mean prediction: {pred_mean:.4f}')\n",
            "print(f'Squared Bias: {bias_sq:.6f}')\n",
            "print(f'Model Variance: {variance:.6f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Describe how model bias and variance behave as capacity increases."
        ],
        "exercise_code": [
            "print('As model capacity increases, bias decreases (model fits training data better) while variance increases (model becomes sensitive to noise).')\n"
        ]
    },
    12: {
        "title": "Imbalanced Data and SMOTE and Oversampling",
        "summary": "SMOTE and minority oversampling.",
        "theory": [
            "### Balancing Distributions\n",
            "- **Oversampling:** Duplicating minority class observations.\n",
            "- **SMOTE:** Synthetic Minority Over-sampling Technique interpolates new data points along lines joining local neighbors."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import make_classification\n",
            "\n",
            "X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_clusters_per_class=1, weights=[0.9, 0.1], random_state=42)\n",
            "\n",
            "minority_idx = np.where(y == 1)[0]\n",
            "majority_idx = np.where(y == 0)[0]\n",
            "num_to_add = len(majority_idx) - len(minority_idx)\n",
            "\n",
            "np.random.seed(42)\n",
            "oversampled_noise = np.random.normal(0, 0.1, size=(num_to_add, 2))\n",
            "synthetic_X = X[np.random.choice(minority_idx, num_to_add)] + oversampled_noise\n",
            "\n",
            "X_resampled = np.vstack([X, synthetic_X])\n",
            "y_resampled = np.hstack([y, np.ones(num_to_add)])\n",
            "\n",
            "fig, axes = plt.subplots(1, 2, figsize=(10, 4))\n",
            "axes[0].scatter(X[y==0, 0], X[y==0, 1], color='blue', alpha=0.6, label='Majority')\n",
            "axes[0].scatter(X[y==1, 0], X[y==1, 1], color='red', alpha=0.6, label='Minority')\n",
            "axes[0].set_title('Before Oversampling')\n",
            "axes[0].legend()\n",
            "\n",
            "axes[1].scatter(X_resampled[y_resampled==0, 0], X_resampled[y_resampled==0, 1], color='blue', alpha=0.6, label='Majority')\n",
            "axes[1].scatter(X_resampled[y_resampled==1, 0], X_resampled[y_resampled==1, 1], color='red', alpha=0.6, label='Oversampled')\n",
            "axes[1].set_title('After Oversampling')\n",
            "axes[1].legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is evaluation using raw accuracy misleading on imbalanced datasets?"
        ],
        "exercise_code": [
            "print('For a dataset with 95% majority samples, a dummy model predicting majority class gets 95% accuracy while failing to identify any minority class instances.')\n"
        ]
    },
    13: {
        "title": "Hyperparameter Tuning with Optuna",
        "summary": "Search space, trials, and automated parameter tuning.",
        "theory": [
            "### Optimization Algorithms\n",
            "Optuna optimizes hyperparameters using Tree-structured Parzen Estimators (TPE) to suggest parameters dynamically."
        ],
        "code": [
            "# Uncomment and run the line below if you need to install Optuna:\n",
            "# !pip install optuna\n",
            "\n",
            "import optuna\n",
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "from sklearn.datasets import load_breast_cancer\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.model_selection import cross_val_score\n",
            "\n",
            "optuna.logging.set_verbosity(optuna.logging.WARNING)\n",
            "\n",
            "def objective(trial):\n",
            "    n_estimators = trial.suggest_int('n_estimators', 10, 50)\n",
            "    max_depth = trial.suggest_int('max_depth', 2, 8)\n",
            "    X, y = load_breast_cancer(return_X_y=True)\n",
            "    clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)\n",
            "    return cross_val_score(clf, X, y, cv=3).mean()\n",
            "\n",
            "study = optuna.create_study(direction='maximize')\n",
            "study.optimize(objective, n_trials=15)\n",
            "\n",
            "print('Best trial parameters:', study.best_params)\n",
            "print('Best cross-validation accuracy:', study.best_value)\n",
            "\n",
            "# Extract optimization history\n",
            "trial_values = [t.value for t in study.trials if t.value is not None]\n",
            "best_values = np.maximum.accumulate(trial_values)\n",
            "\n",
            "# Plot optimization history\n",
            "plt.figure(figsize=(9, 4.5))\n",
            "plt.plot(trial_values, 'o-', color='#1f77b4', label='Trial Objective Value', alpha=0.7)\n",
            "plt.plot(best_values, 'r--', drawstyle='steps-post', label='Best Value So Far', linewidth=2)\n",
            "plt.xlabel('Trial Number')\n",
            "plt.ylabel('Mean Accuracy')\n",
            "plt.title('Optuna Hyperparameter Optimization History', fontsize=12, fontweight='bold')\n",
            "plt.grid(True, linestyle=':', alpha=0.6)\n",
            "plt.legend(loc='lower right')\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain the difference between `suggest_int` and `suggest_float` in Optuna."
        ],
        "exercise_code": [
            "print('suggest_int samples discrete integer parameters, while suggest_float samples continuous real-valued parameters within specified ranges.')\n"
        ]
    },
    14: {
        "title": "Random State",
        "summary": "Pseudo-random number generators, seed settings, and ML reproducibility.",
        "theory": [
            "### Deterministic Pseudo-Randomness\n",
            "Standardizes model weight initialization and data split indices to allow comparative experimentation."
        ],
        "code": [
            "import numpy as np\n",
            "\n",
            "np.random.seed(42)\n",
            "arr1 = np.random.rand(3)\n",
            "np.random.seed(42)\n",
            "arr2 = np.random.rand(3)\n",
            "print('Array 1:', arr1)\n",
            "print('Array 2 (using same seed):', arr2)\n",
            "print('Are arrays identical?:', np.allclose(arr1, arr2))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is it crucial to set a fixed random state during experimental testing?"
        ],
        "exercise_code": [
            "print('Setting random state ensures reproducibility, so that model accuracy improvements are due to code/parameter changes rather than random split differences.')\n"
        ]
    },
    15: {
        "title": "Accuracy Score explained",
        "summary": "Mathematical calculation of accuracy, binary vs multiclass accuracy, and limits on unbalanced data.",
        "theory": [
            "### Accuracy Math\n",
            "Accuracy = $\\frac{TP + TN}{TP + TN + FP + FN}$"
        ],
        "code": [
            "from sklearn.metrics import accuracy_score\n",
            "import numpy as np\n",
            "\n",
            "y_true = np.array([0, 1, 2, 0, 1, 2])\n",
            "y_pred = np.array([0, 1, 1, 0, 1, 2])\n",
            "print('Calculated accuracy score:', accuracy_score(y_true, y_pred))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Express accuracy calculation manually in Python."
        ],
        "exercise_code": [
            "manual_acc = np.mean(y_true == y_pred)\n",
            "print('Manual Accuracy calculation:', manual_acc)\n"
        ]
    },
    16: {
        "title": "Steps to build any ML model",
        "summary": "Detailed step-by-step checklist of end-to-end ML workflows.",
        "theory": [
            "### ML Process Lifecycle\n",
            "1. Ingestion, 2. EDA, 3. Split, 4. Feature Selection/Engineering, 5. Baselines, 6. Hyperparameter Tuning, 7. Final Evaluation."
        ],
        "code": [
            "import pandas as pd\n",
            "from sklearn.datasets import load_iris\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "\n",
            "iris = load_iris()\n",
            "X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)\n",
            "model = RandomForestClassifier(random_state=42).fit(X_train, y_train)\n",
            "print('Built pipeline score:', model.score(X_test, y_test))\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Describe the purpose of a baseline model."
        ],
        "exercise_code": [
            "print('A baseline model provides a simple, standard benchmark performance level (e.g., majority class prediction or simple linear model) that complex models must beat.')\n"
        ]
    },
    17: {
        "title": "Stanford CS229 Lec 12: Debugging ML and Error Analysis",
        "summary": "Learning curves, diagnosing bias vs variance, and error analysis.",
        "theory": [
            "### Learning Diagnostics\n",
            "- **High Bias (Underfitting):** Train and test errors are high and close. Getting more data will not help.\n",
            "- **High Variance (Overfitting):** Large gap between train (low) and test (high) errors. Getting more data helps."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.model_selection import learning_curve\n",
            "from sklearn.linear_model import Ridge\n",
            "from sklearn.datasets import make_regression\n",
            "\n",
            "X, y = make_regression(n_samples=150, n_features=10, noise=5.0, random_state=42)\n",
            "train_sizes, train_scores, test_scores = learning_curve(\n",
            "    Ridge(alpha=10.0), X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10), scoring='neg_mean_squared_error', random_state=42\n",
            ")\n",
            "\n",
            "train_rmse = np.sqrt(-np.mean(train_scores, axis=1))\n",
            "test_rmse = np.sqrt(-np.mean(test_scores, axis=1))\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "plt.plot(train_sizes, train_rmse, 'b-o', label='Training Error')\n",
            "plt.plot(train_sizes, test_rmse, 'r-o', label='Validation Error')\n",
            "plt.xlabel('Training Set Size')\n",
            "plt.ylabel('RMSE Error')\n",
            "plt.title('Learning Curves (Diagnosing Bias vs Variance)')\n",
            "plt.legend()\n",
            "plt.grid(True)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Describe how to resolve a High Variance issue diagnosed from learning curves."
        ],
        "exercise_code": [
            "print('High Variance can be resolved by getting more training data, reducing the feature space, increasing regularization, or simplifying the model architecture.')\n"
        ]
    }
}



PHASE_10_NOTEBOOK_CONTENTS = {
    1: {
        "title": "PCA Part 1: Geometric intuition",
        "summary": "Geometric intuition behind Principal Component Analysis: maximizing variance and minimizing projection error.",
        "theory": [
            "### Principal Component Analysis (PCA) Intuition\n",
            "PCA seeks to find a linear projection of high-dimensional data into a lower-dimensional subspace such that:\n",
            "1. **Variance is Maximized**: The projected data retains as much spread (information) as possible.\n",
            "2. **Projection Error is Minimized**: The orthogonal distance from the original points to the projection subspace is minimized.\n",
            "These two objectives are mathematically equivalent."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import load_iris\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "from sklearn.decomposition import PCA\n",
            "\n",
            "# 1. Load real data (Iris) and pick 2 features for 2D visualization\n",
            "X = load_iris().data[:, :2] # Sepal length and width\n",
            "X_scaled = StandardScaler().fit_transform(X)\n",
            "\n",
            "# 2. Apply PCA to find the 1st principal component\n",
            "pca = PCA(n_components=1)\n",
            "pca.fit(X_scaled)\n",
            "\n",
            "# 3. Plot original data and the principal component vector\n",
            "plt.figure(figsize=(8, 6))\n",
            "plt.scatter(X_scaled[:, 0], X_scaled[:, 1], alpha=0.5, label='Standardized Data')\n",
            "\n",
            "# Draw the principal component axis\n",
            "mean = np.mean(X_scaled, axis=0)\n",
            "vector = pca.components_[0] * 3  # Scale for visibility\n",
            "plt.plot([mean[0] - vector[0], mean[0] + vector[0]], \n",
            "         [mean[1] - vector[1], mean[1] + vector[1]], \n",
            "         color='red', linewidth=3, label='1st Principal Component (Max Variance)')\n",
            "\n",
            "plt.title('PCA Geometric Intuition (Iris Dataset)')\n",
            "plt.xlabel('Sepal Length (Standardized)')\n",
            "plt.ylabel('Sepal Width (Standardized)')\n",
            "plt.axis('equal')\n",
            "plt.grid(True, linestyle='--')\n",
            "plt.legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is it important to standardize the data before applying PCA?"
        ],
        "exercise_code": [
            "print('PCA is sensitive to scale. Since it maximizes variance, features with naturally larger numeric scales will artificially dominate the principal components if not standardized.')\n"
        ]
    },
    2: {
        "title": "PCA Part 2: Math and step by step",
        "summary": "Mathematical derivation of PCA: Covariance matrix and Eigendecomposition.",
        "theory": [
            "### The Mathematics of PCA (5 Steps)\n",
            "1. **Standardize the dataset**: $Z = \\frac{X - \\mu}{\\sigma}$\n",
            "2. **Compute Covariance Matrix**: $\\Sigma = \\frac{1}{n-1} Z^T Z$\n",
            "3. **Compute Eigendecomposition**: $\\Sigma v = \\lambda v$ (where $\\lambda$ are eigenvalues, $v$ are eigenvectors).\n",
            "4. **Sort Eigenpairs**: Sort eigenvectors by descending eigenvalues to rank them by explained variance.\n",
            "5. **Projection Matrix**: Select the top $k$ eigenvectors to form matrix $W$, and project data: $X_{pca} = Z W$."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "from sklearn.datasets import load_wine\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "\n",
            "# 1. Load and Standardize Wine Dataset (13 features)\n",
            "X, y = load_wine(return_X_y=True)\n",
            "Z = StandardScaler().fit_transform(X)\n",
            "\n",
            "# 2. Compute Covariance Matrix\n",
            "cov_matrix = np.cov(Z.T)\n",
            "\n",
            "# 3 & 4. Eigendecomposition and Sorting\n",
            "eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)\n",
            "sorted_idx = np.argsort(eigenvalues)[::-1]\n",
            "sorted_eigenvalues = eigenvalues[sorted_idx]\n",
            "\n",
            "# Visualizations\n",
            "fig, ax = plt.subplots(1, 2, figsize=(14, 5))\n",
            "\n",
            "# Heatmap of Covariance Matrix\n",
            "sns.heatmap(cov_matrix, cmap='coolwarm', ax=ax[0], square=True)\n",
            "ax[0].set_title('Feature Covariance Matrix Heatmap')\n",
            "\n",
            "# Scree Plot of Eigenvalues\n",
            "ax[1].plot(range(1, 14), sorted_eigenvalues, 'bo-', linewidth=2)\n",
            "ax[1].set_title('Scree Plot (Eigenvalues)')\n",
            "ax[1].set_xlabel('Principal Component Rank')\n",
            "ax[1].set_ylabel('Eigenvalue (Magnitude of Variance)')\n",
            "ax[1].grid(True, linestyle=':')\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What does the eigenvector associated with the largest eigenvalue represent?"
        ],
        "exercise_code": [
            "print('It represents the 1st Principal Component, which is the direction in the feature space that captures the absolute maximum variance of the dataset.')\n"
        ]
    },
    3: {
        "title": "PCA Part 3: Code and visualization",
        "summary": "Applying PCA using scikit-learn for image compression and variance analysis.",
        "theory": [
            "### Cumulative Explained Variance & Dimensionality Reduction\n",
            "We evaluate how many components to keep by looking at the **Cumulative Explained Variance Ratio**. We can use PCA to compress high-dimensional images (like 64-pixel digits) into a tiny fraction of their original size while retaining visual structure."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "from sklearn.datasets import load_digits\n",
            "from sklearn.decomposition import PCA\n",
            "\n",
            "# Load MNIST digits (8x8 images = 64 dimensions)\n",
            "digits = load_digits()\n",
            "X = digits.data\n",
            "\n",
            "# Fit PCA without reducing dimensionality to see variance ratio\n",
            "pca_full = PCA().fit(X)\n",
            "cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_)\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "plt.plot(cumulative_variance, color='purple', linewidth=2)\n",
            "plt.axhline(y=0.90, color='r', linestyle='--', label='90% Variance Threshold')\n",
            "plt.xlabel('Number of Components')\n",
            "plt.ylabel('Cumulative Explained Variance')\n",
            "plt.title('Explained Variance vs Components (Digits Dataset)')\n",
            "plt.legend()\n",
            "plt.grid(True)\n",
            "plt.show()\n",
            "\n",
            "# Image Compression Example\n",
            "pca_reduced = PCA(n_components=15) # Retain 15 dims out of 64\n",
            "X_reduced = pca_reduced.fit_transform(X)\n",
            "X_reconstructed = pca_reduced.inverse_transform(X_reduced)\n",
            "\n",
            "fig, axes = plt.subplots(1, 2, figsize=(6, 3))\n",
            "axes[0].imshow(X[0].reshape(8, 8), cmap='gray')\n",
            "axes[0].set_title('Original (64 Dims)')\n",
            "axes[0].axis('off')\n",
            "\n",
            "axes[1].imshow(X_reconstructed[0].reshape(8, 8), cmap='gray')\n",
            "axes[1].set_title('Compressed (15 Dims)')\n",
            "axes[1].axis('off')\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Explain why `pca.inverse_transform()` yields an image that looks slightly blurry compared to the original."
        ],
        "exercise_code": [
            "print('The inverse transform attempts to reconstruct the 64-pixel image using only the 15 retained principal components. The blurry artifacts represent the information (variance) that was permanently discarded in the other 49 components.')\n"
        ]
    },
    4: {
        "title": "Stanford CS229 Lec 15: PCA and ICA",
        "summary": "Independent Component Analysis (ICA) vs Principal Component Analysis (PCA) and the Cocktail Party Problem.",
        "theory": [
            "### PCA vs ICA\n",
            "- **PCA (Principal Component Analysis):** Finds orthogonal directions of maximum variance. Assumes features are Gaussian-distributed.\n",
            "- **ICA (Independent Component Analysis):** Finds a non-orthogonal linear transformation that minimizes statistical dependence between components. Assumes features are **Non-Gaussian**. Used extensively to solve the *Blind Source Separation (Cocktail Party) Problem*."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from scipy import signal\n",
            "from sklearn.decomposition import FastICA, PCA\n",
            "\n",
            "# Generate 2 Independent Sources (Sine and Sawtooth)\n",
            "np.random.seed(42)\n",
            "time = np.linspace(0, 8, 2000)\n",
            "s1 = np.sin(2 * time)  # Signal 1\n",
            "s2 = signal.sawtooth(2 * np.pi * time)  # Signal 2\n",
            "S = np.c_[s1, s2]\n",
            "\n",
            "# Mix Data\n",
            "A = np.array([[1, 1], [0.5, 2]])  # Mixing matrix\n",
            "X = np.dot(S, A.T)  # Mixed signals observation\n",
            "\n",
            "# Apply PCA and ICA\n",
            "pca = PCA(n_components=2)\n",
            "H_pca = pca.fit_transform(X)  # PCA fails to separate independent non-gaussian sources\n",
            "\n",
            "ica = FastICA(n_components=2, random_state=42, whiten='unit-variance')\n",
            "H_ica = ica.fit_transform(X)  # ICA isolates the independent sources\n",
            "\n",
            "models = [X, S, H_pca, H_ica]\n",
            "names = ['Mixed Observations', 'True Sources', 'PCA Recovered', 'ICA Recovered']\n",
            "colors = ['red', 'steelblue']\n",
            "\n",
            "fig, axes = plt.subplots(4, 1, figsize=(8, 8), sharex=True)\n",
            "for i, (model, name) in enumerate(zip(models, names)):\n",
            "    axes[i].set_title(name)\n",
            "    for sig, color in zip(model.T, colors):\n",
            "        axes[i].plot(sig, color=color)\n",
            "\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why does PCA fail to recover the original signals in the Cocktail Party problem?"
        ],
        "exercise_code": [
            "print('PCA only looks for orthogonal directions of highest variance. Independent source signals in audio are usually non-orthogonal and non-Gaussian. PCA completely ignores higher-order statistical independence, blending the signals together.')\n"
        ]
    },
    5: {
        "title": "PCA explained",
        "summary": "Addressing PCA limitations, non-linear manifolds, and comparing to Kernel PCA.",
        "theory": [
            "### Limitations of Linear PCA\n",
            "PCA is strictly a **linear** transformation. If the data lies on a complex, non-linear manifold (like a sphere, spiral, or nested rings), standard PCA cannot unroll or unfold the data. It will simply crush the data onto a flat hyperplane.\n",
            "In such cases, non-linear techniques like **Kernel PCA**, **t-SNE**, or **UMAP** are required."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import make_moons\n",
            "from sklearn.decomposition import PCA, KernelPCA\n",
            "\n",
            "# Generate Non-Linear data (Moons)\n",
            "X, y = make_moons(n_samples=200, noise=0.05, random_state=42)\n",
            "\n",
            "# Standard PCA\n",
            "pca = PCA(n_components=2)\n",
            "X_pca = pca.fit_transform(X)\n",
            "\n",
            "# Kernel PCA (RBF)\n",
            "kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15)\n",
            "X_kpca = kpca.fit_transform(X)\n",
            "\n",
            "fig, ax = plt.subplots(1, 3, figsize=(15, 4))\n",
            "\n",
            "ax[0].scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')\n",
            "ax[0].set_title('Original Non-Linear Data')\n",
            "\n",
            "ax[1].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolors='k')\n",
            "ax[1].set_title('Standard PCA (Linear Failure)')\n",
            "\n",
            "ax[2].scatter(X_kpca[:, 0], X_kpca[:, 1], c=y, cmap='viridis', edgecolors='k')\n",
            "ax[2].set_title('Kernel PCA (RBF Unfolding)')\n",
            "\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What is the fundamental mechanism behind Kernel PCA that allows it to separate non-linear data?"
        ],
        "exercise_code": [
            "print('Kernel PCA uses the kernel trick to implicitly map the data into an extremely high-dimensional space where the non-linear manifold becomes linearly separable, and then performs standard PCA in that space.')\n"
        ]
    },
    6: {
        "title": "LDA",
        "summary": "Linear Discriminant Analysis: Supervised dimensionality reduction.",
        "theory": [
            "### PCA vs LDA\n",
            "- **PCA:** Unsupervised. Finds axes that maximize total variance, ignoring class labels.\n",
            "- **LDA (Linear Discriminant Analysis):** Supervised. Finds axes that maximize the separation (distance) between multiple classes while minimizing the variance within each class."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import load_wine\n",
            "from sklearn.decomposition import PCA\n",
            "from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "\n",
            "# Load 13-feature Wine dataset\n",
            "X, y = load_wine(return_X_y=True)\n",
            "X_scaled = StandardScaler().fit_transform(X)\n",
            "\n",
            "# Apply Unsupervised PCA\n",
            "pca = PCA(n_components=2)\n",
            "X_pca = pca.fit_transform(X_scaled)\n",
            "\n",
            "# Apply Supervised LDA\n",
            "lda = LDA(n_components=2)\n",
            "X_lda = lda.fit_transform(X_scaled, y)\n",
            "\n",
            "fig, ax = plt.subplots(1, 2, figsize=(12, 5))\n",
            "\n",
            "scatter1 = ax[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='Set1', edgecolors='k')\n",
            "ax[0].set_title('PCA Projection (Unsupervised)')\n",
            "ax[0].set_xlabel('Principal Component 1')\n",
            "ax[0].set_ylabel('Principal Component 2')\n",
            "\n",
            "scatter2 = ax[1].scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='Set1', edgecolors='k')\n",
            "ax[1].set_title('LDA Projection (Supervised)')\n",
            "ax[1].set_xlabel('Linear Discriminant 1')\n",
            "ax[1].set_ylabel('Linear Discriminant 2')\n",
            "\n",
            "plt.suptitle('PCA vs LDA on Wine Dataset', fontsize=14, fontweight='bold')\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is the maximum number of components in LDA strictly constrained by the number of classes?"
        ],
        "exercise_code": [
            "print('LDA projects data onto the subspace spanned by the class means. If there are C classes, they span at most a (C-1) dimensional subspace. Therefore, max components = C - 1.')\n"
        ]
    },
    7: {
        "title": "Feature Importance",
        "summary": "Reducing dimensionality explicitly by dropping least important features using tree-based analysis.",
        "theory": [
            "### Feature Selection as Dimensionality Reduction\n",
            "Instead of mathematically transforming features (like PCA/LDA), we can simply discard irrelevant ones based on model evaluation.\n",
            "- **Gini/Impurity Importance:** Provided directly by Random Forests. Fast, but biased towards high-cardinality features.\n",
            "- **Permutation Importance:** Model-agnostic. Evaluates how much validation score drops when a feature column is randomly shuffled."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import numpy as np\n",
            "from sklearn.datasets import load_breast_cancer\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "data = load_breast_cancer()\n",
            "X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)\n",
            "\n",
            "clf = RandomForestClassifier(n_estimators=100, random_state=42)\n",
            "clf.fit(X_train, y_train)\n",
            "\n",
            "# Extract top 10 important features\n",
            "importances = clf.feature_importances_\n",
            "indices = np.argsort(importances)[-10:] # Top 10\n",
            "\n",
            "plt.figure(figsize=(8, 5))\n",
            "plt.barh(range(len(indices)), importances[indices], color='mediumseagreen', align='center')\n",
            "plt.yticks(range(len(indices)), [data.feature_names[i] for i in indices])\n",
            "plt.xlabel('Relative Feature Importance (Gini)')\n",
            "plt.title('Top 10 Features (Breast Cancer Dataset)')\n",
            "plt.grid(axis='x', linestyle='--', alpha=0.7)\n",
            "plt.tight_layout()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Name one advantage of Feature Selection over PCA."
        ],
        "exercise_code": [
            "print('Feature selection preserves the original meaning and units of the features (interpretability). PCA creates new features that are mathematical linear combinations, making them difficult to interpret in business or medical contexts.')\n"
        ]
    }
}



PHASE_11_NOTEBOOK_CONTENTS = {
    1: {
        "title": "Intro to Ensemble Learning",
        "summary": "The wisdom of the crowd: aggregating predictions to improve performance.",
        "theory": [
            "### Ensemble Learning\n",
            "Ensemble learning relies on the **Wisdom of the Crowd**. By aggregating the predictions of a group of diverse, moderately performing predictors (weak learners), we can often construct a single strong learner.\n",
            "For this to work effectively, the models should be as **independent** as possible (making different types of errors)."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "\n",
            "# Simulating the Law of Large Numbers for Ensembles\n",
            "coin_tosses = (np.random.rand(10000, 10) < 0.51).astype(int) # 51% biased coin\n",
            "cumulative_heads_ratio = np.cumsum(coin_tosses, axis=0) / np.arange(1, 10001).reshape(-1, 1)\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "plt.plot(cumulative_heads_ratio[:, 0], label='1 Weak Learner (Coin)')\n",
            "plt.plot(cumulative_heads_ratio[:, 1:4], alpha=0.5)\n",
            "plt.axhline(y=0.51, color='k', linestyle='--', label='51% Probability')\n",
            "plt.axhline(y=0.50, color='r', linestyle='--', label='50% Boundary')\n",
            "plt.title('Law of Large Numbers in Ensembles')\n",
            "plt.xlabel('Number of Tosses (or Trees)')\n",
            "plt.ylabel('Heads Ratio')\n",
            "plt.legend()\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is diversity among the models important in an ensemble?"
        ],
        "exercise_code": [
            "print('If all models are identical, they will make the exact same errors. Diversity ensures their errors are uncorrelated, allowing the majority vote to correct individual mistakes.')\n"
        ]
    },
    2: {
        "title": "Stanford CS229 Lec 9: Decision Trees and Ensemble theory",
        "summary": "Notes on the theoretical foundations of Ensembles based on Stanford CS229.",
        "theory": [
            "### Ensemble Theory (Stanford CS229)\n",
            "- **Bias-Variance Decomposition:** Error = Bias + Variance + Noise.\n",
            "- **Bagging (Bootstrap Aggregation):** Reduces **Variance** without increasing bias by averaging independent models trained on bootstrap samples.\n",
            "- **Boosting:** Reduces **Bias** (and often variance) by sequentially training models to correct the errors of previous ones."
        ],
        "code": [
            "print('Ensembles inherently manipulate the Bias-Variance tradeoff.')\n",
            "print('- Complex Trees: High Variance, Low Bias -> Bagging fixes Variance.')\n",
            "print('- Shallow Stumps: High Bias, Low Variance -> Boosting fixes Bias.')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Does bagging work well with linear regression?"
        ],
        "exercise_code": [
            "print('Not very well. Linear regression is a stable, low-variance model. Bagging only provides significant improvements on unstable, high-variance models like unpruned Decision Trees.')\n"
        ]
    },
    3: {
        "title": "Voting Classifier: Hard and Soft",
        "summary": "Implementing Hard (majority) and Soft (probability) Voting classifiers.",
        "theory": [
            "### Hard vs Soft Voting\n",
            "- **Hard Voting:** Each classifier gets 1 vote for a class. The class with the most votes wins.\n",
            "- **Soft Voting:** Each classifier outputs a probability. The ensemble averages the probabilities and picks the class with the highest average. (Requires classifiers that support `predict_proba`)."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import make_moons\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.ensemble import RandomForestClassifier, VotingClassifier\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "from sklearn.svm import SVC\n",
            "from sklearn.metrics import accuracy_score\n",
            "\n",
            "X, y = make_moons(n_samples=500, noise=0.30, random_state=42)\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)\n",
            "\n",
            "log_clf = LogisticRegression(random_state=42)\n",
            "rnd_clf = RandomForestClassifier(random_state=42)\n",
            "svm_clf = SVC(probability=True, random_state=42)\n",
            "\n",
            "voting_clf = VotingClassifier(\n",
            "    estimators=[('lr', log_clf), ('rf', rnd_clf), ('svc', svm_clf)],\n",
            "    voting='soft'\n",
            ")\n",
            "\n",
            "for clf in (log_clf, rnd_clf, svm_clf, voting_clf):\n",
            "    clf.fit(X_train, y_train)\n",
            "    y_pred = clf.predict(X_test)\n",
            "    print(f'{clf.__class__.__name__:25s} Accuracy: {accuracy_score(y_test, y_pred):.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why does Soft Voting usually achieve higher performance than Hard Voting?"
        ],
        "exercise_code": [
            "print('Soft voting gives more weight to highly confident votes. If a model is 99% sure, it carries more mathematical weight than a model that is only 51% sure.')\n"
        ]
    },
    4: {
        "title": "Voting Regressor",
        "summary": "Combining multiple regression models.",
        "theory": [
            "### Voting Regressor\n",
            "In regression, voting implies averaging the numerical predictions of all the base estimators."
        ],
        "code": [
            "from sklearn.datasets import fetch_california_housing\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.ensemble import VotingRegressor, RandomForestRegressor\n",
            "from sklearn.linear_model import LinearRegression\n",
            "from sklearn.tree import DecisionTreeRegressor\n",
            "from sklearn.metrics import mean_squared_error\n",
            "\n",
            "data = fetch_california_housing()\n",
            "X_train, X_test, y_train, y_test = train_test_split(data.data[:1000], data.target[:1000], random_state=42)\n",
            "\n",
            "reg1 = LinearRegression()\n",
            "reg2 = RandomForestRegressor(random_state=42, n_estimators=50)\n",
            "reg3 = DecisionTreeRegressor(random_state=42, max_depth=5)\n",
            "\n",
            "ereg = VotingRegressor(estimators=[('lr', reg1), ('rf', reg2), ('dt', reg3)])\n",
            "ereg.fit(X_train, y_train)\n",
            "reg1.fit(X_train, y_train) # Fit standalone reg1 so we can compare its prediction\n",
            "\n",
            "print(f'Linear Reg MSE: {mean_squared_error(y_test, reg1.predict(X_test)):.3f}')\n",
            "print(f'Voting Reg MSE: {mean_squared_error(y_test, ereg.predict(X_test)):.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Can a Voting Regressor perform worse than its best individual estimator?"
        ],
        "exercise_code": [
            "print('Yes, if the other estimators in the ensemble are extremely poor, their predictions will drag the average down.')\n"
        ]
    },
    5: {
        "title": "Bagging full series",
        "summary": "Bootstrap Aggregation applied to decision trees.",
        "theory": [
            "### Bagging (Bootstrap Aggregation)\n",
            "1. **Bootstrap**: Sample the training set with replacement to create $m$ different training sets.\n",
            "2. **Aggregation**: Train a base estimator on each subset. Average their predictions (regression) or take majority vote (classification)."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import make_circles\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.ensemble import BaggingClassifier\n",
            "from sklearn.tree import DecisionTreeClassifier\n",
            "from sklearn.metrics import accuracy_score\n",
            "\n",
            "X, y = make_circles(n_samples=500, factor=0.5, noise=0.25, random_state=42)\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)\n",
            "\n",
            "tree_clf = DecisionTreeClassifier(random_state=42)\n",
            "bag_clf = BaggingClassifier(\n",
            "    DecisionTreeClassifier(random_state=42),\n",
            "    n_estimators=100, max_samples=100, bootstrap=True, random_state=42\n",
            ")\n",
            "\n",
            "tree_clf.fit(X_train, y_train)\n",
            "bag_clf.fit(X_train, y_train)\n",
            "\n",
            "print(f'Single Tree Accuracy: {accuracy_score(y_test, tree_clf.predict(X_test)):.3f}')\n",
            "print(f'Bagging Accuracy:     {accuracy_score(y_test, bag_clf.predict(X_test)):.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What is the difference between Pasting and Bagging?"
        ],
        "exercise_code": [
            "print('Bagging samples the training data WITH replacement. Pasting samples the training data WITHOUT replacement.')\n"
        ]
    },
    6: {
        "title": "Random Forest intuition and bias variance",
        "summary": "Random Forest = Bagging + Random Feature Selection.",
        "theory": [
            "### Random Forest Intuition\n",
            "A Random Forest is fundamentally a Bagging ensemble of Decision Trees. However, it introduces an extra layer of randomness: when splitting a node, it only considers a **random subset of features** (usually $\\sqrt{n}$).\n",
            "This forces the trees to be even more uncorrelated, which drastically reduces Variance at the cost of a slight increase in Bias."
        ],
        "code": [
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.datasets import load_wine\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "X, y = load_wine(return_X_y=True)\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)\n",
            "\n",
            "rf_clf = RandomForestClassifier(n_estimators=100, max_leaf_nodes=16, random_state=42)\n",
            "rf_clf.fit(X_train, y_train)\n",
            "\n",
            "print(f'Random Forest Accuracy on Wine: {rf_clf.score(X_test, y_test):.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why restrict the number of features considered at each split?"
        ],
        "exercise_code": [
            "print('If you do not restrict features, the strongest predictive feature will be chosen at the root node of almost every tree, making all the trees highly correlated and identical at the top. Restricting features forces trees to use secondary features, ensuring diversity.')\n"
        ]
    },
    7: {
        "title": "Bagging vs Random Forest",
        "summary": "Comparing explicit BaggingClassifier with RandomForestClassifier.",
        "theory": [
            "### Bagging vs Random Forest\n",
            "In Scikit-Learn, `RandomForestClassifier` is heavily optimized. It is functionally identical to using a `BaggingClassifier` wrapping `DecisionTreeClassifier(splitter='best')`, but with `max_features` restricted."
        ],
        "code": [
            "from sklearn.ensemble import BaggingClassifier, RandomForestClassifier\n",
            "from sklearn.tree import DecisionTreeClassifier\n",
            "\n",
            "bag_clf = BaggingClassifier(\n",
            "    DecisionTreeClassifier(max_features='sqrt', max_leaf_nodes=16),\n",
            "    n_estimators=100, random_state=42\n",
            ")\n",
            "\n",
            "rf_clf = RandomForestClassifier(n_estimators=100, max_leaf_nodes=16, random_state=42)\n",
            "print('Both approaches yield highly similar functional ensembles under the hood.')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. When would you use BaggingClassifier instead of RandomForestClassifier?"
        ],
        "exercise_code": [
            "print('If you want to bag an algorithm that is NOT a decision tree (e.g., Bagging SVMs or Bagging Logistic Regressions), you must use BaggingClassifier.')\n"
        ]
    },
    8: {
        "title": "Random Forest hyperparameters and tuning",
        "summary": "Tuning `n_estimators`, `max_depth`, and `max_features`.",
        "theory": [
            "### Tuning Random Forests\n",
            "- `n_estimators`: More trees = less variance, but diminishing returns and slower training.\n",
            "- `max_depth`: Limits tree size, prevents overfitting.\n",
            "- `max_features`: Smaller values = less variance, more bias."
        ],
        "code": [
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.model_selection import GridSearchCV\n",
            "from sklearn.datasets import load_breast_cancer\n",
            "\n",
            "X, y = load_breast_cancer(return_X_y=True)\n",
            "\n",
            "param_grid = {\n",
            "    'n_estimators': [50, 100],\n",
            "    'max_depth': [None, 5, 10],\n",
            "    'max_features': ['sqrt', 'log2']\n",
            "}\n",
            "\n",
            "rf = RandomForestClassifier(random_state=42)\n",
            "grid_search = GridSearchCV(rf, param_grid, cv=3, n_jobs=-1)\n",
            "grid_search.fit(X, y)\n",
            "\n",
            "print(f'Best Parameters: {grid_search.best_params_}')\n",
            "print(f'Best CV Score: {grid_search.best_score_:.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Can you overfit a Random Forest by adding too many trees (`n_estimators`)?"
        ],
        "exercise_code": [
            "print('No. Because trees are averaged, adding more trees mathematically converges the variance. It will never overfit just by adding more trees (it just wastes compute). Overfitting in RF comes from tree depth.')\n"
        ]
    },
    9: {
        "title": "OOB Score",
        "summary": "Out-of-Bag Evaluation for Bagged ensembles.",
        "theory": [
            "### Out-of-Bag (OOB) Evaluation\n",
            "In bagging with replacement, on average, a tree only sees about 63% of the training instances. The remaining 37% are **out-of-bag (OOB)**.\n",
            "Since the tree never saw these instances during training, we can use them as an automatic validation set without needing a separate validation split!"
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.datasets import make_classification\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore') # Suppress OOB warnings for low tree counts\n",
            "\n",
            "X, y = make_classification(n_samples=500, n_features=10, random_state=42)\n",
            "\n",
            "oob_scores = []\n",
            "n_estimators_range = range(20, 150, 10)\n",
            "\n",
            "for n in n_estimators_range:\n",
            "    rf = RandomForestClassifier(n_estimators=n, oob_score=True, random_state=42, n_jobs=-1)\n",
            "    rf.fit(X, y)\n",
            "    oob_scores.append(rf.oob_score_)\n",
            "\n",
            "plt.plot(n_estimators_range, oob_scores, marker='o', color='teal')\n",
            "plt.title('OOB Accuracy vs Number of Trees')\n",
            "plt.xlabel('n_estimators')\n",
            "plt.ylabel('OOB Score')\n",
            "plt.grid(True)\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why does the OOB score curve flatten out as `n_estimators` increases?"
        ],
        "exercise_code": [
            "print('As the forest grows, the variance reduction from averaging converges. Additional trees provide negligible improvement to the ensemble decision boundary.')\n"
        ]
    },
    10: {
        "title": "Feature Importance using RF and DT",
        "summary": "Evaluating feature importance internally through Gini reduction.",
        "theory": [
            "### Feature Importance\n",
            "Random Forests measure how much a feature reduces impurity (Gini/Entropy) across all nodes in all trees. It is a fast, built-in way to perform Feature Selection."
        ],
        "code": [
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "from sklearn.datasets import load_breast_cancer\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "\n",
            "data = load_breast_cancer()\n",
            "rf = RandomForestClassifier(n_estimators=100, random_state=42)\n",
            "rf.fit(data.data, data.target)\n",
            "\n",
            "importances = rf.feature_importances_\n",
            "indices = np.argsort(importances)[-8:] # Top 8 features\n",
            "\n",
            "plt.figure(figsize=(8, 4))\n",
            "plt.barh(range(len(indices)), importances[indices], color='darkorange')\n",
            "plt.yticks(range(len(indices)), [data.feature_names[i] for i in indices])\n",
            "plt.title('Random Forest Feature Importances')\n",
            "plt.show()\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What is a key flaw of Random Forest Gini importance?"
        ],
        "exercise_code": [
            "print('It is biased towards high-cardinality continuous features. Permutation importance is usually a better, unbiased metric.')\n"
        ]
    },
    11: {
        "title": "AdaBoost intuition and math and code",
        "summary": "Adaptive Boosting: learning from past mistakes by updating instance weights.",
        "theory": [
            "### AdaBoost (Adaptive Boosting)\n",
            "Unlike Bagging (which is parallel), Boosting is **sequential**. AdaBoost pays attention to training instances that the previous predictor underfitted.\n",
            "It does this by increasing the relative weight of misclassified instances. The next predictor is forced to focus on these hard cases."
        ],
        "code": [
            "import matplotlib.pyplot as plt\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore') # Suppress FutureWarning for AdaBoost defaults\n",
            "from sklearn.ensemble import AdaBoostClassifier\n",
            "from sklearn.tree import DecisionTreeClassifier\n",
            "from sklearn.datasets import make_moons\n",
            "\n",
            "X, y = make_moons(n_samples=300, noise=0.25, random_state=42)\n",
            "\n",
            "ada_clf = AdaBoostClassifier(\n",
            "    DecisionTreeClassifier(max_depth=1), n_estimators=50,\n",
            "    learning_rate=0.5, random_state=42\n",
            ")\n",
            "ada_clf.fit(X, y)\n",
            "\n",
            "print(f'AdaBoost Accuracy: {ada_clf.score(X, y):.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why are decision stumps (depth=1) often used as the base estimator for AdaBoost?"
        ],
        "exercise_code": [
            "print('Because boosting drastically reduces bias. If you start with a high-variance tree, boosting will overfit horribly. Stumps have extremely high bias, making them perfect candidates for boosting.')\n"
        ]
    },
    12: {
        "title": "Bagging vs Boosting",
        "summary": "Comparing parallel Variance-reduction vs sequential Bias-reduction.",
        "theory": [
            "### Bagging vs Boosting\n",
            "- **Bagging:** Parallel. Each model is built independently. Fixes Variance. Prevents Overfitting. Use complex trees.\n",
            "- **Boosting:** Sequential. Each model corrects the previous model's errors. Fixes Bias. Prone to Overfitting. Use simple stumps."
        ],
        "code": [
            "print('Bagging = Democracy (Averaging distinct opinions)')\n",
            "print('Boosting = Assembly Line (Each worker fixes the defects left by the previous worker)')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. If a model is severely overfitting the training data, which ensemble method is most appropriate?"
        ],
        "exercise_code": [
            "print('Bagging (e.g., Random Forest). Bagging reduces variance and helps prevent overfitting, whereas Boosting reduces bias and can exacerbate overfitting on noisy data.')\n"
        ]
    },
    13: {
        "title": "Boosting implementation",
        "summary": "Understanding Gradient Boosting concepts conceptually.",
        "theory": [
            "### How Gradient Boosting Works\n",
            "Instead of tweaking instance weights like AdaBoost, Gradient Boosting tries to fit the new predictor to the **residual errors** made by the previous predictor."
        ],
        "code": [
            "print('1. Fit Tree1 on (X, y)')\n",
            "print('2. Calculate residuals: y2 = y - Tree1(X)')\n",
            "print('3. Fit Tree2 on (X, y2)')\n",
            "print('4. Final Prediction = Tree1(X) + Tree2(X)')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. In Gradient Boosting, what exactly is the target variable for the second tree in the ensemble?"
        ],
        "exercise_code": [
            "print('The target variable for the second tree is the residual error (the difference between the actual label and the prediction of the first tree).')\n"
        ]
    },
    14: {
        "title": "Gradient Boosting full series",
        "summary": "Gradient Boosting Regressors and early stopping.",
        "theory": [
            "### Gradient Boosting in Scikit-Learn\n",
            "The `GradientBoostingRegressor` fits regression trees on the negative gradient of the loss function (residuals)."
        ],
        "code": [
            "from sklearn.ensemble import GradientBoostingRegressor\n",
            "from sklearn.datasets import fetch_california_housing\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.metrics import mean_squared_error\n",
            "\n",
            "data = fetch_california_housing()\n",
            "X_train, X_test, y_train, y_test = train_test_split(data.data[:1000], data.target[:1000], random_state=42)\n",
            "\n",
            "gbrt = GradientBoostingRegressor(max_depth=2, n_estimators=100, learning_rate=0.1, random_state=42)\n",
            "gbrt.fit(X_train, y_train)\n",
            "\n",
            "print(f'GBRT MSE: {mean_squared_error(y_test, gbrt.predict(X_test)):.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What is the effect of lowering the learning rate in Gradient Boosting?"
        ],
        "exercise_code": [
            "print('Lowering the learning rate shrinks the contribution of each tree. You will need more trees (n_estimators) to fit the data, but it usually generalizes better.')\n"
        ]
    },
    15: {
        "title": "XGBoost full series",
        "summary": "Extreme Gradient Boosting: The Kaggle King.",
        "theory": [
            "### XGBoost (eXtreme Gradient Boosting)\n",
            "An optimized, highly scalable implementation of Gradient Boosting. It includes:\n",
            "1. System optimization (cache awareness, parallelization).\n",
            "2. Regularization (L1/L2 penalties) to prevent overfitting.\n",
            "3. Built-in handling for missing values."
        ],
        "code": [
            "import xgboost as xgb\n",
            "from sklearn.datasets import fetch_california_housing\n",
            "from sklearn.model_selection import train_test_split\n",
            "from sklearn.metrics import mean_squared_error\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore')\n",
            "\n",
            "data = fetch_california_housing()\n",
            "X_train, X_test, y_train, y_test = train_test_split(data.data[:1000], data.target[:1000], random_state=42)\n",
            "\n",
            "xgb_reg = xgb.XGBRegressor(objective='reg:squarederror', max_depth=3, n_estimators=100, learning_rate=0.1)\n",
            "xgb_reg.fit(X_train, y_train)\n",
            "\n",
            "print(f'XGBoost MSE: {mean_squared_error(y_test, xgb_reg.predict(X_test)):.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why does XGBoost generally outperform Scikit-Learn's GradientBoosting?"
        ],
        "exercise_code": [
            "print('XGBoost applies Newton Boosting (using 2nd order derivatives of the loss function) and enforces strict L1/L2 regularization on the leaf weights, making it faster to converge and much less prone to overfitting.')\n"
        ]
    },
    16: {
        "title": "Stacking and Blending",
        "summary": "Using a Meta-Learner to aggregate predictions.",
        "theory": [
            "### Stacking (Stacked Generalization)\n",
            "Instead of using trivial functions (like hard voting) to aggregate predictions, why don't we train a model to perform the aggregation?\n",
            "1. Train base models (e.g., SVM, Random Forest).\n",
            "2. Feed their predictions as *input features* to a final **Meta-Learner** (e.g., Logistic Regression) which makes the final prediction."
        ],
        "code": [
            "from sklearn.ensemble import StackingClassifier, RandomForestClassifier\n",
            "from sklearn.linear_model import LogisticRegression\n",
            "from sklearn.svm import SVC\n",
            "from sklearn.datasets import make_classification\n",
            "from sklearn.model_selection import train_test_split\n",
            "\n",
            "X, y = make_classification(n_samples=500, random_state=42)\n",
            "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)\n",
            "\n",
            "estimators = [\n",
            "    ('rf', RandomForestClassifier(n_estimators=10, random_state=42)),\n",
            "    ('svr', SVC(random_state=42))\n",
            "]\n",
            "clf = StackingClassifier(\n",
            "    estimators=estimators, final_estimator=LogisticRegression()\n",
            ")\n",
            "clf.fit(X_train, y_train)\n",
            "\n",
            "print(f'Stacking Classifier Accuracy: {clf.score(X_test, y_test):.3f}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. What is Blending compared to Stacking?"
        ],
        "exercise_code": [
            "print('Blending uses a held-out validation set to train the meta-learner, whereas strict Stacking uses out-of-fold predictions from Cross-Validation. Blending is faster but uses less data for training.')\n"
        ]
    },
    17: {
        "title": "Bagging vs Boosting vs Stacking",
        "summary": "Summary comparison of the big three ensemble frameworks.",
        "theory": [
            "### The Big Three Summarized\n",
            "| Feature | Bagging | Boosting | Stacking |\n",
            "|---|---|---|---|\n",
            "| Paradigm | Parallel | Sequential | Meta-Learning |\n",
            "| Focus | Reduce Variance | Reduce Bias | Learn best combinations |\n",
            "| Base Models | Same type (homogeneous) | Same type (homogeneous) | Different types (heterogeneous) |\n",
            "| Algorithm | Random Forest | XGBoost | StackingClassifier |"
        ],
        "code": [
            "print('When in doubt: Start with Random Forest (requires almost no tuning). Then move to XGBoost if you need to squeeze out maximum performance.')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Why is Stacking generally better suited for Kaggle competitions than production environments?"
        ],
        "exercise_code": [
            "print('Stacking creates highly complex, black-box meta-models that are computationally expensive to infer and incredibly difficult to maintain and explain in production, despite their fractional accuracy gains.')\n"
        ]
    },
    18: {
        "title": "Random Forest: Step wise explanation",
        "summary": "Deep dive into navigating an individual estimator inside a Random Forest.",
        "theory": [
            "### Exploring the Forest\n",
            "A Random Forest is just an array of `DecisionTreeClassifier` objects. You can access individual trees using the `.estimators_` attribute."
        ],
        "code": [
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.datasets import load_iris\n",
            "\n",
            "X, y = load_iris(return_X_y=True)\n",
            "rf = RandomForestClassifier(n_estimators=3, max_depth=2, random_state=42)\n",
            "rf.fit(X, y)\n",
            "\n",
            "# Accessing the 1st Tree in the Forest\n",
            "first_tree = rf.estimators_[0]\n",
            "print(f'Type of 1st tree: {type(first_tree)}')\n",
            "print(f'Depth of 1st tree: {first_tree.get_depth()}')\n"
        ],
        "exercises": [
            "### Exercises\n",
            "1. Since you can access individual trees using `.estimators_`, could you plot or print the rules of a single tree inside a Random Forest?"
        ],
        "exercise_code": [
            "from sklearn.tree import export_text\n",
            "from sklearn.datasets import load_iris\n",
            "\n",
            "# Yes! We can print the text representation of the 1st tree.\n",
            "tree_rules = export_text(first_tree, feature_names=load_iris().feature_names)\n",
            "print(tree_rules)\n"
        ]
    }
}


def sanitize_filename(name):
    """Clean the topic name to make it a valid filename."""
    chars_to_replace = [" — ", " —", "— ", "—", " + ", " +", "+ ", "+", " & ", " &", "& ", "&", " / ", " /", "/ ", "/", " ", ",", ".", ":", "(", ")", "[", "]", "?", "!", "→", "–"]
    cleaned = name.lower()
    for char in chars_to_replace:
        cleaned = cleaned.replace(char, "_")
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    return cleaned.strip("_")

def migrate_completed_projects():
    """Locate and move completed projects to their new locations."""
    print("Migrating completed projects...")
    
    # 1. ThinkBoard
    old_thinkboard = os.path.join(REPO_ROOT, "PHASE_1_Foundational_Core", "Projects", "ThinkBoard")
    new_thinkboard_dir = os.path.join(REPO_ROOT, "PHASE_05_Data_Visualization", "Projects")
    new_thinkboard = os.path.join(new_thinkboard_dir, "ThinkBoard")
    if os.path.exists(old_thinkboard):
        os.makedirs(new_thinkboard_dir, exist_ok=True)
        if os.path.exists(new_thinkboard):
            shutil.rmtree(new_thinkboard)
        shutil.move(old_thinkboard, new_thinkboard)
        print(f"Moved ThinkBoard to: {new_thinkboard}")
        
    # 2. Linear Algebra Operations
    old_la = os.path.join(REPO_ROOT, "PHASE_1_Foundational_Core", "Projects", "Mini_Projects", "Linear_Algebra_Operations")
    new_la_dir = os.path.join(REPO_ROOT, "PHASE_02_Math_Stats_Probability", "Projects")
    new_la = os.path.join(new_la_dir, "Linear_Algebra_Operations")
    if os.path.exists(old_la):
        os.makedirs(new_la_dir, exist_ok=True)
        if os.path.exists(new_la):
            shutil.rmtree(new_la)
        shutil.move(old_la, new_la)
        print(f"Moved Linear_Algebra_Operations to: {new_la}")

    # 3. Gradient Descent Simulation
    old_gd = os.path.join(REPO_ROOT, "PHASE_1_Foundational_Core", "Projects", "Mini_Projects", "Gradient_Descent_Simulation")
    new_gd_dir = os.path.join(REPO_ROOT, "PHASE_07_Regression_Algorithms", "Projects")
    new_gd = os.path.join(new_gd_dir, "Gradient_Descent_Simulation")
    if os.path.exists(old_gd):
        os.makedirs(new_gd_dir, exist_ok=True)
        if os.path.exists(new_gd):
            shutil.rmtree(new_gd)
        shutil.move(old_gd, new_gd)
        print(f"Moved Gradient_Descent_Simulation to: {new_gd}")

    # 4. Titanic Survival Predictor
    old_titanic = os.path.join(REPO_ROOT, "PHASE_2_ML_Data_Science_Fundamentals", "Projects", "Mini_Projects", "Titanic_Survival_Predictor")
    new_titanic_dir = os.path.join(REPO_ROOT, "PHASE_08_Classification_Algorithms", "Projects")
    new_titanic = os.path.join(new_titanic_dir, "Titanic_Survival_Predictor")
    if os.path.exists(old_titanic):
        os.makedirs(new_titanic_dir, exist_ok=True)
        if os.path.exists(new_titanic):
            shutil.rmtree(new_titanic)
        shutil.move(old_titanic, new_titanic)
        print(f"Moved Titanic_Survival_Predictor to: {new_titanic}")

def clean_old_folders():
    """Deletes the old deprecated Phase folders."""
    print("Cleaning up old directories...")
    old_p1 = os.path.join(REPO_ROOT, "PHASE_1_Foundational_Core")
    old_p2 = os.path.join(REPO_ROOT, "PHASE_2_ML_Data_Science_Fundamentals")
    
    if os.path.exists(old_p1):
        shutil.rmtree(old_p1)
        print(f"Removed old folder: {old_p1}")
    if os.path.exists(old_p2):
        shutil.rmtree(old_p2)
        print(f"Removed old folder: {old_p2}")

def make_template_notebook(title, idx, category):
    """Generates standard Jupyter template for later phases without the Status field."""
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Topic {idx}: {title}\n",
                    "\n",
                    f"- **Domain:** {category}\n",
                    "\n",
                    "## 📋 Learning Objectives & Overview\n",
                    "Write down your key learnings and key takeaways here.\n",
                    "\n",
                    "## 📝 Core Concepts & Mathematical Formulation\n",
                    "Detail the core concepts and equations (e.g., in LaTeX) related to this topic.\n",
                    "\n",
                    "## 💻 Implementation & Exercises\n",
                    "Write your implementation or exercises inside the cells below.\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Start coding your implementation here\n",
                    "print(\"Jupyter Notebook template for: " + title + "\")\n"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    return notebook

def make_populated_notebook(phase_num, topic_num, details):
    """Generates fully populated notebooks for Phase 1 & Phase 2 without the Status field."""
    cells = []
    
    # Emoji based on phase
    if phase_num == 1:
        emoji = "🐍"
    elif phase_num == 2:
        emoji = "📊"
    elif phase_num == 3:
        emoji = "🔢"
    elif phase_num == 4:
        emoji = "🐼"
    elif phase_num == 5:
        emoji = "📈"
    elif phase_num == 6:
        emoji = "🧹"
    elif phase_num == 7:
        emoji = "📉"
    elif phase_num == 8:
        emoji = "🎯"
    elif phase_num == 9:
        emoji = "✅"
    elif phase_num == 10:
        emoji = "📉"
    elif phase_num == 11:
        emoji = "🌳"
    else:
        emoji = "📓"
    
    # 1. Header & Summary
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# {emoji} Topic {topic_num}: {details['title']}\n",
            "\n",
            f"**Summary:** {details['summary']}\n",
            "\n",
            "---"
        ]
    })
    
    # 2. Theory notes
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 📝 Core Concepts & Explanations\n\n"
        ] + details['theory']
    })
    
    # 3. Code demonstration
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 💻 Code Demonstration\n",
            "Run the cells below to see the concepts in action:"
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": details['code']
    })
    
    # 4. Exercises
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": details['exercises']
    })
    
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": details['exercise_code']
    })
    
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    return notebook

def generate_roadmap():
    """Generates the new roadmap structure, including directories, local READMEs, and Jupyter Notebook templates."""
    print("Generating new roadmap folders and notebooks...")
    
    for phase_idx, phase in enumerate(ROADMAP_DATA, 1):
        phase_dir = os.path.join(REPO_ROOT, phase["dir_name"])
        os.makedirs(phase_dir, exist_ok=True)
        print(f"Created/Verified Phase directory: {phase_dir}")
        
        # Write Notebooks
        for idx, (title, category) in enumerate(phase["topics"], 1):
            clean_title = sanitize_filename(title)
            filename = f"{idx:02d}_{clean_title}.ipynb"
            file_path = os.path.join(phase_dir, filename)
            
            # Create either fully populated notebooks (for Phase 1 and Phase 2) or template notebooks (for later phases)
            if phase["dir_name"] == "PHASE_01_Python_Fundamentals" and idx in PHASE_1_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(1, idx, PHASE_1_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_02_Math_Stats_Probability" and idx in PHASE_2_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(2, idx, PHASE_2_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_03_NumPy" and idx in PHASE_3_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(3, idx, PHASE_3_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_04_Pandas_Data_Loading" and idx in PHASE_4_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(4, idx, PHASE_4_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_05_Data_Visualization" and idx in PHASE_5_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(5, idx, PHASE_5_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_06_Data_Preprocessing_Feature_Engineering" and idx in PHASE_6_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(6, idx, PHASE_6_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_07_Regression_Algorithms" and idx in PHASE_7_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(7, idx, PHASE_7_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_08_Classification_Algorithms" and idx in PHASE_8_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(8, idx, PHASE_8_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_09_Model_Evaluation_Validation" and idx in PHASE_9_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(9, idx, PHASE_9_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_10_Dimensionality_Reduction" and idx in PHASE_10_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(10, idx, PHASE_10_NOTEBOOK_CONTENTS[idx])
            elif phase["dir_name"] == "PHASE_11_Ensemble_Methods" and idx in PHASE_11_NOTEBOOK_CONTENTS:
                nb_json = make_populated_notebook(11, idx, PHASE_11_NOTEBOOK_CONTENTS[idx])
            else:
                nb_json = make_template_notebook(title, idx, category)
                
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(nb_json, f, indent=2)
        
        # Create local README.md
        readme_path = os.path.join(readme_path := os.path.join(phase_dir, "README.md"))
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {phase['title']}\n\n")
            f.write(f"{phase['description']}\n\n")
            f.write("## 📚 Topics\n\n")
            f.write("| Order | Topic | Domain | Status |\n")
            f.write("|---|---|---|---|\n")
            for idx, (title, category) in enumerate(phase["topics"], 1):
                clean_title = sanitize_filename(title)
                nb_link = f"./{idx:02d}_{clean_title}.ipynb"
                
                # Check status
                if phase["dir_name"] == "PHASE_01_Python_Fundamentals":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_02_Math_Stats_Probability":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_03_NumPy":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_04_Pandas_Data_Loading":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_05_Data_Visualization":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_06_Data_Preprocessing_Feature_Engineering":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_07_Regression_Algorithms":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_08_Classification_Algorithms":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_09_Model_Evaluation_Validation":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_10_Dimensionality_Reduction":
                    status = "✅ Completed"
                elif phase["dir_name"] == "PHASE_11_Ensemble_Methods":
                    status = "✅ Completed"
                else:
                    status = "📋 Planned"
                    
                f.write(f"| {idx} | [{title}]({nb_link}) | {category} | {status} |\n")
            
            # If Phase 8, append Classification mind map
            if phase["dir_name"] == "PHASE_08_Classification_Algorithms":
                f.write("\n## 🗺️ Classification Algorithm Map\n\n")
                f.write("Below is a visual taxonomy map of the classification models covered in this phase:\n\n")
                f.write("```mermaid\n")
                f.write("graph TD\n")
                f.write("    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px,color:#111;\n")
                f.write("    classDef generative fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b;\n")
                f.write("    classDef discriminative fill:#efebe9,stroke:#5d4037,stroke-width:2px,color:#3e2723;\n")
                f.write("    \n")
                f.write("    A[Classification Algorithms] --> B[Generative Models]\n")
                f.write("    A --> C[Discriminative Models]\n")
                f.write("    \n")
                f.write("    B --> B1[Gaussian Discriminant Analysis GDA]\n")
                f.write("    B --> B2[Naive Bayes Gaussian, Multinomial, Bernoulli]\n")
                f.write("    \n")
                f.write("    C --> C1[Linear Boundaries]\n")
                f.write("    C --> C2[Non-Linear Boundaries]\n")
                f.write("    \n")
                f.write("    C1 --> C1a[Logistic Regression]\n")
                f.write("    C1 --> C1b[Linear SVM]\n")
                f.write("    C1 --> C1c[Linear Discriminant Analysis LDA]\n")
                f.write("    \n")
                f.write("    C2 --> C2a[Kernel SVM RBF, Poly]\n")
                f.write("    C2 --> C2b[K-Nearest Neighbors KNN]\n")
                f.write("    C2 --> C2c[Decision Trees CART]\n")
                f.write("    \n")
                f.write("    class B,B1,B2 generative;\n")
                f.write("    class C,C1,C2,C1a,C1b,C1c,C2a,C2b,C2c discriminative;\n")
                f.write("```\n")

            # Add section for projects in this phase if they exist
            projects_dir = os.path.join(phase_dir, "Projects")
            if os.path.exists(projects_dir):
                f.write("\n## 🛠️ Projects\n\n")
                f.write("Completed projects in this phase:\n")
                for item in os.listdir(projects_dir):
                    if os.path.isdir(os.path.join(projects_dir, item)):
                        f.write(f"- [{item}](./Projects/{item})\n")

    # Clean up outdated notebooks that are no longer in the topics list
    valid_paths = set()
    for p in ROADMAP_DATA:
        p_dir = os.path.join(REPO_ROOT, p["dir_name"])
        for idx, (title, category) in enumerate(p["topics"], 1):
            clean_title = sanitize_filename(title)
            valid_paths.add(os.path.normpath(os.path.join(p_dir, f"{idx:02d}_{clean_title}.ipynb")).lower())
            
    for p in ROADMAP_DATA:
        p_dir = os.path.join(REPO_ROOT, p["dir_name"])
        if os.path.exists(p_dir):
            for filename in os.listdir(p_dir):
                if filename.endswith(".ipynb"):
                    full_path = os.path.normpath(os.path.join(p_dir, filename))
                    if full_path.lower() not in valid_paths:
                        os.remove(full_path)
                        print(f"Cleaned up outdated notebook: {full_path}")

    print("Generation complete!")

if __name__ == "__main__":
    # Perform migration of completed projects first to keep files safe
    migrate_completed_projects()
    
    # Delete old folders
    clean_old_folders()
    
    # Generate new roadmap folders and files
    generate_roadmap()
