import re

def get_calculator_input(previousResult):
    while True:
        user_input = input("\nEnter calculation (e.g., 5+10 or +5): ").strip()

        # Regex Breakdown:
        # (\d+\.?\d*) -> Matches a number (integer or decimal)
        # ([\+\-\*/]) -> Matches one of the four basic operators

        # Case 1: Standard input like "5+10"
        full_pattern = r"^(\d+\.?\d*)\s*([\+\-\*/])\s*(\d+\.?\d*)$"

        # Case 2: Shorthand input like "+5"
        short_pattern = r"^([\+\-\*/])\s*(\d+\.?\d*)$"

        match_full = re.match(full_pattern, user_input)
        match_short = re.match(short_pattern, user_input)

        if match_full:
            firstArgument = float(match_full.group(1))
            operator = match_full.group(2)
            secondArgument = float(match_full.group(3))
            return firstArgument, secondArgument, operator

        elif match_short:
            # Here we use the previousResult passed into the function
            operator = match_short.group(1)
            secondArgument = float(match_short.group(2))
            firstArgument = previousResult
            return firstArgument, secondArgument, operator

        elif (user_input=='exit'):
            print("Okay, bye-bye!")
            quit()

        else:
            print("Invalid input! Please use formats like '10 + 5' or '/ 2'.")

def calculation(firstArgument, secondArgument, operator):
    if operator == "+": # calculatiobs
        return firstArgument + secondArgument
    elif operator == "-":
        return firstArgument - secondArgument
    elif operator == "*":
        return firstArgument * secondArgument
    elif operator == "/":
        return firstArgument / secondArgument
    else: # this isn't supposed to happen, since this is supposed to be handled by get_calculator_input, but here it is
        print("Invalid operator! Please use formats like '10 + 5' or '/ 2'. (also, you somehow passed the input and this only turned up in the calculation phase, which is weird, please report this to the developer)")


print("Hey! I'm a small calculator, I'm here to calculate things for you. I support operators +, -, * and /. I will ask you to input the calculation that you want in the format of '5 + 10', and I will caluclate the result for you. And if you type something like '+ 5', I will use the result of the previous calculation. To exit, type 'exit'.")
previousResult = 0
while True:
    firstArgument, secondArgument, operator = get_calculator_input(previousResult)
    previousResult = calculation(firstArgument, secondArgument, operator)
    print(previousResult)