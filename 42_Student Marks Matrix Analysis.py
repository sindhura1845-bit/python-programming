marks = [
    [80, 75, 90],
    [60, 70, 65],
    [85, 95, 88]
]

for i, row in enumerate(marks):
    print("Student", i + 1, "Total:", sum(row))

for j in range(3):
    total = sum(marks[i][j] for i in range(3))
    print("Subject", j + 1, "Average:", total / 3)