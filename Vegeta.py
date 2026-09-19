import random

name = "Goku"
power = random.randint(1, 10000)

print("*Vegeta scans{name}...*")
print(f"power level: {power}")

if power > 9000:
    print("Vegeta: IT's OVER 9000")
else:
    print("Vegeta: Pathetic.")
