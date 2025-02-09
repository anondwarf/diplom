from praktikum.ingredient import Ingredient

def test_name_is_set_correctly():
    ingredient = Ingredient("Filling", "Tomato", 0.3)
    assert ingredient.get_name() == "Tomato"

def test_price_is_set_correctly():
    ingredient = Ingredient("Sauce", "Ketchup", 0.2)
    assert ingredient.get_price() == 0.2

def test_type_is_set_correctly():
    ingredient = Ingredient("Sauce", "Mustard", 0.1)
    assert ingredient.get_type() == "Sauce"

def test_name_is_empty_string():
    ingredient = Ingredient("Filling", "", 0.4)
    assert ingredient.get_name() == ""

def test_price_is_zero():
    ingredient = Ingredient("Filling", "Onion", 0.0)
    assert ingredient.get_price() == 0.0

def test_price_is_negative():
    ingredient = Ingredient("Sauce", "Mayonnaise", -0.1)
    assert ingredient.get_price() == -0.1

def test_type_is_empty_string():
    ingredient = Ingredient("", "Pickle", 0.2)
    assert ingredient.get_type() == ""