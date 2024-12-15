from django.contrib.auth import get_user_model
from django.test import TestCase


from apps.goods.models import Goods, Category

from ..models import Cart
from ...utils import run_field_parameter_test, assert_model_field_value

User = get_user_model()


class CartTests(TestCase):
    """Класс тестов для модели корзины"""

    @classmethod
    def setUpTestData(cls):
        """Заполнение тестовой базы данных данными"""
        cls.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        cls.category = Category.objects.create(name='Телефоны')
        cls.goods = Goods.objects.create(
            name='Iphone X',
            price=1200,
            description='Самый лучший телефон',
            category=cls.category,
            characteristics={
                'Цвет': 'Белый',
                'ОЗУ': 16
            },
            quantity=2
        )
        cls.cart = Cart.objects.create(
            user=cls.user,
            goods=cls.goods,
            quantity=2
        )
        cls.field_and_verbose_name = {
            'user': 'Пользователь, которому соответсвует товар в корзине',
            'goods': 'Товар, который пользователь добавил в корзину',
            'quantity': 'Количество товара в заказе'
        }

    def test_verbose_name(self):
        """Тест параметра verbose_name"""

        run_field_parameter_test(
            Cart,
            self,
            self.field_and_verbose_name,
            'verbose_name'
        )

    def test_user_value(self):
        """Тест значения поля user"""

        assert_model_field_value(self, self.cart, 'user', self.user)

    def test_goods_value(self):
        """Тест значения поля goods"""

        assert_model_field_value(self, self.cart, 'goods', self.goods)

    def test_quantity_value(self):
        """Тест значения поля quantity"""

        assert_model_field_value(self, self.cart, 'quantity', self.cart.quantity)
