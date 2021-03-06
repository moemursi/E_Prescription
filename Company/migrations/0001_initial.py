# Generated by Django 2.2.6 on 2019-12-02 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntibioticType',
            fields=[
                ('antibioticTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('antibioticTypeName', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('licence', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineForm',
            fields=[
                ('medicineFormId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineFormName', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('medicineTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineTypeName', models.CharField(max_length=33)),
                ('antibioticType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.AntibioticType')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicineId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineName', models.CharField(max_length=25)),
                ('singleUnitQuantity', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Company')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.MedicineForm')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.MedicineType')),
            ],
        ),
    ]
