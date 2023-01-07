# Generated by Django 4.0.4 on 2022-12-31 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agriapp', '0005_alter_devise_amount_paid_alter_devise_balance_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='APICountThreshold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.IntegerField()),
                ('orange', models.IntegerField()),
                ('blue', models.IntegerField()),
                ('green', models.IntegerField()),
                ('devise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.devise')),
            ],
        ),
    ]
