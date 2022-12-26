# Generated by Django 4.0.4 on 2022-12-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriapp', '0004_remove_deviselocation_api_call'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devise',
            name='amount_paid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='devise',
            name='balance_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='deviselocation',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='deviselocation',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]