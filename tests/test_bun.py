from praktikum.bun import Bun


class TestBun:
    def test_name_is_set_correctly(self):
        bun = Bun("Sesame", 1.5)
        assert bun.get_name() == "Sesame"

    def test_price_is_set_correctly(self):
        bun = Bun("Sesame", 1.5)
        assert bun.get_price() == 1.5

    def test_name_is_empty_string(self):
        bun = Bun("", 1.5)
        assert bun.get_name() == ""

    def test_price_is_zero(self):
        bun = Bun("Sesame", 0.0)
        assert bun.get_price() == 0.0

    def test_price_is_negative(self):
        bun = Bun("Sesame", -1.0)
        assert bun.get_price() == -1.0
