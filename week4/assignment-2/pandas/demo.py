# ============================================================
# PART 2: PANDAS PRACTICE
# ============================================================

st.header("Part 2: Pandas")

students = pd.DataFrame({
    "name": ["Amit", "Priya", "Rahul", "Neha", "Arjun", "Sara"],
    "age": [20, 21, 19, 22, 20, 21],
    "score": [85, 92, 74, 88, 95, 67],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Pune"]
})

print("\nStudent Data:")
print(students)

# ------------------------------------------------------------
# Problem 6: Explore a DataFrame
# ------------------------------------------------------------
# Display:
# 1. First 3 rows
# 2. Last 2 rows
# 3. Shape
# 4. Column names
#
# Solution:
print("\nFirst 3 rows:")
print(students.head(3))

print("\nLast 2 rows:")
print(students.tail(2))

print("\nShape:")
print(students.shape)

print("\nColumns:")
print(students.columns)

# ------------------------------------------------------------
# Problem 7: Select columns
# ------------------------------------------------------------
# Select only the name and score columns.
#
# Solution:
print("\nName and score:")
print(students[["name", "score"]])

# ------------------------------------------------------------
# Problem 8: Filter students
# ------------------------------------------------------------
# Find all students who scored 80 or above.
#
# Solution:
high_scorers = students[students["score"] >= 80]

print("\nStudents scoring 80 or above:")
print(high_scorers)

# ------------------------------------------------------------
# Problem 9: Sort students
# ------------------------------------------------------------
# Sort students from highest score to lowest score.
#
# Solution:
sorted_students = students.sort_values("score", ascending=False)

print("\nSorted students:")
print(sorted_students)

# ------------------------------------------------------------
# Problem 10: Add a new column
# ------------------------------------------------------------
# Create a new column called "passed".
# The value should be True if score >= 50, otherwise False.
#
# Solution:
students["passed"] = students["score"] >= 50

print("\nPassed column:")
print(students)

# ------------------------------------------------------------
# Problem 11: Group by city
# ------------------------------------------------------------
# Find the average score for each city.
#
# Solution:
city_scores = students.groupby("city")["score"].mean()

print("\nAverage score by city:")
print(city_scores)

# ------------------------------------------------------------
# Problem 12: Count categories
# ------------------------------------------------------------
# Count how many students belong to each city.
#
# Solution:
city_counts = students["city"].value_counts()

print("\nStudents by city:")
print(city_counts)

# ------------------------------------------------------------
# Problem 13: Missing values
# ------------------------------------------------------------
# Create this DataFrame:
#
# name:  A, B, C, D
# score: 80, missing, 90, missing
#
# 1. Find missing values.
# 2. Fill missing scores with 0.
# 3. Create another version where missing rows are removed.
#
# Solution:
missing_df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "score": [80, None, 90, None]
})

print("\nMissing values:")
print(missing_df.isnull())

filled = missing_df.fillna(0)

print("\nFilled:")
print(filled)

removed = missing_df.dropna()

print("\nRows with missing values removed:")
print(removed)

# ------------------------------------------------------------
# Problem 14: Sales analysis
# ------------------------------------------------------------
# Create a DataFrame with:
# product, price, quantity
#
# Add a revenue column:
# revenue = price * quantity
#
# Find total revenue for each product.
#
# Solution:
sales = pd.DataFrame({
    "product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone"],
    "price": [70000, 30000, 65000, 25000, 32000],
    "quantity": [2, 4, 1, 3, 2]
})

sales["revenue"] = sales["price"] * sales["quantity"]

print("\nSales:")
print(sales)

print("\nRevenue by product:")
print(sales.groupby("product")["revenue"].sum())