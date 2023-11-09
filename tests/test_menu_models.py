from django.test import TestCase
from restaurant.models import RestaurantModel
from menu.models import MenuModel, ProductModel


class MenuModelTestCase(TestCase):
    def setUp(self):
        self.restaurant = RestaurantModel.objects.create(name="Test Restaurant")
        self.menu = MenuModel.objects.create(name="Test Menu", restaurant_foren=self.restaurant)

    def test_menu_name(self):
        self.assertEqual(self.menu.name, "Test Menu")

    def test_menu_date_field(self):
        # Перевірка чи поле date_field дійсно автоматично заповнюється при створенні об'єкта
        self.assertIsNotNone(self.menu.date_field)

    def test_menu_like_default(self):
        self.assertEqual(self.menu.like, 0)

    def test_menu_restaurant_foreign_key(self):
        self.assertEqual(self.menu.restaurant_foren, self.restaurant)


class ProductModelTestCase(TestCase):
    def setUp(self):
        self.restaurant = RestaurantModel.objects.create(name="Test Restaurant")
        self.menu = MenuModel.objects.create(name="Test Menu", restaurant_foren=self.restaurant)
        self.product = ProductModel.objects.create(name="Test Product", price=10.99, menu_foren=self.menu)

    def test_product_name(self):
        self.assertEqual(self.product.name, "Test Product")

    def test_product_price(self):
        self.assertEqual(self.product.price, 10.99)

    def test_product_menu_foreign_key(self):
        self.assertEqual(self.product.menu_foren, self.menu)
