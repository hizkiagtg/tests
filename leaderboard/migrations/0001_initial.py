# Generated by Django 4.1 on 2022-10-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField(null=True)),
                ('weight', models.IntegerField(null=True)),
            ],
        ),
    ]
