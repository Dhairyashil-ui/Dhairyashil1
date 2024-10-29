def main():
    name_game = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total_price = 0
    for i in range(3):
            try:




                coin = input("Item: ").title()



                if coin in name_game:
                    total_price += name_game[coin]
                    print(f"Total: ${total_price:.2f}")












            except EOFError:
                print("enter valid value")
                break






if __name__ == "__main__":
    main()
