# Generated by Django 2.1.2 on 2018-11-04 15:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Результат')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Результат тестирования',
                'verbose_name_plural': 'Результаты тестирований',
            },
        ),
        migrations.CreateModel(
            name='UserST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('login', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Login')),
                ('email', models.CharField(max_length=50, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='E-mail')),
                ('bday', models.DateField(verbose_name='Дата рождения')),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Хэш пароля')),
                ('tokenToConfirmEmail', models.CharField(max_length=1000, null=True, unique=True, verbose_name='Токен для почты')),
                ('tokenToResetPassword', models.CharField(max_length=1000, verbose_name='Токен для сброса пароля')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AddField(
            model_name='test',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchulteTable.UserST', verbose_name='Пользователь'),
        ),
    ]