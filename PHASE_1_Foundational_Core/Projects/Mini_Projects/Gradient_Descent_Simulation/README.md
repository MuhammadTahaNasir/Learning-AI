# Gradient Descent Simulation

This project demonstrates gradient descent optimization on various mathematical functions with comprehensive visualization of convergence behavior.

## Features

### 1. 1D Gradient Descent
- **Quadratic Function**: f(x) = x² + 2x + 1
- Step-by-step convergence visualization
- Parameter and function value tracking
- Gradient magnitude analysis

### 2. 2D Gradient Descent
- **Rosenbrock Function**: f(x,y) = (1-x)² + 100(y-x²)²
- **Himmelblau Function**: f(x,y) = (x² + y - 11)² + (x + y² - 7)²
- 2D contour plots with optimization paths
- 3D surface visualization
- Multi-parameter convergence tracking

### 3. Advanced Visualizations
- Function landscapes with optimization paths
- Convergence plots for parameters and function values
- Gradient magnitude analysis
- Step size tracking
- Learning rate comparison

### 4. Learning Rate Analysis
- Comparison of different learning rates
- Convergence speed analysis
- Stability assessment

## Mathematical Functions

### 1. Quadratic Function
```
f(x) = x² + 2x + 1
f'(x) = 2x + 2
```
- **Global minimum**: x = -1, f(-1) = 0
- **Properties**: Convex, smooth, single minimum

### 2. Rosenbrock Function
```
f(x,y) = (1-x)² + 100(y-x²)²
```
- **Global minimum**: (1, 1), f(1,1) = 0
- **Properties**: Non-convex, narrow valley, challenging for optimization

### 3. Himmelblau Function
```
f(x,y) = (x² + y - 11)² + (x + y² - 7)²
```
- **Local minima**: (3, 2), (-2.81, 3.13), (-3.78, -3.28), (3.58, -1.85)
- **Properties**: Multiple local minima, good for testing optimization algorithms

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main simulation:
```bash
python gradient_descent_simulation.py
```

## Output

The script will generate:

### 1. Console Output
- Convergence information for each function
- Final parameter values and function values
- Comparison with analytical solutions

### 2. Visualization Files
- `1d_gradient_descent.png`: 1D optimization visualization
- `2d_gradient_descent.png`: 2D optimization visualization  
- `learning_rate_comparison.png`: Learning rate comparison

### 3. Visualization Components

#### 1D Gradient Descent:
- Function plot with optimization path
- Parameter convergence over iterations
- Function value convergence
- Gradient magnitude analysis

#### 2D Gradient Descent:
- Contour plot with optimization path
- 3D surface plot with path
- Parameter convergence plots
- Function value and gradient magnitude
- Step size analysis

## Example Output

```
Gradient Descent Simulation
==================================================

1. 1D Gradient Descent on Quadratic Function
----------------------------------------
Converged after 156 iterations
Initial x: 5.0
Final x: -1.000000
Final function value: 0.000000
Analytical minimum: x = -1, f(-1) = 0

2. 2D Gradient Descent on Rosenbrock Function
----------------------------------------
Converged after 847 iterations
Initial point: [-2, 2]
Final point: [1.000000, 1.000000]
Final function value: 0.000000
Global minimum: (1, 1), f(1,1) = 0
```

## Learning Objectives

- Understand gradient descent algorithm
- Visualize optimization convergence
- Analyze learning rate effects
- Compare different optimization landscapes
- Implement mathematical functions and their gradients

## Mathematical Concepts Covered

1. **Optimization**: Gradient descent algorithm
2. **Calculus**: Derivatives and gradients
3. **Linear Algebra**: Vector operations and norms
4. **Visualization**: 2D/3D plotting and contour maps
5. **Numerical Analysis**: Convergence criteria and tolerance

## Key Parameters

- **Learning Rate**: Controls step size (default: 0.01)
- **Max Iterations**: Maximum optimization steps (default: 1000)
- **Tolerance**: Convergence threshold (default: 1e-6)

## Applications

This simulation demonstrates concepts fundamental to:
- Machine Learning optimization
- Neural Network training
- Mathematical optimization
- Algorithm analysis and comparison

The project serves as an excellent foundation for understanding optimization algorithms used in modern AI and machine learning systems. 