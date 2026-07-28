# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(prompt_name=""):
    """Read an M x N matrix from the user. Returns a 2D list of integers."""
    if prompt_name:
        print(f"\n--- {prompt_name} ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(1, rows + 1):
        while True:
            line = input(f"Enter row {i}: ").strip()
            values = line.split()
            if len(values) != cols:
                print(f"  Expected {cols} values. Try again.")
                continue
            try:
                row = [int(v) for v in values]
                matrix.append(row)
                break
            except ValueError:
                print("  Please enter integers only. Try again.")
    return matrix


def print_matrix(matrix, title=""):
    """Display a matrix in a neat, aligned grid."""
    if title:
        print(title)
    if not matrix:
        print("(empty)")
        return
    # Determine column width based on the widest number
    max_width = max(len(str(val)) for row in matrix for val in row)
    for row in matrix:
        print("  ".join(f"{val:>{max_width}}" for val in row))


def transpose(matrix):
    """Return the transpose of the given matrix (rows become columns)."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(A, B):
    """Return the element-wise sum of two matrices of the same size."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(A[i][j] + B[i][j])
        result.append(new_row)
    return result


def multiply_matrices(A, B):
    """Return the matrix product A × B. Requires columns of A == rows of B."""
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")
    m = len(A)          # rows of A
    n = len(A[0])       # cols of A / rows of B
    p = len(B[0])       # cols of B
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def main():
    print("=" * 50)
    print("MATRIX OPERATIONS")
    print("=" * 50)

    # -------------------------------------------------------------------------
    # PART A — Transpose
    # -------------------------------------------------------------------------
    print("\n*** PART A: Transpose a Matrix ***")
    matrix = read_matrix("Original Matrix")
    print()
    print_matrix(matrix, "Original Matrix:")
    print()
    transposed = transpose(matrix)
    print_matrix(transposed, "Transposed Matrix:")

    # -------------------------------------------------------------------------
    # PART B — Matrix Addition
    # -------------------------------------------------------------------------
    print("\n*** PART B: Add Two Matrices ***")
    print("Both matrices must have the same dimensions.")
    A = read_matrix("Matrix A")
    B = read_matrix("Matrix B")

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("\nError: Matrices must be the same size for addition.")
    else:
        print()
        print_matrix(A, "Matrix A:")
        print()
        print_matrix(B, "Matrix B:")
        print()
        result = add_matrices(A, B)
        print_matrix(result, "Sum (A + B):")

    # -------------------------------------------------------------------------
    # PART C — Matrix Multiplication
    # -------------------------------------------------------------------------
    print("\n*** PART C: Multiply Two Matrices ***")
    print("Columns of A must equal rows of B.")
    A = read_matrix("Matrix A (M x N)")
    B = read_matrix("Matrix B (N x P)")

    if len(A[0]) != len(B):
        print("\nError: Number of columns in A must equal number of rows in B.")
    else:
        print()
        print_matrix(A, "Matrix A:")
        print()
        print_matrix(B, "Matrix B:")
        print()
        product = multiply_matrices(A, B)
        print_matrix(product, "Product (A × B):")

    print("\n" + "=" * 50)
    print("Done.")


if __name__ == "__main__":
    main()
