# Generated by Django 5.0.1 on 2024-01-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend1', '0014_alter_categorydb_comapnyname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorydb',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
