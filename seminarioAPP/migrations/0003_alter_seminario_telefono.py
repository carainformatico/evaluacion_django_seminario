# Generated by Django 4.1.4 on 2022-12-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminarioAPP', '0002_rename_nombrer_seminario_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminario',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
    ]