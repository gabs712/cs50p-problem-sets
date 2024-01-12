def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.replace('$', ''))
    d = round(d, 1)
    return d


def percent_to_float(p):
    p = float(p.replace('%', ''))
    p = p * .01
    return p


main()