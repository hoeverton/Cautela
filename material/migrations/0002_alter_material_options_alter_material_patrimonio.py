# Generated by Django 5.1 on 2024-08-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['categoria', 'titulo']},
        ),
        migrations.AlterField(
            model_name='material',
            name='patrimonio',
            field=models.IntegerField(unique=True),
        ),
    ]
