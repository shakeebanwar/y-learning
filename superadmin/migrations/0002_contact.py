# Generated by Django 3.1 on 2020-08-19 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Last Name', max_length=100)),
                ('Email', models.CharField(default='Email Name', max_length=100)),
                ('ContactNo', models.CharField(default='Contact no', max_length=100)),
                ('Message', models.TextField(default='No')),
            ],
        ),
    ]