# Generated by Django 2.2 on 2019-04-23 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0003_userprofileinfo_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='hall_name',
            field=models.CharField(default='Dr. muhammad sahidullah hall', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True),
        ),
    ]
