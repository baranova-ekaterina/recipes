from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def counter(request, name):
    servings = int(request.GET.get("servings", 1))  

    try:
        recipe = DATA[name]
        new_recipe = {}
        for ingridient, value in recipe.items():
            #recipe[ingridient] = value * servings 
            new_value = value * servings
            new_recipe[ingridient] = new_value
        context = { 
            #'recipe' : recipe
            'recipe' : new_recipe
        }
        #print(new_recipe)
    except KeyError:
        context = {
            'recipe' : None
        }
    return render(request, 'calculator/index.html', context) 
    #print(new_recipe)     
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
