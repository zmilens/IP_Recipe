# Generated by Django 3.1.5 on 2021-01-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_author_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='level',
            field=models.CharField(max_length=20),
        ),
    ]
