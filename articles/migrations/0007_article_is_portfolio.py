# Generated by Django 3.1.1 on 2020-09-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200926_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_portfolio',
            field=models.BooleanField(default=False),
        ),
    ]
