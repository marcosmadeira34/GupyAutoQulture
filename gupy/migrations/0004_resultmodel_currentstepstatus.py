# Generated by Django 4.1.2 on 2022-10-25 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gupy', '0003_resultmodel_currentstepname_resultmodel_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultmodel',
            name='currentStepStatus',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
