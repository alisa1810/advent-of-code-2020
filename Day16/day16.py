import numpy as np


def get_conditions(infos):
    conditions = []
    while True:
        for i, line in enumerate(infos):
            if line == '\n':
                break
            else:
                conditions.append(infos[i].strip('\n'))
        break

    cond_dict = {}

    for cond in conditions:
        fract = cond.split(': ')
        key = fract[0]
        values = fract[1].split(' or ')

        cond_dict[key] = (values[0], values[1])

    return cond_dict


def get_my_ticket(infos):
    my_ticket = []
    while True:
        for i, line in enumerate(infos):
            if 'your ticket' in line:
                my_ticket = infos[i + 1].strip('\n').split(',')

                for c, cond in enumerate(my_ticket):
                    my_ticket[c] = int(cond)
                break
        break
    return my_ticket


def get_other_tickets(infos):
    other_tickets = []
    while True:
        for i, line in enumerate(infos):
            if 'nearby tickets' in line:
                count = i
                while count < len(infos) - 1:
                    other_tickets.append(infos[count + 1].strip('\n'))
                    count += 1
                break
        break
    for i, ticket in enumerate(other_tickets):
        other_tickets[i] = ticket.split(',')
        for n, ns in enumerate(other_tickets[i]):
            other_tickets[i][n] = int(ns)
    return other_tickets


def find_limits(conditions):
    cond1 = []
    cond2 = []

    for cond in conditions.values():
        for c in cond[0].split('-'):
            cond1.append(int(c))
        for c in cond[1].split('-'):
            cond2.append(int(c))

    return min(cond1), max(cond1), min(cond2), max(cond2)


def find_invalids(oth_tickets, min1, max1, min2, max2):
    invalids = []
    for ticket in oth_tickets:
        for con in ticket:
            if not (min1 <= con <= max1 or min2 <= con <= max2):
                invalids.append(con)
    return invalids


def list_valid_tickets(my_ticket, other_tickets, invalids):
    other_tickets.append(my_ticket)
    only_valids = []

    for i, ticket in enumerate(other_tickets):
        if not set(ticket).intersection(set(invalids)):
            only_valids.append(ticket)

    return only_valids


def find_fields(valids, conditions):
    ticket_array = (np.array(valids)).transpose()
    translations = []

    for cond_name, cond_value in conditions.items():
        new_value = []
        for c in cond_value[0].split('-'):
            new_value.append(int(c))
        for c in cond_value[1].split('-'):
            new_value.append(int(c))

        conditions[cond_name] = new_value

    lines_on_passport = []

    for t in ticket_array:
        line = []
        for key, value in conditions.items():
            all_in_cond = True
            for n, numb in enumerate(t):
                if not (value[0] <= numb <= value[1] or value[2] <= numb <= value[3]):
                    all_in_cond = False

            if all_in_cond:
                line.append(key)

        lines_on_passport.append(line)

        final_lines = [' '] * len(conditions)
        count = 0

    while count < len(conditions):
        for i, l in enumerate(lines_on_passport):
            if len(l) == count + 1:
                count += 1
                for x in l:
                    if not x in final_lines:
                        final_lines[i] = x

    return final_lines


with open('input.txt') as file:
    lines_list = file.readlines()

    conditions = get_conditions(lines_list)
    my_ticket = get_my_ticket(lines_list)
    other_tickets = get_other_tickets(lines_list)
    min1, max1, min2, max2 = find_limits(conditions)

    # Part 1
    invalids = find_invalids(other_tickets, min1, max1, min2, max2)
    print(sum(invalids))

    # Part 2
    valid_tickets = list_valid_tickets(my_ticket, other_tickets, invalids)
    fields_passport = find_fields(valid_tickets, conditions)
    product = 1

    for i, f in enumerate(fields_passport):
        if f.startswith('departure'):
            product *= my_ticket[i]

    print(product)
