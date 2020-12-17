start_numbers = [17,1,3,16,19,0]

def play_game(start_numbers, number_turns):
    turns = {}
    last_number = start_numbers[0]

    for i, number in enumerate(start_numbers):
        turns[last_number] = i - 1
        last_number = number

    count_turns = len(start_numbers)

    while count_turns < number_turns:
        if last_number in turns:
            new_number = (count_turns - 1) - turns[last_number]
        else:
            new_number = 0

        turns[last_number] = count_turns - 1
        last_number = new_number
        count_turns += 1

    return last_number

# Part 1
print(play_game(start_numbers, 2020))

# Part 2
print(play_game(start_numbers, 30000000))