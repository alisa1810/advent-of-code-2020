import numpy as np
import itertools
from numpy import zeros, newaxis


def change_states(current_states, dim=3):
    new_states = np.pad(np.zeros(current_states.shape), 1, "constant")
    grow = np.pad(current_states, 1, "constant")

    for index, cube in np.ndenumerate(grow):
        count = 0

        for position in itertools.product([-1, 0, 1], repeat=dim):
            if np.count_nonzero(np.array(position)) == 0:
                continue

            abs_pos = tuple(np.array(position) + np.array(index))

            if -1 in abs_pos or any([abs_pos[i] > shape_size - 1 for i, shape_size in enumerate(grow.shape)]):
                continue
            neighbor = grow[abs_pos]
            count += neighbor

        if cube == 1 and count not in [2, 3]:
            new_states[index] = 0
        elif cube == 0 and count == 3:
            new_states[index] = 1
        else:
            new_states[index] = cube

    return new_states


with open('input.txt') as file:
    lines_list = file.readlines()
    cube_states_2d = []

    for line in lines_list:
        cube_states_2d.append(list(line.strip('\n')))

    for row in cube_states_2d:
        for i, char in enumerate(row):
            if char == '#':
                row[i] = 1
            else:
                row[i] = 0

    cube_states_2d = np.array(cube_states_2d)

    # Part 1
    cube_states = cube_states_2d[..., newaxis]
    for _ in range(6):
        cube_states = change_states(cube_states)

    print(np.count_nonzero(cube_states))

    # Part 2
    cube_states = cube_states_2d[..., newaxis, newaxis]
    for _ in range(6):
        cube_states = change_states(cube_states, 4)

    print(np.count_nonzero(cube_states))
