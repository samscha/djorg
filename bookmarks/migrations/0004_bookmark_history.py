# Generated by Django 2.0.5 on 2018-05-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_auto_20180508_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='history',
            field=models.TextField(blank=True),
        ),
    ]
