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
    "Salad": ["lettuce", "dressing", "cheese", "croutons"],
}

user_input = input("Enter ingredients separated by commas: ")  # Prompt user for input
entered_ingredients = []  # Initialize an empty list to store cleaned ingredients

# Split the user input by commas and iterate over each ingredient
for ingredient in user_input.split(','):
    # Remove leading and trailing whitespaces from the ingredient and convert it to lowercase
    cleaned_ingredient = ingredient.strip().lower()
    # Append the cleaned ingredient to the list of entered ingredients
    entered_ingredients.append(cleaned_ingredient)


for food_item in food_ingredients.keys():
    # Initialize a boolean variable to track if all ingredients are present
    all_ingredients_present = True
    
    # Iterate over each ingredient required for the current food item
    for ing in food_ingredients[food_item]:
        # Check if the current ingredient is in the list of entered ingredients
        if ing not in entered_ingredients:
            # If any ingredient is not found, set the flag to False and break the loop
            all_ingredients_present = False
            break
    
    # After checking all ingredients for the current food item
    if all_ingredients_present:
        # If all ingredients are present, print the message
        print(f"You can make '{food_item}' with the provided ingredients.")