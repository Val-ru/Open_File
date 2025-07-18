from pprint import pprint

from Cook_book_hw.ex import cook_book


class CookBook:
    cook_book = {}

    with open('recipes.txt', 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    flag = 0
    dish_count = 0
    while flag < len(all_lines):

        name = all_lines[flag].strip()

        # if name == 'Фахитос':
        #     break
        if name == '':
            dish_count += 1

        if dish_count == 3:
            break
        flag += 1

        num_ingredients = int(all_lines[flag].strip())
        flag += 1

        ingredients = []
        for i in range(num_ingredients):
            ingr_line = all_lines[flag].strip()
            flag += 1

            ingredient_name, quantity, measure = ingr_line.split(' | ')
            ingredients.append({
                'ingredient_name' : ingredient_name,
                'quantity' : int(quantity),
                'measure' : measure
            })
        cook_book[name] = ingredients

        if flag < len(all_lines) and all_lines[flag].strip() == '':
            flag += 1

    # print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:

        if dish in cook_book:
            ingredients = [cook_book[dish]]
            flag = 0

            for ingr in ingredients:
                for i in ingr:

                    ingr_name = ingr[flag].get('ingredient_name')
                    ingr_count = int(ingr[flag].get('quantity'))
                    ingr_measure = ingr[flag].get('measure')

                    flag += 1
                    count = ingr_count * person_count

                    if ingr_name in shop_list:
                        ingr_count += count

                    else:
                        shop_list.setdefault(ingr_name, {'measure' : ingr_measure, 'quantity' : count})

        else:
            print("Такого блюда нет")
    return shop_list

dishes = ['Омлет', 'Запеченный картофель']
persons = 2
shopping_list = get_shop_list_by_dishes(dishes, persons)
pprint(shopping_list)




