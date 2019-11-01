# Generated by Django 2.2.6 on 2019-10-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, choices=[('MBBS', 'MBBS'), ('CTS', 'CTS')], max_length=15, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]