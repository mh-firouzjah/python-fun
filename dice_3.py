"""Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
```
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point```
"""


def score(dice):
    dice = ''.join(map(str, dice))
    score = 0
    for i in range(1, 7):
        score += (dice.count(f'{i}') // 3) * (1000 if i == 1 else i * 100)

    score += dice.count(f'{1}') % 3 * 100
    score += dice.count(f'{5}') % 3 * 50
    return score
