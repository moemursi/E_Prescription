# Generated by Django 2.2.6 on 2019-11-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='company',
        ),
        migrations.AddField(
            model_name='medicine',
            name='companyNumber',
            field=models.CharField(default=2, max_length=11),
            preserve_default=False,
        ),
    ]