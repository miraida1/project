# Generated by Django 4.2.7 on 2023-12-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_task_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('availability', models.BooleanField(default=True, verbose_name='azyrky uchurda barbi')),
                ('image', models.ImageField(blank=True, upload_to='p/%Y/%m/%d')),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
