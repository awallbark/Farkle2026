import random
from constants import ONE, FIVE, THREE_OF_A_KIND, FOUR_OF_A_KIND, FIVE_OF_A_KIND, SIX_OF_A_KIND, STRAIGHT, THREE_PAIRS, TWO_TRIPLETS, FOUR_OF_A_KIND_AND_A_PAIR
import Roll


player_roll = Roll.Roll()

first_roll = player_roll.roll_dice()

sort_roll = player_roll.determine_scoring_dice(first_roll)

second_roll = player_roll.reroll_dice(sort_roll)





# ones_count = scoring_dice.count(1)
# fives_count = scoring_dice.count(5)
#
#
# if ones_count == 3:
#     roll_score += THREE_OF_A_KIND * 3
# elif ones_count == 4:
#     roll_score += FOUR_OF_A_KIND
# elif ones_count == 5:
#     roll_score += FIVE_OF_A_KIND
# elif ones_count == 6:
#     roll_score += SIX_OF_A_KIND
# elif ones_count == 1:
#     roll_score += ONE
# elif ones_count == 2:
#     roll_score += ONE * 2
#
#
#
# if fives_count == 3:
#     roll_score += THREE_OF_A_KIND * 5
# elif fives_count == 4:
#     roll_score += FOUR_OF_A_KIND
# elif fives_count == 5:
#     roll_score += FIVE_OF_A_KIND
# elif fives_count == 6:
#     roll_score += SIX_OF_A_KIND
# elif fives_count == 1:
#     roll_score += FIVE
# elif fives_count == 2:
#     roll_score += FIVE * 2
# print(f"Your score is {roll_score}")
#
#
#
#
# reroll_ones_count = reroll.count(1)
# reroll_fives_count = reroll.count(5)
#
# if reroll_ones_count == 1:
#     roll_score += 100
# elif reroll_ones_count == 2:
#     roll_score += 200
# elif reroll_ones_count == 3:
#     roll_score += 300
# elif reroll_ones_count == 4:
#     roll_score += 1000
# elif reroll_ones_count == 5:
#     roll_score += 2000
# elif reroll_ones_count == 6:
#     roll_score += 3000
#
# if reroll_fives_count == 1:
#     roll_score += 50
# elif reroll_fives_count == 2:
#     roll_score += 100
# elif reroll_fives_count == 3:
#     roll_score += 500
# elif reroll_fives_count == 4:
#     roll_score += 1000
# elif reroll_fives_count == 5:
#     roll_score += 2000
# elif reroll_fives_count == 6:
#     roll_score += 3000
#
# print(f"Your new score with the additional points is {roll_score}")




