# Generated by Django 5.0.1 on 2024-01-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend1', '0009_rename_experiance_categorydb_jobexperience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydb',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
