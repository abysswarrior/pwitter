# Generated by Django 4.0.2 on 2022-08-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]