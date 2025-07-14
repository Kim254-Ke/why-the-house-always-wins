# The code below tries to simulate placing multiple bets and testing the financial outcomes using two different strategies
# and starting from a bankroll of 100.

# The data used was obtained from https://footystats.org/download-stats-csv, Premier league 2018/ 2019 CSV

import matplotlib.pyplot as plt
import pandas as pd

file_path = "C:/Users/USER/Downloads/england-premier-league-matches-2018-to-2019-stats.csv"

df = pd.read_csv(file_path)

df['odds_ft_home_team_win'] = df['odds_ft_home_team_win'].fillna('Unknown')
df['odds_ft_draw'] = df['odds_ft_draw'].fillna('Unknown')
df['odds_ft_away_team_win'] = df['odds_ft_away_team_win'].fillna('Unknown')

df['home_team_goal_count'] = df['home_team_goal_count'].fillna('Unknown')
df['away_team_goal_count'] = df['away_team_goal_count'].fillna('Unknown')

home_odds_list = df['odds_ft_home_team_win'].tolist()
draw_odds_list = df['odds_ft_draw'].tolist()
away_odds_list = df['odds_ft_away_team_win'].tolist()

home_goals = df['home_team_goal_count'].tolist()
away_goals = df['away_team_goal_count'].tolist()

result_12 = []
odds = 4.75
# House edge = 5%
Bankroll = 100
uniform_strategy_Bankroll_g = []
proportional_strategy_Bankroll_g = []


def uniform_bet_strategy(uniform_strategy_Bankroll_g: list[float], Bankroll: float) -> list[float]:
    for q in result_12:
        if q == "N":
            Bankroll -= 1
            if Bankroll >= 0:
                uniform_strategy_Bankroll_g.append(Bankroll)
            else:
                print("Bankroll depleted!!!!!!!!!!!!!!!!!!!")
                break

        elif q == "Y":
            Bankroll += (1 * (odds - 1))
            uniform_strategy_Bankroll_g.append(Bankroll)

    return uniform_strategy_Bankroll_g


def proportional_bet_strategy(proportional_strategy_Bankroll_g: list[float], Bankroll: float) -> list[float]:
    # This strategy uses 1% of the bankroll for each bet, and that is why I am using Bankroll -= Bankroll / 100 as Bankroll / 100 represents the cost per bet.

    for r in result_12:
        if r == "N":
            Bankroll -= Bankroll / 100
            if Bankroll >= 0:
                proportional_strategy_Bankroll_g.append(Bankroll)
            else:
                print("Bankroll depleted!!!!!!!!!!!!!!!!!!!")
                break

        elif r == "Y":
            Bankroll += ((Bankroll / 100) * (odds - 1))
            proportional_strategy_Bankroll_g.append(Bankroll)

    return proportional_strategy_Bankroll_g


def graph_plotting_function(games_proportional: list, proportional_strategy_Bankroll_g: list, games_uniform: list,
                            uniform_strategy_Bankroll_g: list):
    print("plotting begins")
    plt.figure(figsize=(10, 5), dpi=350)  # High DPI is used for sharpness
    plt.figure(figsize=(10, 5))
    plt.plot(games_proportional, proportional_strategy_Bankroll_g, marker='o', linestyle='-', color='red',
             label='Bankroll', linewidth=1, alpha=1, antialiased=False)
    plt.plot(games_uniform, uniform_strategy_Bankroll_g, marker='o', linestyle='-', color='blue', label='Bankroll',
             linewidth=1, alpha=1, antialiased=False)
    plt.title('Bankroll vs. Number of Games')
    plt.xlabel('Number of Games')
    plt.ylabel('Bankroll ($)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    print("plotting complete")


if len(home_odds_list) != len(draw_odds_list) or len(home_odds_list) != len(away_odds_list) or len(
        draw_odds_list) != len(away_odds_list):
    #print("len(draw_odds_list): ", len(draw_odds_list))
    #print("len(home_odds_list): ", len(home_odds_list))
    #print("len(away_odds_list): ", len(away_odds_list))

    print("ERROR. THE RESPECTIVE LENGTHS DO NOT MATCH.")

else:
    for t in list(range(1, (len(home_odds_list) + 1))):
        if 4.9 > home_odds_list[t - 1] > 4.6:
            if home_odds_list[t - 1] != "Unknown" and home_goals[t - 1] != "Unknown" and away_goals[t - 1] != "Unknown":
                if home_goals[t - 1] > away_goals[t - 1]:
                    result_12.append("Y")
                else:
                    result_12.append("N")

        if 4.9 > draw_odds_list[t - 1] > 4.6:
            if draw_odds_list[t - 1] != "Unknown" and home_goals[t - 1] != "Unknown" and away_goals[t - 1] != "Unknown":
                if home_goals[t - 1] == away_goals[t - 1]:
                    result_12.append("Y")
                else:
                    result_12.append("N")

        if 4.9 > away_odds_list[t - 1] > 4.6:
            if away_odds_list[t - 1] != "Unknown" and home_goals[t - 1] != "Unknown" and away_goals[t - 1] != "Unknown":
                if home_goals[t - 1] < away_goals[t - 1]:
                    result_12.append("Y")
                else:
                    result_12.append("N")

    print("result_12: ", result_12)
    print(len(result_12))
    print(result_12.count("Y"))
    print("win_rate(as a percentage): ", (result_12.count("Y") / len(result_12))) # This shows the win rate in order to compare if it matches with the predefined probability.

    uniform_bet_strategy(uniform_strategy_Bankroll_g, Bankroll)
    proportional_bet_strategy(proportional_strategy_Bankroll_g, Bankroll)

    # print("uniform_strategy_Bankroll_g: ", uniform_strategy_Bankroll_g)
    # print("proportional_strategy_Bankroll_g: ", proportional_strategy_Bankroll_g)

    games_proportional = list(range(1, len(proportional_strategy_Bankroll_g) + 1))
    games_uniform = list(range(1, len(uniform_strategy_Bankroll_g) + 1))
    graph_plotting_function(games_proportional, proportional_strategy_Bankroll_g, games_uniform, uniform_strategy_Bankroll_g)
    #
