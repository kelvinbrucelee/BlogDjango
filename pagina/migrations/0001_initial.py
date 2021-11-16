# Generated by Django 3.2.9 on 2021-11-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('contato', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
                ('situacao', models.BooleanField(default=False)),
                ('atualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-atualizado',),
            },
        ),
    ]
