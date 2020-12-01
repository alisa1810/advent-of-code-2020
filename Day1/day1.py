def find_two_numbers(lines_list):
    for number in lines_list:
        for other_number in lines_list:
            if number + other_number == 2020:
                return number * other_number


def find_three_numbers(lines_list):
    for number in lines_list:
        for other_number in lines_list:
            for third_number in lines_list:
                if number + other_number + third_number == 2020:
                    return number * other_number * third_number


with open('input.txt') as file:
    lines_list = list(map(int, file.readlines()))
    print(find_two_numbers(lines_list))
    print(find_three_numbers(lines_list))
