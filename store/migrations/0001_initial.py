# Generated by Django 3.1.4 on 2020-12-09 19:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner_id', models.UUIDField()),
                ('name', models.TextField()),
                ('phone_number', models.TextField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('priority', models.BigIntegerField(default=10)),
                ('image_url', models.TextField()),
                ('description', models.TextField()),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('total_visitor', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True)),
                ('created_by', models.UUIDField(blank=True)),
                ('updated_by', models.UUIDField(blank=True)),
            ],
            options={
                'db_table': 'store_models',
            },
        ),
    ]
