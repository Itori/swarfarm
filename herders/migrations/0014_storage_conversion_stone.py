# Generated by Django 2.2.13 on 2020-07-31 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herders', '0013_runebuild_speed_pct'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='conversion_stone',
            field=models.IntegerField(default=0, help_text='Conversion Stone'),
        ),
    ]
