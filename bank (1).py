number =input("greeting: ")
if number.lower() == "hello" or number.lower() == " hello " or number.lower() == "hello, newman":
    print("$0")
elif number.lower().startswith('h'):
    print("$20")

else:
    print("$100")

