# Python equivalent to passing code for Roman Numeral Converter for FCC JS cert
def numeral_converter(num):
    numeral_dict = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    output = ""
    for k, v in reversed(numeral_dict.items()):
        while num - k >= 0:
            num = num - k
            output += v
    return output
