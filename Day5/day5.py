# decimal to binary --> "BFFFBBF" == "row 70" == 1000110 --> B == 1, F == 0
# decimal to binary --> "RRR" == "seat 7" == 111 --> R == 1, L == 0

def find_seat_ids(boarding_passes):
    id_list = []
    for boarding_pass in boarding_passes:
        row = int(boarding_pass.strip("\n")[:-3].replace('B', '1').replace('F', '0'), 2)
        seat = int(boarding_pass.strip("\n")[-3:].replace('R', '1').replace('L', '0'), 2)

        id_list.append(row * 8 + seat)

    return id_list

def find_my_seat_id(other_seat_ids):
    other_seat_ids.sort()

    return [my_id for my_id in range(other_seat_ids[0], other_seat_ids[-1]+1) if my_id not in other_seat_ids]

with open('input.txt') as file:
    lines_list = file.readlines()
    other_seat_ids = find_seat_ids(lines_list)
    my_seat_id = find_my_seat_id(other_seat_ids)[0]

    print(max(find_seat_ids(lines_list)))
    print(my_seat_id)