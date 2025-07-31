import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class GradientDescentSimulator:
    """A class to simulate gradient descent on various functions"""
    
    def __init__(self, learning_rate=0.001, max_iterations=1000, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.history = []
    
    def quadratic_function(self, x):
        """Quadratic function: f(x) = x^2 + 2x + 1"""
        return x**2 + 2*x + 1
    
    def quadratic_gradient(self, x):
        """Gradient of quadratic function: f'(x) = 2x + 2"""
        return 2*x + 2
    
    def rosenbrock_function(self, x, y):
        """Rosenbrock function: f(x,y) = (1-x)^2 + 100(y-x^2)^2"""
        return (1 - x)**2 + 100 * (y - x**2)**2
    
    def rosenbrock_gradient(self, x, y):
        """Gradient of Rosenbrock function"""
        dx = -2*(1 - x) - 400*x*(y - x**2)
        dy = 200*(y - x**2)
        return np.array([dx, dy])
    
    def himmelblau_function(self, x, y):
        """Himmelblau function: f(x,y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2"""
        return (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    
    def himmelblau_gradient(self, x, y):
        """Gradient of Himmelblau function"""
        dx = 4*x*(x**2 + y - 11) + 2*(x + y**2 - 7)
        dy = 2*(x**2 + y - 11) + 4*y*(x + y**2 - 7)
        return np.array([dx, dy])
    
    def run_1d_gradient_descent(self, initial_x, function, gradient_func):
        """Run gradient descent on a 1D function"""
        x = initial_x
        self.history = [x]
        
        for iteration in range(self.max_iterations):
            # Calculate gradient
            grad = gradient_func(x)
            
            # Update x
            x_new = x - self.learning_rate * grad
            
            # Check convergence
            if abs(x_new - x) < self.tolerance:
                print(f"Converged after {iteration + 1} iterations")
                break
            
            x = x_new
            self.history.append(x)
        
        return x, self.history
    
    def run_2d_gradient_descent(self, initial_point, function, gradient_func):
        """Run gradient descent on a 2D function"""
        point = np.array(initial_point, dtype=float)
        self.history = [point.copy()]
        
        for iteration in range(self.max_iterations):
            # Calculate gradient
            grad = gradient_func(point[0], point[1])
            
            # Check for numerical instability
            if np.any(np.isnan(grad)) or np.any(np.isinf(grad)):
                print(f"Numerical instability detected at iteration {iteration + 1}")
                break
            
            # Update point
            point_new = point - self.learning_rate * grad
            
            # Check for numerical instability in new point
            if np.any(np.isnan(point_new)) or np.any(np.isinf(point_new)):
                print(f"Numerical instability detected at iteration {iteration + 1}")
                break
            
            # Check convergence
            if np.linalg.norm(point_new - point) < self.tolerance:
                print(f"Converged after {iteration + 1} iterations")
                break
            
            point = point_new
            self.history.append(point.copy())
        
        return point, self.history
    
    def visualize_1d_convergence(self, function, x_range=(-5, 5)):
        """Visualize 1D gradient descent convergence"""
        x = np.linspace(x_range[0], x_range[1], 1000)
        y = function(x)
        
        plt.figure(figsize=(12, 8))
        
        # Plot function
        plt.subplot(2, 2, 1)
        plt.plot(x, y, 'b-', linewidth=2, label='f(x) = x² + 2x + 1')
        plt.plot(self.history, [function(x) for x in self.history], 'ro-', 
                markersize=4, label='Gradient Descent Path')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gradient Descent on Quadratic Function')
        plt.legend()
        plt.grid(True)
        
        # Plot convergence
        plt.subplot(2, 2, 2)
        iterations = range(len(self.history))
        plt.plot(iterations, self.history, 'g-', linewidth=2)
        plt.xlabel('Iteration')
        plt.ylabel('x value')
        plt.title('Convergence of x')
        plt.grid(True)
        
        # Plot function values
        plt.subplot(2, 2, 3)
        function_values = [function(x) for x in self.history]
        plt.plot(iterations, function_values, 'r-', linewidth=2)
        plt.xlabel('Iteration')
        plt.ylabel('f(x)')
        plt.title('Function Value Convergence')
        plt.grid(True)
        
        # Plot gradient magnitude
        plt.subplot(2, 2, 4)
        gradients = [abs(self.quadratic_gradient(x)) for x in self.history]
        plt.plot(iterations, gradients, 'm-', linewidth=2)
        plt.xlabel('Iteration')
        plt.ylabel('|∇f(x)|')
        plt.title('Gradient Magnitude')
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('1d_gradient_descent.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def visualize_2d_convergence(self, function, gradient_func, x_range=(-5, 5), y_range=(-5, 5)):
        """Visualize 2D gradient descent convergence"""
        x = np.linspace(x_range[0], x_range[1], 100)
        y = np.linspace(y_range[0], y_range[1], 100)
        X, Y = np.meshgrid(x, y)
        Z = function(X, Y)
        
        # Convert history to arrays
        history_array = np.array(self.history)
        
        plt.figure(figsize=(15, 10))
        
        # 2D contour plot
        plt.subplot(2, 3, 1)
        contour = plt.contour(X, Y, Z, levels=20, cmap='viridis')
        plt.colorbar(contour)
        plt.plot(history_array[:, 0], history_array[:, 1], 'ro-', 
                markersize=4, linewidth=2, label='Gradient Descent Path')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gradient Descent Path')
        plt.legend()
        plt.grid(True)
        
        # 3D surface plot
        ax = plt.subplot(2, 3, 2, projection='3d')
        surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
        ax.plot(history_array[:, 0], history_array[:, 1], 
               [function(x, y) for x, y in history_array], 'ro-', 
               markersize=4, linewidth=2)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('f(x, y)')
        ax.set_title('3D Surface with Path')
        
        # Convergence plots
        plt.subplot(2, 3, 3)
        plt.plot(range(len(self.history)), history_array[:, 0], 'b-', label='x')
        plt.plot(range(len(self.history)), history_array[:, 1], 'r-', label='y')
        plt.xlabel('Iteration')
        plt.ylabel('Parameter Value')
        plt.title('Parameter Convergence')
        plt.legend()
        plt.grid(True)
        
        plt.subplot(2, 3, 4)
        function_values = [function(x, y) for x, y in self.history]
        plt.plot(range(len(self.history)), function_values, 'g-', linewidth=2)
        plt.xlabel('Iteration')
        plt.ylabel('f(x, y)')
        plt.title('Function Value Convergence')
        plt.grid(True)
        
        plt.subplot(2, 3, 5)
        gradients = [np.linalg.norm(gradient_func(x, y)) for x, y in self.history]
        plt.plot(range(len(self.history)), gradients, 'm-', linewidth=2)
        plt.xlabel('Iteration')
        plt.ylabel('||∇f(x, y)||')
        plt.title('Gradient Magnitude')
        plt.grid(True)
        
        plt.subplot(2, 3, 6)
        distances = [np.linalg.norm(np.array([x, y]) - np.array([x_prev, y_prev])) 
                   for (x, y), (x_prev, y_prev) in zip(self.history[1:], self.history[:-1])]
        plt.plot(range(1, len(self.history)), distances, 'c-', linewidth=2)
        plt.xlabel('Iteration')
        plt.ylabel('Step Size')
        plt.title('Step Size')
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('2d_gradient_descent.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def compare_learning_rates(self, initial_x, function, gradient_func):
        """Compare convergence with different learning rates"""
        learning_rates = [0.001, 0.01, 0.1, 0.5]
        colors = ['blue', 'green', 'red', 'orange']
        
        plt.figure(figsize=(12, 8))
        
        for lr, color in zip(learning_rates, colors):
            # Reset learning rate
            original_lr = self.learning_rate
            self.learning_rate = lr
            
            # Run gradient descent
            final_x, history = self.run_1d_gradient_descent(initial_x, function, gradient_func)
            
            # Plot convergence
            iterations = range(len(history))
            function_values = [function(x) for x in history]
            plt.plot(iterations, function_values, color=color, linewidth=2, 
                    label=f'Learning Rate = {lr}')
            
            # Reset learning rate
            self.learning_rate = original_lr
        
        plt.xlabel('Iteration')
        plt.ylabel('f(x)')
        plt.title('Convergence Comparison with Different Learning Rates')
        plt.legend()
        plt.grid(True)
        plt.yscale('log')
        plt.savefig('learning_rate_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()

def main():
    """Main function to demonstrate gradient descent simulations"""
    print("Gradient Descent Simulation")
    print("=" * 50)
    
    # Initialize simulator
    simulator = GradientDescentSimulator(learning_rate=0.01, max_iterations=1000)
    
    # 1. 1D Gradient Descent on Quadratic Function
    print("\n1. 1D Gradient Descent on Quadratic Function")
    print("-" * 40)
    
    initial_x = 5.0
    final_x, history = simulator.run_1d_gradient_descent(
        initial_x, simulator.quadratic_function, simulator.quadratic_gradient
    )
    
    print(f"Initial x: {initial_x}")
    print(f"Final x: {final_x:.6f}")
    print(f"Final function value: {simulator.quadratic_function(final_x):.6f}")
    print(f"Analytical minimum: x = -1, f(-1) = 0")
    
    # Visualize 1D convergence
    simulator.visualize_1d_convergence(simulator.quadratic_function)
    
    # 2. 2D Gradient Descent on Rosenbrock Function
    print("\n2. 2D Gradient Descent on Rosenbrock Function")
    print("-" * 40)
    
    # Use smaller learning rate for Rosenbrock function
    simulator.learning_rate = 0.0001
    initial_point = [-2, 2]
    final_point, history = simulator.run_2d_gradient_descent(
        initial_point, simulator.rosenbrock_function, simulator.rosenbrock_gradient
    )
    # Reset learning rate
    simulator.learning_rate = 0.001
    
    print(f"Initial point: {initial_point}")
    print(f"Final point: [{final_point[0]:.6f}, {final_point[1]:.6f}]")
    print(f"Final function value: {simulator.rosenbrock_function(final_point[0], final_point[1]):.6f}")
    print(f"Global minimum: (1, 1), f(1,1) = 0")
    
    # Visualize 2D convergence
    simulator.visualize_2d_convergence(simulator.rosenbrock_function, simulator.rosenbrock_gradient)
    
    # 3. 2D Gradient Descent on Himmelblau Function
    print("\n3. 2D Gradient Descent on Himmelblau Function")
    print("-" * 40)
    
    initial_point = [0, 0]
    final_point, history = simulator.run_2d_gradient_descent(
        initial_point, simulator.himmelblau_function, simulator.himmelblau_gradient
    )
    
    print(f"Initial point: {initial_point}")
    print(f"Final point: [{final_point[0]:.6f}, {final_point[1]:.6f}]")
    print(f"Final function value: {simulator.himmelblau_function(final_point[0], final_point[1]):.6f}")
    print("Himmelblau function has 4 local minima at:")
    print("  (3, 2), (-2.81, 3.13), (-3.78, -3.28), (3.58, -1.85)")
    
    # Visualize 2D convergence for Himmelblau
    simulator.visualize_2d_convergence(simulator.himmelblau_function, simulator.himmelblau_gradient, 
                                      x_range=(-5, 5), y_range=(-5, 5))
    
    # 4. Learning Rate Comparison
    print("\n4. Learning Rate Comparison")
    print("-" * 40)
    
    simulator.compare_learning_rates(5.0, simulator.quadratic_function, simulator.quadratic_gradient)
    
    print("\nGradient Descent Simulation completed!")
    print("Visualizations saved as PNG files.")

if __name__ == "__main__":
    main() 