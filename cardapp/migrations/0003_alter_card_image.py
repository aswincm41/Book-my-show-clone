# Generated by Django 4.2.5 on 2024-03-01 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0002_rename_discription_card_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
