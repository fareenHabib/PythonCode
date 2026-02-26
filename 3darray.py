import numpy as np

# -----------------------------
# 1️⃣ Create 1D Array
# -----------------------------
arr1D = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1D)

# Fetch individual element
print("Element at index 2:", arr1D[2])

# Slice operation
print("Slice (index 1 to 3):", arr1D[1:4])


# -----------------------------
# 2️⃣ Create 2D Array
# -----------------------------
arr2D = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print("\n2D Array:")
print(arr2D)

# Fetch individual element
print("Element at row 1, column 2:", arr2D[1, 2])

# Slice sub-matrix
print("Sub-matrix (first 2 rows, first 2 columns):")
print(arr2D[0:2, 0:2])


# -----------------------------
# 3️⃣ Create 3D Array
# -----------------------------
arr3D = np.array([[[1, 2, 3],
                   [4, 5, 6]],
                  
                  [[7, 8, 9],
                   [10, 11, 12]]])

print("\n3D Array:")
print(arr3D)

# Fetch individual element
print("Element at [1, 0, 2]:", arr3D[1, 0, 2])

# Slice sub-matrix
print("Slice of first 2D block:")
print(arr3D[0, :, :])

print("Slice: All blocks, first row only:")
print(arr3D[:, 0, :])