# Generated by Django 3.0.4 on 2020-03-12 19:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20200312_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('d2b0d85f-fdfd-466e-b28a-b4ea90017b60'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_id',
            field=models.UUIDField(default=uuid.UUID('121253b0-d51e-48a1-9501-866da00219d9'), editable=False, primary_key=True, serialize=False),
        ),
    ]