def main():
    coke_machine = int(input("enter value "))
    print("Amount Due:",coke_machine)

    while coke_machine > 0:
        try:
            coin = int(input("Insert Coin: "))
            coke_machine -= coin


            if  coke_machine < 0:
                print("Amount Due:",coke_machine)

        except ValueError:
            print("Please enter a valid integer coin value.")


if __name__ == "__main__":
    main()
