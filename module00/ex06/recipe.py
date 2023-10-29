welcome_message = 'Welcome to the Python Cookbook !'

available_options = '''\
List of available option:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit\
'''

prompt = '''\
Please select an option:
>> \
'''

wrong_input = '''\
This option does not exist, please type the corresponding number.
To exit, enter 5.\
'''

empty_input = 'Empty input, please type the corresponding number.'

add_recipe_name = '>>> Enter a name:'
add_recipe_ingredients = '>>> Enter ingredients:'
add_recipe_meal_type = '>>> Enter a meal type:'
add_recipe_preparation_time = '>>> Enter a preparation time:'
recipe_already_exists = 'Recipe already exists'
empty_recipe_name = 'Empty recipe name'
empty_meal_type = 'Empty meal type'

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
    recipe_name = input(add_recipe_name)
    print('[' + recipe_name + ']')
    if len(recipe_name) == 0:
        print(empty_recipe_name)
        return
    if recipe_name in cookbook:
        print(recipe_already_exists)
        return
    
    recipe_ingredients = []
    ingredient = ' '
    print(add_recipe_ingredients)
    while len(ingredient) > 0:
        ingredient = input(add_recipe_ingredients)
        if len(ingredient) > 0:
            recipe_ingredients.append(ingredient)
    if len(recipe_ingredients) == 0:
        print(empty_recipe_name)
        return
    recipe_meal_type = input(add_recipe_meal_type)
    if len(recipe_meal_type) == 0:
        print(empty_recipe_name)
        return
    recipe_preparation_time = input(add_recipe_preparation_time)

#todo: implement the recipe deletion
def delete_recipe():
    print('Delete a recipe')

#todo: implement the recipe printing
def print_recipe():
    print('Print a recipe')

#todo: implement the cookbook printing
def print_cookbook():
    print('Print the cookbook')
    

if __name__ == '__main__':
    print(welcome_message)
    while True:
        print(available_options)
        user_input = input(prompt)
        if len(user_input) == 0:
            print(empty_input)
            continue
        try:
            user_input = int(user_input)
        except ValueError:
            print(wrong_input)
            continue
        if user_input == 1:
            add_recipe()
        elif user_input == 2:
            delete_recipe()
        elif user_input == 3:
            print_recipe()
        elif user_input == 4:
            print_cookbook()
        elif user_input == 5:
            quit()
        else:
            print(wrong_input)
