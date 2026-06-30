import random

roll = []

die_count = 0

while die_count < 6:
    die = random.randint(1, 6)
    roll.append(die)
    die_count += 1

roll.sort()
print(f"Initial sorted roll {roll}")

scoring_dice = []
for number in roll:
    if number in [1, 5]:
        scoring_dice.append(number)

print(f"Roll after pulling out 1s and 5s {roll}")
print(f"Scoring dice {scoring_dice}")

ones_count = scoring_dice.count(1)
fives_count = scoring_dice.count(5)

roll_score = 0

if ones_count == 1:
    roll_score += 100
elif ones_count == 2:
    roll_score += 200
elif ones_count == 3:
    roll_score += 300
elif ones_count == 4:
    roll_score += 1000
elif ones_count == 5:
    roll_score += 2000
elif ones_count == 6:
    roll_score += 3000

if fives_count == 1:
    roll_score += 50
elif fives_count == 2:
    roll_score += 100
elif fives_count == 3:
    roll_score += 500
elif fives_count == 4:
    roll_score += 1000
elif fives_count == 5:
    roll_score += 2000
elif fives_count == 6:
    roll_score += 3000

print(f"Your score is {roll_score}")




