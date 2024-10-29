# nutrition.py

# Dictionary to store the calorie information for various fruits
calories = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
    "kiwifruit": 90,  # Added Kiwifruit
    "pear": 100       # Added Pear
}

# Get user input
fruit = input("Enter a fruit: ").strip().lower()  # Normalize input by stripping whitespace and converting to lowercase

# Output the calorie information if the fruit is found
if fruit in calories:
    print(f"Calories: {calories[fruit]}")
else:

    pass
