# Updated the file.
# Created a dictionary of 10 foods and their ingredients.

food_ingredients = {
    "Pizza": ["dough", "tomato sauce", "cheese", "pepperoni"],
    "Burger": ["bun", "beef patty", "cheese", "lettuce", "tomato", "onion", "ketchup", "mayonnaise"],
    "Fried Chicken": ["chicken", "flour", "breadcrumbs", "spices", "oil"],
    "Macaroni and Cheese": ["macaroni pasta", "cheese", "butter", "milk", "flour"],
    "Hot Dog": ["hot dog bun", "sausage", "ketchup", "mustard", "relish", "onion"],
    "Pancakes": ["flour", "milk", "eggs", "baking powder", "butter", "syrup"],
    "Grilled Cheese Sandwich": ["bread", "cheese", "butter"],
    "Chicken Wings": ["chicken wings", "hot sauce", "butter", "celery", "blue cheese dressing"],
    "French Fries": ["potatoes", "oil", "salt"],
    "Salad": ["romaine lettuce", "Caesar dressing", "parmesan cheese", "croutons"],
}

# Created a function that makes a list of the user entered ingredients and limit it to ALL lower case format.

def find_food_item(ingredient):
    matches = []
    for food, ingredients in food_ingredients.items():
        if ingredient.lower() in [i.lower() for i in ingredients]:
            matches.append(food)
    return matches

# Created a function that will take the user submitted list of ingredients and make sure each item in the list matches for the intended food item.

def can_make_food(food_item, ingredients):
    required_ingredients = food_ingredients.get(food_item, [])
    return all(ingredient in ingredients for ingredient in required_ingredients)

#  Created an user input field that will allow the user to enter the ingredients as a comma separated value. It will split the entry at the comma and create a SET.

user_input = input("Enter ingredients separated by commas: ")
user_ingredients = [ingredient.strip() for ingredient in user_input.split(',')]

matching_food_items = set()

# The for loop will go through each item in the list and compare the submited list to the dictionary's key/value pair.

for ingredient in user_ingredients:
    matches = find_food_item(ingredient)
    if matches:
        matching_food_items.update(matches)
    else:
        print(f"No matches found for the ingredient '{ingredient}'")

# The for loop will go through the matches and print out if the food item and the ingredient match the option to make the product.

for food_item in matching_food_items:
    if can_make_food(food_item, user_ingredients):
        print(f"You can make '{food_item}' with the provided ingredients.")