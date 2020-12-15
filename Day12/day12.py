import numpy as np


def get_directions(list):
    directions = []

    for l in list:
        directions.append([l[0], int(l[1:])])

    return directions


def turn(direction, turn, angle):
    for i in range(int(angle / 90)):
        if turn == "R":
            if direction == "E":
                direction = "S"
            elif direction == "S":
                direction = "W"
            elif direction == "W":
                direction = "N"
            elif direction == "N":
                direction = "E"
        elif turn == "L":
            if direction == "E":
                direction = "N"
            elif direction == "N":
                direction = "W"
            elif direction == "W":
                direction = "S"
            elif direction == "S":
                direction = "E"

    return direction


def maneuver_ship(directions, start):
    current_dir = start[0]
    coordinates = np.array([0, 0])

    for dir in directions:
        if dir[0] == 'E':
            coordinates += np.array([dir[1], 0])
        elif dir[0] == 'W':
            coordinates += np.array([-dir[1], 0])
        elif dir[0] == 'N':
            coordinates += np.array([0, dir[1]])
        elif dir[0] == 'S':
            coordinates += np.array([0, -dir[1]])
        elif dir[0] == 'F':
            if current_dir == 'E':
                coordinates += np.array([dir[1], 0])
            elif current_dir == 'W':
                coordinates += np.array([-dir[1], 0])
            elif current_dir == 'N':
                coordinates += np.array([0, dir[1]])
            elif current_dir == 'S':
                coordinates += np.array([0, -dir[1]])
        elif dir[0] in ["R", "L"]:
            current_dir = turn(current_dir, dir[0], dir[1])

    return coordinates


def rotate_waypoint(wp_coord, ship_pos, new_rot):
    for i in range(int(new_rot[1] / 90)):
        distance = wp_coord - ship_pos
        if new_rot[0] == "R":
            wp_coord = ship_pos + np.array([distance[1], -distance[0]])
        elif new_rot[0] == "L":
            wp_coord = ship_pos + np.array([-distance[1], distance[0]])
    return wp_coord


def steer_ship_w_wp(directions, wp_position, ship_position):
    wp_position = np.array(wp_position)
    ship_position = np.array(ship_position)

    for dir in directions:
        distance_wp_ship = wp_position - ship_position
        if dir[0] == 'E':
            wp_position += np.array([dir[1], 0])
        elif dir[0] == 'W':
            wp_position += np.array([-dir[1], 0])
        elif dir[0] == 'N':
            wp_position += np.array([0, dir[1]])
        elif dir[0] == 'S':
            wp_position += np.array([0, -dir[1]])
        elif dir[0] in ['R', 'L']:
            wp_position = rotate_waypoint(wp_position, ship_position, dir)
        elif dir[0] == 'F':
            ship_position += dir[1] * distance_wp_ship
            wp_position = ship_position + distance_wp_ship

    return ship_position


with open('input.txt') as file:
    lines_list = file.readlines()
    direction_list = []

    for direction in lines_list:
        direction_list.append(direction.strip('\n'))

    directions = get_directions(direction_list)

    # Part 1
    start_position = ['E', 0]
    end_position = maneuver_ship(directions, start_position)

    print(abs(end_position[0]) + abs(end_position[1]))

    # Part 2
    start_position_wp = [10, 1]
    start_position_ship = [0, 0]

    end_position_ship_wp = steer_ship_w_wp(directions, start_position_wp, start_position_ship)

    print(abs(end_position_ship_wp[0]) + abs(end_position_ship_wp[1]))
