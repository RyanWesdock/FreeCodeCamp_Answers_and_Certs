# Python Equivalent to the passing JS code
def palindrome(palindrome_string):
    new_string = ""
    for ch in palindrome_string:
        if ch.isalpha():
            new_string += ch
        else:
            pass
    if new_string == new_string[::-1]:
        return True
    else:
        return False
