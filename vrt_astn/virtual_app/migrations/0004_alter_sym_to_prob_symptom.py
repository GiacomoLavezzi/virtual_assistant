# Generated by Django 3.2.12 on 2023-05-26 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_app', '0003_auto_20230526_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sym_to_prob',
            name='symptom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_problems', to='virtual_app.symptom'),
        ),
    ]