def valid_problem(name):
    names = ["HELLO" , "CS50" , "ECTO88" , "NRVOUS"]
    return name in names










def main():
    name = input("Plate: ")

    if valid_problem(name):
        print("Valid")


    else:
        print("Invalid")
main()
