# Generated by Django 3.0.5 on 2021-01-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_remove_selections_ou'),
    ]

    operations = [
        migrations.AddField(
            model_name='selections',
            name='ou',
            field=models.CharField(default='Over', max_length=30),
            preserve_default=False,
        ),
    ]