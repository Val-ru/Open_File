from Cook_book_hw.ex import cook_book


class CookBook:
    cook_book = {}

    with open('recipes.txt', 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    flag = 0
    while flag < len(all_lines):
        name = all_lines[flag].strip()
        if name == 'Фахитос':
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

    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:

        if dish in cook_book:
            ingredients = cook_book[dish]

            # print(ingredients)
        for ingr in ingredients:
            i = 0
            ingr_name = ingredients[i]['ingredient_name']
            # print(ingredients[0])
            # print(ingr_name)
            ingr_count = int(ingredients[i]['quantity'])

            ingr_measure = ingredients[i]['measure']


            count = ingr_count * person_count
            i += 1
            if ingr_name in shop_list:
                ingr_count += count
            else:
                shop_list = {
                    'ingr_name': {
                    'measure': ingr_measure,
                    'quantity': ingr_count
                }}

        else:
            print("Такого блюда нет")

    return shop_list

dishes = ['Омлет', 'Фахитос']
persons = 3
shopping_list = get_shop_list_by_dishes(dishes, persons)





