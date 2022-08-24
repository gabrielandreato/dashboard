# Generated by Django 4.1 on 2022-08-23 01:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_dashboard', '0002_despesas_alter_vendas_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesas',
            name='valor',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 22, 42, 4, 702184)),
        ),
    ]
