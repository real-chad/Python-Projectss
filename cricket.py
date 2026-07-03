scores = [14,76,42,36,98,0,5,0]
ducks = []

good_scores = []

for i in scores:
    if i == 0:
        ducks.append(i)
    else:
        good_scores.append(i)
highest_score = good_scores[0]
highest_index = 0
for i in range(len(good_scores)):
    if good_scores[i] > highest_score:
        highest_score = good_scores[i]
        highest_index = i
print(f"Total number of ducks are {len(ducks)}")
print(f"The good scores are {good_scores}")
print(f"The highest score is {highest_score} at index {highest_index}")

