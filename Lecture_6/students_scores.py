
scores = []
scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)
# scores.extend([45, 88, 92, 60, 75]) ასე ყველაფერი ერთად ემატება

scores.remove(45)

print(sum(scores) / len(scores))
print(max(scores))
print(min(scores))

scores.sort()

passed_scores = []
for num in scores:
    if num >= 60:
        passed_scores.append(num)
print(passed_scores)

