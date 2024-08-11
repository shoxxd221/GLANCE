from django.core.exceptions import ValidationError


class PasswordBaseInit:
    """Базовый класс для валидаторов пароля."""

    message = 'Введите правильное значение'
    code = 'password_incorrect'
    help_message = 'Проверьте правильность ввода пароля.'

    def __init__(self, message=None, code=None, help_message=None) -> None:
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if help_message is not None:
            self.help_message = help_message

    def get_help_text(self) -> str:
        """Получение описательного текста для поля формы."""
        return self.help_message


class PasswordMaximumLengthValidator(PasswordBaseInit):
    """Валидатор максимальной длинны пароля."""

    max_length = 20
    help_message = f'Максимальная длинна: {max_length} символов.'

    def __init__(
        self, message=None, code=None, help_message=None, max_length=None
    ) -> None:
        super().__init__(message, code, help_message)
        if max_length is not None:
            self.max_length = max_length

    def validate(self, password, user=None) -> None:
        """Проверка на максимальную длинну пароля."""

        if len(password) > self.max_length:
            raise ValidationError(
                f'{self.message} {self.help_message}',
                code=self.code,
                params={'password': self.help_message},
            )
