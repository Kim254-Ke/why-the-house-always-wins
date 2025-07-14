# The code below tries to simulate placing multiple bets and testing the financial outcomes using two different strategies
# and starting from a bankroll of 100.

# The code generates a random number of outputs represented by N and Y where N are the games that lost and Y those that
# won. It is also set up to represent a winning rate of 20%

import random
import matplotlib.pyplot as plt

last = 10000

N_result = ["N"] * 8 * (10 ** 6)
Y_result = ["Y"] * 2 * (10 ** 6)
result_12 = N_result + Y_result
random.shuffle(result_12)
result_12 = result_12[:last]

print("result_12: ", result_12)
odds = 4.75
# House edge = 5%
Bankroll = 100
uniform_strategy_Bankroll_g = []
proportional_strategy_Bankroll_g = []


def uniform_bet_strategy(uniform_strategy_Bankroll_g: list[float], Bankroll: float) -> list[float]:
    for i in result_12:
        if i == "N":
            Bankroll -= 1
            if Bankroll >= 0:
                uniform_strategy_Bankroll_g.append(Bankroll)
            else:
                print("Bankroll depleted!!!!!!!!!!!!!!!!!!!")
                break

        elif i == "Y":
            Bankroll += (1 * (odds - 1))
            uniform_strategy_Bankroll_g.append(Bankroll)

    return uniform_strategy_Bankroll_g


def proportional_bet_strategy(proportional_strategy_Bankroll_g: list[float], Bankroll: float) -> list[float]:
    # This strategy uses 1% of the bankroll for each bet, and that is why I am using Bankroll -= Bankroll / 100 as Bankroll / 100 represents the cost per bet.

    for i in result_12:
        if i == "N":
            Bankroll -= Bankroll / 100
            if Bankroll >= 0:
                proportional_strategy_Bankroll_g.append(Bankroll)
            else:
                print("Bankroll depleted!!!!!!!!!!!!!!!!!!!")
                break

        elif i == "Y":
            Bankroll += ((Bankroll / 100) * (odds - 1))
            proportional_strategy_Bankroll_g.append(Bankroll)

    return proportional_strategy_Bankroll_g


uniform_bet_strategy(uniform_strategy_Bankroll_g, Bankroll)
proportional_bet_strategy(proportional_strategy_Bankroll_g, Bankroll)

# print("uniform_strategy_Bankroll_g: ", uniform_strategy_Bankroll_g)
# print("proportional_strategy_Bankroll_g: ", proportional_strategy_Bankroll_g)

games_proportional = list(range(1, len(proportional_strategy_Bankroll_g) + 1))
games_uniform = list(range(1, len(uniform_strategy_Bankroll_g) + 1))

plt.figure(figsize=(10, 5), dpi=350) # High DPI is used for sharpness
plt.figure(figsize=(10, 5))
plt.plot(games_proportional, proportional_strategy_Bankroll_g, marker='o', linestyle='-', color='red', label='Bankroll', linewidth=1, alpha=1, antialiased=False)
plt.plot(games_uniform, uniform_strategy_Bankroll_g, marker='o', linestyle='-', color='blue', label='Bankroll', linewidth=1, alpha=1, antialiased=False)
plt.title('Bankroll vs. Number of Games')
plt.xlabel('Number of Games')
plt.ylabel('Bankroll ($)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
