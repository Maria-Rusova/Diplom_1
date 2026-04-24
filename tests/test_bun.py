import pytest
import allure
from unittest.mock import Mock
from praktikum.bun import Bun

class TestBun:

    @allure.title("Проверка получение названия булочки")
    @pytest.mark.parametrize("test_name", [
        "Classic Bun",
        "Special Edition Bun",
    ])
    def test_get_name(self, test_name):
        bun = Bun(test_name, 100.0)
        assert bun.get_name() == test_name

    @allure.title("Проверка с использованием мока")
    def test_mock_get_price(self):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100.0
        assert mock_bun.get_price() == 100.0    


    @allure.title("Проверка установки имени булочки")
    @pytest.mark.parametrize("name", [
        "black bun",
        "red bun",
        "gluten-free Bun",
        ""
    ])
    def test_bun_name_initialization(self, name):
        bun = Bun(name, 100.0)
        assert bun.get_name() == name

    @allure.title("Проверка установки цены булочки")
    @pytest.mark.parametrize("price", [
        100.0,
        200.0,
        300.0,
        0.0
    ])
    def test_bun_price_initialization(self, price):
        bun = Bun("Test Bun", price)
        assert bun.get_price() == price


    @allure.title("Проверка возврата имени после полной инициализации с валидными данными")
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100.0),
        ("white bun", 200.0),
        ("red bun", 300.00)
    ])
    def test_bun_get_name_after_full_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @allure.title("Проверка возврата цены после полной инициализации с валидными данными")
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100.0),
        ("white bun", 200.0),
        ("red bun", 300.0)
    ])
    def test_bun_get_price_after_full_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price


    @allure.title("Проверка возврата имени при пустом имени и цене ноль")
    def test_bun_get_name_empty_name_zero_price(self):
        bun = Bun("", 0.0)
        assert bun.get_name() == ""

    @allure.title("Проверка возврата цены при пустом имени и цене ноль")
    def test_bun_get_price_empty_name_zero_price(self):
        bun = Bun("", 0.0)
        assert bun.get_price() == 0.0