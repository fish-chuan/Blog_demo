# Generated by Django 2.2.9 on 2020-02-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_artical_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_artical',
            name='post',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='like_artical',
            name='user',
            field=models.CharField(default='user', max_length=20),
        ),
    ]