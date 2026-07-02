import random
class Roll():
    def __init__(self):
        self.roll_score = 0
        self.roll = []
        self.scoring_dice = []
        self.active_roll = []
        self.dice_to_reroll = []
        self.dice_to_keep = []

    def roll_dice(self):
        die_count = 0
        while die_count < 6:
            die = random.randint(1, 6)
            self.roll.append(die)
            die_count += 1
        print(f"Initial sorted roll {self.roll}")
        self.roll.sort()
        return self.roll

    def determine_scoring_dice(self, roll_dice):
        for number in roll_dice:
            if number in [1, 5]:
                self.scoring_dice.append(number)
        if len(self.scoring_dice) == 0:
            self.farkle(self.scoring_dice)
        elif len(self.scoring_dice) != 0:
            while roll_dice.count(1) > 0 or roll_dice.count(5) > 0:
                if 1 in roll_dice:
                    roll_dice.remove(1)
                if 5 in roll_dice:
                    roll_dice.remove(5)
        self.dice_to_reroll = roll_dice
        print(f"Roll after pulling out 1s and 5s {self.dice_to_reroll}")
        self.scoring_dice.sort()
        print(f"Scoring dice {self.scoring_dice}")

        return self.scoring_dice


    def reroll_dice(self, roll_dice):
        roll_again = input("Do you want to roll the remaining dice? y/n")

        if roll_again == 'y':
            dice_to_roll_again = len(self.dice_to_reroll)
            while dice_to_roll_again > 0:
                die = random.randint(1, 6)
                self.active_roll.append(die)
                dice_to_roll_again -= 1
        self.active_roll.sort()
        print(f"This is what you just rerolled {self.active_roll}")
        return self.active_roll

    def farkle(self, scoring_dice):
        if len(scoring_dice) == 0:
            self.roll_score = 0
            print("You Farkled!")


# roll = Roll()
# dice = [4, 3, 6, 2, 5, 6]
#
# roll.determine_scoring_dice(dice)



