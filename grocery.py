from collections import Counter
def main():

    game = []
    while True:

        name = input("")
        if name == "":
            break


        game.append(name)
    name_Count = Counter(game)
    result = []
    for name,Count in name_Count.items():
        result.append(f"{Count} {name.upper()}")
    for atom in result:
        print(atom)





if __name__ == "__main__":
    main()
