country = input("Enter country: ")

match country.lower():
    case "uk":
        print("britania rules the world")
    case "usa":
        print("we are not dumb")
    case _:
        print("losers")
