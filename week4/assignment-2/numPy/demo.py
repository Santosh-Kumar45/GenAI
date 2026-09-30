# ============================================================
# PART 3: NUMPY PRACTICE
# ============================================================

st.header("Part 3: NumPy")

# ------------------------------------------------------------
# Problem 15: Create and inspect an array
# ------------------------------------------------------------
# Create a NumPy array:
# [10, 20, 30, 40, 50]
#
# Print:
# 1. The array
# 2. Its shape
# 3. Its data type
#
# Solution:
numbers = np.array([10, 20, 30, 40, 50])

print("\nArray:")
print(numbers)

print("Shape:", numbers.shape)
print("Data type:", numbers.dtype)

# ------------------------------------------------------------
# Problem 16: Create a 3 x 3 matrix
# ------------------------------------------------------------
# Create a NumPy array containing numbers 1 to 9.
# Reshape it into 3 rows and 3 columns.
#
# Solution:
matrix = np.arange(1, 10).reshape(3, 3)

print("\n3 x 3 matrix:")
print(matrix)

# ------------------------------------------------------------
# Problem 17: Array calculations
# ------------------------------------------------------------
# Create:
# a = [10, 20, 30]
# b = [1, 2, 3]
#
# Calculate:
# 1. a + b
# 2. a * b
# 3. a * 10
#
# Solution:
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\na + b:")
print(a + b)

print("\na * b:")
print(a * b)

print("\na * 10:")
print(a * 10)

# ------------------------------------------------------------
# Problem 18: Analyze marks
# ------------------------------------------------------------
# Create an array of marks:
# [70, 85, 90, 65, 95]
#
# Find:
# 1. Total
# 2. Average
# 3. Minimum
# 4. Maximum
# 5. Median
# 6. Standard deviation
#
# Solution:
marks = np.array([70, 85, 90, 65, 95])

print("\nTotal:", np.sum(marks))
print("Average:", np.mean(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))

# ------------------------------------------------------------
# Problem 19: Filter an array
# ------------------------------------------------------------
# Find all marks >= 80.
#
# Solution:
high_marks = marks[marks >= 80]

print("\nMarks >= 80:")
print(high_marks)

# ------------------------------------------------------------
# Problem 20: Sort and find unique values
# ------------------------------------------------------------
# Given:
# [5, 2, 8, 2, 9, 5, 1]
#
# 1. Sort the array.
# 2. Find unique values.
#
# Solution:
values = np.array([5, 2, 8, 2, 9, 5, 1])

print("\nSorted:")
print(np.sort(values))

print("\nUnique:")
print(np.unique(values))

# ------------------------------------------------------------
# Problem 21: Student marks matrix
# ------------------------------------------------------------
# Create this matrix:
#
#         Python  Pandas  NumPy
# Student1  80      70      90
# Student2  60      75      85
# Student3  95      88      92
#
# Find:
# 1. Average mark for each student.
# 2. Average mark for each subject.
#
# Solution:
marks_matrix = np.array([
    [80, 70, 90],
    [60, 75, 85],
    [95, 88, 92]
])

student_average = np.mean(marks_matrix, axis=1)
subject_average = np.mean(marks_matrix, axis=0)

print("\nStudent averages:")
print(student_average)

print("\nSubject averages:")
print(subject_average)

# ------------------------------------------------------------
# Problem 22: Weighted score
# ------------------------------------------------------------
# Create:
# features = [10, 20, 30]
# weights = [0.2, 0.3, 0.5]
#
# Calculate the weighted score using np.dot().
#
# Solution:
features = np.array([10, 20, 30])
weights = np.array([0.2, 0.3, 0.5])

weighted_score = np.dot(features, weights)

print("\nWeighted score:")
print(weighted_score)