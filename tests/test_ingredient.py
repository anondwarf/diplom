from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_name_is_set_correctly(self):
        ingredient = Ingredient("Filling", "Lettuce", 0.5)
        assert ingredient.get_name() == "Lettuce"

    def test_price_is_set_correctly(self):
        ingredient = Ingredient("Filling", "Lettuce", 0.5)
        assert ingredient.get_price(self) == 0.5

    def test_type_is_set_correctly(self):
        ingredient = Ingredient("Filling", "Lettuce", 0.5)
        assert ingredient.get_type() == "Filling"

    def test_name_is_empty_string(self):
        ingredient = Ingredient("Filling", "", 0.5)
        assert ingredient.get_name() == ""

    def test_price_is_zero(self):
        ingredient = Ingredient("Filling", "Lettuce", 0.0)
        assert ingredient.get_price() == 0.0

    def test_price_is_negative(self):
        ingredient = Ingredient("Filling", "Lettuce", -0.5)
        assert ingredient.get_price() == -0.5

    def test_type_is_empty_string(self):
        ingredient = Ingredient("", "Lettuce", 0.5)
        assert ingredient.get_type() == ""
