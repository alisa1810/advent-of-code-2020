import itertools


def convert_list_to_numbers(lines_list):
    for i, line in enumerate(lines_list):
        lines_list[i] = int(line)

    return lines_list


def calculate_sums(converted_list, len_preamble, current_line):
    sums = []

    combinations = itertools.combinations(converted_list[current_line - len_preamble: current_line], 2)

    for comb in combinations:
        sums.append(sum(comb))

    return sums


def find_wrong_number(converted_list, len_preamble):
    current_line = len_preamble
    found_wrong_number = False

    while not found_wrong_number:

        for number in lines_list[len_preamble:]:
            # only combination of 2 numbers possible
            sums = calculate_sums(converted_list, len_preamble, current_line)

            if number not in sums:
                found_wrong_number = True
                break
            else:
                current_line += 1

    return number


def find_encryption_weakness(list, number):
    first_entry = 0
    last_entry = 1

    while True:
        entry_sum = sum(list[first_entry: last_entry])
        if entry_sum == number:
            return min(list[first_entry: last_entry]) + max(list[first_entry : last_entry])
        elif entry_sum > number:
            first_entry += 1
        else:
            last_entry += 1


with open('input.txt') as file:
    lines_list = file.readlines()
    converted_list = convert_list_to_numbers(lines_list)

    # Part 1
    wrong_number = find_wrong_number(converted_list, 25)
    print(wrong_number)

    # Part 2
    print(find_encryption_weakness(converted_list, wrong_number))
