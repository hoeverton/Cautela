# Generated by Django 5.1 on 2024-08-12 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['categoria']},
        ),
    ]
