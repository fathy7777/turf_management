# Generated by Django 5.1.3 on 2024-12-18 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_complaint_complainttable'),
    ]

    operations = [
        migrations.AddField(
            model_name='turf',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.logintable'),
            preserve_default=False,
        ),
    ]