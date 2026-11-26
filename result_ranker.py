students = [("Aarav", 88),("Diya", 42),("Rohan", 74),("Meera", 95),("Kabir", 35),]

get_status = lambda marks: "Pass" if marks >= 50 else "Fail"

# Highest marks pehle (reverse=True)
ranked = sorted(students, key=lambda student: student[1], reverse=True)

report = [
    f"{rank}. {name} - {marks} ({get_status(marks)})"
    for rank, (name, marks) in enumerate(ranked, start=1)
]

for line in report:
    print(line)