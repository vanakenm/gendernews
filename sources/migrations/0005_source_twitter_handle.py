# Generated by Django 3.2.9 on 2022-04-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0004_reportline'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='twitter_handle',
            field=models.CharField(max_length=200, null=True),
        ),
    ]