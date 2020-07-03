# Generated by Django 3.0.7 on 2020-07-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0010_auto_20200701_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='liked_by',
            field=models.ManyToManyField(blank=True, default=1, null=True, related_name='liked_by', to='src.RegisterUser'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='superliked_by',
            field=models.ManyToManyField(blank=True, default=1, null=True, related_name='superliked_by', to='src.RegisterUser'),
        ),
    ]
