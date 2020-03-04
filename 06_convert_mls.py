# ask user for amount
# ask user for Unit
# check that unit is in dictionary

# if unit is dictionary, convert to mL

# if no unit given / unit is unknown, leave as it.


# *** Functions go here ***
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

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in ml {:.2f}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("press <enter> to continue or 'q' to quit.")