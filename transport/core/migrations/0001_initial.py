# Generated by Django 3.2.7 on 2021-12-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('license_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('retail_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('maharashtra', 'maharashtra')], max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('tal', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tanker',
            fields=[
                ('truck_id', models.AutoField(primary_key=True, serialize=False)),
                ('veh_type', models.CharField(max_length=100)),
                ('fuel', models.CharField(max_length=100)),
                ('veh_num', models.CharField(max_length=100)),
                ('maximum_allowed', models.IntegerField()),
                ('estimaion', models.IntegerField()),
                ('current_amount', models.IntegerField()),
                ('veh_volume', models.IntegerField()),
                ('veh_weight', models.CharField(max_length=100)),
                ('veh_run', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('veh_type', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(choices=[('diesel', 'diesel'), ('gas', 'gas'), ('petrol', 'petrol')], max_length=100)),
                ('veh_run', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('shipping', 'shipping'), ('completed', 'completed')], max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.retail')),
                ('driver_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.driver')),
                ('tanker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tanker')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.retail'),
        ),
    ]