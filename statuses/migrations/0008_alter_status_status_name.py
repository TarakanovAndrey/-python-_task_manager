# Generated by Django 4.2.6 on 2023-10-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0007_status_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status_name',
            field=models.TextField(max_length=100),
        ),
    ]