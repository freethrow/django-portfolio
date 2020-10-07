# Generated by Django 3.1.1 on 2020-09-29 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_is_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
    ]