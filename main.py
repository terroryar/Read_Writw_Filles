

#Задача №1,2

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {}
    out_data = {}
    indni = {}
    with open("recipes.txt", 'r', encoding='utf-8') as f:
        data = f.readline().strip()
        while data != '':
            bludo_name = data
            count_ing = f.readline()
            recept = []
            ingridiens = f.readline()
            while ingridiens != '\n' and ingridiens != '':
                ingredient_name, quantity, measure = ingridiens.strip().split('|')
                recept.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measury': measure})
                ingridiens = f.readline()
            cook_book.update({bludo_name: recept})
            data = f.readline().strip()
    print('Словарь рецептов')
    print(cook_book)
    print('Finish')
    print('Ингридиенты дл приготовления блюд(без повторений):')


    for item in dishes:
        for i in range(len(cook_book[item])):
            if out_data.get(cook_book[item][i]['ingredient_name']) == None:
                out_data.update({cook_book[item][i]['ingredient_name']: {
                    'quantity': int(cook_book[item][i]['quantity']) * person_count,
                    'measure': cook_book[item][i]['measury']}})
            else:
                out_data.update({cook_book[item][i]['ingredient_name']: {
                    'quantity': (int(cook_book[item][i]['quantity'])*person_count+int(out_data[cook_book[item][i]['ingredient_name']]['quantity'])),
                    'measure': cook_book[item][i]['measury']}})
    return(out_data)





#Задача №3

def rewrite_files(fils_name,result_file_name):
    res_data = []
    for file in fils_name:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.readlines()
            data.insert(0, f'{file}\n')
        res_data.append(data)
    res_data.sort(key=len)
    with open(result_file_name, 'w', encoding='utf-8') as f:
        for data in res_data:
            data.insert(1, f'{len(data) - 1}\n')
            for item in data:
                f.write(item)


print('Решение Задачи №1 и Задачи № 2')


print(get_shop_list_by_dishes(['Омлет','Фахитос','Запеченный картофель'], 5))
print('')
print('')
print('Решение Задачи №3')
rewrite_files(['1.txt','2.txt','3.txt','4.txt','5.txt'],'result_file1.txt')
with open('result_file1.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
print(data)


