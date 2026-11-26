def analyze_marks(students_marks, pass_mark=50):
    # List comprehension: pass_mark ya usse zyada marks wale students
    passed = [name for name, marks in students_marks.items() if marks >= pass_mark]

    # Dictionary comprehension: har student ke marks ko grade mein badalna
    grades = {
        name: (
            "A" if marks >= 85 else
            "B" if marks >= 60 else
            "C" if marks >= pass_mark else
            "F"
        )
        for name, marks in students_marks.items()
    }

    return passed, grades


if __name__ == "__main__":
    marks_data = {
        "Aarav": 88,
        "Diya": 42,
        "Rohan": 74,
        "Meera": 95,
        "Kabir": 35,
    }

    passed_list, grade_dict = analyze_marks(marks_data)
    print("Passed Students:", passed_list)
    print("Grade Map:", grade_dict)