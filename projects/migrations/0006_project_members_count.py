# Generated by Django 2.2.5 on 2019-09-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190907_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='members_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
