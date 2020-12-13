def convert_list_to_numbers(lines_list):
    for i, line in enumerate(lines_list):
        lines_list[i] = int(line)

    return lines_list


def find_jolt_differences(adapter_list):
    one_jolt_jump = 0
    three_jolt_jump = 0

    for index, jolt_value in enumerate(adapter_list):
        difference = adapter_list[index] - adapter_list[index - 1]

        if index == 0:
            continue
        elif difference == 1:
            one_jolt_jump += 1
        elif difference == 3:
            three_jolt_jump += 1

    return one_jolt_jump * three_jolt_jump


def count_options(adapter_list):
    # [0] --> [0] --> 1 possibility
    # [0, 1] --> [0, 1] --> 1 possibility (1 pos.)
    # [0, 1, 2] --> [0, 1, 2] [0, 2] --> 2 possibilities (1 pos. + 1 pos.)
    # [0, 1, 2, 3] --> [0, 1, 2, 3] [0, 1, 3] [0, 2, 3] [0, 3] --> 4 possibilities (1 pos. + 1 pos. + 2 pos.)
    # [0, 1, 2, 3, 4] --> [0, 1, 2, 3, 4] [0, 1, 2, 4] [0, 1, 3, 4] [0, 2, 3, 4] [0, 1, 4] [0, 2, 4] [0, 3, 4] --> 7 possibilities (1 pos. + 1 pos. + 2 pos. + 4 pos.)
    # numbers:       [0, 1, 2, 3, 4]    [0, 1, 2, 3, 4, 6]    [0, 1, 2, 3, 4, 7]
    # possibilities:  1  1  2  4  7      1  1  2  4  7  11     1  1  3  4  7  7
    # new adapter has sum of possibilities of previous three, if one adapter is missing it's possibilities are counted as zero

    possibilities = {0: 1}
    for jolt_value in adapter_list[1:]:
        possibilities[jolt_value] = \
            possibilities.get(jolt_value - 1, 0) + \
            possibilities.get(jolt_value - 2, 0) + \
            possibilities.get(jolt_value - 3, 0)

    return possibilities[adapter_list[-1]]

with open('input.txt') as file:
    adapter_list = file.readlines()
    adapter_list = convert_list_to_numbers(adapter_list)

    # one jolt jump between outlet and first adapter must be counted
    adapter_list.append(0)

    # three jolt jump to final device must be counted must be counted
    adapter_list.append(max(adapter_list) + 3)

    adapter_list.sort()

    # Part 1
    print(find_jolt_differences(adapter_list))

    # Part 2
    print(count_options(adapter_list))
