# Function equivalent to passing code for ceaser cipher challenge for fcc js certification


def rot13(s):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    punct_list = [" ", ",", "!", "?", "."]
    decoded_s = ""
    for letter in s:
        if letter in punct_list:
            decoded_s += letter
        elif 0 <= alphabet.index(letter) <= 12:
            decoded_ind = alphabet.index(letter) + 13
            decoded_s += alphabet[decoded_ind]
        else:
            decoded_ind = alphabet.index(letter) - 13
            decoded_s += alphabet[decoded_ind]
    return decoded_s


print(rot13("SERR PBQR PNZC!"))

# Note: whereas javascript can take a string like alphabet and turn it into a list
# using split() with an empty seperator, Python cannot. Nor does it need to, since the
# same effect can be achieved using list().

# the only other new difference here -- alphabet.index instead of alphabet.indexOf()