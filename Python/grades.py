names = ["Anna", "Ben", "Cem"]
scores = [87, 54, 92]

score_by_name = {name: score for name, score in zip(names, scores)}

above_sixty = [s[0] for s in zip(names, scores) if s[1] >=60]

highscore = [s for s in zip(names, scores)]
highscore.sort(key=lambda tup: tup[1], reverse = True)

print(score_by_name)
print(above_sixty)

for i, student in enumerate(highscore, start=1):
    print(f"{i}. {highscore[i-1][0]} ({highscore[i-1][1]})")
