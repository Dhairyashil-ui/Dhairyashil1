def dollars_to_float(dollars):
    # Convert the input dollar amount (string) to a float
    return float(dollars.replace('$', '').strip())

def percent_to_float(percent):
    # Convert the input percentage (string) to a float and divide by 100
    return float(percent.replace('%', '').strip()) / 100

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = dollars * percent  # Calculate the tip
    print(f"Leave ${tip:.2f}")  # Format the output to two decimal places

main()
