# Generated by Django 2.1.5 on 2019-01-30 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_published',
            new_name='is_released',
        ),
    ]
