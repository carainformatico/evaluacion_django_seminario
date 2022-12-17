# Generated by Django 4.1 on 2022-12-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seminario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreR', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('institucion', models.CharField(max_length=50)),
                ('fechareserva', models.DateTimeField(auto_now_add=True)),
                ('estado', models.IntegerField(choices=[(1, 'Completada'), (2, 'Anulada'), (3, 'No Asisten'), (4, 'Reservado')], default=1)),
                ('observacion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
