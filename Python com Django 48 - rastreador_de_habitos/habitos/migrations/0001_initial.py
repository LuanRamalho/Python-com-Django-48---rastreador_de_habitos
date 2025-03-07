# Generated by Django 5.1.2 on 2025-03-04 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('cumprido', models.BooleanField(default=False)),
                ('habito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitos.habito')),
            ],
        ),
    ]
