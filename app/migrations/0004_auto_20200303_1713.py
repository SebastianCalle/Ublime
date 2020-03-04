# Generated by Django 3.0.3 on 2020-03-03 22:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200303_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('0a7b2882-5f3b-4780-8f69-1fe7d4fa8076'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_id',
            field=models.UUIDField(default=uuid.UUID('6343b4fc-ef59-4e47-a8a7-5df2a7974f51'), editable=False, primary_key=True, serialize=False),
        ),
    ]
