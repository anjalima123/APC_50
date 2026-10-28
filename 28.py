scores = [45, 100, 75, 120, 30, 55, 90, 110, 40, 65]
print("Highest score:", max(scores))
print("Lowest score:", min(scores))
print("Total runs:", sum(scores))
print("Average runs:", sum(scores) / len(scores))
centuries = 0
half_centuries = 0
for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)