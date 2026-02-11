import re


def i_before_c(word):
    if re.search("^.*(cei)|(^cie)", word):
        return True
    else:
        return False


print(i_before_c("omniscient"))

# Okay, I've learned something here. Python doesn't have a /g flag the way
# JS does. Search seems to be the equivalent, at least in this case.