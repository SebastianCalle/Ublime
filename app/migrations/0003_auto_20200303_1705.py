# Generated by Django 3.0.3 on 2020-03-03 22:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200303_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('241d40ea-5e54-4b2e-ba36-ea88faff103f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_id',
            field=models.UUIDField(default=uuid.UUID('6dc7e9ee-55cb-42b1-a9b7-f62c1da8477c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
