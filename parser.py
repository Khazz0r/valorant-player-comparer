import csv
from constants import KD_5, KAST_6, ADR_7, KPR_8, APR_9, HS_12, CL_13


def parse(*args) -> dict:
    player_dict = {}

    with open("VRLMaster.csv", "r") as file:
        csv_reader = list(csv.reader(file))
        header_row = csv_reader[0]

        for row in csv_reader:
            for i, arg in enumerate(args):
                if row[0] == arg:
                    player_dict[f"Player {i + 1}"] = {}
                    for j in range(len(row)):
                        player_dict[f"Player {i + 1}"][header_row[j]] = row[j]
    return player_dict


def compare(player_dict):
    pass
                    