# Generated by Django 3.0.4 on 2020-03-18 20:39

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('toilet_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200, null=True)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('image_1', models.ImageField(null=True, upload_to='img/')),
                ('image_2', models.ImageField(null=True, upload_to='img/')),
                ('image_3', models.ImageField(null=True, upload_to='img/')),
                ('description', models.CharField(max_length=200, null=True)),
                ('accesibility', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created time')),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]