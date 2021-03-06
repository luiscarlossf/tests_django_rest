# Generated by Django 2.2.4 on 2021-02-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='no_email@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_name='users', to='testapp.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='no_username', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='no_name', max_length=255),
        ),
    ]
