# Generated by Django 2.2.3 on 2019-07-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190205_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(choices=[('ruet', 'RUET, Rajshahi'), ('sust', 'SUST, Sylhet'), ('rmmc', 'RmMC, Rangamati')], max_length=20),
        ),
    ]
