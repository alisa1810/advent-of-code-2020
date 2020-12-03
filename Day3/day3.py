import math

def get_wood_area(wood, right_step, down_step):
    wood = [w.strip() for w in wood]
    path_length = len(wood)
    path_width = len(wood[1])
    pattern_repeats = math.ceil((path_length / down_step) / (path_width / right_step))
    repeat = 0
    woods = wood

    while repeat < pattern_repeats:
        woods = [tree_rows + tree_row for tree_rows, tree_row in zip(woods, wood)]
        repeat += 1

    return woods


def count_trees(wood, right_step, down_step):
    woods = get_wood_area(wood, right_step, down_step)

    step = 0
    tree_count = 0
    for index, tree_row in enumerate(woods):
        if index % down_step == 0:
            if tree_row[step] == '#':
                tree_count += 1
            step += right_step

    return tree_count


with open('input.txt') as file:
    lines_list = file.readlines()

    print(count_trees(lines_list, 1, 1) * count_trees(lines_list, 3, 1) * count_trees(lines_list, 5, 1) * count_trees(
        lines_list, 7, 1) * count_trees(lines_list, 1, 2))
