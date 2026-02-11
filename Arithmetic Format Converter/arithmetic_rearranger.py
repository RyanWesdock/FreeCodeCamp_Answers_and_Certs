def arithmetic_rearranger(problems, answer=False):
    addends, addends2, dashes, sums = "", "", "", ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        addend, operator, addend2 = problem.split(" ")
        if not (addend.isnumeric() and addend2.isnumeric()):
            return "Error: Numbers must only contain digits."
        elif max(len(addend), len(addend2)) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        else:
            width = max(len(addend), len(addend2))
            addends += f"  {addend:>{width}}    "
            addends2 += f"{operator} {addend2:>{width}}    "
            dashes += f"--{"-":->{width}}    "
            sums += f"  {int(addend) + int(addend2)}    "
    if not answer:
        return f'{addends.rstrip()}\n{addends2.rstrip()}\n{dashes.rstrip()}'
    else:
        return f'{addends.rstrip()}\n{addends2.rstrip()}\n{dashes.rstrip()}\n{sums.rstrip()}'

