import numpy as np
import matplotlib.pyplot as plt

def demonstrate_vector_operations():
    """Demonstrate basic vector operations using NumPy"""
    print("=== Vector Operations ===")
    
    # Create vectors
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    
    # Vector addition
    v_sum = v1 + v2
    print(f"Vector addition: {v_sum}")
    
    # Vector subtraction
    v_diff = v1 - v2
    print(f"Vector subtraction: {v_diff}")
    
    # Scalar multiplication
    scalar = 2
    v_scaled = scalar * v1
    print(f"Scalar multiplication ({scalar} * v1): {v_scaled}")
    
    # Dot product
    dot_product = np.dot(v1, v2)
    print(f"Dot product: {dot_product}")
    
    # Cross product (for 3D vectors)
    cross_product = np.cross(v1, v2)
    print(f"Cross product: {cross_product}")
    
    # Vector magnitude
    magnitude_v1 = np.linalg.norm(v1)
    print(f"Magnitude of v1: {magnitude_v1:.4f}")
    
    print()

def demonstrate_matrix_operations():
    """Demonstrate matrix operations using NumPy"""
    print("=== Matrix Operations ===")
    
    # Create matrices
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    
    # Matrix addition
    C = A + B
    print("\nMatrix addition (A + B):")
    print(C)
    
    # Matrix subtraction
    D = A - B
    print("\nMatrix subtraction (A - B):")
    print(D)
    
    # Scalar multiplication
    scalar = 2
    E = scalar * A
    print(f"\nScalar multiplication ({scalar} * A):")
    print(E)
    
    # Matrix multiplication
    F = np.dot(A, B)
    print("\nMatrix multiplication (A * B):")
    print(F)
    
    # Element-wise multiplication (Hadamard product)
    G = A * B
    print("\nElement-wise multiplication (A ⊙ B):")
    print(G)
    
    print()

def demonstrate_matrix_properties():
    """Demonstrate matrix properties and operations"""
    print("=== Matrix Properties ===")
    
    # Create a square matrix
    A = np.array([[2, 1], [1, 3]])
    print("Matrix A:")
    print(A)
    
    # Matrix transpose
    A_transpose = A.T
    print("\nMatrix transpose (A^T):")
    print(A_transpose)
    
    # Matrix determinant
    det_A = np.linalg.det(A)
    print(f"\nDeterminant of A: {det_A:.4f}")
    
    # Matrix inverse
    try:
        A_inverse = np.linalg.inv(A)
        print("\nMatrix inverse (A^(-1)):")
        print(A_inverse)
        
        # Verify inverse: A * A^(-1) = I
        identity_check = np.dot(A, A_inverse)
        print("\nVerification (A * A^(-1)):")
        print(identity_check)
    except np.linalg.LinAlgError:
        print("\nMatrix is not invertible (determinant = 0)")
    
    # Matrix trace
    trace_A = np.trace(A)
    print(f"\nTrace of A: {trace_A}")
    
    print()

def demonstrate_eigenvalues_eigenvectors():
    """Demonstrate eigenvalue and eigenvector calculations"""
    print("=== Eigenvalues and Eigenvectors ===")
    
    # Create a symmetric matrix
    A = np.array([[4, 1], [1, 3]])
    print("Matrix A:")
    print(A)
    
    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    print(f"\nEigenvalues: {eigenvalues}")
    print("\nEigenvectors:")
    print(eigenvectors)
    
    # Verify: A * v = λ * v
    print("\nVerification (A * v = λ * v):")
    for i in range(len(eigenvalues)):
        lambda_val = eigenvalues[i]
        eigenvector = eigenvectors[:, i]
        result = np.dot(A, eigenvector)
        expected = lambda_val * eigenvector
        print(f"Eigenvalue {i+1} (λ = {lambda_val:.4f}):")
        print(f"  A * v = {result}")
        print(f"  λ * v = {expected}")
        print(f"  Difference: {np.linalg.norm(result - expected):.2e}")
    
    print()

def demonstrate_special_matrices():
    """Demonstrate special types of matrices"""
    print("=== Special Matrices ===")
    
    # Identity matrix
    I = np.eye(3)
    print("Identity matrix (3x3):")
    print(I)
    
    # Zero matrix
    Z = np.zeros((3, 3))
    print("\nZero matrix (3x3):")
    print(Z)
    
    # Random matrix
    R = np.random.rand(3, 3)
    print("\nRandom matrix (3x3):")
    print(R)
    
    # Diagonal matrix
    D = np.diag([1, 2, 3])
    print("\nDiagonal matrix:")
    print(D)
    
    # Upper triangular matrix
    U = np.triu(A) if 'A' in locals() else np.triu(np.random.rand(3, 3))
    print("\nUpper triangular matrix:")
    print(U)
    
    print()

def visualize_matrix_operations():
    """Visualize matrix operations using heatmaps"""
    print("=== Matrix Visualization ===")
    
    # Create sample matrices
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    # Create subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Matrix Operations Visualization', fontsize=16)
    
    # Original matrices
    im1 = axes[0, 0].imshow(A, cmap='viridis')
    axes[0, 0].set_title('Matrix A')
    plt.colorbar(im1, ax=axes[0, 0])
    
    im2 = axes[0, 1].imshow(B, cmap='viridis')
    axes[0, 1].set_title('Matrix B')
    plt.colorbar(im2, ax=axes[0, 1])
    
    # Matrix operations
    im3 = axes[0, 2].imshow(A + B, cmap='viridis')
    axes[0, 2].set_title('A + B')
    plt.colorbar(im3, ax=axes[0, 2])
    
    im4 = axes[1, 0].imshow(A * B, cmap='viridis')
    axes[1, 0].set_title('A ⊙ B (Element-wise)')
    plt.colorbar(im4, ax=axes[1, 0])
    
    im5 = axes[1, 1].imshow(np.dot(A, B), cmap='viridis')
    axes[1, 1].set_title('A * B (Matrix multiplication)')
    plt.colorbar(im5, ax=axes[1, 1])
    
    im6 = axes[1, 2].imshow(A.T, cmap='viridis')
    axes[1, 2].set_title('A^T (Transpose)')
    plt.colorbar(im6, ax=axes[1, 2])
    
    plt.tight_layout()
    plt.savefig('matrix_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Matrix visualization saved as 'matrix_visualization.png'")

def main():
    """Main function to run all demonstrations"""
    print("Linear Algebra Operations with NumPy")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_vector_operations()
    demonstrate_matrix_operations()
    demonstrate_matrix_properties()
    demonstrate_eigenvalues_eigenvectors()
    demonstrate_special_matrices()
    
    # Visualize matrix operations
    try:
        visualize_matrix_operations()
    except Exception as e:
        print(f"Visualization failed: {e}")
        print("Make sure matplotlib is installed: pip install matplotlib")
    
    print("\nLinear Algebra Operations demonstration completed!")

if __name__ == "__main__":
    main() 