from enum import Enum


class Ingredient(str, Enum):
    R2_D3 = "61c0c5a71d1f82001bdaaa6d"
    N_200I = "61c0c5a71d1f82001bdaaa6c"
    SPICY_X = "61c0c5a71d1f82001bdaaa72"
    PROTOSTOMIA = "61c0c5a71d1f82001bdaaa6f"
    SALAT = "61c0c5a71d1f82001bdaaa79"

    def __str__(self):
        return self.value