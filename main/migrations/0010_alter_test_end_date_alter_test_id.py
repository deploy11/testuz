# Generated by Django 4.2.6 on 2023-10-24 11:46

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_test_end_date_alter_test_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 11, 46, 2, 989513, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi'),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]