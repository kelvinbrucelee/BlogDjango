# Generated by Django 3.2.8 on 2021-11-03 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0012_auto_20211102_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(blank=True, max_length=255)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Cores',
            },
        ),
    ]