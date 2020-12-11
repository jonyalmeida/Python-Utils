def hexa_to_decimal(hex_string):
    result = []
    hex_string = reversed(hex_string)
    convertions = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    for char in hex_string:
        try:
            result.append(int(char))
        except not char.isnumeric():
            for key in convertions:
                if key == char:
                    result.append(int(convertions[char]))
                else:
                    continue
    result = [*reversed(result)]
    return result


# string = input("Enter Hex-String: ").upper()
string = "8A3DE9"
print(hexa_to_decimal(string))
