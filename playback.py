def main():


    while True:
        names = input("Enter names separated by commas: ")
        name_list = names.split(",")

        for name in name_list:
            name = name.strip()  # Remove any extra spaces

            # Split name into first and last name (if applicable)
            parts = name.split()
            if len(parts) >= 3:
                first_name = parts[0]
                last_name = parts[1]
                home_name = parts[2]
                print(f"{first_name}...{last_name}...{home_name}")
                return

            if len(parts) >= 2:
                first_name = parts[0]
                last_name = parts[1]
                print(f"{first_name}...{last_name}")
                return
            else:
                print(f"{name}...{name}...{name}")  # In case there's no surname
                return


        # Optionally, break out of the loop
        # Uncomment the following line to stop after one iteration
        # break

if __name__ == "__main__":
    main()

    
