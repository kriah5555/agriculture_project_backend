# Generated by Django 4.0.4 on 2022-12-25 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agriapp', '0003_rename_decise_deviselocation_devise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviselocation',
            name='api_call',
        ),
    ]