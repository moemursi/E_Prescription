# Generated by Django 2.2.6 on 2019-11-28 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_auto_20191105_1955'),
        ('Pharmacist', '0012_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=20)),
                ('confirmationState', models.CharField(max_length=50)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Medicine')),
                ('pharmacist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pharmacist.Pharmacist')),
            ],
        ),
    ]
