# Generated by Django 3.2.9 on 2021-11-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
            ],
        ),
    ]