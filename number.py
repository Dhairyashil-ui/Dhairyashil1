distances = {
    "mars": "3",
    "sun" : "1"
}
def main():
    name = input("enter distances")
    ram = float(distances(name))
    m = convert(ram)
    print("{m}m away")
def convert(ram):
    return ram * 2

if __name__ == "__main__":
    main()
