# Generated by Django 4.0.2 on 2022-02-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweeted_at',
            field=models.DateTimeField(null=True, verbose_name='ツイート予定日時'),
        ),
    ]
