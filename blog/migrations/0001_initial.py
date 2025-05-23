# Generated by Django 5.2 on 2025-05-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('alimento', 'Alimento'), ('juego', 'Juego'), ('Mobiliario', 'Mobiliario')], max_length=20)),
                ('descrip', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='servicios/')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
