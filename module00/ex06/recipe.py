# Colors definition:
OKGREEN_COLOR = '\033[92m'
FAIL_COLOR = '\033[93m'
BOLD_COLOR = '\033[1m'
ENDC_COLOR = '\033[0m'

# Program messages:
welcome_message = OKGREEN_COLOR + 'Welcome to the Python Cookbook !' + ENDC_COLOR
available_options = '''\
{}List of available option:{}
{}1:{} Add a recipe
{}2:{} Delete a recipe
{}3:{} Print a recipe
{}4:{} Print the cookbook
{}5:{} Quit\
'''
prompt = OKGREEN_COLOR + '''\
Please select an option:
>> \
''' + ENDC_COLOR
wrong_input = FAIL_COLOR + '''\
This option does not exist, please type the corresponding number.
To exit, enter 5.\
''' + ENDC_COLOR
empty_input = FAIL_COLOR + 'Empty input, please type the corresponding number.' + ENDC_COLOR

# Add recipe prompts:
add_recipe_name = BOLD_COLOR + '>>> Enter a name: ' + ENDC_COLOR
add_recipe_ingredients = BOLD_COLOR + '>>> Enter ingredients: ' + ENDC_COLOR
add_recipe_meal_type = BOLD_COLOR + '>>> Enter a meal type: ' + ENDC_COLOR
add_recipe_preparation_time = BOLD_COLOR + '>>> Enter a preparation time: ' + ENDC_COLOR
print_recipe_prompt = BOLD_COLOR + '''\
Please enter a recipe name to get its details:
>> \
''' + ENDC_COLOR

# Add recipe error messages:
recipe_already_exists = FAIL_COLOR + 'Recipe already exists' + ENDC_COLOR
empty_recipe_name = FAIL_COLOR + 'Empty recipe name' + ENDC_COLOR
empty_meal_type = FAIL_COLOR + 'Empty meal type' + ENDC_COLOR
empty_recipe_preparation_time = FAIL_COLOR + 'Empty recipe preparation time' + ENDC_COLOR
wrong_preparation_time = FAIL_COLOR + 'Wrong preparation time' + ENDC_COLOR

# Add recipe confirmation message:
recipe_added = OKGREEN_COLOR + 'Recipe added\n' + ENDC_COLOR

# Print recipe output:
recipe_output = '''\
Recipe for {}:
\tIngredients list: {}.
\tTo be eaten for {}.
\tTakes {} minutes of cooking.
'''

# Print recipe error messages:
recipe_not_found = FAIL_COLOR + 'Recipe not found\n' + ENDC_COLOR

# Delete recipe prompts:
delete_recipe_prompt = BOLD_COLOR + '''\
Please enter a recipe name to delete:
>> \
''' + ENDC_COLOR

# Delete recipe confirmation message:
recipe_deleted = OKGREEN_COLOR + 'Recipe deleted\n' + ENDC_COLOR

# Cookbook definition:
cookbook = {
    'sandwich': {
        "ingredients": ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal": 'lunch',
        "prep_time": 10
    },
    'cake': {
        "ingredients": ['flour', 'sugar', 'eggs'],
        "meal": 'dessert',
        "prep_time": 60
    },
    'salad': {
        "ingredients": ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal": 'lunch',
        "prep_time": 15
    }
}

def add_recipe():
    '''A function that add a recipe from user input. You will need a name, a list of ingredient, a meal type and a preparation time.'''
    # Get recipe name. If empty, return to main menu
    recipe_name = input(add_recipe_name)
    if len(recipe_name) == 0:
        print(empty_recipe_name)
        return
    if recipe_name in cookbook:
        print(recipe_already_exists)
        return
    # Get recipe ingredients. If empty, return to main menu
    recipe_ingredients = []
    ingredient = ' '
    print(add_recipe_ingredients)
    while len(ingredient) > 0:
        ingredient = input('{}>> {}'.format(BOLD_COLOR, ENDC_COLOR))
        if len(ingredient) > 0:
            recipe_ingredients.append(ingredient)
    if len(recipe_ingredients) == 0:
        print(empty_recipe_name)
        return
    # Get recipe meal type. If empty, return to main menu
    recipe_meal_type = input(add_recipe_meal_type)
    if len(recipe_meal_type) == 0:
        print(empty_recipe_name)
        return
    # Get recipe preparation time. If empty, or not a number, or negative, return to main menu
    recipe_preparation_time = input(add_recipe_preparation_time)
    if len(recipe_preparation_time) == 0:
        print(empty_recipe_preparation_time)
        return
    try:
        recipe_preparation_time = int(recipe_preparation_time)
        if recipe_preparation_time <= 0:
            raise ValueError
    except ValueError:
        print(wrong_preparation_time)
        return
    # Add recipe to cookbook
    cookbook[recipe_name] = {
        'ingredients': recipe_ingredients,
        'meal': recipe_meal_type,
        'prep_time': recipe_preparation_time
    }
    print(recipe_added)

def print_recipe():
    '''A function to print a recipe from the cookbook. If the recipe is not found, print an error message and return to the menu.'''
    print(print_recipe_prompt, end='')
    recipe = input()
    if len(recipe) == 0:
        print(empty_recipe_name)
        return
    if recipe in cookbook:
        print(recipe_output.format(recipe,
                                   cookbook[recipe]['ingredients'],
                                   cookbook[recipe]['meal'],
                                   cookbook[recipe]['prep_time']))
    else:
        print(recipe_not_found)

def print_cookbook():
    print('Print the cookbook')


def delete_recipe():
    '''A function to delete a recipe from the cookbook. If the recipe is not found, print an error message and return to the menu.'''
    print(delete_recipe_prompt, end='')
    recipe = input()
    if len(recipe) == 0:
        print(empty_recipe_name)
        return
    if recipe in cookbook:
        del cookbook[recipe]
        print(recipe_deleted)
    else:
        print(recipe_not_found)

def main():
    print(welcome_message)
    while True:
        print(available_options.format(BOLD_COLOR, ENDC_COLOR,
                                       BOLD_COLOR, ENDC_COLOR,
                                       BOLD_COLOR, ENDC_COLOR,
                                       BOLD_COLOR, ENDC_COLOR,
                                       BOLD_COLOR, ENDC_COLOR,
                                       BOLD_COLOR, ENDC_COLOR))
        user_input = input(prompt)
        if len(user_input) == 0:
            print(empty_input)
            continue
        try:
            user_input = int(user_input)
        except ValueError:
            print(wrong_input)
            continue
        switch_dict = {
            1: add_recipe,
            2: delete_recipe,
            3: print_recipe,
            4: print_cookbook,
            5: quit
        }
        selected_function = switch_dict.get(user_input, lambda: print(wrong_input))
        selected_function()

if __name__ == '__main__':
    main()
