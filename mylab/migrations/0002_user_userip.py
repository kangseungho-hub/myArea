# Generated by Django 3.0.2 on 2020-07-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='UserIP',
            field=models.CharField(default='anonymous', max_length=20),
            preserve_default=False,
        ),
    ]
