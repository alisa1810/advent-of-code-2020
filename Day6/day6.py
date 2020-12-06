def get_groups(lines_list):
    group_list = []
    one_group = []

    for line in lines_list:
        if line == "\n":
            group_list.append(one_group)
            one_group = []
        else:
            line = line.strip("\n")
            one_group.append(line)

    group_list.append(one_group)

    return group_list


def count_all_yesses(group_list):
    yes_count = 0
    for group in group_list:
        sets = [set(member) for member in group]
        yes_count += len(list(sets[0].union(*sets[1:])))

    return yes_count


def count_unanimous_yesses(group_list):
    yes_count = 0
    for group in group_list:
        sets = [set(member) for member in group]
        yes_count += len(list(sets[0].intersection(*sets[1:])))
    return yes_count


with open('input.txt') as file:
    lines_list = file.readlines()

    group_list = get_groups(lines_list)

    print(count_all_yesses(group_list))
    print(count_unanimous_yesses(group_list))
