# Generated by Django 4.2.2 on 2023-06-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=50)),
                ('edad', models.PositiveSmallIntegerField()),
                ('es_activo', models.BooleanField(default=True)),
            ],
        ),
    ]