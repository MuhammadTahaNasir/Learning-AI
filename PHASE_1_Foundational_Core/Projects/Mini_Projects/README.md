# Mini Projects

This folder contains foundational mini projects that demonstrate key mathematical and computational concepts essential for AI and machine learning.

## Projects Overview

### 1. Linear Algebra Operations
**Location**: `Linear_Algebra_Operations/`

A comprehensive demonstration of linear algebra operations using NumPy, including:
- Vector operations (addition, subtraction, dot product, cross product)
- Matrix operations (multiplication, transpose, inverse)
- Eigenvalue and eigenvector calculations
- Special matrix types
- Matrix visualization using heatmaps

**Key Features**:
- Step-by-step demonstrations with explanations
- Visual representation of matrix operations
- Verification of mathematical properties
- Educational output with detailed explanations

### 2. Gradient Descent Simulation
**Location**: `Gradient_Descent_Simulation/`

An interactive simulation of gradient descent optimization on various mathematical functions:
- 1D optimization on quadratic functions
- 2D optimization on Rosenbrock and Himmelblau functions
- Comprehensive visualization of convergence
- Learning rate comparison and analysis

**Key Features**:
- Multiple optimization landscapes
- 2D and 3D visualizations
- Convergence analysis
- Learning rate effects demonstration
- Step-by-step optimization tracking

## Quick Start

### Prerequisites
Both projects require:
```bash
pip install numpy matplotlib
```

### Running the Projects

#### Linear Algebra Operations
```bash
cd Linear_Algebra_Operations/
python linear_algebra_operations.py
```

#### Gradient Descent Simulation
```bash
cd Gradient_Descent_Simulation/
python gradient_descent_simulation.py
```

## Learning Objectives

### Mathematical Foundations
- **Linear Algebra**: Vector and matrix operations, eigenvalues/eigenvectors
- **Calculus**: Derivatives, gradients, optimization
- **Numerical Analysis**: Convergence, tolerance, stability

### Programming Skills
- **NumPy**: Efficient numerical computations
- **Matplotlib**: Data visualization and plotting
- **Object-Oriented Programming**: Class-based implementations

### AI/ML Concepts
- **Optimization**: Gradient descent algorithm
- **Mathematical Modeling**: Function implementation
- **Visualization**: Understanding complex mathematical concepts

## Project Structure

```
Mini Projects/
├── Linear_Algebra_Operations/
│   ├── linear_algebra_operations.py
│   ├── requirements.txt
│   └── README.md
├── Gradient_Descent_Simulation/
│   ├── gradient_descent_simulation.py
│   ├── requirements.txt
│   └── README.md
└── README.md (this file)
```

## Expected Outputs

### Linear Algebra Operations
- Console output with detailed mathematical demonstrations
- Matrix visualization heatmaps (saved as PNG)
- Step-by-step explanations of operations

### Gradient Descent Simulation
- Console output with convergence information
- Multiple visualization files:
  - `1d_gradient_descent.png`
  - `2d_gradient_descent.png`
  - `learning_rate_comparison.png`

## Educational Value

These projects serve as:
1. **Foundation Building**: Essential mathematical concepts for AI/ML
2. **Hands-on Learning**: Interactive demonstrations with visual feedback
3. **Code Practice**: Real implementation of mathematical algorithms
4. **Concept Reinforcement**: Multiple examples and visualizations

## Next Steps

After completing these projects, you can:
- Explore more advanced optimization algorithms
- Implement machine learning algorithms from scratch
- Study more complex mathematical concepts
- Build larger AI/ML projects using these foundations

## Troubleshooting

### Common Issues
1. **Matplotlib not displaying plots**: Ensure you have a display environment or use `plt.savefig()` only
2. **NumPy import errors**: Install NumPy with `pip install numpy`
3. **Memory issues with large matrices**: Reduce matrix sizes in the code

### Getting Help
- Check the individual project README files for specific instructions
- Ensure all dependencies are installed correctly
- Verify Python version compatibility (Python 3.7+ recommended)

These mini projects provide a solid foundation for understanding the mathematical and computational concepts that underpin modern AI and machine learning systems. 