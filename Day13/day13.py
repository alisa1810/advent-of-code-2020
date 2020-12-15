def find_next_bus(busses, earliest_departure):
    arrival = earliest_departure
    time = arrival

    while True:
        for bus in busses:
            if time % bus == 0:
                return bus, time - arrival

        time += 1


def find_offset(all_busses):
    bus_offset = []
    for i, id in enumerate(all_busses):
        if not id == 'x':
            bus_offset.append((i, int(id)))

    return bus_offset


def find_bus_row(all_busses):
    start_time = 100000000000000
    # bus_offset = [(0, 23), (17, 37), (23, 863), (35, 19), (36, 13), (40, 17), (52, 29), (54, 571), (95, 41)]
    #  --> all primes --> smallest common multiple = numbers multiplied
    bus_offset = find_offset(all_busses)
    not_in_line = True

    while not_in_line:
        skip = 1
        not_in_line = False

        for offset, bus in bus_offset:
            if not (start_time + offset) % bus == 0:
                not_in_line = True
                break

            skip *= bus

        if not_in_line:
            start_time += skip

    return start_time


with open('input.txt') as file:
    lines_list = file.readlines()
    earliest_departure = int(lines_list[0].strip('\n'))
    all_busses = lines_list[1].strip('\n').split(',')
    busses = []

    for bus in all_busses:
        if not bus == 'x':
            busses.append(int(bus))

    # Part 1
    bus_id, waiting_time = find_next_bus(busses, earliest_departure)
    print(bus_id * waiting_time)

    # Part 2
    print(find_bus_row(all_busses))
