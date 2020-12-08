from copy import copy, deepcopy


def create_list(commands):
    command_list = []
    for command in commands:
        command = command.strip('\n').split()
        command[1] = int(command[1])
        command_list.append(command)

    return command_list


def execute_code(commands, start_command):
    acc = 0
    code_line = start_command
    in_endless_loop = False
    terminated_correctly = False

    while not in_endless_loop and not terminated_correctly:

        if code_line == len(commands):
            terminated_correctly = True
        elif "check" in commands[code_line]:
            in_endless_loop = True
        else:
            command = commands[code_line]
            command.append("check")

            if "nop" in command:
                code_line += 1
            elif "jmp" in command:
                code_line += command[1]
            elif "acc" in command:
                acc += command[1]
                code_line += 1
            else:
                break

    return acc, terminated_correctly


with open('input.txt') as file:
    lines_list = file.readlines()

    # Part 1
    command_list = create_list(lines_list)
    print(execute_code(command_list, 0))

    # Part 2
    command_list = create_list(lines_list)
    for code_line, command in enumerate(command_list):
        if "nop" in command or "jmp" in command:
            modified_command_list = deepcopy(command_list)
            modified_command_list[code_line][0] = "nop" if "jmp" in command else "jmp"

            acc, terminated = execute_code(modified_command_list, 0)

            if terminated:
                print("line: " + str(code_line), "count: " + str(acc))
        else:
            pass
