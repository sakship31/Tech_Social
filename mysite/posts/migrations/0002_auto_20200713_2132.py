# Generated by Django 3.0.2 on 2020-07-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='description_html',
            field=models.TextField(blank=True, default='', editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=255),
        ),
    ]