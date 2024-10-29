def main():


    name= input("what's your name? ")

    name = name.strip()
    parts = name.split()
    if len(parts) >= 3:
        first_name = parts[0]
        second_name = parts[1]
        last_name = parts[2]
        print(f"hello, {last_name} {first_name} {second_name} from com A")
    else:
        print("i think you are not the owner")


if __name__ == "__main__":
    main()
