score = int(input("Enter Student's score: "))
if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif 80 <= score < 90:
    grade = "B"
    message = "Good job!"
elif 70 <= score < 80:
    grade = "C"
    message = "Satisfactory"
elif 60 <= score < 70:
    grade = "D"
    message = "Needs improvement"
else:
    grade = "F"
    message = "Study more!" 
print("Grade:", grade)
print("Message:", message)