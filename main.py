import sys
import csv
from parser import parse, compare_players, print_result_compare, print_result_best, print_result_worst

def main():
    # Even though this is a csv that isn't changing, for practice I'm assuming it is a dynamically
    # changing csv created via data gotten from Riot's API
    if sys.argv[1].lower() == "get-best-player" or sys.argv[1].lower() == "get-worst-player":
        list_of_players = []
        with open("VRLMaster.csv", "r") as file:
            csv_reader = list(csv.reader(file))
        
        for row in csv_reader[1:]:
            list_of_players.append(row[0])
        
        players_dict = parse(list_of_players)
        best_player_list = compare_players(players_dict)

        if sys.argv[1].lower() == "get-best-player":
            print_result_best(best_player_list)
        else:
            print_result_worst(best_player_list)
    elif sys.argv[1].lower() == "compare-players":
        list_of_players = []
        list_of_players.append(input("Please input the first player you want to compare\n"))
        add_more_players = "y"

        while add_more_players == "y":
            list_of_players.append(input("Add the next player you want to compare\n"))
            add_more_players = input("Input 'y' if you want to add more players, otherwise input anything else\n")
            add_more_players.lower()

        players_dict = parse(list_of_players)
        best_player_list = compare_players(players_dict)
        print_result_compare(best_player_list)
    else:
        print("Invalid input, please input either 'get-best-player', 'get-worst-player', or 'compare-players\n")


main()
