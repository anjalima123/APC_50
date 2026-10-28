x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 1

for i in range(1, n + 1):
    fact = 1
    power = 2 * i

    for j in range(1, power + 1):
        fact = fact * j

    term = (x ** power) / fact

    if i % 2 == 1:
        sum = sum - term
    else:
        sum = sum + term

print("Cosine series =", sum)