# Generated by Django 2.2 on 2019-11-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_merge_20191105_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('DF', 'Dog Food'), ('DT', 'Dog Toys'), ('DS', 'Dog Treats')], max_length=2),
        ),
    ]
