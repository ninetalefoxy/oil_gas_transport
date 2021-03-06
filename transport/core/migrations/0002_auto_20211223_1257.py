# Generated by Django 3.2.7 on 2021-12-23 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='driver_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_detail', to='core.driver'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='tanker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tanker_detail', to='core.tanker'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='veh_type',
            field=models.CharField(choices=[('diesel', 'diesel'), ('gas', 'gas'), ('petrol', 'petrol')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tanker',
            name='fuel',
            field=models.CharField(choices=[('diesel', 'diesel'), ('gas', 'gas'), ('petrol', 'petrol')], max_length=100),
        ),
    ]
