# Generated by Django 2.2.9 on 2020-02-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200222_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='auth',
            field=models.CharField(default='user', max_length=20),
        ),
    ]