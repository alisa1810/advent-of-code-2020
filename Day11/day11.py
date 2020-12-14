def find_seat_status(seat_list, row, column):
    if row < 0 or column > len(seat_list[0]) - 1 or column < 0 or row > len(seat_list) - 1:
        return None
    else:
        try:
            return seat_list[row][column]
        except:
            print(row + column)


def do_seating(seat_list):
    new_seating = []
    changed = False

    for row, this_row in enumerate(seat_list):
        new_row = ""

        for column, _ in enumerate(this_row):
            occupied_count = 0
            seat = find_seat_status(seat_list, row, column)

            if find_seat_status(seat_list, row + 1, column) == "#":
                occupied_count += 1

            if find_seat_status(seat_list, row + 1, column - 1) == "#":
                occupied_count += 1

            if find_seat_status(seat_list, row + 1, column + 1) == "#":
                occupied_count += 1

            if find_seat_status(seat_list, row - 1, column) == "#":
                occupied_count += 1

            if find_seat_status(seat_list, row - 1, column - 1) == "#":
                occupied_count += 1

            if find_seat_status(seat_list, row - 1, column + 1) == "#":
                occupied_count += 1

            if find_seat_status(seat_list, row, column - 1) == "#":
                occupied_count += 1

            if find_seat_status(seat_list, row, column + 1) == "#":
                occupied_count += 1

            if seat == "#" and occupied_count >= 4:
                new_row += "L"
                changed = True
            elif seat == "L" and occupied_count == 0:
                new_row += "#"
                changed = True
            else:
                new_row += seat

        new_seating.append(new_row)

    return new_seating, changed


def find_end_seating(seat_list):
    new_seating, changed = do_seating(seat_list)

    while changed:
        new_seating, changed = do_seating(new_seating)

    return new_seating


def do_new_seating(seat_list):
    new_seating = []
    changed = False
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for row, this_row in enumerate(seat_list):
        new_row = ""

        for column, _ in enumerate(this_row):
            occupied_count = 0
            seat = find_seat_status(seat_list, row, column)

            for direction in directions:
                found_person = False
                x = direction[0]
                y = direction[1]

                while not found_person:
                    seat_in_line = find_seat_status(seat_list, row + x, column + y)

                    if not seat_in_line:
                        break
                    elif seat_in_line == "L":
                        break
                    elif seat_in_line == "#":
                        occupied_count += 1
                        break

                    x += direction[0]
                    y += direction[1]

            if seat == "#" and occupied_count >= 5:
                new_row += "L"
                changed = True
            elif seat == "L" and occupied_count == 0:
                new_row += "#"
                changed = True
            else:
                new_row += seat

        new_seating.append(new_row)

    return new_seating, changed


def find_new_end_seating(seat_list):
    new_seating, changed = do_new_seating(seat_list)

    while changed:
        new_seating, changed = do_new_seating(new_seating)

    return new_seating


def count_occupied_seats(end_seating):
    count = 0
    for row, this_row in enumerate(end_seating):
        for column, _ in enumerate(this_row):
            seat = find_seat_status(end_seating, row, column)
            if seat == "#":
                count += 1

    return count


with open('input.txt') as file:
    line_list = file.readlines()
    seat_list = []

    for row in line_list:
        seat_list.append(row.strip("\n"))

    # Part 1
    end_seating = find_end_seating(seat_list)
    print(count_occupied_seats(end_seating))

    # Part 2
    new_end_seating = find_new_end_seating(seat_list)
    print(count_occupied_seats(new_end_seating))
