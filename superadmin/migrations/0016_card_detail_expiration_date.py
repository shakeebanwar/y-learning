# Generated by Django 3.1 on 2020-08-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0015_remove_package_package_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_detail',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]