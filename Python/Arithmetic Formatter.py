def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    line1, line2, line3, line4 = "", "", "", ""
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(operand1), len(operand2)) + 2

        line1 += operand1.rjust(width) + "    "
        line2 += operator + operand2.rjust(width - 1) + "    "
        line3 += '-' * width + "    "

        if show_answers:
            result = str(eval(problem))
            line4 += result.rjust(width) + "    "

    arranged_problems = "\n".join([line1.rstrip(), line2.rstrip(), line3.rstrip(), line4.rstrip()]).rstrip()
    return arranged_problems
   

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))