# Generated by Django 3.0.1 on 2020-02-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='name',
        ),
        migrations.AddField(
            model_name='website',
            name='des',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
