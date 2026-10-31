marks = [85, 45, 30, 70, 25]

for mark in marks:
    if mark >= 60:
        print(mark, "- Low Risk")
    elif mark >= 40:
        print(mark, "- Medium Risk")
    else:
        print(mark, "- High Risk")
        