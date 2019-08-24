# Generated by Django 2.2 on 2019-08-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caregivers', '0002_auto_20190824_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caregiver',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='caregiver',
            unique_together={('name',)},
        ),
    ]
