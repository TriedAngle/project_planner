# Generated by Django 2.2.5 on 2019-09-08 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20190908_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members_count',
        ),
    ]
