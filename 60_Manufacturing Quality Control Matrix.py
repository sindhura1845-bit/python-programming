quality = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
]

total = 0
defects = 0

for row in quality:
    for item in row:
        total += 1
        if item == 0:
            defects += 1

percentage = (defects / total) * 100

print("Total Products:", total)
print("Defective Products:", defects)
print("Defect Percentage:", percentage)
