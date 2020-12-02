def get_password_policy(line):
    entries = line.split()
    conditions = entries[0].split('-')
    minimum = int(conditions[0])
    maximum = int(conditions[1])
    character = entries[1].strip(':')
    password = list(entries[2])

    return minimum, maximum, character, password

def find_number_of_valid_1(lines_list):
    count_valids = 0

    for line in lines_list:
        minimum, maximum, character, password = get_password_policy(line)
        character_count = password.count(character)

        if character_count >= minimum and character_count <= maximum:
            count_valids += 1

    return count_valids


def find_number_of_valid_2(lines_list):
    count_valids = 0

    for line in lines_list:
        first_place, second_place, character, password = get_password_policy(line)
        password = list(password)

        if (password[first_place - 1] == character and not password[second_place - 1] == character) or (
                not password[first_place - 1] == character and password[second_place - 1] == character):
            count_valids += 1

    return count_valids


with open('input.txt') as file:
    lines_list = file.readlines()
    print(find_number_of_valid_1(lines_list))
    print(find_number_of_valid_2(lines_list))
