def arithmetic_arranger(problem_list, demand=False):
  if len(problem_list) > 5:
      return "Error: Too many problems."
  else:
      try:
          for problem in problem_list:
              separated_list = problem.split(" ")
              first_number = int(separated_list[0])
              second_number = int(separated_list[2])
              operator = separated_list[1]
              if len(str(first_number)) > 4 or len(str(second_number)) > 4:
                  return "Error: Numbers cannot be more than four digits."
              elif operator != "+" and operator != "-":
                  return "Error: Operator must be '+' or '-'."
      except ValueError:
          return "Error: Numbers must only contain digits."
      else:
          first_row = []
          second_row = []
          third_row = []
          fourth_row = []
          part_1 = ""
          part_2 = ""
          part_3 = ""
          part_4 = ""
          for problem in problem_list:
              separated_list = problem.split(" ")
              first_number = int(separated_list[0])
              second_number = int(separated_list[2])
              operator = separated_list[1]
              if operator == "+":
                  total = first_number + second_number
              else:
                  total = first_number - second_number
              if first_number > second_number:
                  longer_number = first_number
                  adjustment_spaces_2 = ((abs(len(str(first_number)) -
                                              len(str(second_number))) + 1) * " ")
              else:
                  longer_number = second_number
                  adjustment_spaces_2 = " "
              adjustment_spaces = ((len(str(longer_number)) + 2) -
                                   (len(str(first_number)))) * " "
              dash_line = (len(str(longer_number)) + 2) * "-"
              adjustment_spaces_total = ((len(str(longer_number)) + 2) -
                                         len(str(total))) * " "
              first_row.append(f'{adjustment_spaces}{first_number}    ')
              second_row.append(f'{operator}{adjustment_spaces_2}{second_number}    ')
              third_row.append(f'{dash_line}    ')
              fourth_row.append(f'{adjustment_spaces_total}{total}    ')
              part_1 = "".join(first_row)
              part_2 = "".join(second_row)
              part_3 = "".join(third_row)
              part_4 = "".join(fourth_row)
          if demand:
            return (f'{part_1.rstrip()}\n{part_2.rstrip()}\n'
              f'{part_3.rstrip()}\n{part_4.rstrip()}')
          if not demand:
              return (f'{part_1.rstrip()}\n{part_2.rstrip()}\n'
              f'{part_3.rstrip()}')