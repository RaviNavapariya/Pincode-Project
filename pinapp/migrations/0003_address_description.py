# Generated by Django 4.1.1 on 2022-10-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinapp', '0002_remove_address_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]