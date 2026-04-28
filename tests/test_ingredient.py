import pytest
import allure
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @allure.title("Проверка получения названия ингредиента")
    @pytest.mark.parametrize("test_name", [
        "bacon",
        "cheddar",
        "salmon"
    ])
    def test_get_name(self, test_name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, test_name, 50.0)
        assert ingredient.get_name() == test_name

    @allure.title("Проверка получения цены ингредиента")
    @pytest.mark.parametrize("test_price", [
        100.0,
        200.0,
        0.0
    ])
    def test_get_price(self, test_price):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Test Ingredient", test_price)
        assert ingredient.get_price() == test_price

    @allure.title("Проверка получения типа ингредиента")
    @pytest.mark.parametrize("test_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING
    ])
    def test_get_type(self, test_type):
        ingredient = Ingredient(test_type, "Test Ingredient", 50.0)
        assert ingredient.get_type() == test_type


    @allure.title("Проверка инициализации названия ингредиента в конструкторе")
    @pytest.mark.parametrize("name", [
        "sour cream",
        "dinosaur",
        "sausage",
        "unknown"
    ])
    def test_constructor_initializes_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 70.0)
        assert ingredient.name == name

    @allure.title("Проверка инициализации типа ингредиента в конструкторе")
    @pytest.mark.parametrize("ingredient_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
        ""
    ])
    def test_constructor_initializes_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Test Name", 90.0)
        assert ingredient.type == ingredient_type

    @allure.title("Проверка инициализации цены ингредиента в конструкторе")
    @pytest.mark.parametrize("price", [
        30.0,
        50.0,
        70.0,
        0.0
    ])
    def test_constructor_initializes_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Test Ingredient", price)
        assert ingredient.price == price


    @allure.title("Проверка использования мока")
    def test_mock_get_price(self):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 70.0
        assert mock_ingredient.get_price() == 70.0