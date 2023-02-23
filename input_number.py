def input_number(value):
    try:
        return float(input(value + ": "))
    except:
        print("Incorrect value!")
        return input_number(value)