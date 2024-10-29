d = int(input("ENTER: "))
for i in range(d):
    print("meow")

if (d == 0):
    while True:
        print("Type Again")
        break
elif(d < 0):
    while True:
        print("you are typing different negative integer")
        break
