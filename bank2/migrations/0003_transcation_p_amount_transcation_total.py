# Generated by Django 4.2.6 on 2023-11-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank2', '0002_transcation_remove_acc_dt_remove_acc_from_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcation',
            name='p_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transcation',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
