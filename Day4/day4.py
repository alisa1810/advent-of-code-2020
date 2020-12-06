import re


def reformat_input(lines_list):
    passport_list = []
    new_passport = ""
    for line in lines_list:
        if ":" in line:
            new_passport += line.strip("\n") + " "
        else:
            new_passport = new_passport.strip(" ")
            passport_list.append(new_passport)
            new_passport = ""

    passport_list.append(new_passport)

    key_ordered_passport_list = []
    for passport in passport_list:
        passport_map = {}

        for pair in passport.split():
            key, value = pair.split(":")
            passport_map[key] = value

        key_ordered_passport_list.append(passport_map)

    return key_ordered_passport_list


def count_valid_key_passports(passports, fields):
    valid_passports_count = 0
    valid_passports = []
    for passport in passports:
        valid = True
        for field in fields:
            if field not in passport:
                valid = False
                break
        if valid:
            valid_passports_count += 1
            valid_passports.append(passport)

    return valid_passports_count, valid_passports


def count_valid_entry_passports(key_valid_passports):
    really_valid_count = 0

    for passport in key_valid_passports:
        valid = True
        for key, value in passport.items():
            if key == "byr" and not 1920 <= int(value) <= 2002:
                valid = False
            elif key == "iyr" and not 2010 <= int(value) <= 2020:
                valid = False
            elif key == "eyr" and not 2020 <= int(value) <= 2030:
                valid = False
            elif key == "hgt":
                if not (value.endswith("cm") or value.endswith("in")):
                    valid = False
                if value.endswith("cm") and not 150 <= int(value.replace("cm", "")) <= 193:
                    valid = False
                if value.endswith("in") and not 59 <= int(value.replace("in", "")) <= 76:
                    valid = False
            elif key == "hcl" and not re.search("^#[0-9a-f]{6}$", value):
                valid = False
            elif key == "ecl" and not (value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                valid = False
            elif key == "pid" and not (len(value) == 9 and int(value)):
                valid = False

        if valid:
            really_valid_count += 1

    return really_valid_count


with open('input.txt') as file:
    lines_list = file.readlines()

    important_fields = ["byr",
                        "iyr",
                        "eyr",
                        "hgt",
                        "hcl",
                        "ecl",
                        "pid"]

    new_passport_list = reformat_input(lines_list)
    count_key_valids, key_valid_passports = count_valid_key_passports(new_passport_list, important_fields)

    print(count_key_valids)
    print(count_valid_entry_passports(key_valid_passports))
