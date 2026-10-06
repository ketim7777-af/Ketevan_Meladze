
scores = [45, 82, 67, 38, 90, 55, 98]

passing_scores = list(filter(lambda score: score >= 50, scores))
print(passing_scores)

bonus_scores = (list(map(lambda score: min(score + 5, 100), passing_scores)))
print(bonus_scores)


# ბოლო რიცხვი ეწერა 72, მე გადავაკეთე 98–ად, რომ მენახა, 100–ზე მეტს ხომ არ დაწერდა
# ბონუსური 5 ქულის მიმატების შემდეგ.

