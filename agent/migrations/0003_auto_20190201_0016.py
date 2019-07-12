# Generated by Django 2.1.5 on 2019-01-31 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_remove_agent_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='description',
        ),
        migrations.AddField(
            model_name='agent',
            name='phone',
            field=models.CharField(default='01936299699', max_length=14),
            preserve_default=False,
        ),
    ]
