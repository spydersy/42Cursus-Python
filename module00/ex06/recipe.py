
cookbook = {}

def init_cookbook():
    cookbook['Sandwich'] = {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                    'meal': 'lunch',
                    'prep_time': 10}

    cookbook['Cake'] = {'ingredients': ['flour', 'sugar', 'eggs'],
                    'meal': 'dessert',
                    'prep_time': 60}

    cookbook['Salads'] = {'ingredients': ['avocado', 'arugula', 'tomatoes' 'spinach'],
                    'meal': 'lunch',
                    'prep_time': 15}

def print_all_recipes():
    print('All recipes:', ", ".join(map(str, cookbook.keys())))

def print_recipe(recipe_name):
    if recipe_name in cookbook.keys():
        print('meal:', cookbook[recipe_name]['meal'])
        print('ingredients:', ", ".join(cookbook[recipe_name]['ingredients']))
        print('preparation time:', cookbook[recipe_name]['prep_time'], 'min')
    else:
        print("Error: Recipe not found")

def add_recip():
    name = str(input(">>> Enter a name:\n"))
    if name == "":
        print('Error: Name cant be empty')
        return
    if name in cookbook.keys():
        print("Recip already exist")
        return
    ingredient = "."
    ingredients = []
    print('>>> Enter ingredients:')
    while ingredient != "":
        ingredient = str(input())
        if len(ingredients) == 0 and ingredient == "":
            print('Error: Ingredients cant be empty')
            return
        elif ingredient != "":
            ingredients.append(ingredient)

    meal = str(input('>>> Enter a meal type:\n'))
    prep_time = int(input('>>> Enter a preparation time:\n'))
    if prep_time <= 0:
        print('Error: Preparation time must be a positif number')
        return
    cookbook[name] = {'ingredients': ingredient,
                    'meal': meal,
                    'prep_time': prep_time}
    print(cookbook)

def delete_recipe(recipe_name):
    if recipe_name in cookbook.keys():
        cookbook.pop('recipe_name')
        print(f'{recipe_name} deleted')
        print('preparation time:', cookbook[recipe_name]['prep_time'], 'min')
    else:
        print("Error: Recipe not found")

def handle_input(option):
    index = options.index(option)
    if index == -1:
        return False
    if index == 0:
        add_recip()
    if index == 1:
        recipe = str(input('Please enter a recipe name to delete:\n>>>'))
        delete_recipe(recipe)
    if index == 2:
        recipe = str(input('Please enter a recipe name to get its details:\n>>>'))
        print_recipe(recipe)
    if index == 3:
        print_all_recipes()
    if index == 4:
        print('Cookbook closed. Goodbye !')
        exit()
    return True

options = ['1', '2', '3','4', '5']

if __name__ == '__main__':
    prompt = '''List of available option:
        1: Add a recipe
        2: Delete a recipe
        3: Print a recipe
        4: Print the cookbook
        5: Quit\n'''
    init_cookbook()
    print('Welcome to the Python Cookbook !')
    while True:
        print(prompt)
        option = str(input("Please select an option:\n>>>"))
        if handle_input(option) == False:
            print('Sorry, this option does not exist.')