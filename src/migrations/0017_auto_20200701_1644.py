# Generated by Django 3.0.7 on 2020-07-01 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0016_usersettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='liked_by_me',
            field=models.ManyToManyField(default=1, related_name='_registeruser_liked_by_me_+', to='src.RegisterUser'),
        ),
        migrations.AddField(
            model_name='registeruser',
            name='super_liked_by_me',
            field=models.ManyToManyField(default=1, related_name='_registeruser_super_liked_by_me_+', to='src.RegisterUser'),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='age_range',
            field=models.IntegerField(default='18', validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(130)]),
        ),
    ]
