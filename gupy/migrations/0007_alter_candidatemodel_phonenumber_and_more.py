# Generated by Django 4.1.2 on 2022-10-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gupy', '0006_resultmodel_manualcandidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatemodel',
            name='phoneNumber',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='resultmodel',
            name='phoneNumber',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
