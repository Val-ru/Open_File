from pprint import pprint

def make_cook_book():

    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    flag = 0
    dish_count = 0
    while flag < len(all_lines):

        name = all_lines[flag].strip()
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
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        cook_book[name] = ingredients

        if flag < len(all_lines) and all_lines[flag].strip() == '':
            flag += 1
    return cook_book

cook_book_ = make_cook_book()

def get_shop_list_by_dishes(dishes, person_count, cook_book_):
    shop_list = {}

    for dish in dishes:

        if dish in cook_book_:
            ingredients = [cook_book_[dish]]

            for ingr in ingredients:
                for i in ingr:

                    ingr_name = i['ingredient_name']
                    ingr_count = i['quantity']
                    ingr_measure = i['measure']

                    count = ingr_count * person_count

                    if ingr_name in shop_list:
                        shop_list[ingr_name]['quantity'] += count

                    else:
                        shop_list.setdefault(ingr_name, {'measure' : ingr_measure, 'quantity' : count})

        else:
            print("Такого блюда нет")
    return shop_list

dishes = ['Омлет', 'Запеченный картофель']
persons = 2

shopping_list = get_shop_list_by_dishes(dishes, persons, cook_book_)
pprint(shopping_list)