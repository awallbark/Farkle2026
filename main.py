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

while roll.count(1) > 0 or roll.count(5) > 0:
    if 1 in roll:
        roll.remove(1)
    if 5 in roll:
        roll.remove(5)


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

roll_again = input("Do you want to roll the remaining dice? y/n")

reroll = []

if roll_again == 'y':
    dice_to_roll_again = len(roll)
    while dice_to_roll_again > 0:
        die = random.randint(1, 6)
        reroll.append(die)
        dice_to_roll_again -= 1


print(reroll)

reroll_ones_count = reroll.count(1)
reroll_fives_count = reroll.count(5)

if reroll_ones_count == 1:
    roll_score += 100
elif reroll_ones_count == 2:
    roll_score += 200
elif reroll_ones_count == 3:
    roll_score += 300
elif reroll_ones_count == 4:
    roll_score += 1000
elif reroll_ones_count == 5:
    roll_score += 2000
elif reroll_ones_count == 6:
    roll_score += 3000

if reroll_fives_count == 1:
    roll_score += 50
elif reroll_fives_count == 2:
    roll_score += 100
elif reroll_fives_count == 3:
    roll_score += 500
elif reroll_fives_count == 4:
    roll_score += 1000
elif reroll_fives_count == 5:
    roll_score += 2000
elif reroll_fives_count == 6:
    roll_score += 3000

print(f"Your new score with the additional points is {roll_score}")




