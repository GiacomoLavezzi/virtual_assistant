# Generated by Django 3.2.12 on 2023-05-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_cpu_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='frequency',
            field=models.FloatField(),
        ),
        migrations.DeleteModel(
            name='Frequency',
        ),
    ]