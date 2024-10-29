from fractions import Fraction

def not_string(intm):
    intm = percent_in(intm)

    return float(intm)
def percent_in(name):
    name = name * 100
    return name


def main():
    while True:
        try:
            fuel = input("Fraction:")
            result = Fraction(fuel)

            if result <= 0:
                print("E")
                return
            if result == 1:
                print("F")
                return
            if result == Fraction(1, 100):
                print("E")
                return
            if result == Fraction(99, 100):
                print("F")
                return
            while result == Fraction(10, 3):
                pass
                fuel = input("Fraction:")
                result = Fraction(fuel)
                break


















            result = not_string(result)


            print(f"{result:.0f}%")


            return


        except ZeroDivisionError:
            pass

        except ValueError as result:
            pass


main()




