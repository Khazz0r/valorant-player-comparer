import sys
from parser import parse, compare

def main():
    if sys.argv[1] == "get-best-player":
        pass
    elif sys.argv[2] == "get-worst-player":
        pass
    
    player_dict = parse(sys.argv)

main()