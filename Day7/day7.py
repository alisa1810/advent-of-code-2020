import re


def structure_bag_list(bag_list):
    bag_map = {}
    for bag in bag_list:
        bag = bag.replace("bags,", ",").replace("bag,", ",").replace("bags.", "").replace("bag.", "")

        z = re.match(r"(.*)\sbags contain\s(\d+[\w\s]*.*)+", bag)

        if not z:
            continue

        bag_name, ingredients = z.groups()

        bag_map[bag_name] = {}

        for sub_bag in ingredients.split(","):
            number, sub_bag_name = sub_bag.strip().split(" ", 1)
            bag_map[bag_name][sub_bag_name] = int(number)

    return bag_map


def count_gold_containers(outer_bag, inner_bags, bag_map):
    if "shiny gold" in outer_bag:
        return False
    elif "shiny gold" in inner_bags:
        return True
    else:
        for bag in inner_bags:
            if bag in bag_map.keys():
                contains_gold = count_gold_containers(bag, bag_map[bag], bag_map)
                if contains_gold:
                    return True

        return False


def search_all_bags(bag_map):
    gold_container_count = 0

    for outer_bag, inner_bags in bag_map.items():

        if count_gold_containers(outer_bag, inner_bags, bag_map):
            gold_container_count += 1

    return gold_container_count


def count_bags_inside_bag(name, bags):
    if name not in bags.keys():
        return 0
    else:
        counter = 0
        for sub_bag, count in bags[name].items():
            counter = counter + (count * count_bags_inside_bag(sub_bag, bags)) + count

        return counter


with open('input.txt') as file:
    lines_list = file.readlines()

    bag_map = structure_bag_list(lines_list)

    print(search_all_bags(bag_map))
    print(count_bags_inside_bag("shiny gold", bag_map))
