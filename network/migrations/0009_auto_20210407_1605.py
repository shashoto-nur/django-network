# Generated by Django 3.1.2 on 2021-04-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_auto_20210407_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=300, null=True),
        ),
    ]