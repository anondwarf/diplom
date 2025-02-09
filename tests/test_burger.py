from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def test_buns_are_set_correctly():
    bun = Mock(spec=Bun)
    burger = Burger()
    burger.set_buns(bun)
    assert burger.bun == bun

def test_ingredient_is_added_correctly():
    ingredient = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ingredient)
    assert ingredient in burger.ingredients

def test_ingredient_is_removed_correctly():
    ingredient = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert ingredient not in burger.ingredients

def test_ingredient_is_moved_correctly():
    ingredient1 = Mock(spec=Ingredient)
    ingredient2 = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]

def test_price_is_calculated_correctly():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 1.5
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 2.0
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_price() == 5.0

def test_receipt_is_generated_correctly():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Sesame"
    bun.get_price.return_value = 1.5
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Lettuce"
    ingredient.get_type.return_value = "Filling"
    ingredient.get_price.return_value = 0.5
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    expected_receipt = "(==== Sesame ====)\n= filling Lettuce =\n(==== Sesame ====)\n\nPrice: 3.5"
    assert burger.get_receipt() == expected_receipt