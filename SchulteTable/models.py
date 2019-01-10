from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, validate_email
from django.core.exceptions import ValidationError
from django.utils import timezone

class UserST(models.Model):
    name = models.CharField(max_length=100, unique=False, verbose_name=u"Имя пользователя")
    login = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3)], verbose_name=u"Login")
    email = models.CharField(max_length=50, unique=True, validators=[validate_email], verbose_name=u"E-mail")
    bday = models.DateField(verbose_name=u"Дата рождения")
    password = models.CharField(max_length=100, validators=[MinLengthValidator(8)], verbose_name=u"Хэш пароля")
    tokenToConfirmEmail = models.CharField(max_length=1000, unique=True, null=True, verbose_name=u"Токен для почты")
    tokenToResetPassword = models.CharField(max_length=1000, unique=True, null=True, verbose_name=u"Токен для сброса пароля")
    def __str__(self):
        return self.login
    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

class Test(models.Model):
    stWE =  models.DecimalField(default = 0, decimal_places=2, max_digits=12, validators=[MinValueValidator(0)], verbose_name=u"Эффективность работы")
    stWU =  models.DecimalField(default = 0, decimal_places=2, max_digits=12, validators=[MinValueValidator(0)], verbose_name=u"Степень врабатываемости")
    stPS =  models.DecimalField(default = 0, decimal_places=2, max_digits=12, validators=[MinValueValidator(0)], verbose_name=u"Психологическая устойчивость")
    user_id = models.ForeignKey(UserST, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    age = models.PositiveIntegerField(verbose_name=u"Возраст")
    date = models.DateField(default=timezone.now, verbose_name=u"Дата")
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = u'Результат тестирования'
        verbose_name_plural = u'Результаты тестирований'
