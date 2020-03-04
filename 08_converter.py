# conversion function


# *** Functions go here ***
def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in unit_central:
        mult_by = dictionary.get(unit)
        how_much = how_much * mult_by * conversion_factor

    return how_much

def unit_checker ():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    ounce = ["oz", "fluid", "ounce", "fluid ounce"]
    cup = ["c","cup","C"]
    pint = ["p", "pt", "fluid pint", "pint"]
    quart = ["q", "qt", "quart", "fluid quart"]
    ml = ["ml", "milliliter", "millilitre", "cc"]
    l = ["liter", "litre", "l", "L"]
    dl = ["deciliter", "decilitre", "dl", "dL"]
    pound = ["pound", "lb", "#"]

    if unit_tocheck == "":
        print("you chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in ml:
        return "ml"
    elif unit_tocheck.lower() in l:
        return "l"
    elif unit_tocheck.lower() in dl:
        return "dl"
    elif unit_tocheck.lower() in pound:
        return "pound"


# *** Main Routine Goes here ***
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    # Get unit and change it to match dictionary
    unit = unit_checker()

    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)

    keep_going = input("press <enter> to continue or 'q' to quit.")