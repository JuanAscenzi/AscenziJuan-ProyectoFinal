# Generated by Django 4.1.7 on 2023-03-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juguete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tamaño', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=10)),
                ('cantidad', models.CharField(max_length=3)),
            ],
        ),
    ]
