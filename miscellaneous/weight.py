weight = int(input("What is your weight ? : "))
unit = input("(L)bs or (K)gs : ")


def weight_convert(weight, unit):
    if unit.upper() == "L":
        final_weight = weight * 0.45
        unit = 'kilos'

    if unit.upper() == "K":
        final_weight = weight // 0.45
        unit = 'pounds'
    output = f"You are {final_weight} {unit}"
    return output


print(weight_convert(weight, unit))
