# Generated by Django 4.2.7 on 2023-12-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
