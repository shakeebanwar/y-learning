# Generated by Django 3.1 on 2020-08-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0020_auto_20200826_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_detail',
            name='Card_number',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
