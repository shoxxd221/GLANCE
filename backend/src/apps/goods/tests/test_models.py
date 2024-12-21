from django.test import TestCase

from ..models import Category, Goods
from apps.constants import DEFAULT_MAX_LENGTH
from apps.utils import run_field_parameter_test, assert_model_field_value


class CategoryTests(TestCase):
    """Класс тестов для модели категорий"""

    @classmethod
    def setUpTestData(cls):
        """Заполнение данных перед запуском всех тестов"""

        cls.category = Category.objects.create(name='Телефоны')
        cls.field_and_verbose_name = {
            'name': 'Название категории'
        }
        cls.field_and_max_length = {
            'name': DEFAULT_MAX_LENGTH
        }

    def test_verbose_name(self):
        """Тест параметра verbose_name"""

        run_field_parameter_test(
            Category,
            self,
            self.field_and_verbose_name,
            'verbose_name'
        )

    def test_max_length(self):
        """Тест параметра max_lenght"""

        run_field_parameter_test(
            Category,
            self,
            self.field_and_max_length,
            'max_length'
        )

    def test_str_method(self):
        """Тест строкового отображения"""

        self.assertEqual(str(self.category), str(self.category.name))

    def test_name_value(self):
        """Тест значения поля name"""

        assert_model_field_value(self, self.category, 'name', 'Телефоны')


class GoodsTests(TestCase):
    """Класс тестов для модели товаров"""

    @classmethod
    def setUpTestData(cls):
        """Заполнение данных перед запуском всех тестов"""
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
        cls.field_and_verbose_name = {
            'name': 'Название товара'
        }
        cls.field_and_max_length = {
            'name': DEFAULT_MAX_LENGTH
        }

    def test_verbose_name(self):
        """Тест параметра verbose_name"""

        run_field_parameter_test(
            Goods,
            self,
            self.field_and_verbose_name,
            'verbose_name'
        )

    def test_max_length(self):
        """Тест параметра max_lenght"""

        run_field_parameter_test(
            Goods,
            self,
            self.field_and_max_length,
            'max_length'
        )

    def test_str_method(self):
        """Тест строкового отображения"""

        self.assertEqual(str(self.goods), str(self.goods.name))

    def test_fields_value(self):
        """Тест значения поля name"""

        assert_model_field_value(self, self.goods, 'name', 'Iphone X')
        assert_model_field_value(self, self.goods, 'price', 1200)
        assert_model_field_value(self, self.goods, 'description', 'Самый лучший телефон')
        assert_model_field_value(self, self.goods, 'category', self.category)
        assert_model_field_value(self, self.goods, 'characteristics', {'Цвет': 'Белый', 'ОЗУ': 16})
        assert_model_field_value(self, self.goods, 'quantity', 2)
