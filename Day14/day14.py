import re


def do_inis(ini_list):
    memory = {}

    for line in ini_list:
        if 'mask' in line:
            ones = 0
            zeros = 0

            for char in line.split(' ')[2]:
                ones = ones << 1
                zeros = zeros << 1
                if char == "1":
                    ones = ones | 1
                if char == "0":
                    zeros = zeros | 1
        else:
            fractions = line.split(' ')
            value = int(fractions[2])
            key = int(re.split('\\[|\\]', fractions[0])[1])

            memory[key] = (value | ones) & ~zeros

    return memory


def do_inis_v2(ini_list):
    memory = {}

    for line in ini_list:
        if 'mask' in line:
            ones = 0
            xs = 0

            for char in line.split(' ')[2]:
                ones = ones << 1
                xs = xs << 1
                if char == "1":
                    ones = ones | 1
                if char == "X":
                    xs = xs | 1
        else:
            addresses = []
            fractions = line.split(' ')
            value = int(fractions[2])
            key = int(re.split('\\[|\\]', fractions[0])[1])

            key = (key | ones) & ~xs
            addresses.append(key)
            floats = "{0:036b}".format(xs)

            for i, bit in enumerate(floats[::-1]):
                if bit == '1':
                    new_addresses = []
                    for address in addresses:
                        new_address = address | 1 << i
                        new_addresses.append(new_address)
                    addresses = addresses + new_addresses

            for address in addresses:
                memory[address] = value
    return memory


def calculate_sum(memory):
    sum = 0
    for key, value in memory.items():
        sum += value

    return sum


with open('input.txt') as file:
    lines_list = file.readlines()
    initalization_list = []

    for ini in lines_list:
        initalization_list.append(ini.strip('\n'))

    # Part 1
    new_memory = do_inis(initalization_list)
    print(calculate_sum(new_memory))

    # Part 2
    memory_v2 = do_inis_v2(initalization_list)
    print(calculate_sum(memory_v2))
