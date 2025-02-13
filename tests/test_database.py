from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def setup_method(self):
        self.db = Database()

    def test_available_buns(self):
        buns = self.db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        expected_names = {"black bun", "white bun", "red bun"}
        actual_names = {bun.name for bun in buns}
        assert actual_names == expected_names

    def test_available_ingredients(self):
        ingredients = self.db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        expected_ingredients = {
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
        }
        actual_ingredients = {(ing.type, ing.name, ing.price) for ing in ingredients}
        assert actual_ingredients == expected_ingredients
