# Generated by Django 3.0.2 on 2020-07-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200713_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description_html',
            field=models.TextField(editable=False),
        ),
    ]
