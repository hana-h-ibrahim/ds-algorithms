
import numpy as np

# Define the matrix
A = np.array([[2, 4], [1, 3]])

# Compute A^T*A
ATA = A.T.dot(A)

# Find the eigenvalues of ATA
eigvals = np.linalg.eigvals(ATA)

# Compute the square roots of the eigenvalues
singular_vals = np.sqrt(eigvals)

# The operator norm is the largest singular value
op_norm = max(singular_vals)
print(op_norm)
