# Generated by Django 3.1.1 on 2020-09-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageto3d', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageto3d',
            name='image_name',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
