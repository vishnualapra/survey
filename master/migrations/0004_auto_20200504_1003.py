# Generated by Django 3.0.5 on 2020-05-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20200504_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
