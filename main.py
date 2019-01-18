def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for dice1roll in dice1:
        for dice2roll in dice2:

            if dice1roll > dice2roll:
                dice1_wins += 1
            elif dice2roll > dice1roll:
                dice2_wins += 1

    return (dice1_wins, dice2_wins)

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    roundWinner = []
    details = dict()
    numberofdices= len(dices)
    comparison_control = numberofdices - 1

    for firstDice in range(comparison_control):
        for secondDice in range(firstDice + 1,len(dices)):
            results = count_wins(dices[firstDice], dices[secondDice])
            if(results[0] < results[1]):
                roundWinner.append(secondDice)
                details[firstDice] = secondDice
            elif(results[0] > results[1]):
                roundWinner.append(firstDice)
                details[secondDice] = firstDice
            else:
                roundWinner.append('draw')


    for die in range(len(dices)):
        occurrences = roundWinner.count(die)
        if ((occurrences/numberofdices) > 0.5):
            return die

    return details

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    bestDiceOutput = find_the_best_dice(dices)

    strategy = dict()

    if(type(bestDiceOutput) is int):
        strategy["choose_first"] = True
        strategy["first_dice"] = bestDiceOutput
    else:
        strategy["choose_first"] = False
        strategy.update(bestDiceOutput)

    return strategy

dice1 = [1, 1, 6, 6, 8, 8]
dice2 = [2, 2, 4, 4, 9, 9]
dice3 = [3, 3, 5, 5, 7, 7]

dices = [dice1, dice2, dice3]

print(compute_strategy(dices))