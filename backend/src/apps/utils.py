def run_field_parameter_test(
        model, self,
        field_and_parameter_value: dict,
        parameter_name: str) -> None:
    """Тестирует значение параметра для всех объектов модели"""

    for instance in model.objects.all():
        for field, expected_value in field_and_parameter_value.items():
            parameter_real_value = getattr(
                instance._meta.get_field(field), parameter_name
            )

            self.assertEqual(parameter_real_value, expected_value)


def assert_model_field_value(self, model_instance, field_name: str, expected_value) -> None:
    """Тестирует значение любого поля для объекта модели"""
    real_value = getattr(model_instance, field_name)
    self.assertEqual(real_value, expected_value)
