# Generated by Django 2.2.4 on 2021-02-11 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_auto_20210211_1935'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
