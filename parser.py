import csv
from constants import KD, KAST, ADR, KPR, APR, HS_PERCENT, CL_PERCENT


def parse(list_of_players) -> dict:
    players_dict = {}

    with open("VRLMaster.csv",  mode="r", encoding="utf-8-sig") as file:
        csv_reader = list(csv.reader(file))
        header_row = csv_reader[0]

    for row in csv_reader:
        for i, player in enumerate(list_of_players):
            if row[0].lower() == player.lower():
                players_dict[f"Player {i + 1}"] = {}
                for j in range(len(row)):
                    players_dict[f"Player {i + 1}"][header_row[j]] = row[j]
    return players_dict


def compare_players(players_dict):
    best_player_list = []
    for player_name, stats in players_dict.items():
        all_stats = (
            float(stats[KD]), 
            float(stats[KAST]), 
            float(stats[ADR]), 
            float(stats[KPR]), 
            float(stats[APR]), 
            float(stats[HS_PERCENT]), 
            float(stats[CL_PERCENT])
            )
        players_dict[player_name]["total_score"] = (sum(all_stats))
        best_player_list.append(players_dict[player_name])

    best_player_list.sort(key=lambda player: player["total_score"], reverse=True)

    return best_player_list


def print_result_best(best_player_list):
    best_player = best_player_list[0]
    print(
f'''
The best player is {best_player["Ign"]} on team {best_player["Team"]}
K:D: {best_player[KD]}
KAST: {best_player[KAST]}
ADR: {best_player[ADR]}
KPR: {best_player[KPR]}
APR: {best_player[APR]}
HS%: {best_player[HS_PERCENT]}
CL%: {best_player[CL_PERCENT]} 
''')


def print_result_worst(best_player_list):
    worst_player = best_player_list[-1]
    print(
f'''
The worst player is {worst_player["Ign"]} on team {worst_player["Team"]}
K:D: {worst_player[KD]}
KAST: {worst_player[KAST]}
ADR: {worst_player[ADR]}
KPR: {worst_player[KPR]}
APR: {worst_player[APR]}
HS%: {worst_player[HS_PERCENT]}
CL%: {worst_player[CL_PERCENT]} 
''')


def print_result_compare(best_player_list):
    for i, player in enumerate(best_player_list):
        print(
f'''
Player#{i + 1}:
{player["Ign"]} on team {player["Team"]}
K:D: {player[KD]}
KAST: {player[KAST]}
ADR: {player[ADR]}
KPR: {player[KPR]}
APR: {player[APR]}
HS%: {player[HS_PERCENT]}
CL%: {player[CL_PERCENT]}
''')
        if i < len(best_player_list) - 1:
            print("=" * 70)
           