# Generated by Django 3.1.2 on 2020-10-30 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swift_realtys', '0005_listing_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(default='none', upload_to='images'),
        ),
    ]
