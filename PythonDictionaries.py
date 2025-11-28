student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# for k, v in student_scores.items():
#     print(k, v)

student_grades = {}

for student, score in student_scores.items():
    if score < 70:
        student_grades[student] = "Fail"
    elif score > 70 and score <= 80:
        student_grades[student] = "Acceptable"
    elif score > 80 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding!"
    
print(student_grades)
    