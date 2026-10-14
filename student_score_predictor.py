"""Machine Learning: Student Practice Score Predictor
Algorithm: Linear Regression. Sample values are illustrative only.
"""
from sklearn.linear_model import LinearRegression

# Input columns: [study hours per day, attendance percentage]
X = [
    [1, 60], [2, 65], [2, 75], [3, 70],
    [4, 80], [4, 90], [5, 85], [6, 95]
]
# Illustrative practice scores out of 100
y = [42, 48, 55, 58, 68, 76, 78, 90]

model = LinearRegression()
model.fit(X, y)

print("=" * 46)
print(" STUDENT PRACTICE SCORE PREDICTOR (ML)")
print("=" * 46)
print("Classroom demo only — not for real academic decisions.")

try:
    hours = float(input("Study hours per day (0 to 12): "))
    attendance = float(input("Attendance percentage (0 to 100): "))

    if not (0 <= hours <= 12 and 0 <= attendance <= 100):
        print("Please enter study hours from 0–12 and attendance from 0–100.")
    else:
        score = float(model.predict([[hours, attendance]])[0])
        score = max(0, min(100, score))
        print(f"Estimated practice score: {score:.1f}/100")
        print("This is an approximate result from a small example dataset.")
except ValueError:
    print("Invalid input. Please enter numbers.")

print("\nAlgorithm: Linear Regression")
print("Type: Supervised Machine Learning")
