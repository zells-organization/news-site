# Generated by Django 3.0.5 on 2020-05-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='My title', max_length=200),
        ),
    ]
