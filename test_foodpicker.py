import unittest
from foodpicker import find_food_item, can_make_food

class TestFoodFunctions(unittest.TestCase):
    def test_find_food_item(self):
        # Test for a single matching ingredient
        self.assertEqual(find_food_item("cheese"), ["Pizza", "Burger", "Macaroni and Cheese", "Grilled Cheese Sandwich"])
        
        # Test for multiple matching ingredients
        self.assertEqual(find_food_item("butter"), ["Macaroni and Cheese", "Pancakes", "Grilled Cheese Sandwich", "Chicken Wings"])
        
        # Test for a non-matching ingredient
        self.assertEqual(find_food_item("apple"), [])

    def test_can_make_food(self):
        # Test for a food item that can be made with provided ingredients
        self.assertTrue(can_make_food("Pizza", ["dough", "cheese", "tomato sauce", "pepperoni"]))
        
        # Test for a food item that cannot be made with provided ingredients
        self.assertFalse(can_make_food("Pizza", ["cheese", "tomato sauce", "pepperoni"]))
        
        # Test for a food item with missing ingredients
        self.assertFalse(can_make_food("Burger", ["bun", "beef patty"]))
        
        # Test for a non-existing food item
        self.assertFalse(can_make_food("Salad", ["lettuce", "tomato", "cucumber", "dressing"]))

if __name__ == '__main__':
    unittest.main()
