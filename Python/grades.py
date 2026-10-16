names = ["Anna", "Ben", "Cem"]
scores = [87, 54, 92]

# Creating a dict using comprehension
score_by_name = {name: score for name, score in zip(names, scores)}

# Lists all students whose score is above 60
above_sixty = [name for name, score in zip(names, scores) if score >=60]

student_tuples = [score for score in zip(names, scores)]

student_tuples.sort(key=lambda tup: tup[1], reverse = True)

print(score_by_name)
print(above_sixty)

for i, (student, score) in enumerate(student_tuples, start=1):
    print(f"{i}. {student} ({score})")
