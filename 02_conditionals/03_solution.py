# Assign Letter Grade based on student's score

student_score = int(input("Enter your score: "))

# MY WAY

# if student_score > 100 :
#     print("! Wrong Grading")
# else:
#     grade = "A" if student_score >= 90 else "B" if student_score >= 80 else "C" if student_score >= 70 else "D" if student_score >= 60 else "E" if student_score >= 50 else "F"
#     print(f"Your Grade: {grade}")

# GURUJI WAY

if student_score >= 101 :
    print("Wrong score entered.")
    exit()                              # to terminate python program

if student_score >= 90 :
    grade = "A"
elif student_score >= 80 :
    grade = "B"
elif student_score >= 70 :
    grade = "C"
elif student_score >= 60 :
    grade = "D"
elif student_score >= 50 :
    grade = "E"
else:
    grade = "F"
print("Your grade: ", grade)



