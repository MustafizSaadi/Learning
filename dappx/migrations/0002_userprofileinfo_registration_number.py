# Generated by Django 2.2 on 2019-04-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='registration_number',
            field=models.CharField(default='2016-814-413', max_length=70),
        ),
    ]
