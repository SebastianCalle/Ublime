# Generated by Django 3.0.4 on 2020-03-12 23:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200312_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('8926efe0-78ba-4c11-93f4-0fc78d27e5a9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
