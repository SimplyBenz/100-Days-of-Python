import numpy as np

# Define the matrix A and vector b
A = np.array([[2, 1], 
              [1, 3]])
b = np.array([8, 13])

# Solve for x using NumPy's linear algebra solver
x = np.linalg.solve(A, b)

# Output the solution
print("Solution (x):", x)

# Verify the solution
print("Verification (Ax):", np.dot(A, x))
print("Expected (b):", b)
