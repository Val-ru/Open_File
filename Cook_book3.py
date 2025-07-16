from pprint import pprint

def make_cook_book():

    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    right_list = all_lines[:-8]
    flag = 0
    while flag < len(right_list):
        name = all_lines[flag].strip()
        flag += 1

        num_ingredients = int(right_list[flag].strip())
        flag += 1

        ingredients = []
        for i in range(num_ingredients):

            ingr_line = right_list[flag].strip()
            flag += 1
            ingredient_name, quantity, measure = ingr_line.split(' | ')
            ingredients.append({
                'ingredient_name' : ingredient_name,
                'quantity' : int(quantity),
                'measure' : measure
            })
        cook_book[name] = ingredients

        if flag < len(right_list) and right_list[flag].strip() == '':
            flag += 1
    return cook_book
    # print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:

        if dish in make_cook_book():
            ingredients = [make_cook_book()[dish]]
            flag = 0

            for ingr in ingredients:
                for i in ingr:

                    ingr_name = ingr[flag].get('ingredient_name')
                    ingr_count = int(ingr[flag].get('quantity'))
                    ingr_measure = ingr[flag].get('measure')

                    flag += 1
                    count = ingr_count * person_count

                    if ingr_name in shop_list:
                        shop_list['quantity'] = ingr_count + count
                    else:
                        shop_list.setdefault(ingr_name, {'measure' : ingr_measure, 'quantity' : count})
        else:
            print("Такого блюда нет")
    return shop_list

dishes = ['Омлет', 'Запеченный картофель']
persons = 2
make_cook_book()
shopping_list = get_shop_list_by_dishes(dishes, persons)
pprint(shopping_list)