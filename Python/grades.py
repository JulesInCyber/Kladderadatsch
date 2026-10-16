names = ["Anna", "Ben", "Cem"]
scores = [87, 54, 92]

score_by_name = {name: score for name, score in zip(names, scores)}

above_sixty = [name for name, score in zip(names, scores) if score >=60]

highscore = [score for score in zip(names, scores)]
highscore.sort(key=lambda tup: tup[1], reverse = True)

print(score_by_name)
print(above_sixty)

for i, (student, score) in enumerate(highscore, start=1):
    print(f"{i}. {student} ({score})")
