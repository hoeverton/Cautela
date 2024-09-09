# Generated by Django 5.1 on 2024-08-12 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policial', '0003_alter_policial_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policial',
            name='senha',
            field=models.CharField(help_text='Senha deve ter pelo menos 8 caracteres.', max_length=128, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
