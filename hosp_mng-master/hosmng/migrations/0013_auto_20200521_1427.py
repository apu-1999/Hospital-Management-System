# Generated by Django 3.0 on 2020-05-21 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosmng', '0012_medical_sr_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medical',
            old_name='sr_no',
            new_name='Outstanding',
        ),
    ]
