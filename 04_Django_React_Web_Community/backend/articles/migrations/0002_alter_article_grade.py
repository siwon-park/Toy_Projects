# Generated by Django 3.2.12 on 2022-08-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='grade',
            field=models.IntegerField(choices=[(1, 'F급'), (2, 'D급'), (3, 'C급'), (4, 'B급'), (5, 'A급'), (6, 'S급')]),
        ),
    ]
