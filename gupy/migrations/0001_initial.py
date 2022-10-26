# Generated by Django 4.1.2 on 2022-10-25 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField()),
                ('candidate', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('identificationDocument', models.CharField(max_length=255)),
                ('countryOfOrigin', models.CharField(max_length=255)),
                ('linkedinProfileUrl', models.URLField()),
                ('gender', models.CharField(max_length=255)),
                ('mobileNumber', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gupy.candidatemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ResultModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.CharField(max_length=100)),
                ('partnerName', models.CharField(max_length=100)),
                ('endedAt', models.DateTimeField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('tags', models.CharField(max_length=100)),
                ('birthdate', models.CharField(default=None, max_length=100)),
                ('countryOfOrigin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gupy.jobmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ManualCandidateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manualCandidate', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gupy.jobmodel')),
            ],
        ),
    ]
