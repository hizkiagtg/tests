# Generated by Django 4.1 on 2022-10-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buat_sumbangan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donasi',
            name='bank_sampah',
            field=models.CharField(max_length=50),
        ),
    ]
