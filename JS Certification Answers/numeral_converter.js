// FCC certification challenge to convert Arabic numerals to Roman numerals
function convertToRoman(num) {
    const numeralObject = {
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
    let outputString = ""
    for (const [key, value] of Object.entries(numeralObject).reverse()) {
        while (num - key >= 0) {
            num = num - key
            outputString += value
        }
    } return outputString
}
