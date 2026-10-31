timetable = [
    ("Monday", "9AM", "Maths"),
    ("Monday", "10AM", "Physics"),
    ("Tuesday", "9AM", "English"),
    ("Monday", "9AM", "Chemistry")
]

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        if timetable[i][0:2] == timetable[j][0:2]:
            print("Clash:", timetable[i], timetable[j])

print("Timetable Checked")