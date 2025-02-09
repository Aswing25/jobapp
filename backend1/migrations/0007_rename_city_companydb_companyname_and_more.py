# Generated by Django 5.0 on 2024-01-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend1', '0006_companydb_remove_categorydb_comdes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydb',
            old_name='city',
            new_name='companyname',
        ),
        migrations.RenameField(
            model_name='companydb',
            old_name='comname',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='companydb',
            old_name='descrip',
            new_name='password',
        ),
        migrations.AddField(
            model_name='companydb',
            name='description',
            field=models.CharField(blank=True, default='Add Details', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companydb',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
