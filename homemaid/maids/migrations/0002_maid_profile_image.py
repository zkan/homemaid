# Generated by Django 3.0.8 on 2020-07-18 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maid',
            name='profile_image',
            field=models.FileField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
