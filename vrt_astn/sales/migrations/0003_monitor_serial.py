# Generated by Django 3.2.12 on 2023-05-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20230529_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='serial',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]