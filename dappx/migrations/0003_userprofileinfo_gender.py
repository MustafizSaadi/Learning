# Generated by Django 2.2 on 2019-04-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0002_userprofileinfo_registration_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True),
        ),
    ]
