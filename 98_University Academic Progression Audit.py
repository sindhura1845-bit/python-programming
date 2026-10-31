marks = [75, 65, 35]
attendance = 80
prerequisite = True

for mark in marks:
    if mark >= 40 and attendance >= 75 and prerequisite:
        print(mark, "- Eligible")
    else:
        print(mark, "- Not Eligible")