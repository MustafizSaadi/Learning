# Generated by Django 2.2 on 2019-04-23 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0008_userprofileinfo_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
